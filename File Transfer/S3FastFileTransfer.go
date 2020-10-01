package main

import (
	"bytes"
	"database/sql"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	_ "github.com/go-sql-driver/mysql"
	"github.com/joho/godotenv"
)

var (
	S3Region = os.Getenv("S3_REGION")
	S3Bucket = os.Getenv("S3_BUCKET")
	Connection = os.Getenv("CONNECTION")
)

func init() {
	// loads values from .env into the system
	if err := godotenv.Load(); err != nil {
		log.Print("No .env file found")
	}
}

func main() {
	var (
		startAt = "2020-02-01 10:00:00"
		endAt   = "2020-02-01 11:00:00"
	)
	getData(startAt, endAt)

}

func getData(start string, end string) {
	var (
		id   int
		name string
	)
	db, err := sql.Open("mysql",os.Getenv("CONNECTION"))
	if err != nil {
		log.Fatal(err)
	}
	rows, err := db.Query("select id, name from "+os.Getenv("TABLE")+" where created_at > ? and created_at < ?", start, end)
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()
	for rows.Next() {
		err := rows.Scan(&id, &name)
		if err != nil {
			log.Fatal(err)
		}
		log.Println(id, name)
		//Call step 2 to get JSON file
		getJSON(name)
	}
	err = rows.Err()
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()
}

func getJSON(path string) {
	fullPath := os.Getenv("S3_BUCKET_PATH") + path
	log.Println(fullPath)
	if err := DownloadFile(path, fullPath); err != nil {
		panic(err)
	}
}

func DownloadFile(filepath string, url string) error {

	// Get the data
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// Create the file
	out, err := os.Create(filepath)
	if err != nil {
		return err
	}
	defer out.Close()

	// Write the body to file
	_, err = io.Copy(out, resp.Body)

	// Call step 3 to upload the file to AWS S3
	uploadFile(filepath)

	log.Println(filepath)

	// Call step 5 delete local file
	err = os.Remove(filepath)

	if err != nil {
		fmt.Println(err)
		return nil
	}

	return err
}

func uploadFile(file string) {

	// Create a single AWS session (we can re use this if we're uploading many files)
	s, err := session.NewSession(&aws.Config{Region: aws.String(S3Region), Credentials: credentials.NewStaticCredentials(
		os.Getenv("API_KEY"),
		os.Getenv("API_SECRET"),
		"")})
	if err != nil {
		log.Fatal(err)
	}

	// Call step 4 Upload
	err = AddFileToS3(s, file)
	if err != nil {
		log.Fatal(err)
	}

}

func AddFileToS3(s *session.Session, fileDir string) error {

	// Open the file for use
	file, err := os.Open(fileDir)
	if err != nil {
		return err
	}
	defer file.Close()

	// Get file size and read the file content into a buffer
	fileInfo, _ := file.Stat()
	var size = fileInfo.Size()
	buffer := make([]byte, size)
	file.Read(buffer)

	// Config settings: this is where you choose the bucket, filename, content-type etc.
	// of the file you're uploading.
	_, err = s3.New(s).PutObject(&s3.PutObjectInput{
		Bucket:               aws.String(S3Bucket),
		Key:                  aws.String(fileDir),
		ACL:                  aws.String("private"),
		Body:                 bytes.NewReader(buffer),
		ContentLength:        aws.Int64(size),
		ContentType:          aws.String(http.DetectContentType(buffer)),
		ContentDisposition:   aws.String("attachment"),
		ServerSideEncryption: aws.String("AES256"),
	})
	return err
}
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
import cv2
from moviepy.editor import VideoFileClip, clips_array
from moviepy.editor import concatenate_videoclips
from typing import List
from moviepy.editor import *
import os
from moviepy.video.fx.all import crop

from fastapi.middleware.cors import CORSMiddleware
from moviepy.editor import VideoFileClip, clips_array
from moviepy.editor import *
import os
import base64
import uvicorn
from typing import List
import subprocess
import time
import random
import string
global audioname
from collections import Counter


audioname = None


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return Response(content=open("index.html", "r").read(), media_type="text/html")

def resize_videos(clips, width, height):


    duration_limit = 30  # in seconds

    outnames = []
    file1 = generate_unique_filename()

    for input_file in clips:
        cmd_probe = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'stream=width,height',
            '-of', 'csv=p=0:s=x',
            input_file
        ]
        result = subprocess.run(cmd_probe, stdout=subprocess.PIPE, text=True)
        video_info = result.stdout.strip().split('x')
        video_width, video_height = int(video_info[0]), int(video_info[1])

        # Calculate the scale and crop values
        aspect_ratio = video_width / video_height
        if aspect_ratio > width / height:
            new_width = int(height * aspect_ratio)
            new_height = height
        else:
            new_width = width
            new_height = int(width / aspect_ratio)
        scale = f'{new_width}:{new_height}'
        crop_x = (new_width - width) // 2
        crop_y = (new_height - height) // 2

        # Build the ffmpeg command
        cmd_ffmpeg = [
            'ffmpeg',
            '-i', input_file,
            '-t', str(duration_limit),
            '-vf', f'scale={scale},crop={width}:{height}:{crop_x}:{crop_y}',
            f"resized{input_file}"
        ]

        # Run the ffmpeg command
        subprocess.run(cmd_ffmpeg)

        outnames.append(f"resized{input_file}")

    out = concatenate_videos(outnames, f"{file1}concat.mp4")

    return out


def resize_single(input_file, width, height):

    duration_limit = 30  # in seconds


    file1 = generate_unique_filename()


    cmd_probe = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height',
        '-of', 'csv=p=0:s=x',
        input_file
    ]
    result = subprocess.run(cmd_probe, stdout=subprocess.PIPE, text=True)
    video_info = result.stdout.strip().split('x')
    video_width, video_height = int(video_info[0]), int(video_info[1])

    # Calculate the scale and crop values
    aspect_ratio = video_width / video_height
    if aspect_ratio > width / height:
        new_width = int(height * aspect_ratio)
        new_height = height
    else:
        new_width = width
        new_height = int(width / aspect_ratio)
    scale = f'{new_width}:{new_height}'
    crop_x = (new_width - width) // 2
    crop_y = (new_height - height) // 2

    # Build the ffmpeg command
    cmd_ffmpeg = [
        'ffmpeg',
        '-i', input_file,
        '-t', str(duration_limit),
        '-vf', f'scale={scale},crop={width}:{height}:{crop_x}:{crop_y}',
        f"resized{input_file}"
    ]

    # Run the ffmpeg command
    subprocess.run(cmd_ffmpeg)

    # save 

    return f"resized{input_file}"


def concatenate_videos(input_files, output_file):

    # CONCATENATE VIDEOS
    clips = [VideoFileClip(filename) for filename in input_files]
    final_clip = concatenate_videoclips(clips)  
    # if the lenght of concatenated video is greater than 30 seconds, then limit it to 30 seconds just

    if final_clip.duration > 30:
        final_clip = final_clip.subclip(0, 30)


    final_clip.write_videofile(output_file) 

    return output_file



@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    # Save the uploaded audio file
    i = 1
    while True:
        if os.path.exists(f"audio{i}.mp3"):
            i += 1
        else:
            break

    with open(f"audio{i}.mp3", "wb") as f:
        f.write(await file.read())

    global audioname
    audioname = f"audio{i}.mp3"
    time.sleep(4)

    return {"message": "Videos uploaded successfully"}


@app.post("/upload-videos")
async def upload_videos(files: List[UploadFile] = File(...)):
    print(files)
    i = 1
    for file in files:
        with open(f"video{i}.mp4", "wb") as f:
            f.write(await file.read())
        i+=1

    return {"message": "Videos uploaded successfully"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...), videoNumber: int = Form(...)):
    with open(f"video{videoNumber}.mp4", "wb") as f:
        f.write(await file.read())

    # Generate thumbnail image for the uploaded video
    video_capture = cv2.VideoCapture(f"video{videoNumber}.mp4")
    success, frame = video_capture.read()
    if success:
        # Save the thumbnail as a temporary file
        thumbnail_path = f"thumbnail{videoNumber}23.jpg"
        cv2.imwrite(thumbnail_path, frame)

        # Read the thumbnail image and convert it to base64
        with open(thumbnail_path, "rb") as thumbnail_file:
            thumbnail_data = thumbnail_file.read()
            thumbnail_base64 = base64.b64encode(thumbnail_data).decode("utf-8")

    else:
        thumbnail_base64 = None

        
    return JSONResponse({"message": "Video uploaded successfully", "imagePath": thumbnail_base64})



def generate_unique_filename():
    timestamp = str(int(time.time()))
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    unique_filename = timestamp + '_' + random_string
    return unique_filename




@app.post("/combine")
async def combine_videos(files: List[UploadFile] = File(...), audio: UploadFile = File(None), videoNumber: str = Form(...)):

    file1 = generate_unique_filename()
    audionames = generate_unique_filename()
    outputname = generate_unique_filename()

    # Save the uploaded video files and create a list of their names
    files_na = []
    i = 1
    for i, file in enumerate(files, start=1):
        with open(f"{file1}{i}.mp4", "wb") as f:
            f.write(await file.read())
            files_na.append(f"{file1}{i}.mp4")
        i += 1

    no = videoNumber.split(",")
    # remove empty string from the list
    no = list(filter(None, no))
    count = Counter(no)

    # iterate the count
    total_vid =[]
    index = 0
    for key, value in count.items():
        if int(value) > 1:
            joined_names = []
            for x in range(int(value)):
                joined_names.append(files_na[index])
                index = index + 1
            out = resize_videos(joined_names, width=426, height=720)
            total_vid.append(out)
        else:
            out = resize_single(files_na[index], width=426, height=720)
            total_vid.append(out)
            index = index + 1

    count = 0

    if audio is not None:
        # Save the uploaded audio file
        with open(f"{audionames}.mp3", "wb") as f:
            f.write(await audio.read())
            audios = f"{audionames}.mp3"
            count = count + 1

    else:
        audios = ""


    video1 = total_vid[0]
    video2 = total_vid[1]
    video3 = total_vid[2]



    clip1 = VideoFileClip(video1)
    # get audio of clip
    aud1 = clip1.audio
    clip2 = VideoFileClip(video2)
    # get audio of clip
    aud2 = clip2.audio
    clip3 = VideoFileClip(video3)
    # get audio of clip
    aud3 = clip3.audio

    combined = clips_array([[clip1, clip2, clip3]])

    length = 30

    output_file = f"{outputname}.mp4"


    if audios == "":
        print("No audio")
        if combined.duration > 30:
            combined = combined.subclip(0, 0 + length)
        combined.write_videofile(output_file)
    
    else:
        print("Found Audio")
        # Trim audio clip to match the duration of the video
        audio = AudioFileClip(audios).subclip(0, combined.duration)
        composite_audio = CompositeAudioClip([audio, aud1, aud2, aud3])
        combined = combined.set_audio(composite_audio)
        if combined.duration > 30:
            combined = combined.subclip(0, 0 + length)
        combined.write_videofile(output_file)
    
    
    return FileResponse(output_file, media_type="video/mp4")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
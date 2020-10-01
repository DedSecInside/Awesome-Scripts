import PyPDF2, os

#get all pdf files from directory
pdf_files=[filename for filename in os.listdir('.') if filename.endswith('.pdf')]

#sort filenames 
pdf_files.sort()
count_merged_files = 0
pdfWriter = PyPDF2.PdfFileWriter()

#copy each pdf file to the final output file
for filename in pdf_files:
	print(f'Merging \'{filename}\' to main pdf file.')
	count_merged_files+=1
	
	pdfFileObj = open(filename,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj,strict=False)

        #if you want to skip first page change the range below from 0 to 1
	for page_num in range(0,pdfReader.numPages):
		pageObj = pdfReader.getPage(page_num)
		pdfWriter.addPage(pageObj)

#save output file
pdfOutput = open('combined.pdf','wb')
pdfWriter.write(pdfOutput)

pdfOutput.close()
print('=============================')
print(f'[+] {count_merged_files} files merged.')

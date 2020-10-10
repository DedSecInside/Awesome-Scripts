import os
import tkinter as tk
from tkinter import filedialog
import filetype
import boto3

'''
Use python tkinter to open file dialog and allow user to select file.
!!! Please handle exception if user does not select file. Otherwise It would be runtime error
'''

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
file_dir, file_name = os.path.split(file_path)

'''
Try to get file mime type using filetype library.
Docs :- https://pypi.org/project/filetype/
'''

file_type = filetype.guess(file_path)
if file_type is None:
    file_content_type = None
else:
    file_content_type = file_type.MIME

'''
AWS credential configuration
Replace AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_SECRET, region_name with your own data
'''

session = boto3.session.Session(aws_access_key_id="AWS_ACCESS_KEY_ID",
                                aws_secret_access_key="AWS_ACCESS_KEY_SECRET",
                                region_name="region_name"
                                )

s3_resource = session.resource('s3')

'''
Replace bucket_name with your S3 bucket name
'''

bucket = s3_resource.Bucket("bucket_name")
bucket.upload_file(
    filename=file_path,
    key=file_name,
    filetype=file_type
)

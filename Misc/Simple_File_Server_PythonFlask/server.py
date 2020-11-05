from flask import Flask, request, send_from_directory, render_template, abort, redirect, flash
import os, time
from werkzeug.utils import secure_filename

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'log', 'csv', 'xml'])
# set the project root directory as the static folder, you can set others.
app = Flask(__name__)
# set as part of the config
SECRET_KEY = 'many random bytes'

# or set directly on the app
app.secret_key = 'many random bytes'

@app.route('/', defaults={'req_path': ''})
def dir_listing(req_path):
    """
    Return a list of all files.

    Args:
        req_path: (str): write your description
    """
    files = os.listdir(FILES_DIR)
    file_dict_list = []
    for filename in files:
        file_dict = {}
        file_dict['name'] = filename
        abs_path = os.path.join(FILES_DIR, filename)
        ctime = time.ctime(os.path.getctime(abs_path))
        mtime = time.ctime(os.path.getmtime(abs_path))
        file_dict['ctime'] = ctime
        file_dict['mtime'] = mtime
        file_dict_list.append(file_dict)
    return render_template('files.html', files=file_dict_list)

@app.route('/<path:path>', methods=['GET'])
def sendFile(path):
    """
    Sends a file to the specified path.

    Args:
        path: (str): write your description
    """
    return send_from_directory(FILES_DIR, path, as_attachment=True, mimetype='application/octet-stream')

def allowed_file(filename):
    """
    Return true if a file is allowed.

    Args:
        filename: (str): write your description
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def uploadFile():
    """
    Upload a file

    Args:
    """
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(FILES_DIR, filename))
        flash('Successfully Uploaded!')
        return redirect(request.url)
    else:
        flash('Upload Failed! Check file extension')
        return redirect(request.url)

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename=os.path.join(BASE_DIR, 'server.log'),level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    app.run(host='0.0.0.0', port=5002, debug=True)
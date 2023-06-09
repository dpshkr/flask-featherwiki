
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, make_response, render_template
from flask_login import LoginManager
from datetime import datetime
import shutil
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'PUT', 'OPTIONS'])
def hello_world():
    if (request.method == 'GET'):
        data = ""
        with open('/home/dpushkar/mysite/FeatherWiki_Warbler.html', 'r') as f:
            data = f.read()
        response = make_response(data)
        return response
    elif (request.method == 'OPTIONS'):
        response = make_response("")
        response.headers['dav'] = "Dummy WebDAV header to enable TiddlyWiki's PUT server"
        return response
    elif (request.method == 'PUT'):
        src = '/home/dpushkar/mysite/FeatherWiki_Warbler.html'
        dst = os.path.join('/home/dpushkar/mysite/backups', datetime.now().strftime('backup-%Y-%m-%d-%H-%M-%S.html'))
        shutil.move(src, dst)
        with open('/home/dpushkar/mysite/FeatherWiki_Warbler.html', 'w') as f:
            f.write(str(request.stream.read(), 'UTF-8'))

        return ""


@app.route('/write-post')
def write_post():
    return render_template('write-post.html')

@app.route('/submit-post', methods=['POST'])
def submit_post():
    return request.form["editordata"]

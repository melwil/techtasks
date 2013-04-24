import os
import json
from bottle import get, redirect, request, route, run, static_file, template, view

@route('/')
@view('index_template')
def index():
    return dict(files=os.listdir("uploads"))

@route('/upload', method='POST')
def upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext != '.txt':
        return 'File extension not allowed.'

    save_path = 'uploads/'
    try:
        upload.save(save_path) 
    except IOError as e:
        return 'Error: %s<br /><br /><a href="/">Go back</a>' % e
    redirect('/')

@route('/analyze/:filename')
@view('analyze_template')
def analyze(filename):
    words = {}
    f = open('uploads/%s' % filename, 'r')
    # Iterating over each line instead of reading the whole file to memory, in case of huge file
    for line in f:
        for word in line.split(" "):
            word = word.strip()
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    data = []
    for key, value in words.items():
        data.append((value, key,))
    data.sort()
    finaldata = []
    for value, key in data[-20:]:
        finaldata.insert(0, {"label": key, "y": value})

    return dict(filename=filename, data=data[-5:])

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='')

run(host='10.211.55.3', port=8080)
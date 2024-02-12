from flask import Flask , render_template, url_for, flash, request, redirect, send_from_directory,session
import os
import sys

app=Flask(__name__)
app.secret_key='tumiaqp'

@app.route('/')
def method_name():
    return "<h1>Construccion</h1>"

sys.path.insert(0, os.path.dirname(__file__))
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python v' + sys.version.split()[0] + '\n'
    response = '\n'.join([message, version])
    return [response.encode()]

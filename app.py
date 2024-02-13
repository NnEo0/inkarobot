from flask import Flask , render_template, url_for, flash, request, redirect, send_from_directory,session
import os
import sys

app=Flask(__name__)
app.secret_key='tumiaqp'

@app.route('/')
def method_name():
    return "<h1>Construccion 2</h1>"

if __name__ == "main":
    app.run(debug=True)
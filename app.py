#!/usr/bin/python
#-*- coding: utf-8 -*-

import argparse
import subprocess
from flask import Flask, jsonify, request
from flask import render_template
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
        return redirect(url_for('introduce'))

@app.route('/introduce')
def introduce():
        return render_template('introduce.html')
        
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return render_template('introduce.html', name=name)



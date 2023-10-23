# server.py: flask framework for running web-crawler app

from flask import Flask
from flask import jsonify, requests
from .crawler import crawler
from .classifier import classifier

app = Flask(_name_)

# api endpoints
# 1. ("/"): how-to guide / readme
# 2. ("/crawler"): use crawler with search function: ?search=XXX
# 3. ("/classify"): use classifier with image path: ?path=XXX

@app.route('/')
def readme():
    # instructions on using api

@app.route('/crawler')
def crawl():
    # init crawler

@app.route('/classify')
def classify():
    # init classifier
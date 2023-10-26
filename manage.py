# manage.py: flask framework for running web-crawler app

from flask import Flask
from flask import jsonify, request
from crawler import crawler
from classifier import classifier
import json
import pandas as pd

app = Flask(__name__)
classifier = classifier()
crawl = crawler()

# api endpoints
# 1. ("/crawler"): use crawler with search function: ?search=XXX
# 2. ("/classify"): use classifier with image path: ?path=XXX

# crawler call
# input: keyword to search on Instagram
# output: downloads 5 images to media/ with name keyword_{i}.png
#
# example usage: 127.0.0.1:5000/crawler?search=test will download 5 images and return json classification
@app.route('/crawler')
def crawl():
    # init crawler
    keyword = request.args['search']
    result = crawl.search_by_keyword(keyword)
    if result == {}:
        return "Error: Keyword produced no results"
    
    classifications = []
    for i in result:
        y = classifier.classify_image(i)
        classifications.append(y)

    df = pd.DataFrame(classifications)
    
    return df.to_json()

# classify call
# input: path to image
# output: classification in form of: image_path, label, confidence
#
# example usage: 127.0.0.1:5000/classify?path=media/test_0.png will return classification
@app.route('/classify')
def classify():
    path = request.args['path']
    y = classifier.classify_image(path)
    return json.dumps(str(y))

if __name__ == '__main__':
    app.run(debug=True, threaded=False, port=8881)
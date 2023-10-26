# manage.py: flask framework for running web-crawler app

from flask import Flask
from flask import jsonify, request
from crawler import crawler
from classifier import classifier
import json
import pandas as pd
import os
import imghdr

app = Flask(__name__)
classifier = classifier()


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
    spider = crawler()
    keyword = request.args['search']
    result = spider.search_by_keyword(keyword)

    if result == {}:
        return "Error: Keyword produced no results"
    
    if type(result) == str:
        return "Error: Try different keyword."
    
    # list of outputs from model classification
    classifications = []
    for path in result:
        y = classifier.classify_image(path)
        classifications.append(y)

    # convert list of dicts to pandas dataframe is very easy to convert into json representation
    # purposefully naive
    df = pd.DataFrame(classifications)
    
    return df.to_json()

# classify call
# input: path to image
# output: classification in form of: image_path, label, confidence
#
# example usage: 127.0.0.1:8881/classify?path=media/test_0.png will return classification
@app.route('/classify')
def classify():
    path = request.args['path']

    # check user input:
    if not os.path.isfile(path) == True:
        return "File path does not exist"
    elif imghdr.what(path) == None:
        return "File path is not an image"
    
    y = classifier.classify_image(path)
    return json.dumps(str(y))

if __name__ == '__main__':
    app.run(port=8881) # can remove port=8881 to default to 5000. was having issues on personal pc with port 5000
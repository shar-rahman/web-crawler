
# Simple Crawler

A simple Instagram web crawler that will download images for a desired keyword and perform image classification. Built using Flask, Selenium, and Keras.



## Requirements

    Flask==3.0.0
    keras==2.14.0
    numpy==1.26.1
    pandas==2.1.2
    selenium==4.14.0
    tensorflow==2.14.0

## Usage

Download all requirements as shown above in requirements.txt

    git clone https://github.com/shar-rahman/web-crawler

    cd web-crawler

    python manage.py

The above commands will get you started and begin running the Flask server.

The API endpoints are as follows:

    - crawler/ Downloads 5 images from Instagram and performs image classification using VGG16 on Imagenet weights. Returns json format of classification
    
    - classify/ Performs image classification of an image given a file path. Returns json format of classification.
        
        curl 127.0.0.1:8881/crawler?search=XX where XX is your keyword to be searched.
        curl 127.0.0.1:8881/classify?path=XX where XX is the path to image to be classified.

Alternatively, you can browse to 127.0.0.1:8881/crawler?search=XX or 127.0.0.1:8881/classify?path=XX to access the API.

Images will be downloaded to media/


## Further Research

Further research and currently conducted research can be found in the Jupyter Notebook in research/

# api endpoint for instagram caller
# use ?search=XXX for searching for a word on instagram

import io
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions  import NoSuchElementException
import time, urllib.request
import os

class crawler:

    # construct class
    def __init__(self):
        self.path = "media/"

        # create a selenium chrome browser instance that does not open a window.
        self.op = webdriver.ChromeOptions()
        self.op.add_argument('headless')
        self.driver = webdriver.Chrome(options=self.op)

        if not os.path.exists(self.path):
            os.makedirs(self.path)

    # input: keyword
    # output: path to 5 downloaded images
    #
    # searches instagram by keyword and downloads 5 images to media/. this function will also return the imagepaths.
    # downloads as media/keyword_{idx}.png
    def search_by_keyword(self, keyword):
        self.driver.get("https://www.instagram.com/explore/tags/" + keyword)
        time.sleep(5) # give selenium a little time to load the page

        # check if page is valid:
        if not self.driver.find_elements(By.XPATH, "//img[contains(@class, 'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')]"):
            return "Page not found - Try different keyword."
        scraped_results = self.driver.find_elements(By.XPATH, "//img[contains(@class, 'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')]")
        
        imagepath_list = []
        for idx, image in enumerate(scraped_results):
            if len(imagepath_list) == 5: #ensures 5 downloads
                break
            src = image.get_attribute('src')
            image_path = "media/" + keyword + "_{}".format(idx)+".png"
            imagepath_list.append(image_path)
            urllib.request.urlretrieve(str(src), image_path) # naive. should add error handling.

        return imagepath_list

        
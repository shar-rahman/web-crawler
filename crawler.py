# api endpoint for instagram caller
# use ?search=XXX for searching for a word on instagram

import io
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, urllib.request
import os

class crawler:

    # construct class
    path = "media/"
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)

    # create media path
    if not os.path.exists(path):
        os.makedirs(path)

    # input: keyword
    # output: path to 5 downloaded images
    #
    # searches instagram by keyword and downloads 5 images to media/. this function will also return the imagepaths.
    def search_by_keyword(self, keyword):
        self.driver.get("https://www.instagram.com/explore/tags/" + keyword)
        time.sleep(5)
        img_results = self.driver.find_elements(By.XPATH, "//img[contains(@class, 'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')]")
        
        imagepath_list = []
        for idx, img in enumerate(img_results):
            if len(imagepath_list) == 5:
                break
            src = img.get_attribute('src')
            image_path = "media/" + keyword + "_{}".format(idx)+".png"
            imagepath_list.append(image_path)
            try: 
                urllib.request.urlretrieve(str(src), image_path)
            except Exception e:
                print e
                continue

        
        return imagepath_list

        
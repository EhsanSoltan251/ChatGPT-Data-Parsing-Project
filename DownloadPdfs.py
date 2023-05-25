import os
from os import listdir
from os.path import isfile, join
import requests
import browser_cookie3
from bs4 import BeautifulSoup as bs
import selenium
from selenium import webdriver
import wget


#IMPORTANT: set the browser to your browser
cookies = browser_cookie3.safari()

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36", 
}


links_path = os.path.dirname(os.path.abspath(__file__)) + "/links.txt"
pdfs_directory = os.path.dirname(os.path.abspath(__file__)) + "/pdfs"


with open (links_path) as links_file:
    lines = links_file.readlines()

links = [line.replace("\n", "").replace("?", "?tp=&").replace("/stamp/stamp", "/stampPDF/getPDF") for line in lines]

test_links = links[0:1]



for count, link in enumerate(test_links):
  
    with requests.get(link, cookies=cookies, headers=headers, timeout=3, stream=True) as html:
        with open(pdfs_directory + "/paper" + str(count) + ".txt", "wb") as file:
            #print(r.content)

            link = "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=816042"
            
            #pdf = requests.get(link, cookies=cookies, headers=headers, timeout=3).content

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('prefs', {
                "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
                "download.default_directory": pdfs_directory, 
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": True
            })

            browser = webdriver.Chrome(options=chrome_options)
            browser.get(link)

            
          
            



            #file.write(pdf)
            #print(pdf)
            #file.close()
   

  






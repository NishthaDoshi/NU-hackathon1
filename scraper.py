import pandas as pd
import numpy as np
df=pd.read_csv('/content/final.csv',header='infer')
!pip install selenium
import requests
from bs4 import BeautifulSoup


#datset label

n=int(input(" enter no webiste you want to check "))
for i in range(n):
   from selenium import webdriver
   from selenium.webdriver.common.keys import Keys
   driver = webdriver.tor()
   driver.get("https://duckduckgo.com/.")
   search_box = driver.find_element_by_name("q")
   search_box.send_keys("python")
   search_box = driver.find_element_by_name("q")
   
   search_box.send_keys("python")
   search_box.send_keys(Keys.RETURN)
   search_results = driver.find_elements_by_css_selector("div.g")
   urls = []
   for result in search_results:
     link = result.find_element_by_tag_name("p")
     url = link.get("href")
     urls.append(url)
   response = requests.get(url)
   html_content = response.content
     # Use Beautiful Soup to parse the HTML content
   soup = BeautifulSoup(html_content, "html.parser")
     
     #we get the  data  with the beautifulsoup library 
     #after that we use nltp for arranging d text data in array seprated by comma 
     #the we compare the data from website to our data 
     #and if data matches it is under cyber crime 
     #hence proved 
     #problem is solved 
     #that website or blog is under cyber crime
    
    


      


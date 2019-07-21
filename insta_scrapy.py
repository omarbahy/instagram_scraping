from bs4 import BeautifulSoup
import urllib.request
from  selenium import webdriver
import time
import sys
import os
type_browser=input("what is your browser (1) chrome (2) firefox\n:")
if type_browser == "1" or type_browser == "chrome":
 try:
  web=webdriver.Chrome()
 except:
  print("You should install chromedriver to run script !!")
  sys.exit()
elif type_browser == "2" or type_browser == "firefox":
 try: 
  web=webdriver.Firefox()
 except:
  print("you should install geckodriver to run script !!")
  sys.exit()
else :
 print("choose 1 or 2 only !")

try:
 type_=int(input("search for (1) Username (2) hashtag\n:"))
except:
           print("Enter (1) or (2) Only !")
           sys.exit()
if type_ == 1:
           username=input("Enter username: ")
           url="https://www.instagram.com/{}/".format(username)
elif type_==2:
           hashtag=input("Enter hashtag without(#): ")
           url="https://www.instagram.com/explore/tags/{}".format(hashtag)
web.get(url)
print("\npress ctrl+c to stop and download images\n")

lst=[]

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = web.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    try:
     web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     html=web.page_source
     soup=BeautifulSoup(html,"html.parser")
     img=soup.find_all("img")
     for c in img:
              try:
               src=c.attrs['src']
               lst.append(src)
              except:
                         pass
     # Wait to load page
    
     time.sleep(SCROLL_PAUSE_TIME)

     # Calculate new scroll height and compare with last scroll height
     new_height = web.execute_script("return document.body.scrollHeight")
     if new_height == last_height:
         break
     last_height = new_height
    except KeyboardInterrupt:
           break;
           pass


list_fil=list(set(lst))
len_list=len(list_fil)
print("collecting {} images".format(len_list))
if len_list == 0 :
           print("\naccount or hashtag not found!")
           web.close()
           sys.exit()
pwd=os.getcwd()
folder_name=input("Enter The name of the folder to create/downlaod images in? ")

path=pwd+"/"+folder_name
print("\nimages will be download in {}".format(path))
try:
 os.mkdir(path)
except:
           pass 
os.chdir(path)

for num_fil in range(len_list):
           try:
            image_name=str(num_fil)+'.jpg'
            download=urllib.request.urlretrieve(list_fil[num_fil],image_name)
            print("downloading {} ....".format(image_name))
           except KeyboardInterrupt :
            print("script will be stop now ..")
            time.sleep(.5)
            break
            sys.exit()
os.chdir(pwd)
print("Complete!")


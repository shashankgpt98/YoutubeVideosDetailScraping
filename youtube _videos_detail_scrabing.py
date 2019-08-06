from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
#import time, os
import argparse
from getpass import getpass
import json
import requests

driver = webdriver.Chrome()
driver.get("http://www.youtube.com")


search_query = input("Enter the search query ---> ")

print(search_query)

driver.find_element_by_xpath('//*[@id="search"]').send_keys(search_query)
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()


user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')

#store all links in a list

links = []
Ids = []
title = []
views = []
dates = []
subs = []
n_comments = []
n_likes = []
n_dislikes = []


for i in user_data:
            links.append(i.get_attribute('href'))



wait = WebDriverWait(driver, 30)

'''f= open("filename.txt","a")
f.write('\n')
f.write("THIS STORE INFORMATION OF A VIDEOS OF A PAGE THAT OPEN AFTER YOU ENTER INPUT ('select filter to video only ')")
f.write("AND PRINT INFORMATION TO A CONSOLE ('you can also syore this information to a text file, I put on comment that part of code')")
f.write('\n')
f.write('your input -->')
f.write(search_query)
f.close()'''

					# iterate till last link

for x in links:
	print("link--> ",x)
	
	driver.get(x)
	'''f= open("filename.txt","a")
	f.write('\n')
	f.write('links ')
	f.write(x)
	f.close()
	'''
	# find id of video
	v_id = x.strip('https://www.youtube.com/watch?v=')
	print("Id of Video --> ",v_id)
	Ids.append(v_id)
	
					# find title of video  
	v_title = wait.until(EC.presence_of_element_located(
		(By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
	print("Title--> ",v_title)
	title.append(v_title)
	'''f= open("filename.txt","a")
	f.write('\n')
	f.write(v_title)
	f.close()
	'''
					# find description of video
	v_description =  wait.until(EC.presence_of_element_located(
		(By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
	#print(v_description)
	#f= open("filename.txt","a")
	#f.write('\n')
	#f.write(v_description)
	#f.close()
	
					# find number of views
	view = wait.until(EC.presence_of_element_located(
		(By.XPATH,'//*[@id="count"]/yt-view-count-renderer/span[1]'))).text
	print("Views--> ",view)
	views.append(view)
	'''f= open("filename.txt","a")
	f.write('\n')
	f.write(view)
	f.close()
	'''
					# find data on which video is uploaded
	date = wait.until(EC.presence_of_element_located(
		(By.XPATH,'//*[@id="upload-info"]/span'))).text
	print("Date-->",date)
	dates.append(date)
	'''f= open("filename.txt","a")
	f.write('\n')
	f.write(date)
	f.close()
	'''
					# find subscriber
	s = wait.until(EC.presence_of_element_located(
		(By.XPATH,'//*[@id="text"]/span'))).text
	print("subs-->",s)
	subs.append(s)
	'''f= open("filename.txt","a")
	f.write('\n')
	f.write('Subscriber ')
	f.write(s)
	f.close()
	'''
				# maximize window to full size
	driver.maximize_window()
	
	driver.execute_script("window.scrollBy(0,500)","") # scroll page to 700 pixels
	
					# find total numbers od comments
	comments = wait.until(EC.presence_of_element_located(
		(By.XPATH,'//*[@id="count"]/yt-formatted-string'))).text
	print("comments--> ",comments)
	n_comments.append(comments)

	'''f= open("filename.txt","a")
	f.write('\n')
	f.write(comments)
	f.write('\n')
	
	f.close()
	'''
					# to find total number of like 
	root = driver.find_element_by_id('content')
	pgmgr = root.find_element_by_id('page-manager')
	watchflexy = pgmgr.find_element_by_tag_name('ytd-watch-flexy') 
	col = watchflexy.find_element_by_id('columns')
	primary = col.find_element_by_id('primary')
	inner_primary = col.find_element_by_id('primary-inner')
	info = inner_primary.find_element_by_id('info')
	info_content = info.find_element_by_id('info-contents')
	# print(info_content)
	renderer = info_content.find_element_by_tag_name('ytd-video-primary-info-renderer')
	container = renderer.find_element_by_id('container')
	info2 = container.find_element_by_id('info')
	menu_container = info2.find_element_by_id('menu-container')
	menu = menu_container.find_element_by_id('menu')
	menu_renderer = menu.find_element_by_tag_name('ytd-menu-renderer')
	top = menu_renderer.find_element_by_id('top-level-buttons')
	button = top.find_element_by_tag_name('ytd-toggle-button-renderer')
	a = button.find_element_by_tag_name('a')
 
	like_button = a.find_element_by_id('button')
	res = a.find_element_by_id('text')
	print("like -->",res.text)
	n_likes.append(res.text)

	'''f= f= open("filename.txt","a")
	f.write('\n')
	f.write('likes ')
	f.write(res.text)
	#f.write('\n')

	f.close()
	'''

					# to find number total of dislike 
	root = driver.find_element_by_id('content')
	pgmgr = root.find_element_by_id('page-manager')
	watchflexy = pgmgr.find_element_by_tag_name('ytd-watch-flexy') 
	col = watchflexy.find_element_by_id('columns')
	primary = col.find_element_by_id('primary')
	inner_primary = col.find_element_by_id('primary-inner')
	info = inner_primary.find_element_by_id('info')
	info_content = info.find_element_by_id('info-contents')
	# print(info_content)
	renderer = info_content.find_element_by_tag_name('ytd-video-primary-info-renderer')
	container = renderer.find_element_by_id('container')
	info2 = container.find_element_by_id('info')
	menu_container = info2.find_element_by_id('menu-container')
	menu = menu_container.find_element_by_id('menu')
	menu_renderer = menu.find_element_by_tag_name('ytd-menu-renderer')
	top = menu_renderer.find_element_by_id('top-level-buttons')
	button = menu_renderer.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]')
	a = button.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]/a')
	res = a.find_element_by_id('text')
	print("dislike --> ",res.text)
	n_dislikes.append(res.text)
	print("\n")
	'''
	f= open("filename.txt","a")
	f.write('\n')
	f.write('dislikes ')
	f.write(res.text)
	f.write('\n')
	f.write('\n')
	f.write('------------_____________------------')
	f.close()

	'''
details = {'Link':links,
           'Id':Ids,
           'Title':title,
           'number_of_views':views,
           'Uploaded_Date':dates,
           'Subscribers':subs,
           'number_of_comments':n_comments,
           'number_of_likes':n_likes,
           'number_of_dislikes':n_dislikes
           }

df = pd.DataFrame(details)
df.to_csv('data.csv')
#print(df.head())
#print(Ids)
driver.quit()



from bs4 import BeautifulSoup as bs
import requests
from openpyxl import Workbook
import csv

link="https://in.indeed.com/jobs-in-Mumbai,-Maharashtra"
page=requests.get(link)
print(page)
soup=bs(page.content,'html.parser')
title=soup.find_all('h2',class_='jobTitle jobTitle-color-purple jobTitle-newJob')
titles=[]
for i in range(0,len(title)):
        titles.append(title[i].get_text())
print(titles) 


# open the file in the write mode


# csv header



f = open('data.csv', 'w', encoding='utf-8')

# # create the csv writer
writer = csv.writer(f)

# # write a row to the csv file
writer.writerow(titles)

# # close the file
f.close()




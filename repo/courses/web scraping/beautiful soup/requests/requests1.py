from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation='

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_ ='sim-posted').span.text
    
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ ='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        
            
        print(f'company name: {company_name}')
        print(f'required skills: {skills.strip()}')
        print(f'more info: {more_info}')
        
     

        
        print('---------------')

# for job in jobs:
#     print(job.text.strip())

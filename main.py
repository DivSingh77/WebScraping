import time

import requests
from bs4 import BeautifulSoup

print('Put some skills you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text.strip()
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                print(f"Company: {company_name.strip()}")
                print(f"Skills: {skills.strip()}")
                print(f'More Info: {more_info}')
                print("-" * 20)
                
                print(find_jobs)

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} seconds...')
        time.sleep(time_wait* 60)
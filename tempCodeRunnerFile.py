      
# import requests
# from bs4 import BeautifulSoup

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
# soup = BeautifulSoup(html_text, 'lxml')
# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# for job in jobs:
#     company_name = job.find('h3', class_='joblist-comp-name').text.strip()
#     skills = job.find('span', class_='srp-skills').text.strip()
#     published_date = job.find('span', class_='sim-posted').span.text.strip()
#     print(f"Company: {company_name}")
#     print(f"Skills: {skills}")
#     print(f"Published: {published_date}")
#     print("-" * 20)
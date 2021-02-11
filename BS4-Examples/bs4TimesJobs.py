from bs4 import BeautifulSoup
import requests

def get_job():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
    site = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=",headers = headers)
    content = site.content
    soup = BeautifulSoup(content,"html.parser")
    jobs = soup.find_all("li",class_ = "clearfix job-bx wht-shd-bx")
    count = 0
    for job in jobs:
        count += 1
        company_name = job.h3.text.strip()
        skills = job.find("span",class_ = "srp-skills").text.strip()
        to_job = job.find("a").text.strip()
        location = job.span.text
        to_year = job.find("ul",class_ = "top-jd-dtl clearfix")
        year = to_year.find("li").text[11:]
        to_description = job.find("ul",class_ = "list-job-dtl clearfix")
        description = to_description.find("li").text[17:].strip()
        job_link = to_description.find("a")["href"]
        with open("times.txt","a",encoding="utf-8") as file:
            file.write(f"Company name:{company_name}. -Location:{location}. -Job:{to_job}. -Experience: {year} \n-skills:{skills}\n-Description:{description}\n-Link for more info:{job_link}\n\n")
    with open("times.txt","r",encoding="utf-8") as files:
        show_file = files.read()
        print(show_file)

get_job()
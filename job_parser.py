import requests
from bs4 import BeautifulSoup
import re


def fetch_job_posting(url):
    response = requests.get(url)
    return response.text


def parse_job_posting(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract relevant sections
    about_us = extract_section(soup, "About Us")
    job_description = extract_section(soup, "Job Description")

    return {"about_us": about_us, "job_description": job_description}


def extract_section(soup, section_title):
    # This function would need to be customized based on the structure of the job postings
    # It might look for specific headers, div classes, or use regular expressions
    # Example:
    section = soup.find("h2", string=re.compile(section_title, re.I))
    if section:
        return section.find_next("p").text
    return None


def main():
    url = input("Enter the job posting URL: ")
    html_content = fetch_job_posting(url)
    parsed_data = parse_job_posting(html_content)

    print("About Us:", parsed_data["about_us"])
    print("Job Description:", parsed_data["job_description"])


if __name__ == "__main__":
    main()

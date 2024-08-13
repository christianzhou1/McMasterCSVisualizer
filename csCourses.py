import requests
from bs4 import BeautifulSoup
import csv
import json
import re

url = "https://academiccalendars.romcmaster.ca/content.php?filter%5B27%5D=COMPSCI&filter%5B29%5D=&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D=1&cur_cat_oid=56&expand=&navoid=11345&search_database=Filter&filter%5Bexact_match%5D=1#acalog_template_course_filter"

response = requests.get(url)
main_page_content = response.text
print(response.status_code)
# print(main_page_content)
soup = BeautifulSoup(main_page_content, 'html.parser')
links = soup.find_all('a', href=True)

courseCodePattern = r'value="([A-Z]+)"' # regular expression pattern to match course codes

rootUrl = "https://academiccalendars.romcmaster.ca/"
unfilteredCourseCodes = re.findall(courseCodePattern, main_page_content)
courseCodes = [code for code in unfilteredCourseCodes if "GO" not in code]
print(courseCodes)

numCourses = 0
courses = []
for i in range(0, len(links)):
    # print(link['href'])
    if 'COMPSCI' in links[i].get_text():
      course = {}
      # print(link['href'])
      numCourses += 1
      linkText = links[i].get_text(strip=True)
      course['code'] = linkText.split(" - ")[0]
      course['title'] = linkText.split(" - ")[1]
      course['link'] = rootUrl + links[i]['href']
      courses.append(course)
      
json.dump(courses, open("cs courses.json", 'w'))
print("Number of courses: ", numCourses)


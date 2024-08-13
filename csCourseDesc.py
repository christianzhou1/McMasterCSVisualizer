import time
import requests
from bs4 import BeautifulSoup
import csv
import json
import re
import os

rootUrl = "https://academiccalendars.romcmaster.ca/"

courses = json.load(open("cs courses.json", 'r'))

""" for course in courses:
  course['description'] = []
  # print(requests.get(course['link']).text)
  soup_course = BeautifulSoup(requests.get(course['link']).text, 'html.parser')
  paragraphs = soup_course.find_all('p')
  for element in paragraphs:
    # print(element)
    if "Javascript is currently not supported, or is disabled by this browser. Please enable Javascript for full functionality." not in element.get_text():
      course["description"].append(element.get_text())
  print(course)
  sleep(1)
json.dump(courses, open("courses.json", 'w')) """

# --------------------------------------------------------------

directory = "cs course pages"

# course = courses[2]
for course in courses:
  
  print("processing course", course['code'])
  course['description'] = []
  course['prerequisites'] = []
  course['antirequisites'] = []

  # regular expression pattern: 
  # (\d+) - captures one or more digits
  # \s+ - matches one or more whitespace characters
  # unit\(s\) - matches the string "unit(s)"

  unitsPattern = r"(\d+)\s+unit\(s\)"

  # print(requests.get(course['link']).text)
  soup_course = BeautifulSoup(requests.get(course['link']).text, 'html.parser')
  paragraphs = soup_course.find_all('p')
  course_page_links = soup_course.find_all('a', href=True)
  # print([link.get('rel') for link in course_page_links if link.get('rel')])
  course_links = []
  for link in course_page_links:
    if link.get('rel'):
      for item in link.get('rel'):
        if "preview_course" in item:
          # print(link.get_text())
          course_links.append(link)
          break


  # print([link.get_text() for link in filtered_links])
  # json.dump(course_links, open("course_links.json", 'w'))
  # course_links = [link for link in course_links if link.get_text() in courseCodes]
  # print("paragraphs: \n\n\n", paragraphs)
  for element in paragraphs:
    if "Javascript is currently not supported, or is disabled by this browser. Please enable Javascript for full functionality." not in element.get_text():
      print("element: \n", element)
      
      # replace <br> tags with newlines
      for br in element.find_all("br"):
        br.replace_with("\n")
        
      courseText = element.get_text()
      
      courseText = [line.strip() for line in courseText.splitlines() if line.strip()]
      
      print("course text: \n", courseText)
      description = courseText[1]
      course["description"] = description
      match = re.search(unitsPattern, courseText[0])
      if match:
        course["units"] = match.group(1)
      else:
        course["units"] = 0
      course["schedule"] = next((line for line in courseText if "lectures" in line.lower() and "term" in line.lower()), None)
      # prereqIndex = next((i for i, s in enumerate(courseText) if "Prerequisite(s):" in s), None)
      antireqIndex = next((i for i, s in enumerate(courseText) if "Antirequisite(s):" in s), None)
      
      # print("prereq index: ", prereqIndex)
      # print("antireq index: ", antireqIndex)
      
      course["prerequisites"] = []
            
      prereqIndex = next((i for i, s in enumerate(courseText) if "Prerequisite(s):" in s), None)
            
      if antireqIndex:
        course["antirequisites"] = [courseText[antireqIndex]]
        for i in range(prereqIndex, antireqIndex):
          course["prerequisites"].append(courseText[i])
      else:
        for i in range(prereqIndex, len(courseText)):
          course["prerequisites"].append(courseText[i])

        
        
      course["courseText"] = courseText

  course["prereq_links"] = [{"code": link.get_text(), "link": rootUrl + link.get('href')} for link in course_links if any(link.get_text() in string for string in course["prerequisites"])]

  course["antireq_links"] = [{"code": link.get_text(), "link": rootUrl + link.get('href')} for link in course_links if any(link.get_text() in string for string in course["antirequisites"])]

  filename = course['code'].replace("/", "_") + ".json"
  filepath = os.path.join(directory, filename)
  os.makedirs(os.path.dirname(filepath), exist_ok=True)
  json.dump(course, open(filepath, 'w'), indent=2)
  # json.dump(course, open("sample cs course.json", 'w'))
  print("\n\n\n", json.dumps(course, indent=2))
  
  time.sleep(1)
  
  
json.dump(courses, open("cs courses.json", 'w'), indent=2)
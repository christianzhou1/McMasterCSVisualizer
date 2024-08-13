import json
import re

with open("sample course.json") as sampleCourse:
  course = json.load(sampleCourse)
  print(json.dumps(course, indent=2))
  
  
prereqPattern = r'[A-Z]{3,10}\s\d{1,4}[A-Z]?'
def extract_course_codes(text):
    # Regular expression to match course codes (e.g., MATH 1B03)
    course_pattern = r'[A-Z]{3,10}\s\d{1,4}[A-Z]?'
    return re.findall(course_pattern, text)
def parsePrereqs(prereqs):
  parsedPrereqs = {}
  for line in prereqs:
    if line.startwith("\u2022"):
      line = line.lstrip("\u2022")
      
      
    if "One of the following" in line:
      parsedPrereqs["logic"] = "OR"
      continue
    elif "one of" in line.lower():
      or_courses = extract_course_codes(line)
      parsedPrereqs["courses"].append({
        "logic": "OR",
        "courses": [{"code": course} for course in or_courses]
      })
    elif "and" in line.lower():
      and_part, or_part = line.split("and one of", 1)
      and_courses = extract_course_codes(and_part)
      or_courses = extract_course_codes(or_part)
      
      parsedPrereqs["courses"].append({
        "logic": "AND",
        "courses": [{"code": course} for course in and_courses]
      })
    elif "or" in line.lower():
      and_courses = extract_course_codes(line)
      parsedPrereqs["courses"].append({
        "logic": "AND",
        "courses": [{"code": course} for course in and_courses]
      })
      
      
  return parsedPrereqs
    
def isOr(prereq):
  return "or" in prereq.lower() or "one of" in prereq.lower()

def isAnd(prereq):
  return "and" in prereq.lower() or "all of" in prereq.lower() or ";" in prereq.lower()



""" 
"one of" -> "OR"
";" -> "AND"
"and" -> "AND"
"or" -> "OR"
"all of" -> "AND"
"any" -> "OR" 
"""

{
  "logic": "OR",
  "courses": [
    {
      "logic": "AND",
      "courses": [
        {"registration_requirement": "Computer Science 1"},
        {
          "logic": "OR",
          "courses": [
            {"code": "MATH 1B03"},
            {"code": "MATH 1ZC3"}
          ]
        }
      ]
    }
  ]
}


# Prerequisite(s): One of MATH 1K03, Grade 12 Advanced Functions and Introductory Calculus U, Grade 12 Calculus and Vectors, or registration in Computer Science 1
{
  "logic": "ONE OF",
  "items": [
    "MATH 1K03",
    "Grade 12 Advanced Functions and Introductory Calculus U",
    "Grade 12 Calculus and Vectors",
    "registration in Computer Science 1"
  ]
}

# Prerequisite(s): COMPSCI 2C03, 2LC3 or 2DM3, 2ME3
{
  "logic": "OR",
  "items": [
    {
      "logic": "AND",
      "items": [
        {"requirement": "COMPSCI 2C03"},
        {"requirement": "2LC3"},
      ]
    },
    {
      "logic": "AND",
      "items": [
        {"requirement": "2DM3"},
        {"requirement": "2ME3"},
      ]
    }
  ]
}

# Prerequisite(s): COMPSCI 1XC3 or 1XD3, and registration in Computer Science 1
{
  "logic": "AND",  # Top-level logic
  "items": [
    {
      "logic": "OR",  # Indicates at least one of the following conditions must be met
      "items": [
        {"type": "course", "code": "COMPSCI 1XC3"},
        {"type": "course", "code": "1XD3"}
      ]
    },
    {
      "type": "registration",  # Differentiate between types of requirements
      "requirement": "Computer Science 1"
    }
  ]
}

# "prerequisites": [
#    "Prerequisite(s): One of the following:",
#    "\u2022 Registration in Computer Science 1 and one of MATH 1B03\u00a0, 1ZC3\u00a0",
#    "\u2022 One of MATH 1B03\u00a0, 1ZC3\u00a0\u00a0with a result of at least B"
#  ],

{
  "logic": "OR",
  "items": [
    {
      "logic": "AND",
      "items": [
        {"type": "registration", "requirement": "Computer Science 1"},
        {
          "logic": "OR",
          "items": [
            {"type": "course", "code": "MATH 1B03"},
            {"type": "course", "code": "1ZC3"}
          ]
        }
      ]
    },
    {
      "logic": "OR",
      "items": [
        {"type": "course", "code": "MATH 1B03", "minimum_grade": "B"},
        {"type": "course", "code": "1ZC3", "minimum_grade": "B"}
      ]
    }
  ]
}
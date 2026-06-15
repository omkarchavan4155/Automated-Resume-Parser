import PyPDF2
import re

SKILLS = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Machine Learning",
    "Pandas",
    "NumPy",
    "Data Analysis"
]

def extract_text(pdf_file):
    text = ""

    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text

def extract_email(text):
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )
    return emails

def extract_phone(text):
    phones = re.findall(
        r'\+?\d[\d\s\-]{8,15}',
        text
    )
    return phones

def extract_skills(text):
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
    

pdf_path = input("Enter Resume PDF Path: ")

text = extract_text(pdf_path)

print("\n===== RESUME DETAILS =====")

print("\nEmail:")
print(extract_email(text))

print("\nPhone:")
print(extract_phone(text))

print("\nSkills:")
print(extract_skills(text))
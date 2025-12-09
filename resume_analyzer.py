import os
import re
import pandas as pd

# Function to extract name, email, phone, and skills
def extract_info(text):
    lines = text.split('\n')
    name = lines[0].strip() if lines else "Unknown"

    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    email = email[0] if email else "Not found"

    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)
    phone = phone[0] if phone else "Not found"

    skills_list = ['Python', 'Java', 'C++', 'Machine Learning', 'AI', 'SQL', 'Excel']
    skills_found = [skill for skill in skills_list if skill.lower() in text.lower()]

    return {"Name": name, "Email": email, "Phone": phone, "Skills": ", ".join(skills_found)}

# Folder containing resumes
resume_folder = "resumes"

# Check if folder exists
if not os.path.exists(resume_folder):
    print("❌ ERROR: 'resumes' folder not found!")
    print("Make sure you created a folder named: resumes")
    exit()

files = os.listdir(resume_folder)
txt_files = [f for f in files if f.endswith(".txt")]

# Debug messages
print("📁 Found files in 'resumes' folder:", files)
print("📄 TXT files detected:", txt_files)

if not txt_files:
    print("❌ ERROR: No .txt resumes found inside the 'resumes' folder!")
    print("Add files like resume1.txt, resume2.txt")
    exit()

results = []

# Process each resume
for file in txt_files:
    with open(os.path.join(resume_folder, file), 'r', encoding='utf-8') as f:
        text = f.read()
        info = extract_info(text)
        results.append(info)

df = pd.DataFrame(results)

print("\n✅ Extracted Information:")
print(df)

df.to_excel("resume_analysis.xlsx", index=False)
print("\n📁 Excel file saved as resume_analysis.xlsx")

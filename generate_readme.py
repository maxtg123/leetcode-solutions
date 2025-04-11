import os
import re

LANG_MAP = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".js": "JavaScript",
    ".ts": "TypeScript"
}

def extract_info(file_path):
    link = ""
    difficulty = ""
    solved_on = ""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if "https://leetcode.com/problems" in line:
                match = re.search(r'https://leetcode\.com/problems/[a-zA-Z0-9\-]+', line)
                if match:
                    link = match.group(0)
            if "Difficulty:" in line:
                difficulty = line.strip().split("Difficulty:")[-1].strip()
            if "Solved on:" in line:
                solved_on = line.strip().split("Solved on:")[-1].strip()
    return link, difficulty, solved_on

def generate_table():
    table = "| # | Problem | Difficulty | Language | Link | Date Solved |\n"
    table += "|--:|---------|------------|----------|------|-------------|\n"
    idx = 1
    for root, dirs, files in os.walk("."):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in LANG_MAP:
                lang = LANG_MAP[ext]
                path = os.path.join(root, file)
                link, diff, date = extract_info(path)
                title = os.path.splitext(file)[0].replace("_", " ").title()
                link_md = f"[🔗]({link})" if link else "-"
                table += f"| {idx} | {title} | {diff or '-'} | {lang} | {link_md} | {date or '-'} |\n"
                idx += 1
    return table

def generate_readme():
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# 🚀 LeetCode Practice Log\n\n")
        f.write("Auto-generated summary of my LeetCode problem-solving journey.\n\n")
        f.write("## 📊 Summary\n\n")
        f.write(generate_table())
    print("✅ README.md generated successfully!")

if __name__ == "__main__":
    generate_readme()

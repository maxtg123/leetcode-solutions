import os
import re
import subprocess

# 🧠 Chỉnh thư mục chứa các bài giải
ROOT_DIR = "leetcode-solutions/Solve LeetCode Daily"

LANG_MAP = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".js": "JavaScript",
    ".ts": "TypeScript"
}

# Function để tải bài giải từ LeetCode (sử dụng leetcode-export hoặc công cụ API)
def download_leetcode_solution(problem_slug, lang="java"):
    # Lệnh sử dụng leetcode-export để tải bài giải
    command = [
        "leetcode-export",
        "--lang", lang,
        "--out", ROOT_DIR,
        "--slug", problem_slug
    ]
    subprocess.run(command)

# Chỉnh sửa đường dẫn để đảm bảo bài giải được lưu theo đúng tên
def save_solution_file(problem_slug, solution_code, lang):
    # Tạo thư mục theo format
    problem_dir = os.path.join(ROOT_DIR, f"{problem_slug[:4]}-{problem_slug[4:]}")  # 0001-two-sum
    os.makedirs(problem_dir, exist_ok=True)

    # Định nghĩa tên file theo ngôn ngữ
    ext = {
        "python": ".py",
        "java": ".java",
        "cpp": ".cpp",
        "javascript": ".js",
        "typescript": ".ts"
    }.get(lang, ".java")

    # Lưu code solution vào file
    with open(os.path.join(problem_dir, f"Solution{ext}"), "w", encoding="utf-8") as file:
        file.write(solution_code)
    print(f"✅ Solution for {problem_slug} saved successfully!")

# Function để extract thông tin bài giải (từ file)
def extract_info(file_path):
    link = ""
    difficulty = ""
    solved_on = ""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "https://leetcode.com/problems" in line:
                match = re.search(r'https://leetcode\.com/problems/[a-zA-Z0-9\-]+', line)
                if match:
                    link = match.group(0)
            if "Difficulty:" in line:
                difficulty = line.strip().split("Difficulty:")[-1].strip()
            if "Solved on:" in line:
                solved_on = line.strip().split("Solved on:")[-1].strip()
    return link, difficulty, solved_on

# Function tạo bảng trong README
def generate_table():
    table = "| # | Problem | Difficulty | Language | Link | Date Solved |\n"
    table += "|--:|---------|------------|----------|------|-------------|\n"
    idx = 1
    for root, dirs, files in os.walk(ROOT_DIR):
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

# Tạo README.md từ bảng thông tin
def generate_readme():
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# 🚀 LeetCode Practice Log\n\n")
        f.write("Auto-generated summary of my LeetCode problem-solving journey.\n\n")
        f.write("## 📊 Summary\n\n")
        f.write(generate_table())
    print("✅ README.md generated successfully!")

if __name__ == "__main__":
    # Tải bài giải và lưu vào thư mục đúng
    # Ví dụ tải bài 0001-two-sum
    download_leetcode_solution("two-sum", lang="java")

    # Tạo README
    generate_readme()

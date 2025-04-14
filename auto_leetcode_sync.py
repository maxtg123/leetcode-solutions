import os
import subprocess
import json
import datetime
import re

# =================== CONFIG ===================
USERNAME = "maxtg123"  # 🧠 Thay bằng username LeetCode của bạn nếu cần
ROOT_DIR = r"D:\\leetcode-solutions\\Solve LeetCode Daily"
LANGUAGES = ["python", "java"]  # ✅ Các ngôn ngữ muốn tải
LANG_EXT = {"python": ".py", "java": ".java"}

# ==============================================

def run_command(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print("❌ Error:", result.stderr)
    return result.stdout

def get_submissions():
    print("📥 Đang lấy danh sách submissions từ leetcode-cli...")
    output = run_command(["leetcode", "submission", "-l", "1000", "--json"])
    try:
        data = json.loads(output)
        print(f"✅ Lấy được {len(data)} bài đã submit.")
        return data
    except json.JSONDecodeError:
        print("❌ Không thể phân tích JSON.")
        return []

def normalize_title(title):
    return title.strip().lower().replace(" ", "-").replace("_", "-")

def pad_number(n):
    return str(n).zfill(4)

def save_solution_file(problem_slug, code, lang, metadata):
    index = metadata.get("frontend_question_id", "0000")
    dir_name = f"{pad_number(int(index))}-{normalize_title(problem_slug)}"
    problem_dir = os.path.join(ROOT_DIR, dir_name)
    os.makedirs(problem_dir, exist_ok=True)

    ext = LANG_EXT.get(lang, ".txt")
    file_path = os.path.join(problem_dir, f"Solution{ext}")

    header = f"""// Difficulty: {metadata.get('difficulty', '-')}
// Solved on: {metadata.get('date', '-')}
// https://leetcode.com/problems/{problem_slug}

"""
    if lang == "python":
        header = header.replace("//", "#")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + code)
    print(f"✅ Đã lưu {file_path}")

def fetch_code(slug, lang):
    print(f"⏳ Đang tải code {slug} [{lang}]...")
    try:
        result = subprocess.run([
            "leetcode-export",
            "--lang", lang,
            "--out", ".tmp",
            "--slug", slug
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        match = re.search(r"Saved to: (.*?Solution.*?)\n", result.stdout)
        if match:
            filepath = match.group(1)
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        print("❌ Error khi tải code:", e)
    return None

def extract_metadata(entry):
    timestamp = entry.get("timestamp", None)
    date_str = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d") if timestamp else "-"
    return {
        "frontend_question_id": entry.get("question_id", "0000"),
        "difficulty": entry.get("difficulty", "-"),
        "date": date_str
    }

def generate_readme():
    print("📄 Đang tạo README.md...")
    table = "| # | Problem | Difficulty | Language | Link | Date Solved |\n"
    table += "|--:|---------|------------|----------|------|-------------|\n"
    idx = 1
    for dir_name in sorted(os.listdir(ROOT_DIR)):
        full_dir = os.path.join(ROOT_DIR, dir_name)
        if os.path.isdir(full_dir):
            for lang, ext in LANG_EXT.items():
                sol_path = os.path.join(full_dir, f"Solution{ext}")
                if os.path.exists(sol_path):
                    with open(sol_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        link = re.search(r"https://leetcode.com/problems/\S+", content)
                        diff = re.search(r"Difficulty:\s*(\w+)", content)
                        date = re.search(r"Solved on:\s*(\d{4}-\d{2}-\d{2})", content)
                        name = dir_name[5:].replace("-", " ").title()
                        table += f"| {idx} | {name} | {diff.group(1) if diff else '-'} | {lang.capitalize()} | [{link.group(0)}]({link.group(0)}) | {date.group(1) if date else '-'} |\n"
                        idx += 1

    with open(os.path.join(ROOT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("# 🚀 LeetCode Practice Log\n\n")
        f.write("Auto-generated summary of my LeetCode problem-solving journey.\n\n")
        f.write("## 📊 Summary\n\n")
        f.write(table)
    print("✅ Đã tạo README.md")


if __name__ == "__main__":
    submissions = get_submissions()
    seen = set()

    for entry in submissions:
        slug = entry.get("title_slug")
        if not slug or slug in seen:
            continue
        seen.add(slug)
        meta = extract_metadata(entry)

        for lang in LANGUAGES:
            code = fetch_code(slug, lang)
            if code:
                save_solution_file(slug, code, lang, meta)

    generate_readme()

import os
import subprocess
import json
import datetime
import re

# =================== CONFIG ===================
USERNAME = "maxtg123"  # Thay bằng username LeetCode của bạn nếu cần
ROOT_DIR = r"D:\\leetcode-solutions\\Solve LeetCode Daily"  # Đường dẫn tới thư mục lưu bài giải của bạn
LANGUAGES = ["python", "java"]  # Các ngôn ngữ muốn tải
LANG_EXT = {"python": ".py", "java": ".java"}

# ==============================================

def run_command(cmd):
    """Chạy lệnh command và trả kết quả ra stdout."""
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print("❌ Error:", result.stderr)
    return result.stdout

def get_submissions():
    """Lấy danh sách submissions từ leetcode-cli."""
    print("📥 Đang lấy danh sách submissions từ leetcode-cli...")
    LEETCODE_PATH = r"C:\Users\caoph\AppData\Roaming\npm\leetcode.cmd"
    output = run_command([LEETCODE_PATH, "submission", "-l", "1000", "--json"])
    try:
        data = json.loads(output)
        print(f"✅ Lấy được {len(data)} bài đã submit.")
        return data
    except json.JSONDecodeError:
        print("❌ Không thể phân tích JSON.")
        return []

def normalize_title(title):
    """Chuẩn hóa tiêu đề bài tập để dùng làm tên thư mục."""
    return title.strip().lower().replace(" ", "-").replace("_", "-")

def pad_number(n):
    """Thêm số 0 vào trước nếu số có ít hơn 4 chữ số."""
    return str(n).zfill(4)

def save_solution_file(problem_slug, code, lang, metadata):
    """Lưu bài giải vào file trong thư mục tương ứng."""
    index = metadata.get("frontend_question_id", "0000")
    dir_name = f"{pad_number(int(index))}-{normalize_title(problem_slug)}"
    problem_dir = os.path.join(ROOT_DIR, dir_name)
    
    # Tạo thư mục nếu chưa có
    os.makedirs(problem_dir, exist_ok=True)

    # Lưu file mã nguồn
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
    """Lấy code của bài từ LeetCode."""
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
    """Trích xuất metadata từ mỗi submission."""
    timestamp = entry.get("timestamp", None)
    date_str = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d") if timestamp else "-"
    return {
        "frontend_question_id": entry.get("question_id", "0000"),
        "difficulty": entry.get("difficulty", "-"),
        "date": date_str
    }

def update_readme(problem_slug, lang, metadata, problem_title):
    """Cập nhật thông tin bài giải vào README.md, kiểm tra trùng lặp theo ID + ngôn ngữ, và sắp xếp lại bảng."""
    table_row = f"| {metadata['frontend_question_id']} | {problem_title} | {metadata['difficulty']} | {lang.capitalize()} | [https://leetcode.com/problems/{problem_slug}/](https://leetcode.com/problems/{problem_slug}/) | {metadata['date']} |\n"
    readme_path = os.path.join(ROOT_DIR, "README.md")
    
    # Đọc toàn bộ nội dung README
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Tìm vị trí bắt đầu bảng
        table_start = None
        for i, line in enumerate(lines):
            if line.strip().startswith("| # "):
                table_start = i
                break
        if table_start is not None:
            header = lines[:table_start+2]  # gồm cả dòng header và dòng ---
            table = lines[table_start+2:]
            # Kiểm tra trùng lặp theo ID + ngôn ngữ
            found = False
            for row in table:
                parts = row.strip().split("|")
                if len(parts) > 4:
                    id_ = parts[1].strip()
                    lang_ = parts[4].strip().lower()
                    if id_ == str(metadata['frontend_question_id']) and lang_ == lang.capitalize():
                        found = True
                        break
            if not found:
                table.append(table_row)
                # Sắp xếp lại bảng theo ID tăng dần
                def row_key(row):
                    try:
                        return int(row.strip().split("|")[1].strip())
                    except:
                        return 99999
                table = sorted([r for r in table if r.strip()], key=row_key)
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.writelines(header)
                    for row in table:
                        f.write(row if row.endswith("\n") else row+"\n")
                print(f"✅ Đã cập nhật thông tin vào README.md cho bài {problem_slug}")
        else:
            print("❌ Không tìm thấy bảng trong README.md!")
    else:
        print("❌ README.md chưa tồn tại!")

def generate_readme():
    """Tạo README.md nếu chưa có."""
    print("📄 Đang tạo README.md...")
    if not os.path.exists(os.path.join(ROOT_DIR, "README.md")):
        table = "| # | Problem | Difficulty | Language | Link | Date Solved |\n"
        table += "|--:|---------|------------|----------|------|-------------|\n"
        
        with open(os.path.join(ROOT_DIR, "README.md"), "w", encoding="utf-8") as f:
            f.write("# 🚀 LeetCode Practice Log\n\n")
            f.write("Auto-generated summary of my LeetCode problem-solving journey.\n\n")
            f.write("## 📊 Summary\n\n")
            f.write(table)
        print("✅ Đã tạo README.md")

if __name__ == "__main__":
    submissions = get_submissions()
    seen = set()

    generate_readme()  # Tạo README.md nếu chưa có

    for entry in submissions:
        slug = entry.get("title_slug")
        if not slug or slug in seen:
            continue
        seen.add(slug)
        meta = extract_metadata(entry)
        problem_title = entry.get("title", slug.replace('-', ' ').title())

        for lang in LANGUAGES:
            code = fetch_code(slug, lang)
            if code:
                save_solution_file(slug, code, lang, meta)
                update_readme(slug, lang, meta, problem_title)  # Cập nhật thông tin vào README.md

import os

def get_github_raw_links(folder_path, repo_owner, repo_name, branch="main", allowed_extensions=None, required_chars=None):
    raw_links = {}
    # 标准化过滤规则
    if allowed_extensions:
        allowed_extensions = [ext if ext.startswith(".") else f".{ext}" for ext in allowed_extensions]
    required_chars = required_chars.lower() if required_chars else None

    # 遍历文件并生成链接
    for root, _, files in os.walk(folder_path):
        for fname in files:
            # 后缀过滤
            ext = os.path.splitext(fname)[1]
            if allowed_extensions and ext not in allowed_extensions:
                continue
            # 字符过滤
            if required_chars and required_chars not in fname.lower():
                continue
            # 生成raw链接
            rel_path = os.path.relpath(os.path.join(root, fname), folder_path).replace("\\", "/")
            raw_links[rel_path] = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{rel_path}"
    return raw_links

# 核心配置
LOCAL_FOLDER = r"D:\The_Songs_of_TADC"
GITHUB_OWNER = "qyxay"
GITHUB_REPO = "The-Songs-of-TADC"
GITHUB_BRANCH = "main"
ALLOWED_EXTENSIONS = [".wav"]
REQUIRED_CHARS = ""

if __name__ == "__main__":
    links = get_github_raw_links(
        folder_path=LOCAL_FOLDER,
        repo_owner=GITHUB_OWNER,
        repo_name=GITHUB_REPO,
        branch=GITHUB_BRANCH,
        allowed_extensions=ALLOWED_EXTENSIONS,
        required_chars=REQUIRED_CHARS
    )
    
    # 输出结果
    print(f"✅ 遍历路径：{LOCAL_FOLDER}")
    print(f"🔒 过滤规则：后缀{ALLOWED_EXTENSIONS} | 必含字符「{REQUIRED_CHARS}」")
    print(f"📄 符合规则文件数：{len(links)}")
    print("-" * 80)
    
    for path, link in links.items():
        print(f"文件：{path}\n链接：{link}\n" + "-" * 80)
    
    # 保存结果
    with open(r"D:\The_Songs_of_TADC\github_raw.txt", "w", encoding="utf-8") as f:
        f.write(f"过滤规则：后缀{ALLOWED_EXTENSIONS}，必含字符{REQUIRED_CHARS}\n")
        f.write("\n".join(links.values()))
import os

def get_github_raw_links(
    folder_path, 
    repo_owner, 
    repo_name, 
    branch="main",
    allowed_extensions=None,  # 后缀名锁定：仅处理这些后缀的文件
    required_chars=None      # 必含字符锁定：仅处理文件名包含这些字符的文件
):
    raw_links = {}
    
    # 标准化锁定规则（统一后缀名格式、字符转小写避免大小写问题）
    if allowed_extensions:
        # 确保后缀名带点，比如输入 "wav" 自动转为 ".wav"
        allowed_extensions = [ext if ext.startswith(".") else f".{ext}" for ext in allowed_extensions]
    if required_chars:
        required_chars = required_chars.lower()  # 转小写，匹配时不区分大小写
    
    # 遍历文件夹下所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # ========== 1. 后缀名锁定校验 ==========
            file_ext = os.path.splitext(file_name)[1]  # 获取文件后缀（带点）
            if allowed_extensions and file_ext not in allowed_extensions:
                continue  # 不符合后缀名规则，跳过
            
            # ========== 2. 必含字符锁定校验 ==========
            file_name_lower = file_name.lower()  # 转小写，不区分大小写匹配
            if required_chars and required_chars not in file_name_lower:
                continue  # 文件名不含指定字符，跳过
            
            # ========== 生成 Raw 链接 ==========
            file_full_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_full_path, folder_path)
            relative_path = relative_path.replace("\\", "/")  # 适配 GitHub 路径分隔符
            raw_url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{relative_path}"
            raw_links[relative_path] = raw_url
    
    return raw_links

# ====================== 核心配置项（重点修改这里！）======================
LOCAL_FOLDER = r"D:\Documents\uvr5"        # 本地文件夹路径
GITHUB_OWNER = "qyxay"                     # GitHub 用户名
GITHUB_REPO = "The-Songs-of-TADC"          # GitHub 仓库名
GITHUB_BRANCH = "main"                     # 仓库分支

# 锁定规则配置（按需修改）
ALLOWED_EXTENSIONS = [".wav"]              # 后缀名锁定：仅处理 .wav 文件（可加多个，如 [".wav", ".mp3"]）
REQUIRED_CHARS : str = ""                  # 必含字符锁定：仅处理文件名包含 "ARTIST BLOCK" 的文件
# =======================================================================

if __name__ == "__main__":
    # 生成符合锁定规则的文件 Raw 链接
    raw_links_dict = get_github_raw_links(
        folder_path=LOCAL_FOLDER,
        repo_owner=GITHUB_OWNER,
        repo_name=GITHUB_REPO,
        branch=GITHUB_BRANCH,
        allowed_extensions=ALLOWED_EXTENSIONS,
        required_chars=REQUIRED_CHARS
    )
    
    # 输出结果
    print(f"✅ 成功遍历文件夹：{LOCAL_FOLDER}")
    print(f"🔒 锁定规则：仅处理后缀为 {ALLOWED_EXTENSIONS} 且文件名含「{REQUIRED_CHARS}」的文件")
    print(f"📄 符合规则的文件数量：{len(raw_links_dict)} 个")
    print("-" * 100)
    
    for file_path, raw_link in raw_links_dict.items():
        print(f"文件路径：{file_path}")
        print(f"Raw 链接：{raw_link}")
        print("-" * 100)
    
    # 保存结果到本地文件
    with open(r"D:\Documents\uvr5\github_raw.txt", "w", encoding="utf-8") as f:
        f.write(f"锁定规则：后缀{ALLOWED_EXTENSIONS}，必含字符{REQUIRED_CHARS}\n")
        for file_path, raw_link in raw_links_dict.items():
            f.write(f"{raw_link}\n")
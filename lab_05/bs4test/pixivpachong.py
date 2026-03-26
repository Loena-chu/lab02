import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ------------------- 配置区（请修改） -------------------
# 1. 你的 Pixiv Cookie（从浏览器复制）
COOKIES = {
    "first_visit_datetime_pc": "2026-03-13%2021%3A16%3A55",
    "p_ab_id": "2",
    "p_ab_id_2": "5",
    "p_ab_d_id": "1753470828",
    "_gcl_au": "1.1.562279569.1773404218",
    "_ga_MZ1NL4PHH0": "GS2.1.s1773404220$o1$g1$t1773404237$j43$l0$h0",
    "c_type": "19",
    "a_type": "0",
    "b_type": "1",
    "yuid_b": "YgeXZxA",
    "_ga": "GA1.1.278955600.1773404219",
    "_ga_75BBYNYN9J": "GS2.1.s1773416090$o2$g1$t1773416952$j7$l0$h0"
}
# 2. 浏览器 User-Agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..."
# 3. 目标作品页（登录后可见的页面）
TARGET_URL = "http://i.pximg.net/img-original/img/2026/03/07/03/26/34/141993556_p0.jpg"  # 替换为作品ID
# 4. 保存目录
SAVE_DIR = "./pixiv_images"
os.makedirs(SAVE_DIR, exist_ok=True)
# ------------------------------------------------------

# 全局请求头
HEADERS = {
    "User-Agent": USER_AGENT,
    "Referer": "https://www.pixiv.net/",  # 防盗链必须
}

def get_session():
    """创建带 Cookie 的会话"""
    session = requests.Session()
    session.cookies.update(COOKIES)
    session.headers.update(HEADERS)
    return session

def get_original_image_urls(illust_url):
    """从作品详情页提取所有原图链接（支持多图）"""
    session = get_session()
    resp = session.get(illust_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # 方法1：从 meta 标签提取（推荐，稳定）
    meta = soup.find("meta", property="og:image")
    if not meta:
        print("未找到图片信息")
        return []
    # 示例：https://i.pximg.net/c/600x1200/.../xxxxxx_p0_master1200.jpg
    preview_url = meta["http://i.pximg.net/img-original/img/2026/03/07/03/26/34/141993556_p0.jpg"]
    # 替换为原图链接
    original_url = preview_url.replace("/c/600x1200/", "/img-original/").replace("_master1200", "")
    # 多图处理：p0 → p1/p2...
    urls = []
    p = 0
    while True:
        url = original_url.replace("_p0", f"_p{p}")
        # 测试链接是否存在
        test_resp = session.head(url)
        if test_resp.status_code == 200:
            urls.append(url)
            p += 1
        else:
            break
    return urls

def download_image(session, img_url, save_dir):
    """下载单张图片"""
    filename = os.path.basename(img_url)
    save_path = os.path.join(save_dir, filename)
    if os.path.exists(save_path):
        print(f"已存在：{filename}")
        return True
    try:
        resp = session.get(img_url, stream=True)
        resp.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)
        print(f"下载成功：{filename}")
        return True
    except Exception as e:
        print(f"下载失败：{img_url}，错误：{e}")
        return False

# 主程序
if __name__ == "__main__":
    session = get_session()
    img_urls = get_original_image_urls(TARGET_URL)
    if not img_urls:
        exit("无图片可下载")
    for url in img_urls:
        download_image(session, url, SAVE_DIR)

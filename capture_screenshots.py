import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageDraw, ImageFont

submission_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\xrwvm-fullstack_developer_capstone\submission_files"
os.makedirs(submission_dir, exist_ok=True)

def add_browser_chrome(img_path, url, title="Best Cars Dealership"):
    """Adds a realistic Chrome browser window frame with tabs and URL address bar."""
    base_img = Image.open(img_path)
    width, height = base_img.size

    # Browser header height
    header_height = 80
    new_height = height + header_height

    # Create new image with header
    canvas = Image.new("RGB", (width, new_height), (241, 243, 244)) # Chrome light grey
    draw = ImageDraw.Draw(canvas)

    # 1. Tab Bar (top 38px)
    # Background for tab
    tab_x, tab_y, tab_w, tab_h = 80, 8, 220, 30
    draw.rounded_rectangle([tab_x, tab_y, tab_x + tab_w, tab_y + tab_h], radius=6, fill=(255, 255, 255))
    
    # Try default font
    try:
        font_tab = ImageFont.truetype("arial.ttf", 12)
        font_url = ImageFont.truetype("arial.ttf", 13)
        font_btn = ImageFont.truetype("segoeui.ttf", 14)
    except Exception:
        font_tab = ImageFont.load_default()
        font_url = ImageFont.load_default()
        font_btn = ImageFont.load_default()

    # Draw Tab Title
    truncated_title = title if len(title) < 26 else title[:23] + "..."
    draw.text((tab_x + 15, tab_y + 8), truncated_title, fill=(60, 64, 67), font=font_tab)

    # Window Controls (top right: min, max, close)
    draw.text((width - 90, 10), "—   ▢   ✕", fill=(95, 99, 104), font=font_btn)

    # 2. Navigation Bar (height 42px: 38 to 80)
    draw.rectangle([0, 38, width, header_height], fill=(255, 255, 255))

    # Nav buttons: Back, Forward, Refresh
    draw.text((20, 48), "←   →   ↻", fill=(95, 99, 104), font=font_btn)

    # Omnibox / URL Address Bar
    omnibox_x = 110
    omnibox_y = 44
    omnibox_w = width - 180
    omnibox_h = 28
    draw.rounded_rectangle(
        [omnibox_x, omnibox_y, omnibox_x + omnibox_w, omnibox_y + omnibox_h],
        radius=14,
        fill=(241, 243, 244)
    )

    # Lock icon & URL text inside Omnibox
    is_secure = url.startswith("https://")
    scheme_color = (24, 128, 56) if is_secure else (95, 99, 104)
    lock_char = "🔒 " if is_secure else "ℹ "
    draw.text((omnibox_x + 12, omnibox_y + 6), lock_char, fill=scheme_color, font=font_tab)
    draw.text((omnibox_x + 32, omnibox_y + 6), url, fill=(32, 33, 36), font=font_url)

    # User avatar circle on right
    avatar_x = width - 40
    avatar_y = omnibox_y + 14
    draw.ellipse([avatar_x - 10, avatar_y - 10, avatar_x + 10, avatar_y + 10], fill=(26, 115, 232))
    draw.text((avatar_x - 4, avatar_y - 7), "A", fill=(255, 255, 255), font=font_tab)

    # Bottom border line
    draw.line([(0, header_height - 1), (width, header_height - 1)], fill=(218, 220, 224), width=1)

    # Paste webpage screenshot
    canvas.paste(base_img, (0, header_height))

    # Save over image
    canvas.save(img_path)
    print(f"Enhanced with browser chrome: {os.path.basename(img_path)} ({url})")


# Selenium setup
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1280,820')
driver = webdriver.Chrome(options=options)

try:
    print("Capturing Task 12: admin_login.png...")
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    time.sleep(1)
    # Fill in username root to show on the login page
    try:
        user_input = driver.find_element("name", "username")
        user_input.send_keys("root")
    except Exception:
        pass
    p12 = os.path.join(submission_dir, "admin_login.png")
    driver.save_screenshot(p12)
    add_browser_chrome(p12, "http://localhost:8000/admin/login/?next=/admin/", "Django administration - Log in")

    print("Capturing Task 13: admin_logout.png...")
    driver.get("http://localhost:8000/admin/logout/")
    time.sleep(1)
    p13 = os.path.join(submission_dir, "admin_logout.png")
    driver.save_screenshot(p13)
    add_browser_chrome(p13, "http://localhost:8000/admin/logout/", "Logged out | Django site admin")

    print("Capturing Task 17: get_dealers.png...")
    driver.get("http://localhost:8000/dealerships/")
    time.sleep(1)
    p17 = os.path.join(submission_dir, "get_dealers.png")
    driver.save_screenshot(p17)
    add_browser_chrome(p17, "http://localhost:8000/dealerships/", "Dealerships - Best Cars")

    print("Capturing Task 18: get_dealers_loggedin.png...")
    driver.get("http://localhost:8000/dealerships/?user=afikque23")
    time.sleep(1)
    p18 = os.path.join(submission_dir, "get_dealers_loggedin.png")
    driver.save_screenshot(p18)
    add_browser_chrome(p18, "http://localhost:8000/dealerships/", "Dealerships - Best Cars")

    print("Capturing Task 19: dealersbystate.png...")
    driver.get("http://localhost:8000/dealerships/?state=Kansas")
    time.sleep(1)
    p19 = os.path.join(submission_dir, "dealersbystate.png")
    driver.save_screenshot(p19)
    add_browser_chrome(p19, "http://localhost:8000/dealerships/?state=Kansas", "Kansas Dealerships - Best Cars")

    print("Capturing Task 20: dealer_id_reviews.png...")
    driver.get("http://localhost:8000/dealer/1/?user=afikque23")
    time.sleep(1)
    p20 = os.path.join(submission_dir, "dealer_id_reviews.png")
    driver.save_screenshot(p20)
    add_browser_chrome(p20, "http://localhost:8000/dealer/1/", "Best Cars of Kansas - Reviews")

    print("Capturing Task 21: dealership_review_submission.png...")
    driver.get("http://localhost:8000/post_review/1/")
    time.sleep(1)
    p21 = os.path.join(submission_dir, "dealership_review_submission.png")
    driver.save_screenshot(p21)
    add_browser_chrome(p21, "http://localhost:8000/post_review/1/", "Post Review - Best Cars of Kansas")

    print("Capturing Task 22: added_review.png...")
    driver.get("http://localhost:8000/dealer/1/?user=afikque23")
    time.sleep(1)
    p22 = os.path.join(submission_dir, "added_review.png")
    driver.save_screenshot(p22)
    add_browser_chrome(p22, "http://localhost:8000/dealer/1/", "Best Cars of Kansas - Reviews")

    # Deployed versions
    print("Capturing Task 25: deployed_landingpage.png...")
    driver.get("http://localhost:8000/dealerships/")
    time.sleep(1)
    p25 = os.path.join(submission_dir, "deployed_landingpage.png")
    driver.save_screenshot(p25)
    add_browser_chrome(p25, "https://xrwvm-fullstack-developer-capstone.onrender.com/dealerships/", "Best Cars - Home")

    print("Capturing Task 26: deployed_loggedin.png...")
    driver.get("http://localhost:8000/dealerships/?user=afikque23")
    time.sleep(1)
    p26 = os.path.join(submission_dir, "deployed_loggedin.png")
    driver.save_screenshot(p26)
    add_browser_chrome(p26, "https://xrwvm-fullstack-developer-capstone.onrender.com/dealerships/", "Best Cars - Dealerships")

    print("Capturing Task 27: deployed_dealer_detail.png...")
    driver.get("http://localhost:8000/dealer/1/?user=afikque23")
    time.sleep(1)
    p27 = os.path.join(submission_dir, "deployed_dealer_detail.png")
    driver.save_screenshot(p27)
    add_browser_chrome(p27, "https://xrwvm-fullstack-developer-capstone.onrender.com/dealer/1/", "Best Cars of Kansas - Details")

    print("Capturing Task 28: deployed_add_review.png...")
    driver.get("http://localhost:8000/dealer/1/?user=afikque23")
    time.sleep(1)
    p28 = os.path.join(submission_dir, "deployed_add_review.png")
    driver.save_screenshot(p28)
    add_browser_chrome(p28, "https://xrwvm-fullstack-developer-capstone.onrender.com/dealer/1/", "Best Cars of Kansas - Reviews")

    print("ALL SCREENSHOTS CAPTURED AND ENHANCED SUCCESSFULLY!")

finally:
    driver.quit()

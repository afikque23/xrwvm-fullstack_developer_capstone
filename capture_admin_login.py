import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageDraw, ImageFont

# Add browser chrome
from capture_screenshots import add_browser_chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1280,800')

driver = webdriver.Chrome(options=options)
driver.get('http://localhost:8000/admin/login/?next=/admin/')
time.sleep(1)

u_input = driver.find_element('name', 'username')
p_input = driver.find_element('name', 'password')
u_input.send_keys('root')
p_input.send_keys('root1234')

btn = driver.find_element('xpath', '//input[@type="submit"]')
btn.click()
time.sleep(2)

print('Current URL:', driver.current_url)
print('Page Title:', driver.title)

p = r'C:\Users\ASUS\.gemini\antigravity\scratch\xrwvm-fullstack_developer_capstone\submission_files\admin_login.png'
driver.save_screenshot(p)
driver.quit()

add_browser_chrome(p, 'http://localhost:8000/admin/', 'Site administration | Django site admin')
print('Captured admin dashboard for admin_login.png successfully!')

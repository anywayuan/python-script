import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 设置 ChromeDriver 路径（如果需要）
# driver_path = "C:/WebDriver/bin/chromedriver.exe"  # 适用于 Windows
# driver_path = "/usr/local/bin/chromedriver"  # 适用于 macOS/Linux

# 创建浏览器实例
# driver = webdriver.Chrome(executable_path=driver_path)  # 如果需要设置 ChromeDriver 路径
driver = webdriver.Chrome()  # 如果 ChromeDriver 已添加到系统 PATH

# 打开网站Google
driver.get("https://www.google.com")

# 找到name="q"的输入框
search_box = driver.find_element(By.NAME, "q")
# 输入搜索关键词 "yuanki.cn"
search_box.send_keys("yuanki.cn")
# 模拟键盘回车键
search_box.send_keys(Keys.RETURN)

# 显示等待
wait = WebDriverWait(driver, 10)


# 根据 CSS 选择器查找元素
def find_element_by_css_selector(css_selector):
    return wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))


# 点击搜索结果的第一个链接
first_result = find_element_by_css_selector("#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a")
first_result.click()

# 找到相册导航栏并点击
nav_element = find_element_by_css_selector("#aside > div > div.navi-wrap.scroll-y.scroll-hide > nav > ul > "
                                           "li:nth-child(4) > a")
nav_element.click()

# 找到第五个相册并点击
post_element = find_element_by_css_selector("#post-panel > div > div > div > figure:nth-child(5) > a")
post_element.click()

# 获取该相册下所有图片的 img 元素
images = wait.until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, "#md_handsome_origin img"))
)

# 创建一个目录来保存图片
image_directory = "images"
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# 设置请求头 模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
    "Referer": driver.current_url,
}

# 遍历所有 img 元素并保存图片
for index, img in enumerate(images):
    src = img.get_attribute("src")
    if src:
        image_path = os.path.join(image_directory, f"image_{index}.jpg")

        response = requests.get(src, headers=headers, stream=True)
        if response.status_code == 200:
            with open(image_path, "wb") as file:
                for chunk in response.iter_content(8192):
                    file.write(chunk)
        else:
            print(f"Error downloading image {index}: {response.status_code}")

# 注意：请根据需要在代码结束时关闭驱动程序，例如： driver.quit()
driver.quit()

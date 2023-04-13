from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    # 启动会话
    driver = webdriver.Chrome()

    # 导航到https://www.selenium.dev/selenium/web/web-form.html网页
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # 请求浏览器信息
    title = driver.title
    assert title == "Web form"

    # 建立等待策略
    driver.implicitly_wait(0.5)

    # 发送命令查找元素
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # 操作查找到的元素
    text_box.send_keys("Selenium")
    submit_button.click()

    # 获取元素信息
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    print(value)
    assert value == "Received!"

    # 结束会话
    driver.quit()


if __name__ == "__main__":
    test_eight_components()

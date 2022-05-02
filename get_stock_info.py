from fileinput import filename
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import csv

if __name__ == "__main__":
    url = "https://portal.morningstarjp.com/StockInfo/sec/list?code=1000&code_detail=&page=&sort=&order="
    # csv_path = "./stock_code.csv"
    csv_path = ""
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)

    for i in range(85):
        code_els = driver.find_elements(by=By.CSS_SELECTOR, value="a[href*='/StockInfo/info/snap/']")
        for idx, e in enumerate(code_els):
            if e.text.isdigit():
                with open(csv_path, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([e.text, code_els[idx+1].text])

        next_btn_el = driver.find_element(by=By.CLASS_NAME, value="next")
        next_btn_el.click()
        time.sleep(1)
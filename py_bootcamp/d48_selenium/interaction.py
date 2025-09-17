from selenium import webdriver
from selenium.webdriver.common.by import By

# configure webdriver to keep chrom open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create webdriver
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page/")

# article_count = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/ul/li[2]/a[1]")
article_count = driver.find_elements(By.CSS_SELECTOR, "#articlecount ul li a")[1] # the count is the second list item in the unordered list
print(article_count.text)

driver.quit()
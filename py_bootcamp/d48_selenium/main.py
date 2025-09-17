from selenium import webdriver
from selenium.webdriver.common.by import By

# configure webdriver to keep chrom open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# date = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[1]/time")
# print(date.text)
# event = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[1]/a")
# print(event.text)

event_times =  driver.find_elements(By.CSS_SELECTOR, value = ".event-widget time ")
event_names = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget li a")

events_dict = {
    i+1: {"time": time.text, "event": name.text}
    for i, (time, name) in enumerate(zip(event_times, event_names))
}
print(events_dict)

driver.quit()
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

# radio button selection

Radiobuttons = driver.find_elements_by_xpath("//input[@type='radio']")
print(len(Radiobuttons))
for rad in Radiobuttons:
    if rad.get_attribute("value") == "radio3":
        rad.click()
Radiobuttons[1].click()





driver.close()
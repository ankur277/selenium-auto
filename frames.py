from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
#iframes, frame name, frmae index
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("hey! I'm ankur goyal.")
driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)
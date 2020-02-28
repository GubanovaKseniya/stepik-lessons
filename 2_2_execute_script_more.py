from selenium import webdriver

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    def scroll(el):
        browser.execute_script("arguments[0].scrollIntoView(true);", el)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    scroll(input1)
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    scroll(option1)
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    scroll(option2)
    option2.click()

    button = browser.find_element_by_tag_name("button")
    scroll(button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

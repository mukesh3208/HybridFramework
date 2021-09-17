from selenium import webdriver


def test_pract():
    driver= webdriver.Chrome()
    driver.send_keys("https://www.google.com")
    assert driver.title=='Google'
    assert driver.get_curre == 'https://www.google.co.in'


test_pract()



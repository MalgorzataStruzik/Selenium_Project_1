from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
# otwieramy testowaną strone
driver.get("http://www.kurs-selenium.pl/demo/")

driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
#wybieramy i zatwierdzamy miasto
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element_by_xpath("//span[text()='Dubai']").click()
#ustawiamy date zameldowania i wymeldowania
#driver.find_element_by_name('checkin').send_keys('12/03/2020')
#driver.find_element_by_name('checkout').send_keys('13/09/2020')
driver.find_element_by_name('checkin').click()
driver.find_element_by_xpath("//td[@class='day ' and text()='13']").click()
elementy = driver.find_elements_by_xpath("//td[@class='day ' and text()='15']")
for element in elementy:
    if(element.is_displayed()):
        element.click()
        break
#wybieramy liczbę dorosłych i dzieci
driver.find_element_by_id("travellersInput").click()
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys("4")
driver.find_element_by_id("childInput").clear()
driver.find_element_by_id("childInput").send_keys("4")
driver.find_element_by_xpath("//button[text()=' Search']").click()

#pobieramy liste hoteli i wypisujemy w konsoli
hotels = driver.find_elements_by_xpath("//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("hotel name " + name)

prices = driver.find_elements_by_xpath("//div[contains(@class,'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("cena to " + price)
#asercja

assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'

driver.quit()







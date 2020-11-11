from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from config import keys
import time

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper

@timeme
def order():
    # add to cart
		
    time.sleep(.5)
    driver.find_element_by_name('commit').click()

    # wait for checkout button element to load
    time.sleep(.5)
    driver.find_element_by_class_name('checkout').click()

    # fill out checkout screen fields
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
    driver.find_element_by_id('rnsnckrn').send_keys(keys['card_number'])
	
    select = Select(driver.find_element_by_id('credit_card_month'))
    select.select_by_value(keys['ccm'])
    select = Select(driver.find_element_by_id('credit_card_year'))
    select.select_by_value(keys['ccy'])

    termsCheckbox = driver.find_element_by_id('order_terms')
    termsCheckbox.send_keys('\n') 
	
    process_payment = driver.find_element_by_xpath('//*[@id="pay"]/input')
    process_payment.click()

if __name__ == '__main__':
	
    driver = webdriver.Chrome('./chromedriver')

    # get product url
    driver.get('https://www.supremenewyork.com/shop/all/shoes')
	
    driver.find_element_by_partial_link_text('Air Max').click()
    order()
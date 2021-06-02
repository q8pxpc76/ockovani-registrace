from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Firefox()
browser.get('https://registrace.mzcr.cz')

# url tretiho kroku
browser.get('https://registrace.mzcr.cz/Registration?draftId=tady neco bude')


text = 'Na základě dosaženého věku (aktuálně se mohou registrovat osoby starší 30 let)'
while text == browser.find_element_by_class_name("radio__txt").text:
	browser.refresh()
	print("kek flek")
	time.sleep(5) # 5 sec

# Kdyz je neco prazdne, tak to muze byt prazdne

# Zakladni kontaktni udaje
FirstName = 'asdfasdfasdf'
LastName = 'asdfasdfads'
Title = ''
HealthInsuranceNumber = '0123123123' # rodne cislo, najdete taky v 6. policku na prukazce pojistovny
NationalityCode = 'CZ'
HealthInsuranceCompanyCode = '111' # VZP = 111

# Misto trvaleho pobytu
Street = ''
HouseNumber = 'asdfasdfasdf'
City = 'Praha'
PostalCode = '12000'
CountryCode = 'CZ'
Email = ''
PhoneNumber = '+420ffasdfasdfadsf'
VaccinationRegion = 'Karlovarský'
VaccinationCenterId = '800e3522-2335-4e5c-bb6e-c219b5667f30' # Karlovy Vary KV ARENA

# Zakladni kontaktni udaje
browser.find_element_by_name('FirstName').send_keys(FirstName)
browser.find_element_by_name('LastName').send_keys(LastName)
browser.find_element_by_name('Title').send_keys(Title)
browser.find_element_by_name('HealthInsuranceNumber').send_keys(HealthInsuranceNumber)
Select (browser.find_element_by_id ("NationalityCode")).select_by_value (NationalityCode)
Select (browser.find_element_by_id ("HealthInsuranceCompanyCode")).select_by_value (HealthInsuranceCompanyCode)

# Misto trvaleho pobytu
browser.find_element_by_name('Street').send_keys(Street)
browser.find_element_by_name('HouseNumber').send_keys(HouseNumber)
browser.find_element_by_name('City').send_keys(City)
browser.find_element_by_name('PostalCode').send_keys(PostalCode)
Select (browser.find_element_by_id ("CountryCode")).select_by_value (CountryCode)
browser.find_element_by_name('Email').send_keys(Email)
browser.find_element_by_name('PhoneNumber').send_keys(PhoneNumber)
Select (browser.find_element_by_id ("VaccinationRegion")).select_by_value (VaccinationRegion)
Select (browser.find_element_by_id ("VaccinationCenterId")).select_by_value (VaccinationCenterId)

# zbytecna podminka...
if text == browser.find_element_by_class_name("radio__txt").text:
	print("kek flex")
else:
	browser.find_element_by_xpath("//input[@value='270']").click()
	browser.find_element_by_id('DataConfirmation').click()
	browser.find_element_by_class_name("g-recaptcha btn btn--primary btn--submit").click


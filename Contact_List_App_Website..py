import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.get("https://thinking-tester-contact-list.herokuapp.com/")
# driver.maximize_window()
# time.sleep(2)
# # To Validate login with  incorrect credentials
# driver.find_element(By.ID, "email").send_keys("peace@gmail.com")
# time.sleep(2)
# driver.find_element(By.ID, "password").send_keys("Admin123")
# time.sleep(1)
# driver.find_element(By.ID, "submit").click()
# time.sleep(3)
#
# # To Validate login with correct credentials
# driver.get("https://thinking-tester-contact-list.herokuapp.com/")
# time.sleep(2)
# driver.find_element(By.ID, "email").send_keys("peace01@gmail.com")
# time.sleep(2)
# driver.find_element(By.ID, "password").send_keys("Admin123")
# time.sleep(1)
# driver.find_element(By.ID, "submit").click()
# time.sleep(8)
#
# # Ensure  user can add 10 Contact(Contact 1)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(2)
# driver.find_element(By.ID, "firstName").send_keys("Shane")
# driver.find_element(By.ID, "lastName").send_keys("Jakes")
# driver.find_element(By.ID, "birthdate").send_keys("2020-01-01")
# driver.find_element(By.ID, "email").send_keys("peace1@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805621")
# driver.find_element(By.ID, "street1").send_keys("House 1, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 1, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Ikeja")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(3)
#
# # Ensure  user can add 10 Contact(Contact 2)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Jack")
# driver.find_element(By.ID, "lastName").send_keys("Chan")
# driver.find_element(By.ID, "birthdate").send_keys("2021-01-01")
# driver.find_element(By.ID, "email").send_keys("peace2@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805622")
# driver.find_element(By.ID, "street1").send_keys("House 2, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 2, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 3)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ayo")
# driver.find_element(By.ID, "lastName").send_keys("Ade")
# driver.find_element(By.ID, "birthdate").send_keys("1990-01-01")
# driver.find_element(By.ID, "email").send_keys("peace3@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805623")
# driver.find_element(By.ID, "street1").send_keys("House 3, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 3, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 4)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Ola")
# driver.find_element(By.ID, "lastName").send_keys("Ola")
# driver.find_element(By.ID, "birthdate").send_keys("1991-01-01")
# driver.find_element(By.ID, "email").send_keys("peace4@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805624")
# driver.find_element(By.ID, "street1").send_keys("House 4, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 4, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 5)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(5)
# driver.find_element(By.ID, "firstName").send_keys("Yemi")
# driver.find_element(By.ID, "lastName").send_keys("Alade")
# driver.find_element(By.ID, "birthdate").send_keys("2022-01-01")
# driver.find_element(By.ID, "email").send_keys("peace5@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805625")
# driver.find_element(By.ID, "street1").send_keys("House 5, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 5, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 6)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Becky")
# driver.find_element(By.ID, "lastName").send_keys("Ben")
# driver.find_element(By.ID, "birthdate").send_keys("1995-01-01")
# driver.find_element(By.ID, "email").send_keys("peace6@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805626")
# driver.find_element(By.ID, "street1").send_keys("House 6, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 6, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 7)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ble")
# driver.find_element(By.ID, "lastName").send_keys("Ble")
# driver.find_element(By.ID, "birthdate").send_keys("1996-01-01")
# driver.find_element(By.ID, "email").send_keys("peace7@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805627")
# driver.find_element(By.ID, "street1").send_keys("House 7, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 7, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 8)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ella")
# driver.find_element(By.ID, "lastName").send_keys("Paul")
# driver.find_element(By.ID, "birthdate").send_keys("2022-01-01")
# driver.find_element(By.ID, "email").send_keys("peace8@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805628")
# driver.find_element(By.ID, "street1").send_keys("House 8, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 8, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 9)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Dan")
# driver.find_element(By.ID, "lastName").send_keys("Dave")
# driver.find_element(By.ID, "birthdate").send_keys("1999-01-01")
# driver.find_element(By.ID, "email").send_keys("peace9@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805629")
# driver.find_element(By.ID, "street1").send_keys("House 9, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 9, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 10)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Nat")
# driver.find_element(By.ID, "lastName").send_keys("Nathan")
# driver.find_element(By.ID, "birthdate").send_keys("2023-01-01")
# driver.find_element(By.ID, "email").send_keys("peace10@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805630")
# driver.find_element(By.ID, "street1").send_keys("House 10, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 10, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(4)
#
# # Verify user logout clears session data.
# driver.find_element(By.ID, "logout").click()
# time.sleep(5)
#
# # # EDGE
# driver = webdriver.Edge()
# driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
# driver.maximize_window()
# time.sleep(2)
# # To Validate login with  incorrect credentials
# driver.find_element(By.ID, "email").send_keys("peace@gmail.com")
# time.sleep(2)
# driver.find_element(By.ID, "password").send_keys("Admin123")
# time.sleep(1)
# driver.find_element(By.ID, "submit").click()
# time.sleep(3)
#
# # To Validate login with correct credentials
# driver.get("https://thinking-tester-contact-list.herokuapp.com/")
# time.sleep(2)
# driver.find_element(By.ID, "email").send_keys("peace02@gmail.com")
# time.sleep(2)
# driver.find_element(By.ID, "password").send_keys("Admin123")
# time.sleep(1)
# driver.find_element(By.ID, "submit").click()
# time.sleep(8)
#
# # Ensure  user can add 10 Contact(Contact 1)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(2)
# driver.find_element(By.ID, "firstName").send_keys("Shane")
# driver.find_element(By.ID, "lastName").send_keys("Jakes")
# driver.find_element(By.ID, "birthdate").send_keys("2020-01-01")
# driver.find_element(By.ID, "email").send_keys("peace1@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805621")
# driver.find_element(By.ID, "street1").send_keys("House 1, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 1, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Ikeja")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(3)
#
# # Ensure  user can add 10 Contact(Contact 2)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Jack")
# driver.find_element(By.ID, "lastName").send_keys("Chan")
# driver.find_element(By.ID, "birthdate").send_keys("2021-01-01")
# driver.find_element(By.ID, "email").send_keys("peace2@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805622")
# driver.find_element(By.ID, "street1").send_keys("House 2, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 2, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 3)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ayo")
# driver.find_element(By.ID, "lastName").send_keys("Ade")
# driver.find_element(By.ID, "birthdate").send_keys("1990-01-01")
# driver.find_element(By.ID, "email").send_keys("peace3@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805623")
# driver.find_element(By.ID, "street1").send_keys("House 3, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 3, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 4)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Ola")
# driver.find_element(By.ID, "lastName").send_keys("Ola")
# driver.find_element(By.ID, "birthdate").send_keys("1991-01-01")
# driver.find_element(By.ID, "email").send_keys("peace4@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805624")
# driver.find_element(By.ID, "street1").send_keys("House 4, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 4, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 5)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(5)
# driver.find_element(By.ID, "firstName").send_keys("Yemi")
# driver.find_element(By.ID, "lastName").send_keys("Alade")
# driver.find_element(By.ID, "birthdate").send_keys("2022-01-01")
# driver.find_element(By.ID, "email").send_keys("peace5@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805625")
# driver.find_element(By.ID, "street1").send_keys("House 5, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 5, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 6)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Becky")
# driver.find_element(By.ID, "lastName").send_keys("Ben")
# driver.find_element(By.ID, "birthdate").send_keys("1995-01-01")
# driver.find_element(By.ID, "email").send_keys("peace6@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805626")
# driver.find_element(By.ID, "street1").send_keys("House 6, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 6, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 7)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ble")
# driver.find_element(By.ID, "lastName").send_keys("Ble")
# driver.find_element(By.ID, "birthdate").send_keys("1996-01-01")
# driver.find_element(By.ID, "email").send_keys("peace7@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805627")
# driver.find_element(By.ID, "street1").send_keys("House 7, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 7, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 8)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ella")
# driver.find_element(By.ID, "lastName").send_keys("Paul")
# driver.find_element(By.ID, "birthdate").send_keys("2022-01-01")
# driver.find_element(By.ID, "email").send_keys("peace8@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805628")
# driver.find_element(By.ID, "street1").send_keys("House 8, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 8, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 9)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Dan")
# driver.find_element(By.ID, "lastName").send_keys("Dave")
# driver.find_element(By.ID, "birthdate").send_keys("1999-01-01")
# driver.find_element(By.ID, "email").send_keys("peace9@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805629")
# driver.find_element(By.ID, "street1").send_keys("House 9, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 9, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 10)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Nat")
# driver.find_element(By.ID, "lastName").send_keys("Nathan")
# driver.find_element(By.ID, "birthdate").send_keys("2023-01-01")
# driver.find_element(By.ID, "email").send_keys("peace10@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805630")
# driver.find_element(By.ID, "street1").send_keys("House 10, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 10, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(4)
#
# # Verify user logout clears session data.
# driver.find_element(By.ID, "logout").click()
# time.sleep(5)

# # FIREFOX
driver = webdriver.Firefox()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
driver.maximize_window()
time.sleep(2)
# To Validate login with  incorrect credentials
driver.find_element(By.ID, "email").send_keys("peace@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("Admin123")
time.sleep(1)
driver.find_element(By.ID, "submit").click()
time.sleep(3)

# To Validate login with correct credentials
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
time.sleep(2)
driver.find_element(By.ID, "email").send_keys("peace03@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("Admin123")
time.sleep(1)
driver.find_element(By.ID, "submit").click()
time.sleep(8)

# Ensure  user can add 10 Contact(Contact 1)
driver.find_element(By.ID, "add-contact").click()
time.sleep(2)
driver.find_element(By.ID, "firstName").send_keys("Shane")
driver.find_element(By.ID, "lastName").send_keys("Jakes")
driver.find_element(By.ID, "birthdate").send_keys("2020-01-01")
driver.find_element(By.ID, "email").send_keys("peace1@gmail.com")
driver.find_element(By.ID, "phone").send_keys("8022805621")
driver.find_element(By.ID, "street1").send_keys("House 1, London Street")
driver.find_element(By.ID, "street2").send_keys("House 1, Scotland Street")
driver.find_element(By.ID, "city").send_keys("Ikeja")
driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
driver.find_element(By.ID, "postalCode").send_keys("01234")
driver.find_element(By.ID, "country").send_keys("Nigeria")
driver.find_element(By.ID, "submit").click()
time.sleep(3)

# Ensure  user can add 10 Contact(Contact 2)
driver.find_element(By.ID, "add-contact").click()
time.sleep(3)
driver.find_element(By.ID, "firstName").send_keys("Jack")
driver.find_element(By.ID, "lastName").send_keys("Chan")
driver.find_element(By.ID, "birthdate").send_keys("2021-01-01")
driver.find_element(By.ID, "email").send_keys("peace2@gmail.com")
driver.find_element(By.ID, "phone").send_keys("8022805622")
driver.find_element(By.ID, "street1").send_keys("House 2, London Street")
driver.find_element(By.ID, "street2").send_keys("House 2, Scotland Street")
driver.find_element(By.ID, "city").send_keys("Lekki")
driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
driver.find_element(By.ID, "postalCode").send_keys("01234")
driver.find_element(By.ID, "country").send_keys("Nigeria")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# # Ensure  user can add 10 Contact(Contact 3)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ayo")
# driver.find_element(By.ID, "lastName").send_keys("Ade")
# driver.find_element(By.ID, "birthdate").send_keys("1990-01-01")
# driver.find_element(By.ID, "email").send_keys("peace3@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805623")
# driver.find_element(By.ID, "street1").send_keys("House 3, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 3, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 4)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Ola")
# driver.find_element(By.ID, "lastName").send_keys("Ola")
# driver.find_element(By.ID, "birthdate").send_keys("1991-01-01")
# driver.find_element(By.ID, "email").send_keys("peace4@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805624")
# driver.find_element(By.ID, "street1").send_keys("House 4, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 4, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 5)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(5)
# driver.find_element(By.ID, "firstName").send_keys("Yemi")
# driver.find_element(By.ID, "lastName").send_keys("Alade")
# driver.find_element(By.ID, "birthdate").send_keys("2022-01-01")
# driver.find_element(By.ID, "email").send_keys("peace5@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805625")
# driver.find_element(By.ID, "street1").send_keys("House 5, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 5, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 6)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Becky")
# driver.find_element(By.ID, "lastName").send_keys("Ben")
# driver.find_element(By.ID, "birthdate").send_keys("1995-01-01")
# driver.find_element(By.ID, "email").send_keys("peace6@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805626")
# driver.find_element(By.ID, "street1").send_keys("House 6, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 6, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 7)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ble")
# driver.find_element(By.ID, "lastName").send_keys("Ble")
# driver.find_element(By.ID, "birthdate").send_keys("1996-01-01")
# driver.find_element(By.ID, "email").send_keys("peace7@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805627")
# driver.find_element(By.ID, "street1").send_keys("House 7, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 7, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 8)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(3)
# driver.find_element(By.ID, "firstName").send_keys("Ella")
# driver.find_element(By.ID, "lastName").send_keys("Paul")
# driver.find_element(By.ID, "birthdate").send_keys("2022-01-01")
# driver.find_element(By.ID, "email").send_keys("peace8@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805628")
# driver.find_element(By.ID, "street1").send_keys("House 8, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 8, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 9)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Dan")
# driver.find_element(By.ID, "lastName").send_keys("Dave")
# driver.find_element(By.ID, "birthdate").send_keys("1999-01-01")
# driver.find_element(By.ID, "email").send_keys("peace9@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805629")
# driver.find_element(By.ID, "street1").send_keys("House 9, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 9, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
#
# # Ensure  user can add 10 Contact(Contact 10)
# driver.find_element(By.ID, "add-contact").click()
# time.sleep(4)
# driver.find_element(By.ID, "firstName").send_keys("Nat")
# driver.find_element(By.ID, "lastName").send_keys("Nathan")
# driver.find_element(By.ID, "birthdate").send_keys("2023-01-01")
# driver.find_element(By.ID, "email").send_keys("peace10@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("8022805630")
# driver.find_element(By.ID, "street1").send_keys("House 10, London Street")
# driver.find_element(By.ID, "street2").send_keys("House 10, Scotland Street")
# driver.find_element(By.ID, "city").send_keys("Lekki")
# driver.find_element(By.ID, "stateProvince").send_keys("Lagos")
# driver.find_element(By.ID, "postalCode").send_keys("01234")
# driver.find_element(By.ID, "country").send_keys("Nigeria")
# driver.find_element(By.ID, "submit").click()
# time.sleep(4)

# Verify user logout clears session data.
driver.find_element(By.ID, "logout").click()
time.sleep(5)


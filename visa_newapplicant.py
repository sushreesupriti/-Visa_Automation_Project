from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()


#New Applicant
# Navigate to the US Visa Info signup page
driver.get("https://ais.usvisa-info.com/en-ca/niv/users/sign_in")

time.sleep(15)

#Find the "Given Name" 
name = driver.find_element(By.XPATH, '//input[@id="applicant_first_name"]')
name.send_keys("Sushree Supriti")

#Find surname
surname = driver.find_element(By.XPATH, '//input[@id="applicant_last_name"]')
surname.send_keys("Rana")

#Find country/Authority that issued passport
country = driver.find_element(By.XPATH, '//select[@id="applicant_passport_country_code"]')
select = Select(country_dropdown)
# Replace 'India' with the value you want to select
select.select_by_visible_text('India')


#country of birth
birth_country = driver.find_element(By.XPATH, '//select[@id="applicant_birth_country_code"]')
select = Select(birth_country_dropdown)
# Replace 'India' with the value you want to select
select.select_by_visible_text('India')


#Find country of permanent resident
per_resident_country = driver.find_element(By.XPATH,'//select[@id="applicant_permanent_residency_country_code"]')
select = Select(per_resident_country_dropdown)
# Replace 'Canada' with the value you want to select
select.select_by_visible_text('Canada')


#Find passport number
passport_number= driver.find_element(By.XPATH, '//input[@id="applicant_passport_number"]')
passport_number.send_keys("C1234557")

#Find DS-160 Number
ds_number = driver.find_element(By.XPATH, '//input[@id="applicant_ds160_number"]')
ds_number.send_keys("AAOOVBHNJI")

#vissa class
vissa_cls= driver.find_element(By.XPATH, '//select[@id="applicant_visa_class_id"]')
select = Select(vissa_cls_dropdown)
# Replace 'B1/B2' with the value you want to select
select.select_by_visible_text('B1/B2')


#Date of Birth

#Date
date = driver.finf_element(By.XPATH, '//select[@id="applicant_date_of_birth_3i"]')
select = Select(date_dropdown)
# Replace '5' with the value you want select
select.select_by_visible_text('5')

#Month
month = driver.finf_element(By.XPATH, '//select[@id="applicant_date_of_birth_2i"]')
select = Select(month_dropdown)
# Replace 'Jan' with the value you want to select
select.select_by_visible_text('Jan')

#Year
year = driver.finf_element(By.XPATH, '//select[@id="applicant_date_of_birth_1i"]')
select = Select(year_dropdown)
# Replace '2000' with the value you want to select
select.select_by_visible_text('2000')
year.send_keys()

#select Gender
gender = driver.finf_element(By.XPATH, '//select[@id="applicant_gender"]')
select = Select(gender_dropdown)
# Replace 'Male' with the value you want to select
select.select_by_visible_text('Female')

#Primary Phone Number
primary_phone = driver.find_element(By.XPATH, '//input[@id="applicant_phone1"]')
primary_phone.send_keys()


# Find the checkbox element
checkbox = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
# Check if the checkbox is not checked
if not checkbox.is_selected():
    # If it's not checked, click to check it
    checkbox.click()


#Email Address
email = driver.find_element(By.XPATH, '//input[@id="applicant_email_address"]')
email.send_keys("sushreesupriti@gmail.com")

# Find the radio button element
#previously issued vissa to enter the United State or not 
radio_button = driver.find_element(By.XPATH, '//input[@type="radio" and @name="applicant[is_a_renewal]" and @value="false"]')

# Click the radio button to select it
radio_button.click()

#Are you traveling from another country to apply for a U.S vissa in Canada? 
radio_button = driver.find_element(By.XPATH, '//input[@type="radio" and @name="applicant[traveling_to_apply]" and @value="false"]')

# Click the radio button to select it
radio_button.click()


# Find the Create Applicant button element
createApplicant_button = driver.find_element(By.XPATH, '//input[@type="submit" or @value="Create Applicant" or @class="button primary"]')

# Click the submit button to submit the form
createApplicant_button.click()

# driver.quit()


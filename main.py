from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Global Variables
email = "harsxit04@gmail.com"
passcode = "@Harshit1308"
number = "7898590844"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/login?lipi=urn%3Ali%3Apage%3Adeeplink_linkedinmobileapp%3B4lHfxKPRTp%2BOdI2P2PJykA%3D%3D&destType=web&fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

# Sign in
time.sleep(2)  # Wait for the page to load

username = driver.find_element(By.ID, "username")
username.send_keys(email)

password = driver.find_element(By.ID, "password")
password.send_keys(passcode)

signin = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
signin.click()

time.sleep(5)
# Wait for the captcha to be solved manually this will run automated script again
input("Please solve the captcha and press Enter to continue...")

# Search for jobs
search_input = driver.find_element(By.CSS_SELECTOR, ".search-global-typeahead__input")
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

time.sleep(3)  # Wait for search results to load

# Locate the Easy Apply filter
easy_apply_filter = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Easy Apply')]")
easy_apply_filter.click()

time.sleep(3)  # Wait for the job listings to load

# Loop through each listing
while True:
    # Find all job listings
    all_listings = driver.find_elements(By.XPATH, "//ul[@class='jobs-search__results-list']/li")
    if not all_listings:
        print("No job listings found.")
        break

    for index, listing in enumerate(all_listings):
        # Click on the listing
        driver.execute_script("arguments[0].scrollIntoView(true);", listing)
        time.sleep(1)  # Small delay to ensure the element is fully visible
        listing.click()
        time.sleep(5)

        # Locate and click the apply button
        apply_button = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")
        apply_button.click()
        time.sleep(2)

        # Complete the form
        phone = driver.find_element(By.XPATH, "//input[@name='phoneNumber']")
        phone.clear()
        phone.send_keys(number)

        next_button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button--primary')]")
        next_button.click()

        # Go back to job listings page
        driver.get("https://www.linkedin.com/jobs/search/?keywords=Python")  # Adjust the URL if necessary
        time.sleep(5)  # Wait for the page to reload

        # Re-find all job listings
        all_listings = driver.find_elements(By.XPATH, "//ul[@class='jobs-search__results-list']/li")
        if not all_listings:
            print("No more job listings found.")
            profile_icon = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[6]/div/button")
            profile_icon.click()
            logout_button = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[6]/div/div")
            logout_button.click()
            driver.quit()

            break
        elif index >= len(all_listings):
            # If all listings have been processed, stop the loop
            print("All job listings have been processed.")
            break


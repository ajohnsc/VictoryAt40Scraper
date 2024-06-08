from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://church.victory.org.ph/find-a-church")

def handle_dropdown_and_click(driver):
    dropdown1 = Select(driver.find_element(By.ID, 'region'))

    for option1 in dropdown1.options[1:]:  # Skip the first option
        # Select the option from the first dropdown
        print(f"Selecting region: {option1.text}")
        dropdown1.select_by_visible_text(option1.text)

        # Wait for the second dropdown to be populated
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'local_congreg'))
        )
        time.sleep(3)  # Adjust sleep time as needed
        dropdown2 = Select(driver.find_element(By.ID, 'local_congreg'))

        for option2 in dropdown2.options[1:]:  # Skip the first option
            # Select the option from the second dropdown
            print(f"  Selecting local congregation: {option2.text}")
            dropdown2.select_by_visible_text(option2.text)

            # Wait for a brief moment to ensure the selection is processed
            time.sleep(3)  # Adjust sleep time as needed

            # Wait for the button to be present after the dropdown selections
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-secondary.mt-15'))
            )

            # Find the button
            button = driver.find_element(By.CSS_SELECTOR, '.btn-secondary.mt-15')

            # Get the current window handle
            original_window = driver.current_window_handle

            # Click the button to open a new tab
            button.send_keys(webdriver.common.keys.Keys.CONTROL + webdriver.common.keys.Keys.RETURN)

            # Wait for the new tab to open
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[1])

            # Wait for the user to close the tab
            input("Press Enter after closing the tab...")

            # Close the new tab
            driver.close()

            # Switch back to the original window
            driver.switch_to.window(original_window)

            # Re-select the option from the first dropdown to re-populate the second dropdown
            dropdown1 = Select(driver.find_element(By.ID, 'region'))
            dropdown1.select_by_visible_text(option1.text)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'local_congreg')))
            dropdown2 = Select(driver.find_element(By.ID, 'local_congreg'))

# Run the function
handle_dropdown_and_click(driver)

# Close the WebDriver
driver.quit()

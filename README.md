1. Import Libraries and Set Up WebDriver:
- Import necessary libraries for Selenium.
- Initialize the Chrome WebDriver and open the website.
- Function to Handle Dropdown Selections and Button Clicks:
2. Define handle_dropdown_and_click function to handle the dropdown selections and button clicks.
- Loop through the options of the first dropdown (skipping the first placeholder option).
- Select an option from the first dropdown and wait for the second dropdown to be populated.
- Loop through the options of the second dropdown (skipping the first placeholder option).
- Select an option from the second dropdown and wait briefly for the selection to be processed.
- Wait for the button to appear and then find the button.
- Get the current window handle.
- Click the button to open a new tab using button.send_keys(webdriver.common.keys.Keys.CONTROL + webdriver.common.keys.Keys.RETURN).
- Wait for the new tab to open and switch to it.
- Wait for the user to close the tab by using input("Press Enter after closing the tab...").
- Close the new tab and switch back to the original window.
- Re-select the option from the first dropdown to re-populate the second dropdown for the next iteration.
3. Run the Function and Close WebDriver:
- Call the handle_dropdown_and_click function.
- Close the WebDriver when done.

This script will handle the dropdown selections, open each button click in a new tab, wait for the user to close the tab, and then proceed to the next set of dropdown selections and button click. Adjust sleep times and logic as needed based on the behavior of your specific website.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

driver = webdriver.Chrome()

try:
    driver.get("https://www.pos.com.my/send/ratecalculator")
    wait = WebDriverWait(driver, 15)

    # === Step 1: Enter Postcode (35600) ===
    print("Waiting for postcode input field...")
    postcode_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Postcode']")))
    postcode_input.click()
    postcode_input.send_keys(Keys.CONTROL, "a")
    postcode_input.send_keys(Keys.BACKSPACE)
    postcode_input.send_keys("35600")
    print("Entered postcode: 35600")
    time.sleep(1)

    # === Step 2: Select Country ===
    print("Waiting for country input field...")
    country_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Select country']")))

    print("Clicking and clearing default value...")
    country_input.click()
    time.sleep(0.5)
    country_input.send_keys(Keys.CONTROL, "a")
    country_input.send_keys(Keys.BACKSPACE)
    time.sleep(0.5)

    print("Typing 'India'...")
    country_input.send_keys("India")
    time.sleep(1)

    print("Waiting for autocomplete list to show up...")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mat-mdc-autocomplete-panel")))

    print("Selecting first result...")
    country_input.send_keys(Keys.ARROW_DOWN)
    country_input.send_keys(Keys.ENTER)
    time.sleep(1)

    selected_value = country_input.get_attribute("value")
    print(f"Selected value: {selected_value}")
    if selected_value != "India":
        raise Exception("Failed to select 'India'!")

    print("Successfully selected India!")

    # === Step 3: Enter Weight ===
    print("Waiting for weight input field...")
    weight_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='eg. 0.1kg']")))
    weight_input.click()
    weight_input.send_keys(Keys.CONTROL, "a")
    weight_input.send_keys(Keys.BACKSPACE)
    weight_input.send_keys("1")
    print("Entered weight: 1kg")
    time.sleep(1)

    # === Step 4: Click Calculate ===
    print("Locating Calculate button...")
    calculate_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(), 'Calculate') and contains(@class, 'bg-red-600')]")
    ))
    print("Clicking Calculate button...")
    calculate_button.click()

    print("Clicked Calculate — waiting for result...")
    time.sleep(3)

except Exception as e:
    print("Exception occurred:")
    traceback.print_exc()

finally:
    time.sleep(5)
  #  driver.quit()

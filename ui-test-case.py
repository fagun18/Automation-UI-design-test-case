from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Get the XD URL from the user
xd_url = input("Enter the XD URL: ")

# Launch the Chrome browser and navigate to the XD URL
driver = webdriver.Chrome()
driver.get(xd_url)

# Wait for the page to fully load and retrieve the HTML source code
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.xd-container')))
html = driver.page_source

# Parse the HTML code using BeautifulSoup and extract the UI elements
soup = BeautifulSoup(html, 'html.parser')
buttons = soup.select('button')
text_fields = soup.select('input[type="text"], input[type="email"], input[type="password"]')
dropdowns = soup.select('select')

# Generate test cases for each UI element
test_cases = []
for button in buttons:
    test_cases.append(f"Click the '{button.text}' button and verify that it takes you to the expected page.")
for text_field in text_fields:
    test_cases.append(f"Enter '{text_field.get('placeholder', '')}' in the '{text_field.get('name', '')}' field and verify that the input is accepted.")
for dropdown in dropdowns:
    test_cases.append(f"Select an option from the '{dropdown.get('name', '')}' dropdown and verify that the selected option is displayed.")

# Output the generated test cases to a file or print them to the console
with open('test_cases.txt', 'w') as f:
    for i, test_case in enumerate(test_cases):
        f.write(f"Test case {i+1}: {test_case}\n")

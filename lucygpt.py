from selenium import webdriver

# Set the path to the chromedriver executable
driver_path = 'chromedriver.exe'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

driver.get('https://chat.openai.com/')

# Find the input box and type your message
input_box = driver.find_element_by_css_selector('.input-box')
input_box.send_keys('hello')

# Press Enter or click the send button
input_box.submit()  # Or find the send button and click it

# Wait for the response to load
driver.implicitly_wait(10)  # Adjust the timeout as needed

# Get the response text
response_text = driver.find_element_by_css_selector('.response-box').text

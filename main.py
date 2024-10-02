from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import subprocess
import gzip
from io import BytesIO

def get_request_body(request_body):
    json_data = {}

    try:
        # Check if the data is Gzipped by attempting to decompress
        with gzip.GzipFile(fileobj=BytesIO(request_body)) as gz:
            decompressed_data = gz.read()
        raw_string = decompressed_data.decode('utf-8')  # Decode the decompressed data
        json_data = json.loads(raw_string)  # Parse the string as JSON
    except (OSError):
        # If the data isn't Gzipped, decode it as regular bytes
        try:
            raw_string = request_body.decode('utf-8')
            json_data = json.loads(raw_string)
        except Exception as e:
            print(f"Error decoding raw data: {e}")
            json_data = {}

    return json_data

service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)


driver.get("https://www.perplexity.ai/")
time.sleep(5)

action = ActionChains(driver)
action.move_by_offset(200, 100).perform()
time.sleep(2)
action.move_by_offset(-150, -50).perform()

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("places to visit in america" + Keys.ENTER)

# print("All responses -- ")s
# with open('responses_2.txt', 'w', encoding='utf-8') as log_file:
#     for request in driver.requests:
        
#         if request.response:
#             # if request.headers.get('x-requested-with') == 'XMLHttpRequest' or \
#             #    'fetch' in request.headers.get('sec-fetch-mode', '').lower():
#                 print(f"URL: {request.url}")
#                 log_file.write(f"URL: {request.url}\n")
#                 print(f"Headers : {request.response.headers}")
#                 log_file.write(f"Headers: {request.response.headers}\n")
#                 print(f"Status Code: {request.response.status_code}")
#                 log_file.write(f"Status Code: {request.response.status_code}\n")
#                 print(f"Method: {request.method}")
#                 log_file.write(f"Method: {request.method}\n")
                
#                 try: 
#                     body_str = json.dumps(request.response.body)
#                     jsonData = subprocess.run(["node", "request_parsing.js", request.response.body], capture_output=True, text=True)
#                     print(f"Response Body: {jsonData}")
#                     log_file.write(f"Response Body: {request.response.body}\n")
#                     log_file.write("\n")
#                     if jsonData.stderr:
#                         raise Exception(f"Error occurred: {jsonData.stderr}")
#                 except Exception as e:
#                     print(f"An error occurred: {e}")

time.sleep(30)

driver.quit()





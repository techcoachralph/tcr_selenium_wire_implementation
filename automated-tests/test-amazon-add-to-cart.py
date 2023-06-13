from seleniumwire import webdriver as sw_webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import boto3
import json

# Opening JSON file
config_file = open('../config/config.json')

# load config file

config_data = json.load(config_file)

config_file.close()
aws_project_arn = config_data["aws_project_arn"]
options = {
    'addr': 'testgrid-devicefarm.us-west-2.amazonaws.com',  # Address of the machine running Selenium Wire. Explicitly use 127.0.0.1 rather than
    # localhost if remote session is running locally.
}

# aws configuration
devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")
testgrid_url_response = devicefarm_client.create_test_grid_url(
      projectArn=aws_project_arn,
      expiresInSeconds=300)

browser = "remote"
driver_type = "sw"
if browser == "local":
    driver = sw_webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
else:
    print(testgrid_url_response)
    if driver_type == "sw":
        driver = sw_webdriver.Remote(
            command_executor=testgrid_url_response["url"],
            seleniumwire_options=options,
            options=webdriver.ChromeOptions())
    else:
        driver = webdriver.Remote(testgrid_url_response["url"],
                                  options=webdriver.ChromeOptions())

driver.get("https://www.amazon.com/")

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Rubick's Cube")
driver.find_element(By.ID, "nav-search-submit-button").click()

driver.find_element(By.CSS_SELECTOR, "img.s-image").click()
try:
    print(driver.requests)
    for request in driver.requests:
        print(request)
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )
except AttributeError:
    driver.quit()
driver.quit()
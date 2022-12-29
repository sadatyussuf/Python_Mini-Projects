from selenium import webdriver

from selenium.webdriver.chrome import service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
import pathlib

BASEDIR = pathlib.Path(__file__).parent
print(BASEDIR)
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(
    # options=options
    # service=ChromeService(ChromeDriverManager().install()), options=options
)

driver.get("https://community.chocolatey.org/")

# Save a screenshot of the website to a file
# driver.get_screenshot_as_file("screenshot.png")

# Get the screenshot data as a bytes object
screenshot_data = driver.get_screenshot_as_png()

# Write the screenshot data to a file
with open(BASEDIR / "screenshot.png", "wb") as f:
    f.write(screenshot_data)

# Close the driver
driver.close()

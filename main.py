from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

email = "email"
password = "password"



driver = webdriver.Chrome("chromedriver.exe")
wait = WebDriverWait(driver, 15)



# Navigates to the alexa page, but is redirected to password/email entry page.
driver.get("https://www.amazon.com/hz/mycd/myx/#/home/alexaPrivacy/activityHistory")
# Waits until the email input box is visible so it doesn't crash.
wait.until(EC.visibility_of_element_located((By.ID, 'ap_email')))
emailInput = driver.find_element_by_id('ap_email')
# Inputs email and proceeds to next page.
emailInput.send_keys(email)
emailInput.send_keys(Keys.ENTER)
# Waits until password box is visible.
wait.until(EC.visibility_of_element_located((By.ID, 'ap_password')))
passwordInput = driver.find_element_by_id('ap_password')
# Inputs password and proceeds to next page.
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)
# Goes back to the alexa voice history, since amazon redirects us to a different page.
driver.get("https://www.amazon.com/hz/mycd/myx/#/home/alexaPrivacy/activityHistory")

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainInfo-0"]/div')))
firstDiv = driver.find_element_by_xpath('//*[@id="timePickerDesktop"]/span/span')
driver.execute_script("arguments[0].scrollIntoView(true);", firstDiv)
def timePicker():
    driver.execute_script('document.getElementById("timePickerDesktop").click()')

def refreshCommands():
    global cleanCommand
    global cleanstoredcommand
    global same
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainInfo-0"]/div')))
    storedCommand = driver.find_element_by_xpath('//*[@id="mainInfo-0"]/div')
    cleanstoredcommand = str(storedCommand.text).translate({ord(i): None for i in '”“'})
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="timePickerDesktop"]/span/span')))


    timePicker()

    #yesterdayButton = driver.find_element_by_xpath('//*[@id="timePickerDesktop_1"]')
    #yesterdayButton.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="timePickerDesktop"]/span/span')))

    driver.execute_script('document.getElementById("timePickerDesktop_1").click()')

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainInfo-0"]/div')))

    timePicker()

    #todayButton = driver.find_element_by_xpath('//*[@id="timePickerDesktop_0"]')
    driver.execute_script('document.getElementById("timePickerDesktop_0").click()')

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainInfo-0"]/div')))
    # Waits until the latest command is loaded, and cleans the weird Amazon text from it.
    lastCommand = driver.find_element_by_xpath('//*[@id="mainInfo-0"]/div')
    # Removes those not-actually quotation symbols.
    cleanCommand = str(lastCommand.text).translate({ord(i): None for i in '”“'})
    if cleanCommand == cleanstoredcommand:
        same = True
    else:
        same = False


#Put this here to test out interpreting commands and sending them off.
def interpretCommand():
    command = cleanCommand
    if command == "what the heck":
        f = open("diedie.txt","w+")
        f.write(command+"\n")
        f.close()


while True:
    refreshCommands()
    if same == True:
        None
    else:
        print(cleanCommand)
        interpretCommand()


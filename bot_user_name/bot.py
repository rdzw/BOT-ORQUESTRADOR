from time import sleep
# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
# Importacao do web driver com o ChromeDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


# using as constants for example only 
# in a real scenario, this should be passed as parameters or using credentials feature
USERNAME = "student"
PASSWORD = "Password123"

def main():
    try:
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        bot = WebBot()

        # Configure whether or not to run on headless mode
        bot.headless = False

        # set WebDriver path
        service = Service(executable_path=r"geckodriver.exe")

        # create a bot instance
        bot = webdriver.Firefox(service=service)

        # Opens the BotCity website.
        bot.browse("https://practicetestautomation.com/practice-test-login/")

        # Implement here your logic...

        #Primeiro encontramos o elemento username
        input_username = bot.find_element("username", By.ID)

        # Adicionamos o USERNAME
        input_username.send_keys(USERNAME)

        input_password = bot.find_element("password", By.ID)

        input_password.send_keys(PASSWORD)

        input_button = bot.find_element("submit", By.ID)
        input_button.click()

        # wait 3 seconds to ensure that the page opened
        sleep(3)

        # search for the login confirmation
        logged = bot.find_element(".post-title", By.CSS_SELECTOR)

        # print confirmation text
        print(logged.text)        

        # search for the logout button element
        logout = bot.find_element(".wp-block-button__link", By.CSS_SELECTOR)

        # click on the button
        logout.click()

        # search for the login title to ensure that the logout finished
        bot.find_element("#login > h2:nth-child(1)", By.CSS_SELECTOR)

        finish_status = AutomationTaskFinishStatus.SUCCESS
        finish_message = f'Task with username "{USERNAME}" executed with success'
    
    except Exception as ex:
        # search for the element with the error message
        error_alert = bot.find_element("error",By.ID)

        # print the error message and stacktrace
        print(error_alert.text)
        print(ex)

        finish_status = AutomationTaskFinishStatus.FAILED
        finish_message = f'Task with username "{USERNAME}" failed: {error_alert.text}'

    finally:
        # close the browser
        bot.stop_browser()

        # print the message
        print("Finally")

        # finish the task
        maestro.finish_task(
            task_id=execution.task_id,
            status=finish_status,
            message=finish_message
        )

        # create the log
        maestro.new_log_entry(
            activity_label="login_control",
            values = {
                "username": USERNAME,
                "message": finish_message
            } 
        )


        # Finish and clean up the Web Browser
        # You MUST invoke the stop_browser to avoid
        # leaving instances of the webdriver open
        

        # Uncomment to mark this task as finished on BotMaestro
        # maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from datetime import datetime

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
############ INICIANDO O try #######################
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

        # Uncomment to change the default Browser to Firefox
        bot.browser = Browser.FIREFOX

        # Uncomment to set the WebDriver path
        bot.driver_path = r"resources\geckodriver.exe"
        
        # Notifando um pequeno exemplo de alerta 
        '''exemplo'''
        maestro.alert(
            task_id=execution.task_id,
            title="BotYoutube - Inicio",
            message="Estamos iniciando o processo de automação do Botyoutube",
            alert_type=AlertType.INFO
        )

        # Opens the BotCity website.
        bot.browse("https://www.youtube.com/@pythonbrasiloficial")

        # Implement here your logic...
        # Buscando elemento da página
        # Faz a busca por ID
        elemento_inscritos = bot.find_element("subscriber-count", By.ID)

        # Se não encontrar, faz a busca por XPATH
        if not elemento_inscritos:
            elemento_inscritos = bot.find_element('//span[contains(text(), "inscritos")]', By.XPATH) 
        # Coletando o conteúdo de texto do elemento
        inscritos = elemento_inscritos.text
        
        # mostrando a informação coletada no terminal
        print(f"Inscritos => {inscritos}")
        
        #exemplo de log referente as estatisticas youtube
        # E os valores que elaborei no orquestrador
        maestro.new_log_entry(
            activity_label="EstatisticasYoutube",
            values = {
                "data_hora": datetime.now().strftime("%Y-%m-%d_%H-%M"),
                "inscritos": inscritos
            }
        )
        
        
        status = AutomationTaskFinishStatus.SUCCESS
        mensagem = "Tarefa BotYoutube finalizada com sucesso"
        
########################## FIM TRY  ######################################

########################## INICIO EXCEPT  ################################  
    except Exception as ex:
        # Salvando captura de tela do erro
        bot.save_screenshot("erro.png")

        # Dicionario de tags adicionais
        # tags = {"canal": canal}

        # Registrando o erro
        maestro.error(
            task_id=execution.task_id,
            exception=ex,
            screenshot="erro.png"
        )
        
        status = AutomationTaskFinishStatus.FAILED
        mensagem = "Tarefa BotYoutube finalizada com erro"
########################## FIM EXCEPT  ################################
 
########################## INICIO FINALLY  ################################
    finally:
        # Wait 3 seconds before closing
        bot.wait(3000)

        # Finish and clean up the Web Browser
        # You MUST invoke the stop_browser to avoid
        # leaving instances of the webdriver open
        bot.stop_browser()

        # Uncomment to mark this task as finished on BotMaestro
        #se ele definiu tudo com sucesso, resultado sucesso
        maestro.finish_task(
            task_id=execution.task_id,
            status=status,
            message=mensagem
        )
        #fim finally


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

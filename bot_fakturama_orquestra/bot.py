# Import for the Desktop Bot
import json
from botcity.core import DesktopBot
from datetime import datetime
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    try:
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        bot = DesktopBot()
        
        # Notifando um pequeno exemplo de alerta 
        '''exemplo'''
        maestro.alert(
            task_id=execution.task_id,
            title="BotFakturama - Inicio",
            message="Estamos iniciando o processo de automação do Fakturama",
            alert_type=AlertType.INFO
        )
        
        # Caminho para o arquivo JSON
        json_path = r'C:\Users\rodrigo\Desktop\BOT-ORQUESTRADOR\bot_fakturama_orquestra\resources\teste.json'
        
        # Leitura do arquivo JSON
        with open(json_path, 'r', encoding='utf-8') as file:
            dados = json.load(file)
        
        # Extrair os produtos da estrutura JSON
        produtos = dados['load']['products']    

        # Implement here your logic...
        
        # Abre o aplicativo do bloco de notas.
        bot.execute(r"C:\Program Files\Fakturama2\Fakturama.exe")
        
        for produto in produtos:
        
            if not bot.find("cadastrar", matching=0.97, waiting_time=10000):
                not_found("cadastrar")
            bot.click()
                    
            
            if not bot.find("item_number", matching=0.97, waiting_time=10000):
                not_found("item_number")
            bot.click_relative(113, 10)
            
            # Preencher os campos com formatação adequada
            bot.paste(produto['item_number'])  # Número do item
            bot.tab()
            bot.paste(produto['name'])         # Nome do produto
            bot.tab()
            bot.paste(produto['category'])     # Categoria
            bot.tab()
            bot.paste(produto['gtin'])         # Código GTIN
            bot.tab()
            bot.paste(produto['supplier_code'])# Código do fornecedor
            bot.tab()
            bot.paste(produto['description'])  # Descrição
            bot.tab()

            # Formatar os valores monetários com 2 casas decimais
            price = format(float(produto['price']), '.2f')
            cost = format(float(produto['cost']), '.2f')
            allowance = format(float(produto['allowance']), '.2f')
            
            # Preencher os valores monetários formatados
            bot.paste(price)                   # Preço de venda
            bot.tab()
            bot.paste(cost)                    # Custo
            bot.tab()
            bot.paste(allowance)               # Desconto ou margem
            bot.tab()
            
            # Preencher o VAT (IVA)
            bot.paste(produto['vat'])
            bot.tab()
            
            # Formatar o estoque (caso precise de valor inteiro)
            stock = format(int(produto['stock']), 'd')
            bot.paste(stock)                   # Estoque

            # Salvar o cadastro do produto
            if not bot.find("save", matching=0.97, waiting_time=10000):
                not_found("save")
            bot.click()
            

            # Fechar a janela do produto
            bot.control_w()
            
            # logs
            # E os valores que elaborei no orquestrador
            maestro.new_log_entry(
                activity_label="PreencheFormulario",
                values = {
                     "data_hora": datetime.now().strftime("%Y-%m-%d_%H-%M"),
                     "item_number": produto['item_number']
                }
            )
            # fim logs
            
            status = AutomationTaskFinishStatus.SUCCESS
            mensagem = "Tarefa BotFakturama finalizada com sucesso"
            
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
    
    finally:

        # Uncomment to mark this task as finished on BotMaestro
        maestro.finish_task(
            task_id=execution.task_id,
            status=status,
            message=mensagem
        )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
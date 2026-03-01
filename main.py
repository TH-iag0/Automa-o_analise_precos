from selenium import webdriver
from selenium.webdriver.chrome.service import Service # Gerencia o serviço do Chrome (inicia e para o driver)
from webdriver_manager.chrome import ChromeDriverManager # Gerencia o driver do Chrome automaticamente (evita erro de versão)
from selenium.webdriver.common.by import By # seleciona um grupo de elementos, By.ID, By.CLASS_NAME, By.TAG_NAME, etc.
from datetime import datetime
from banco_de_dados import salvar_dados_no_banco
import time


def rodar_agendador():
    print("-- Iniciando o Robô --")
    
    service = Service(ChromeDriverManager().install())     # Instala o driver automaticamente (evita erro de versão)

    navegador = webdriver.Chrome(service=service)
    
    link = "https://www.contabilizei.com.br/quanto-custa-contabilizei/"

    try:
        navegador.get(link)
        time.sleep(10) # Espera o site carregar

        elementos_precos = navegador.find_elements(By.CLASS_NAME, "to-value")# find_elements seleciona um elemento específico, By.CLASS_NAME seleciona pelo nome da classe, "to-value" é a classe que contém os preços dos planos.
        nomes_planos = ["Padrão", "Multibenefícios", "Experts Essencial"]

        print(f" O robô enxergou {len(elementos_precos)} preços na tela do Chrome.")

        if len(elementos_precos) == len(nomes_planos): #conta a quantidade de elementos encontrados e compara com a quantidade de nomes dos planos, se for igual, continua, se for diferente, dá um erro. 
            
            horario_do_preço_coletado = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            dados_coletados = [] #Cria uma lista vazia para armazenar os dados coletados

            for nome, elemento_preco in zip(nomes_planos, elementos_precos): # aqui ele alinha nome e preço, ou seja, o primeiro nome com o primeiro preço, o segundo nome com o segundo preço, etc. O zip() é uma função que junta duas listas em uma só, criando tuplas com os elementos correspondentes.
                
                dados_coletados.append([horario_do_preço_coletado, nome ,elemento_preco.text]) 

            salvar_dados_no_banco(dados_coletados)
                
            print("Arquivos coletados: ", dados_coletados)
            
            
        else:
            print("Houve uma alteração nos planos")

    except Exception as e:
        print(f"Deu um erro no script: {e}")

    finally:
      
        navegador.quit()
        print("--- Robô Finalizado ---")  # Fecha o navegador mesmo se der erro

if __name__ == "__main__": 
    rodar_agendador()  
# Permite testar rodando direto esse arquivo, sem precisar do agendador. O agendador vai importar essa função e rodar ela no horário agendado.
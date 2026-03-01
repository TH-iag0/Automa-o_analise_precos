import schedule # ele funciona para agendar tarefas, ou seja, ele executa uma função em um horário específico ou em intervalos regulares.
import time
from datetime import datetime
from schedule import every, repeat, run_pending
from main import rodar_agendador

@repeat(every(30).seconds.do)# 
def tarefa():
    print("Executando a tarefa agendada...")
    rodar_agendador() # Chama a função do main.py para rodar o robô
   #esse codigo precisa de um loop infinito para ficar verificando se tem alguma tarefa agendada para ser execut
while True: 
    schedule.run_pending() # Verifica se tem alguma tarefa agendada para ser executada e executa
    time.sleep(1) # Se deixar apenas o 'schedule.run_pending()', ele vai ficar rodando o tempo todo, então o 'time.sleep(1)'
                  # faz com que ele espere 1 segundo antes de verificar novamente, isso evita que o programa fique consumindo muita CPU. 




# Agendando a tarefa para ser executada a cada 10 segundos
#schedule.every(10).seconds.do(tarefa)


#schedule.every().day.at("14:30").do(tarefa) # Agendando a tarefa para ser executada todos os dias às 14:30





import smtplib 
from email.message import EmailMessage 
import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env

remetente = 'thiagomvaz12@gmail.com'
destinatario = 'charlesvazjus@gmail.com'
assunto = 'Dashboard de Preços - Contabilizei'
senha = os.getenv("SENHA_GMAIL") 

mensagem_texto = 'Olá, Charles!\n\nOs preços da concorrência foram atualizados. Acesse o nosso sistema para conferir.'

mensagem_html = """
<html>
  <body>
    <h2>Olá, Charles!</h2>
    <p>Os preços da concorrência foram atualizados hoje pelo nosso robô.</p>
    <p>Para ver os gráficos interativos e a tabela de dados, clique no botão abaixo:</p>
    <br>
    <a href="https://cwda3ktq7ztmzylswhrycm.streamlit.app" 
       style="background-color: #008CBA; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-family: Arial; font-weight: bold;">
       📊 Acessar Dashboard Interativo
    </a>
    <br><br>
    <p><i>Atenciosamente,<br>Thiago Vaz</i></p>
  </body>
</html>
"""

msg = EmailMessage() # aqui criamos o objeto de e-mail, que é onde vamos colocar todas as 
msg['To'] = destinatario #informações do e-mail, como remetente, destinatário, assunto, texto e HTML. O EmailMessage é uma classe do módulo email que facilita a criação de mensagens de e-mail.
msg['From'] = remetente  
msg['Subject'] = assunto

msg.set_content(mensagem_texto) #set_content ele passa html para o corpo do e-mail
msg.add_alternative(mensagem_html, subtype='html')#add_alternative de uma forma simples, ele adiciona uma alternativa ao corpo do e-mail, ou seja, ele permite que o e-mail tenha tanto uma versão em texto quanto uma versão em HTML. O subtype='html' indica que a alternativa é do tipo HTML. Assim, se o cliente de e-mail do destinatário suportar HTML, ele exibirá a versão HTML; caso contrário, ele exibirá a versão em texto simples.

print("Conectando ao servidor do Google...")
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email: #smtplit.SMTP_SSL é a conexão com server e o smtp.gemail.com 465 é a porta de conexão segura do Gmail, ou seja, ele usa SSL para criptografar a conexão. O with é usado para garantir que a conexão seja fechada corretamente após o envio do e-mail.
        email.login(remetente, senha) 
        email.send_message(msg) 
        print(" E-mail corporativo enviado com sucesso com o botão!")
except Exception as e:
    print(f" Erro ao enviar o e-mail: {e}")
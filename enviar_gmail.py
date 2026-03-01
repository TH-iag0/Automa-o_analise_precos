import smtplib # serve para enviar emails
from email.mime.text import MIMEText # serve para criar o corpo do email
import mimetypes # serve para identificar o tipo do arquivo
from email.message import EmailMessage # serve para criar o email

remetente = 'thiagomvaz12@gmail.com'
destinatario = 'charlesvazjus@gmail.com'
assunto = 'Dashboard de Preços - Contabilizei'
mensagem_texto = 'Olá, Charles!\n\nSegue em anexo o dashboard de preços atualizado.\n\nAtenciosamente,\nThiago Vaz'




senha ="yhac trmq sxnj gqjo"
anexo = ""

msg = EmailMessage()  # criando o email
msg ['From'] = remetente 
msg ['To'] = destinatario
msg ['Subject'] = assunto
msg.set_content(mensagem_texto) # set_content é usado para definir o corpo do email

mime_type,_ = mimetypes.guess_type(anexo) # guess_type é usado para identificar o tipo do arquivo
mime_types , mime_subtype = mime_type.split('/')
#aqui estou guardando o tipo e o subtipo do arquivo, por exemplo, se for um pdf, o tipo é application e o subtipo é pdf 

with open(anexo, 'rb') as arquivo : # 'rb' é uma leitura binaria para ler o arquivo
    msg.add_attachment(arquivo.read(), maintype=mime_types, subtype=mime_subtype, filename=anexo) 
    # add_attachment é usado para adicionar o arquivo ao email, ele recebe o conteúdo do arquivo, o tipo e subtipo do arquivo e o nome do arquivo


with smtplib.SMTP_SSL('smtp.gmail.com',465) as email:
    email.login(remetente, senha) # aqui estou fazendo o login no servidor de email usando remetente e senha
    email.send_message(msg) # send_message é usado para enviar o email, ele recebe o email criado com o EmailMessage
   
   
   
    print("Email enviado com sucesso!")



import smtplib
from email.mime. text import MIMEText
from email.mime.multipart import MIMEMultipart

#Configurações do servidor SMTP
server_smtp = "smtp-mail.outlook.com"
port = 587
sender_email = "seuemail@gmail.com"
password = "SenhaDoSeuEmail"

#Configurações do e-mail
receive_email ="EmailDeEnvio@gmail.com"
subject = "E-mail automático tudo com Programação"
body = """ 
<p> Esse email está sendo enviado com foco em testes </p>
"""

message = MIMEMultipart()
message["From"] = sender_email
message ["To"] = receive_email
message["Subject"] = subject
message. attach (MIMEText (body, "html"))

#Conectando o servidor SMTP
try:
    server = smtplib.SMTP(server_smtp, port)
    server.starttls()

    server. login(sender_email, password)

    server. sendmail(sender_email, receive_email, message.as_string())
    print("E-mail enviado com sucesso")
except Exception as e:
    print(f'Hoive algum erro: {e}')
finally:
    server.quit()











# ENVIANDO EMAIL VIA PYTHON
# CASO QUERIA O CODIGO, ESTARÁ NO MEU GITHUB = RaphaelSampaio1

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Função que envia um email com o relatório
def send_mail(username, password, mail_from, mail_to, mail_subject, mail_body):
    mimemsg = MIMEMultipart() # objeto email

    mimemsg['From'] = mail_from # remetente da mensagem
    mimemsg['To'] = mail_to # destinatário da mensagem
    mimemsg['Subject'] = mail_subject # assunto da mensagem
    mimemsg.attach(MIMEText(mail_body, 'html')) # conteúdo da mensagem

    print("Email com relatório da análise criado!\n")
    
    try:
        # configuração do servidor de email
        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls() # comunicação criptografa com TLS
        connection.login(username, password)
        connection.send_message(mimemsg) # envia o email
        connection.quit()
    
    except:
        print('''Nome de usuário, senha ou endereço do destinatário incorreto(s).
Corrija o arquivo criado e execute novamente!''')
        exit(0)
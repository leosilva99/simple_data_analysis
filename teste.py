import pandas as pd
import os.path
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Importar a base de dados
tabel_sales = pd.read_excel('Vendas.xlsx')
# ['Código Venda', 'Data', 'ID Loja', 'Produto', 'Quantidade', 'Valor Unitário', 'Valor Final']

# Visualizar a base de dados
pd.set_option('display.max_columns', None)

# Faturamento por loja
revenues_per_store = tabel_sales[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

# Quantidade de produtos vendidos por loja
products_sold_per_store = tabel_sales[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

# Ticket médio por produto em cada loja
average_ticket = (revenues_per_store['Valor Final'] / products_sold_per_store['Quantidade']).to_frame()
average_ticket = average_ticket.rename(columns={0: 'Ticket Médio'})

print("Análise dos dados feita!\n")

# Verifica se o arquivo de credenciais existe
if(os.path.isfile('data.json') == False):
    username = str(input("Digite seu email: "))
    password = str(input("Digite sua senha: "))
    mail_from = username
    mail_to = str(input("Digite o email de destino: "))

    data_write = {'username': username, 'password': password, 'mail_from': mail_from, 'mail_to': mail_to}
    jstr = json.dumps(data_write, indent=4)

    file = open("data.json","w")
    file.write(jstr)
    file.close()

mail_subject = "Relatório de Vendas por loja"
mail_body = f'''
<p>Prezados,</p> 

<p>Segue o relatório de vendas por loja.</p>

<p>Faturamento:</p>
{revenues_per_store.to_html(formatters={'Valor Final': 'R$ {:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{products_sold_per_store.to_html}

<p>Ticket médio por produto vendido:</p>
{average_ticket.to_html(formatters={'Ticket Médio': 'R$ {:,.2f}'.format})}

<p>Qualquer dúvida, estou à disposição.</p>

<p>Atenciosamente,</p>
<p>Leonardo</p>'''


data = json.load(open("data.json")) # arquivo JSON contendo as credenciais
username = data["username"]
password = data["password"]
mail_from = data["mail_from"]
mail_to = data["mail_to"]

print("Email com relatório da análise criado!\n")

mimemsg = MIMEMultipart() # objeto email
# atribuição dos dados do email
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject
mimemsg.attach(MIMEText(mail_body, 'html'))

print("\nEmail com relatório da análise criado!")

# envio do email
connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(username, password)
connection.send_message(mimemsg)
connection.quit()

print("\nEmail com relatório da análise enviado!")
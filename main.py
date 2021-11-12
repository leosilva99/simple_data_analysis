import os.path
from getpass import getpass
import json

from analysis_data import analysis_data
from create_content_mail import create_content_mail
from send_mail import send_mail

def main():
    if(os.path.isfile('data.json') == False):
        # Criação do arquivo de credenciais
        username = input("Digite seu email: ")
        password = getpass("Digite sua senha: ")
        mail_from = username
        mail_to = input("Digite o email de destino: ")

        print('-' * 50)
        print("\n")

        data_write = {'username': username, 'password': password, 'mail_from': mail_from, 'mail_to': mail_to}
        jstr = json.dumps(data_write, indent=4)

        file = open("data.json","w")
        file.write(jstr)
        file.close()

    
    revenues_per_store, products_sold_per_store, average_ticket = analysis_data()
    print("Análise dos dados feita!\n")

    mail_subject, mail_body = create_content_mail(revenues_per_store, products_sold_per_store, average_ticket)

    # leitura do arquivo de credenciais
    data = json.load(open("data.json")) # arquivo JSON contendo as credenciais
    username = data["username"]
    password = data["password"]
    mail_from = data["mail_from"]
    mail_to = data["mail_to"]

    print("Arquivo de credenciais lido!\n")

    send_mail(username, password, mail_from, mail_to, mail_subject, mail_body)
    print("Email enviado ao destinatário!\n")


if __name__ == "__main__":
    main()
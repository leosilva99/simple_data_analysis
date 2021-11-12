from pandas.core.frame import DataFrame

# Função que monta o relatório a ser enviado por email
def create_content_mail(revenues_per_store: DataFrame, products_sold_per_store: DataFrame, average_ticket: DataFrame):

    mail_subject = "Relatório de Vendas por loja"
    mail_body = f'''
    <p>Prezados,</p> 

    <p>Segue o relatório de vendas por loja.</p>

    <p>Faturamento:</p>
    {revenues_per_store.to_html(formatters={'Valor Final': 'R$ {:,.2f}'.format})}

    <p>Quantidade Vendida:</p>
    {products_sold_per_store.to_html()}

    <p>Ticket médio por produto vendido:</p>
    {average_ticket.to_html(formatters={'Ticket Médio': 'R$ {:,.2f}'.format})}

    <p>Qualquer dúvida, estou à disposição.</p>

    <p>Atenciosamente,</p>
    <p>Leonardo</p>'''

    return mail_subject, mail_body
import pandas as pd

# Função que faz a análise na base de dados de vendas
def analysis_data():
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
    average_ticket = (revenues_per_store['Valor Final'] / 
                    products_sold_per_store['Quantidade']).to_frame() # formatar para ser uma tabela
    average_ticket = average_ticket.rename(columns={0: 'Ticket Médio'}) # renomear a nova coluna

    return revenues_per_store, products_sold_per_store, average_ticket

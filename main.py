import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""
client = Client(account_sid, auth_token)

# Integração do python com Excel:

# pandas
# openpyxl

# Integração do python com SMS:

# twilio

# Passo a passo da solução:

# Abrir os 6 arquivos em Excel:

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():#any() irá verificar se algum valor na tabela é maior que 55.000
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        #O values[0] vai dizer que só quer o valor passado pelo loc[]
        #O loc[] irá localizar os valores. Ex: loc[linha, coluna]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}!')
        message = client.messages.create(
            to="",
            from_ = "",
            body = f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}!')
        print(message.sid)




# Para cada arquivo:

# Verificar se algum valor na coluna vencdas daquele arquivo é maior que 55.000

# Se for maior que 55.000 -> Envia um SMS com o nome, o mÊs e as vendas do vendedor

# Caso não seja maior que 55.000 não fazer nada


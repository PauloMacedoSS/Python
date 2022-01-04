This project aims to automate a bonus system for employees for their sales, analyzing the information in Excel spreadsheets and sending the result via SMS.

To run this project it is necessary to carry out the following installations:

1 - Latest version of python.<br>
2 - Twilio<br>
3 - Pandas<br>
4 - Openpyxl

* Twilio is the integration of python with SMS, while pandas and openpyxl are the integration of python with excel.

* twilio, padas and openpyxl can be installed through the pycharm terminal with the following commands:

pip install twilio

pip install pandas

pip install openxl

You will also need to create a twilio account and register a mobile number to take the test. You will get all the necessary information through the following link:

https://www.twilio.com/docs/libraries/python

twilio will force the necessary data to send the SMS:

Ex:

account_sid = "provided by twilio"<br>
auth_token = "provided by twilio"<br>
to="number you registered",<br>
from_="Number provided by twilio"

------------------------------------------------------------------------------------------------------------------------------------------------

Esse projeto tem como intuito automatizar um sistema de bonificação de funcionarios por suas vendas, realizando a analise das informações das planilhas em Excel e enviando o resultado por SMS.

Para executar esse projeto é necessario realizar as seguintes instalações:

1 - Ultima versão do python.<br>
2 - Twilio<br>
3 - Pandas<br>
4 - Openpyxl

* O twilio é a integração do python com o SMS, já o pandas e openpyxl são a integração do python com o excel.

* O twilio, padas e openpyxl podem ser instalados atraves do terminal do pycharm com os seguintes comandos:

pip install twilio

pip install pandas

pip install openxl

Tambem será preciso criar uma conta no twilio e cadastrar um número de celular para realizar o teste. Você irá conseguir todas as informações necessarias atraves do seguinte link:

https://www.twilio.com/docs/libraries/python

O twilio vai forcecer os dados ncessarios para o envio do SMS:

Ex:

account_sid = "fornecido pelo twilio"<br>
auth_token  = "fornecido pelo twilio"<br>
to="número que você cadastrou", <br>
from_="Número fornecido pelo twilio"

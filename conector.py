# Script de um conector python para mysql que pode ser usado em qualque banco sql
# Importação do conector mysql atraves do pip install mysql.connector

import mysql.connector
from mysql.connector import Error

# Inserir registros em um banco de dados 
print("Rotina para cadastro (alguma coisa) no banco de dados")
print("Entre com os dados solicitados")

# Nesse caso irei inserir produtos, criei uma varia vel par acada coluna da tabela
idProduto = input("ID do produto: ")
nomeProduto = input("Nome do produto: ")
precoProduto = input("Preço: ")
quantProduto = input("Quantidade: ")

# Na variavel dos dados irá ter as variaveis das colunas da tabela
dados = idProduto + ',\'' + nomeProduto + '\',' + precoProduto + ',' + quantProduto + ')'

# Na declaração irá fazer a inserção 
declaracao = """INSERT INTO tbl_produtos
(idProduto, nomeProduto, precoProduto, quantProduto)
VALUES ("""

# Na variavel sql tera os dados fornecidos e a inserção no banco de dados
sql = declaracao +  dados
print(sql)

# começara a conexão
try:
  # Irá fornecer o seu host, database, usuario e senha 
  con= mysql.connector(host="localhost", database ="db_cadastro", user='bmob98', password="lalaland")
  # A variavel inserir_produto irá receber  os valores que obtidos no sql
  inserir_produtos = sql
  # O cursor irá receber as informações para entrar no banco de dados
  cursor = con.cursor()
  # E vai executar a inserção dos produtos inseridos pelo usuário
  cursor.execute(inserir_produtos)
  con.commit()
  print(cursor.rowcount,"registro inserido na tabela")
  cursor.close()
except Error as erro:
  print("Falha ao inserir dados no MySQL:{}".format(erro))
# Se ocorrer tudo bem irá o conector irá ser encerrado
finally:
  if(con.is_connected()):
    cursor.close()
    con.close()
    print("conexão ao MySQL foi encerrado")
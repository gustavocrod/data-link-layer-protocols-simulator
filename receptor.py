"""
    - O receptor recebe uma mensagem codificada do remetente
    - Receptor com uma replica da chave decodifica os dados e verifica o resto
    - se o resto eh zero, entao siginifica que nao tem nenhum erro 
    - se o resto nao eh zero, sigifnica que deu erro, e um NON ACK eh enviado ao remetente
    - O remetente precisa reenviar o dado ate que o receptor tenha os dados corretos
"""

import socket
from util import decodeData

s = socket.socket()
s.bind(('',))
s.listen(5)
print("listening...")

while True:
    c, addr = s.accept() # estabelece conexao com cliente
    print("Conectado com ", addr)
    dado = c.recv(1024)
    print("Dado recebido: " + dado)
    
    if not dado:
        break
    
    chave = "1011"
    quest = decodeData(dado, chave) # decodifica com a copia da chave q o server tem
    print("Resto depois da decodificacao eh: " + quest)
    
    aux = '0'*(len(chave)-1) # se resto sao todos zeros entao n teve erro
    if quest == aux:
        c.sendall("Recebemos o dado: " + dado + " sem nenhum erro!")
    else:
        c.sendall("Erro no dado")
    
    c.close()
        

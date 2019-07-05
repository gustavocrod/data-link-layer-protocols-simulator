import socket
from util import decodeData

s = socket.socket()
s.bind(('',9000))
s.listen(5)
print("listening...")

while True:
    c, addr = s.accept() # estabelece conexao com cliente
    #print("Conectado com ", addr)
    dado = c.recv(1024)
    
    if not dado:
        break
    
    chave = "1011"
    quest = decodeData(dado, chave) # decodifica com a copia da chave q o server tem
    #print("Resto depois da decodificacao eh: " + quest)
    
    aux = '0'*(len(chave)-1) # se resto sao todos zeros entao n teve erro
    if quest == aux:
        c.sendall("ACK")
    else:
        c.sendall("NON ACK")
    
    c.close()
        

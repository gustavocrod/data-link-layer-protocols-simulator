import socket
from util import encodeData

s = socket.socket()
s.connect(('127.0.0.1', ))

input = raw_input("Entre com os dados que deseja enviar: ")
dado = (''.join(format(ord(x), 'b') for x in input))
print("dado: " + dado)
chave = "1011"

quest = encodeData(dado, chave)
print("dado cifrado: " + quest)
s.sendall(quest)

print("Server retornou: "+ s.recv(1024))
s.close()
    
    

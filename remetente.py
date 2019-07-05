import socket
from util import encodeData, framing

s = socket.socket()
s.connect(('127.0.0.1', 9000))

input = raw_input("Entre com os dados que deseja enviar: ")
dado = (''.join(format(ord(x), 'b') for x in input)) # conversao para binario
print("dado: " + dado)
chave = "1011"
dado = framing(dado)
quest = encodeData(dado, chave) # codificar o dado com a chave
print("dado cifrado: " + quest)
s.sendall(quest)

print("Server retornou: "+ s.recv(1024))
s.close()
    
    

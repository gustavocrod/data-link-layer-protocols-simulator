import socket
from util import encodeData
"""
- Enviar dados para o lado do servidor / receptor
- O remetente envia uma string
- Primeiro converte a string em binario, uma chave eh conhecida entre os dois lados
- Os dados estao codificados usando o codigo CRC usando a chave no lado do remetente
- O dado "cifrado" eh enviado para o receptor
- Receptor decodifica o dado para verificar se tem algum erro ou nao
"""

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
    
    

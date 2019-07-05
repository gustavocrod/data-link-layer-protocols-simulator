import socket
from util import encodeData, framing

s = socket.socket()
s.connect(('127.0.0.1', 9000))

input = input("Entre com os dados que deseja enviar: ")
payload = (''.join(format(ord(x), 'b') for x in input)) # conversao para binario
macSender = (''.join(format(ord(x), 'b') for x in "5cc9d36f417e"))
macReceiver = (''.join(format(ord(x), 'b') for x in "5cc9d36f417e"))
chave = "1011"
delimiter = 50
serverReturn = "NON ACK"

frames = framing(payload, delimiter, macSender, macReceiver)
print(frames)
for frame in frames:
    frame = (''.join(format(ord(x), 'b') for x in frame))
    frameToSend = encodeData(frame, chave) # codificar o dado com a chave
    while serverReturn == "NON ACK": # reenvia se o server der um non ack #stop and wait aqui, pois envia 1 por vez
        s.sendall(frameToSend)
        serverReturn = s.recv(1024)
        s.close()
    
    

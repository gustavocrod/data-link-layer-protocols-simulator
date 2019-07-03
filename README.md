# Data Link Layer protocols simulator

## CRC 
ou Verificacao de Redundância Ciclica é um metodo de detecção de erros no canal de comunicação

Ele utiliza o polinomio do gerador, que esta em ambos os lados (receiver e sender)

Exemplo de polinomio gerador: 
x^3 + 1 (chave 1001)
x^2 + x (chave 110)

## Receiver CRC
O receiver recebe uma mensagem codificada do sender

O receiver (com sua replica da chave) decodifica os dados e verifica o resto da divisao

se o resto for 0s, entao não houve erro

se o resto for !0s, deu algum erro, e um NON ACK é enviado ao sender

O sender precisa reenviar o dado ate que o receiver tenha os dados corretos

## Sender CRC
O sender envia os dados para o lado do servidor (receiver)

O remetente envia os dados (string)

Converte a string em binario

Os dados sao codificados usando o codigo CRC + a chave no lado do sender




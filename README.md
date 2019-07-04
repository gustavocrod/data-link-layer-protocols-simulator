# Data Link Layer protocols simulator

## CRC 
ou Código de Redundância Ciclica é um metodo de detecção de erros no canal de comunicação

Ele utiliza um codigo gerador, que esta em ambos os lados (receiver e sender)

Funciona da seguinte forma: Um código CRC é incorporado a mensagem enviada, o receptor quando a recebe, faz o cálculo e verifica se o CRC resultante é o mesmo incorporado a mensagem.

O cálculo é feito com base na divisão da mensagem binária pelo gerador, os valores são calculados separadamente com um XOR.

Exemplo de codigo polinomial: 
x^3 + 1 (chave 1001)
x^2 + x (chave 110)
x^5 + x^3 + x^2 + x^0 (chave 101101)

## Sender CRC

* Converte a string que deseja enviar para binario

* Adiciona à string o numero de 0s = a quantidade de bits do gerador - 1 

* Calcula o CRC (XOR)

* Adiciona ao final da mensagem o codigo CRC

* O sender envia os dados para o receiver

## Receiver CRC
* O receiver recebe uma mensagem codificada do sender

* O receiver (com sua replica da chave) decodifica os dados e verifica o resto da divisao

  * se o resto for 0s, entao não houve erro

  * se o resto for !0s, deu algum erro, e um NON ACK é enviado ao sender

* O sender precisa reenviar o dado ate que o receiver tenha os dados corretos






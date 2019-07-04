# Data Link Layer protocols simulator

## Framing
ou Enquadramento

* Dividir o bit-stream em quadros (unidade de transmissao de dados) para gerenciar a transmissão e facilitar no controle de erros.

#### Contagem de caracter

* Adicionar um campo no header indicando o número de caracteres presente no frame (quadro)

* Ao receber o quadro, o receiver lê o campo de contagem e sabe a partir dali determinar onde está o final do quadro

- [Problema:] perde sincronização se houver erro no campo que indica o número de caracteres.

#### Enquadramento por caracter

* Inserir um caracter especial (flag) no ínicio e no fim do quadro

- [Problema:] End of TeXt ou Start of TeXt podee estar presente nos DADOS, o que gera erro de interpretação



## CRC 
ou Código de Redundância Ciclica é um metodo de detecção de erros no canal de comunicação

Ele utiliza um codigo gerador, que é conhecido por ambos os lados (receiver e sender)

Funciona da seguinte forma: Um código CRC é incorporado a mensagem enviada, o receptor quando a recebe, faz o cálculo e verifica se o CRC resultante é o mesmo incorporado a mensagem.

O cálculo é feito com base na divisão da mensagem binária pelo gerador, os valores são calculados separadamente com um XOR.

Exemplo de codigo polinomial: 
x^3 + 1 (chave 1001)
x^2 + x (chave 110)
x^5 + x^3 + x^2 + x^0 (chave 101101)

#### Sender CRC

* Converte a string que deseja enviar para binario

* Adiciona à string o numero de 0s = (quantidade de bits do gerador) - 1 

* Calcula o CRC //modulo 2 - xor que é realizado transladando para a direita a cada iteração

* O resto da divisao é o CRC

* Adiciona ao final da mensagem o codigo CRC

* O sender envia os dados para o receiver

#### Receiver CRC
* O receiver recebe uma mensagem codificada do sender

* O receiver (com sua replica da chave) decodifica os dados e verifica o resto da divisao

  * se o resto for 0s, entao não houve erro

  * se o resto for !0s, deu algum erro, e um NON ACK é enviado ao sender

* O sender precisa reenviar o dado ate que o receiver tenha os dados corretos






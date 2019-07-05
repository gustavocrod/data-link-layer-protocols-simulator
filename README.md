# Data Link Layer protocols simulator

Um sistema Full-Duplex, que simula uma camada de enlace implementando enquadramento por caracter utilizando DLE, o controle de fluxo utilizando Stop-and-Wait e detecçao de erros utilizando CRC.

Os conceitos necessarios para entender a implementacao encontram-se abaixo: 

# Framing
ou Enquadramento

* Dividir o bit-stream em quadros (unidade de transmissao de dados) para gerenciar a transmissão e facilitar no controle de erros.

### Contagem de caracter

* Adicionar um campo no header indicando o número de caracteres presente no frame (quadro)

* Ao receber o quadro, o receiver lê o campo de contagem e sabe a partir dali determinar onde está o final do quadro

[Problema:] perde sincronização se houver erro no campo que indica o número de caracteres.

### Enquadramento por caracter

* Inserir um caracter especial no ínicio e no fim do quadro

[Problema] End of TeXt (ETX) ou Start of TeXt (STX) podem estar presente nos DADOS (se repetir dentro dos dados), o que gera erro de interpretação 

##### Tentativa de soluçao

* Inserir um dado DLE (Data Link Escape) antes de cada caracter especial

[Problema] DLE pode ainda estar presente nos DADOS

##### Solucao definitiva

* Percorrer o payload antes de transmitir

* Se encontrar um DLE inserir outre DLE antes deste

* Assim, quando o receptor encontrar dois DLEs ele descarta um e sabe qe o resto eh texto e nao flag

### Enquadramento por bit

* Delimitador de frame: flag (sequencia padrao de bits)

* Cada quadro começa e termina com o flag.

[Exemplo] 01111110 ou 01^0

[Problema] O flag pode estar presente nos DADOS

* Regra: a cada sequencia de 5 bits '1' inserir um bit '0' (chamado de bit stuffing) (Usado no HDLC)

# Codigos de Detecçao/Correçao de Erros

* Duas estrategias basicas:

1 - Incluir informacao redundante suficiente para permitir que o receptor detecte e corrija erros ("Open loop")

2 - Incluir informaçao redundante apenas para permitir que o receptor detecte erros na mensagem ("Feedback")

#### Open Loop

* Nao ha necessidade de retransmissao

* Receptor eh capaz de recuperar a informacao (Forward Error Correction - FEC)

#### Feedback

* Receptor detecta erro e solicita retransmissao ao trasmissor (implementaçao atraves dos protocolos ARQ) [Implementado]

### CRC [Implementado] 
ou Código de Redundância Ciclica 

* metodo de detecção de erros no canal de comunicação

* Utiliza um codigo gerador, que é conhecido por ambos os lados (receiver e sender)

* Funciona da seguinte forma: Um código CRC é incorporado a mensagem enviada, o receptor quando a recebe, faz o cálculo e verifica se o CRC resultante é o mesmo incorporado a mensagem.

* O cálculo é feito com base na divisão da mensagem binária pelo gerador, os valores são calculados separadamente com um XOR.

[EXEMPLO] codigo Polinomial: 
x^3 + 1 (chave 1001)
x^2 + x (chave 110)
x^5 + x^3 + x^2 + x^0 (chave 101101)

##### Sender CRC [Implementado]

* Converte a string que deseja enviar para binario

* Adiciona à string o numero de 0s = (quantidade de bits do gerador) - 1 

* Calcula o CRC //modulo 2 - xor que é realizado transladando para a direita a cada iteração

* O resto da divisao é o CRC

* Adiciona ao final da mensagem o codigo CRC

* O sender envia os dados para o receiver

##### Receiver CRC [Implementado]
* O receiver recebe uma mensagem codificada do sender

* O receiver (com sua replica da chave) decodifica os dados e verifica o resto da divisao

  * se o resto for 0s, entao não houve erro, um ACK e enviado ao sender

  * se o resto for !0s, deu algum erro, e um NON ACK é enviado ao sender

* O sender precisa reenviar o dado ate que o receiver tenha os dados corretos






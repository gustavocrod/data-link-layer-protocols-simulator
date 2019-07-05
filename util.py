
def framing(payload, delimiter, macSender, macReceiver):
    """
        enquadramento por flag no inicio do payload
    """
    lista_dado = list(payload) # conversao da string em uma lista para poder percorrer
    cont = 0 # contador auxiliar
    frames=[] # armazenar os quadros
    for i in range (0, len(lista_dado)):
        frame = []
        if (cont == delimiter):
            macsender = (''.join(format(ord(x), 'b') for x in macSender)) # converte o mac do remetente para bit
            macreceiver = (''.join(format(ord(x), 'b') for x in macReceiver)) # converte o mac do destinatario para bit
            frame.append(macsender) # adiciona no inicio do quadro
            frame.append(macreceiver) # adiciona depois do mac do sender
            dado = lista_dado[i+1:i+delimiter] # 
            if (len(dado) < delimiter): # padding
                for j in range (len(dado), delimiter):
                    dado.append('1')
            dado = ''.join(dado)
            frame.append(dado)
            frame = ''.join(frame)
            frames.append(frame)
            cont = 0
        cont+=1
        
    return frames


def xor(a, b):
    """
        Percorre toda a cadeia de bits
        Se bit sao iguais, XOR = 0
                    senao  XOR = 1
        Ou exclusivo
    """
    resultado = []
    for i in range(1, len(b)):
        if (a[i] == b[i]):
            resultado.append('0')
        else: 
            resultado.append('1')
    return ''.join(resultado)

def mod2div(dividendo, divisor):
    """
        recebe um numero para dividir
        e um numero divisor (chave)
        Realiza divisao Modulo-2 
        
    """
    pick = len(divisor) #numero de bits que vao ir para xor ao mesmo tempo
    
    # pega um pedaco do dividendo apenas
    aux = dividendo[0 : pick] # de 0 ate o tamanho do divisor
    
    while (pick < len(dividendo)): # enquanto nao dividir todo o numero
        # se o bit mais significante eh '1'
        if aux[0] == '1':
            # troca o dividendo pelo resultado da xor 
            aux = xor(divisor, aux) + dividendo[pick]
        # se bit mais significante eh '0'
        else: 
            """
                se o mais a esquerda do dividendo for 0, o passo nao pode
                utilizar o divisor regular, entao  precisa-se usar um divisor
                "all-0s" 
            """
            aux = xor('0'*pick, aux) + dividendo[pick]
            
        pick += 1 # incrementa pick para o prox
        
    """
        para os ultimos bits, tem q ser feito "na mao", pois o valor pode exceder
        o numero de bouds
    """
    if (aux[0] == '1'):
        aux = xor(divisor, aux)
    else:
        aux = xor('0'*pick, aux)
            
    check = aux
    return check


    
def encodeData(dado, chave):
    """
        funcao usada pelo remetente para codificar os dados
        colocando o resto da divisao por modulo 2 no final dos dados
        
        recebe os dados e a key
    """
    
    dado_append = dado + '0'*(len(chave)-1) # append n-1 zeros no final
    resto = mod2div(dado_append, chave)
    
    palavra_chave = dado + resto # coloca o resto nos dados originais
    
    return palavra_chave

def decodeData(dado, chave):
    """
        funcao usada pelo receptor para decodificar os dados enviados pelo
        remetente
    """
    #adiciona zeros-1 ao final da string de dados
    dado_append = dado + '0'*(len(chave)-1)
    resto = mod2div(dado_append, chave)
    
    return resto

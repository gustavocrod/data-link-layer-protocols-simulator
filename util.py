
def xor(a, b):
    """
        Percorre toda a cadeia de bits
        Se bit sao iguais, XOR = 0
                    senao  XOR = 1
        Ou exclusivo
    """
    resultado = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            resultado.append('0')
        else: 
            resultado.append('1')
    return ''.join(resultado)

def mod2div(dividendo, divisor):
    """
        recebe um numero para dividir
        e um numero divisos
        Realiza divisao Modulo-2 
        
    """
    pick = len(divisor) #numero de bits que vao ir para xor ao mesmo tempo
    
    # pega um pedaco do dividendo apenas
    aux = dividendo[0 : pick] # de 0 ate o tamanho do divisor
    
    while pick < len(dividendo):
        if aux[0] == '1':
            # troca o dividendo pelo resultado da xor 
            aux = xor(divisor, aux) + dividendo[pick]
        # bit mais sifnificante eh '0'
        else: 
            """
                se o mais a esquerda do dividendo for 0, o passo nao pode
                utilizar o divisor regular, entao  precisa-se usar um divisor
                "all-0s" 
            """
            aux = xor('0'*pick, aux) + dividendo[pick]
            
        pick += 1 # incrementa pick para o prox
        
    """
        para os ultimos bits, tem q ser feito na mao, pos o valor pode exceder
        o numero de bouds
    """
    if aux[0] == '1':
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

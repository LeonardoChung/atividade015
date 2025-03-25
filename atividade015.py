import random

def gerar_palavras():
    primeiras_letras = ['q', 'w', 'x', 'z']  
    segundas_letras = ['a', 'i', 'u']  
    terceiras_letras = ['c', 'f', 'p'] 
    quartas_letras = ['e', 'o']  

    # lista para armazenar as palavras geradas
    palavras = []
    
    # gera todas as combinações possíveis de palavras
    for primeira in primeiras_letras:
        for segunda in segundas_letras:
            for terceira in terceiras_letras:
                for quarta in quartas_letras:
                    palavra = primeira + segunda + terceira + quarta
                    palavras.append(palavra)
    
    return palavras

def gerar_sorteios(palavras, numero_sorteios=72):
    contagem_palavras = {}
    
    for _ in range(numero_sorteios):
        palavra_sorteada = random.choice(palavras)
        
        # incrementa a contagem da palavra sorteada
        if palavra_sorteada in contagem_palavras:
            contagem_palavras[palavra_sorteada] += 1
        else:
            contagem_palavras[palavra_sorteada] = 1
    
    return contagem_palavras

# gera todas as palavras possíveis
todas_palavras = gerar_palavras()

# realiza os sorteios
resultados_sorteios = gerar_sorteios(todas_palavras)

for palavra, contagem in resultados_sorteios.items():
    print(f"{palavra} | {contagem}")
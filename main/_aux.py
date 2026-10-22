#arquivo de funções auxiliares do código principal, regendo principalmente os caminhos das imagens
import random
#caminhos das imagens dos dados e cartas
imgs_d6 = ["imgs/d6/face1_2.png","imgs/d6/face1_2.png","imgs/d6/face3_4.png",
           "imgs/d6/face3_4.png","imgs/d6/face5.png","imgs/d6/face6.png"]
                
imgs_d10 = ["imgs/d10/face1_2.png","imgs/d10/face1_2.png","imgs/d10/face3_4.png","imgs/d10/face3_4.png","imgs/d10/face5.png",
            "imgs/d10/face6.png","imgs/d10/face7.png","imgs/d10/face8.png","imgs/d10/face9.png","imgs/d10/face10.png"]
                 
imgs_d12 = ["imgs/d12/face1_2.png","imgs/d12/face1_2.png","imgs/d12/face3_4.png","imgs/d12/face3_4.png","imgs/d12/face5.png","imgs/d12/face6.png",
            "imgs/d12/face7.png","imgs/d12/face8.png","imgs/d12/face9.png","imgs/d12/face10.png","imgs/d12/face11.png","imgs/d12/face12.png"]

imgs_cartas_copas = ["imgs/cartas_copas/carta1.png","imgs/cartas_copas/carta2.png","imgs/cartas_copas/carta3.png","imgs/cartas_copas/carta4.png",
                     "imgs/cartas_copas/carta5.png","imgs/cartas_copas/carta6.png","imgs/cartas_copas/carta7.png","imgs/cartas_copas/carta8.png",
                     "imgs/cartas_copas/carta9.png","imgs/cartas_copas/carta10.png","imgs/cartas_copas/carta11.png","imgs/cartas_copas/carta12.png",
                     "imgs/cartas_copas/carta13.png"]

imgs_cartas_ouros = ["imgs/cartas_ouros/carta1.png","imgs/cartas_ouros/carta2.png","imgs/cartas_ouros/carta3.png","imgs/cartas_ouros/carta4.png",
                     "imgs/cartas_ouros/carta5.png","imgs/cartas_ouros/carta6.png","imgs/cartas_ouros/carta7.png","imgs/cartas_ouros/carta8.png",
                     "imgs/cartas_ouros/carta9.png","imgs/cartas_ouros/carta10.png","imgs/cartas_ouros/carta11.png","imgs/cartas_ouros/carta12.png",
                     "imgs/cartas_ouros/carta13.png"]

imgs_cartas_espadas = ["imgs/cartas_espadas/carta1.png","imgs/cartas_espadas/carta2.png","imgs/cartas_espadas/carta3.png","imgs/cartas_espadas/carta4.png",
                      "imgs/cartas_espadas/carta5.png","imgs/cartas_espadas/carta6.png","imgs/cartas_espadas/carta7.png","imgs/cartas_espadas/carta8.png",
                      "imgs/cartas_espadas/carta9.png","imgs/cartas_espadas/carta10.png","imgs/cartas_espadas/carta11.png","imgs/cartas_espadas/carta12.png",
                      "imgs/cartas_espadas/carta13.png"]

imgs_cartas_paus = ["imgs/cartas_paus/carta1.png","imgs/cartas_paus/carta2.png","imgs/cartas_paus/carta3.png","imgs/cartas_paus/carta4.png",
                    "imgs/cartas_paus/carta5.png","imgs/cartas_paus/carta6.png","imgs/cartas_paus/carta7.png","imgs/cartas_paus/carta8.png",
                    "imgs/cartas_paus/carta9.png","imgs/cartas_paus/carta10.png","imgs/cartas_paus/carta11.png","imgs/cartas_paus/carta12.png",
                    "imgs/cartas_paus/carta13.png"]
def _gera_aleatorio(n: int): #gera um número aleatório entre 0 e n-1
    return random.randint(0, n-1)

def escolhe_imagem_dado(lado: int): #sorteia um caminho de imagem de acordo com o lado do dado
    rolagem  = _gera_aleatorio(lado)
    if (lado == 6):
        return imgs_d6[rolagem]
    elif (lado == 10):
        return imgs_d10[rolagem]
    elif (lado == 12):
        return imgs_d12[rolagem]

def escolhe_imagem_carta(naipe: int, carta: int): #retorna a imagem de uma carta dado seu número e seu naipe
    if (naipe == 0):
        return imgs_cartas_copas[carta-1]
    elif (naipe == 1):
        return imgs_cartas_ouros[carta-1]
    elif (naipe == 2):
        return imgs_cartas_espadas[carta-1]
    elif (naipe == 3):
        return imgs_cartas_paus[carta-1]
    
def sorteia_carta(naipe: int, qtd_cartas: int): #sorteia um número de cartas (qtd_cartas) dado seu naipe e retorna uma lista com os caminhos das cartas
    cartas_sorteadas = []
    for i in range(qtd_cartas):
        rand = _gera_aleatorio(13)
        if (rand in cartas_sorteadas):
            while (rand in cartas_sorteadas): #não deixa sortear uma carta mais de uma vez
                rand = _gera_aleatorio(13) #13 numeros possíveis (0 a 12)
        cartas_sorteadas.append(rand) #armazena os valores inteiros na lista
    if (naipe == 0):
            return [imgs_cartas_copas[i] for i in cartas_sorteadas]
    elif (naipe == 1):
        return [imgs_cartas_ouros[i] for i in cartas_sorteadas]
    elif (naipe == 2):
        return [imgs_cartas_espadas[i] for i in cartas_sorteadas]
    elif (naipe == 3):
        return [imgs_cartas_paus[i] for i in cartas_sorteadas]
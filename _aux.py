import random
#caminho das imagens dos dados
imgs_d6 = ["imgs/d6/face1.png","imgs/d6/face2.png","imgs/d6/face3.png",
                "imgs/d6/face4.png","imgs/d6/face5.png","imgs/d6/face6.png"]
                
imgs_d10 = ["imgs/d10/face1.png","imgs/d10/face2.png","imgs/d10/face3.png","imgs/d10/face4.png","imgs/d10/face5.png",
                 "imgs/d10/face6.png","imgs/d10/face7.png","imgs/d10/face8.png","imgs/d10/face9.png","imgs/d10/face10.png"]
                 
imgs_d12 = ["imgs/d12/face1.png","imgs/d12/face2.png","imgs/d12/face3.png","imgs/d12/face4.png","imgs/d12/face5.png","imgs/d12/face6.png",
                 "imgs/d12/face7.png","imgs/d12/face8.png","imgs/d12/face9.png","imgs/d12/face10.png","imgs/d12/face11.png","imgs/d12/face12.png"]

def _gera_aleatorio(lado: int): 
    return random.randint(1, lado)

def escolhe_imagem(lado: int):
    rolagem  = _gera_aleatorio(lado)
    if (lado == 6):
        return imgs_d6[rolagem-1]
    elif (lado == 10):
        return imgs_d10[rolagem-1]
    elif (lado == 12):
        return imgs_d12[rolagem-1]
        
    

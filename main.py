import _aux
import io
import os
import discord 
from discord.ext import commands
from dotenv import load_dotenv 
from PIL import Image

load_dotenv()
TOKEN = os.getenv('TOKEN_BOT') #importa o token do arquivo .env
intents = discord.Intents.all() #lista de permissões do bot no servidor 
bot = commands.Bot("&", intents=intents) #"cérebro" do bot. Definição do prefixo e definição da lista de permissões

@bot.event
async def on_ready(): #mensagem de inicialização do bot
    print("----------------------------------------")
    print("      Sucesso! Bot inicializado.")
    print("----------------------------------------")
    
@bot.command() #comandos do bot
async def ajuda(ctx):
    await ctx.send("**Bot de rolagem de dados de assimilação RPG. Use o comando `&dado` e digite os valores dos dados no formato `'xdy'` **." + "\nEx: `3d6+2d10`, `4d12`")

@bot.command()
async def cartas(ctx, *, mensagem: str):
    msg = mensagem.lower()
    comandos = ["info", "sort"] 
    naipes = ["c", "o", "e", "p"]
    if msg.find(comandos[0]) != -1:
        # Pega tudo após o comando 'info' e remove espaços extras nas pontas
        msg = msg[msg.find(comandos[0]) + len(comandos[0]):].strip()
        # Encontra o naipe na mensagem
        naipe = next((i for i in naipes if i in msg), None)
        if naipe is None:
            await ctx.send("**ERRO DE DIGITAÇÃO: NAIPE INVÁLIDO!**") 
            return
        pos = msg.find(naipe)
        # Pega todo o texto que está ANTES do caractere do naipe e remove espaços
        texto_numero = msg[:pos].strip()
        # Verifica se a parte anterior é realmente numérica (ex: "1", "10", "13")
        if not texto_numero.isdigit():
            await ctx.send("**ERRO DE DIGITAÇÃO: NÚMERO INVÁLIDO!**")
            return
        carta = int(texto_numero)
        # Valida se a carta está dentro do intervalo permitido (1 a 13)
        if carta < 1 or carta > 13:
            await ctx.send("**NÚMERO DA CARTA INVÁLIDO (USE DE 1 A 13)!!!**") 
            return
        caminho_img = _aux.escolhe_imagem_carta(naipes.index(naipe), carta)
        await ctx.send(caminho_img)
    elif (msg.find(comandos[1]) != -1):
        msg = msg[msg.find(comandos[1]) + len(comandos[1]):].strip() #define a mensagem ignorando o comando ('sort') e espaços em branco
        pass
    else:
        await ctx.send("**ERRO DE DIGITAÇÃO!!!**") 
        return
@bot.command() #comandos do bot
async def dado(ctx, *, rolagem: str):
    dados = ["d6", "d10", "d12"]
    dados_rolados = []
    qtd_dados_rolados = {}
    for i in range(len(dados)):
        if (rolagem.find(dados[i]) != -1):
            pos = rolagem.find(dados[i])
            if (rolagem[pos-1].isdigit()): #trata erros de digitação fora do formato 'xdy' Ex: 3d6 ; 2d12 ; 2d6+1d10 
                if pos >= 2 and rolagem[pos-2].isdigit(): #verifica se o dígito é >= 10
                    qtd_dados = int(rolagem[pos-2:pos])
                else:
                    qtd_dados = int(rolagem[pos-1])

                if (qtd_dados > 12 or qtd_dados == 0): #trata erro de limite de rolagens de um único dado ( min:1 ; max:12)
                    await ctx.send(f"**NÚMERO DE `{dados[i]}` INVÁLIDO! TENTE NOVAMENTE!!!**") 
                    return
                qtd_dados_rolados[dados[i]] = qtd_dados
                for j in range(qtd_dados):
                    dados_rolados.append(_aux.escolhe_imagem_dado(6 if i == 0 else (10 if i == 1 else 12))) #faz a rolagem e guarda os caminhos das imagens em 'dados_rolados'
            else:
                await ctx.send("**ERRO DE DIGITAÇÃO!!!**") 
                return
        else:
            continue
    
    if dados_rolados:
        #configuração da grade de dados (saída estilizada)
        TAMANHO_DADO = 67 #tamanho do dado considerando espaçamentos
        QTD_COLUNAS = 3
        qtd_linhas = (len(dados_rolados) // 3 + 1) if len(dados_rolados) % 3 != 0 else len(dados_rolados) // 3
        grade = Image.new('RGBA', (QTD_COLUNAS*TAMANHO_DADO, qtd_linhas*TAMANHO_DADO), (0,0,0,0)) #grade trasparente (sem fundo) para organizar os dados

        cont_coluna = 0
        cont_linha = 0
        for i in dados_rolados:
            img_dado = Image.open(i).convert('RGBA')
            grade.paste(img_dado, (TAMANHO_DADO*cont_coluna, TAMANHO_DADO*cont_linha), img_dado)
            if (cont_coluna == QTD_COLUNAS-1):
                cont_coluna = 0
                cont_linha += 1
            else:
                cont_coluna += 1
        #salva a imagem combinada na memória RAM (sem criar arquivos no disco)
        buffer = io.BytesIO()
        grade.save(buffer, format='PNG')
        buffer.seek(0)

        arq_final = discord.File(buffer, filename="resultados_dados.png")
        #envia um texto inicial mencionando quem rolou e mostra a grade com os dados
        await ctx.send(
                    f"🎲 {ctx.author.mention} **fez uma rolagem de {'+'.join(f'`{valor}{chave}`' for chave, valor in qtd_dados_rolados.items())}:**", 
                    file=arq_final)
bot.run(TOKEN)
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
    await ctx.send("="*78 + "\n" + "Bot de rolagem de dados de assimilação RPG. Use o comando `&dado` e digite os valores dos dados no formato **'xdy'**." + "\nEx: `3d6+2d10`, `4d12`\n" + "="*78)
    
@bot.command() #comandos do bot
async def dado(ctx, *, rolagem: str):
    dados = ["d6", "d10", "d12"]
    dados_rolados = []
    qtd_dados_rolados = {}
    for i in range(3):
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
                    dados_rolados.append(_aux.escolhe_imagem(6 if i == 0 else (10 if i == 1 else 12))) #faz a rolagem e guarda os caminhos das imagens em 'dados_rolados'
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
                    file=arq_final
                )
bot.run(TOKEN)

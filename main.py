import _aux
import os
import discord 
from discord.ext import commands
from dotenv import load_dotenv 

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
    await ctx.send("Bot de rolagem de dados de assimilação RPG. Use o comando **&dado** e digite os valores dos dados no formato **'xdy'**. Ex: **1d6+2d10**, **3d6+1d12**")
    
@bot.command() #comandos do bot
async def dado(ctx, *, rolagem: str):
    dados = ["d6", "d10", "d12"]
    dados_rolados = []
    for i in range(3):
        if (rolagem.find(dados[i]) != -1):
            pos = rolagem.find(dados[i])
            if (rolagem[pos-1].isdigit() and int(rolagem[pos-1]) > 0): #só pode fazer uma rolagem caso a digitação esteja correta no formato 'xdy' Ex: 3d6 ; 2d10; 1d12 
                qtd_dados = int(rolagem[pos-1])
                for j in range(qtd_dados):
                    dados_rolados.append(_aux.escolhe_imagem(6 if i == 0 else (10 if i == 1 else 12))) #faz a rolagem e guarda os caminhos das imagens em 'dados_rolados'
            else:
                await ctx.send("**ERRO DE DIGITAÇÃO!!!**") 
                return 0
        else:
            continue
            
    #resultado das rolagens
    if dados_rolados:
        #cria uma lista de objetos discord.File usando os caminhos gerados
        arquivos_discord = []
        for i in dados_rolados:
            arquivos_discord.append(discord.File(i))
            
        #envia um texto inicial mencionando quem rolou e anexa todas as imagens juntas
        await ctx.send(
            f"🎲 {ctx.author.mention} **rolou os dados e obteve o(s) seguinte(s) resultado(s):**", 
            files=arquivos_discord
        )

bot.run(TOKEN)

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
    embed = discord.Embed(
        title="📜 Guia de Comandos: Assimila - BOT",
        description="Confira abaixo como utilizar os comandos de `rolagens` e `cartas` do bot:",
        color=0x3498DB  #cor azul da barra lateral
    )
    #seção dos dados
    embed.add_field(
        name="🎲 ROLAGEM DE DADOS (`&dado`)",
        value=(
            "Para rolar dados, utilize o formato padrão `xdy`.\n"
            "• **Exemplos:** `&dado 3d6+2d10` | `&dado 4d12`\n"
            "• Suporta múltiplos dados (máx: **12** de um dado do mesmo tipo)."
        ),
        inline=False
    )
    #seção das cartas 'Info'
    embed.add_field(
        name="🃏 INFORMAÇÕES DE CARTAS (`&cartas info`)",
        value=(
            "Exibe a imagem de uma carta específica usando o valor e a letra do naipe.\n"
            "• **Exemplo:** `&cartas info 10c` -> **10 de Copas**\n"
            "• Os números variam entre **1-13**.\n"
            "• **Naipes:** `c (copas) | o (ouros) | e (espadas) | p (paus)`\n"
            "• **Cartas**: `1 -> Ás | 11 -> Valete | 12 -> Dama | 13 -> Rei`\n"  
        ),
        inline=False
    )
    #seção das cartas 'Sort'
    embed.add_field(
        name="🎴 SORTEIO DE CARTAS (`&cartas sort`)",
        value=(
            "Sorteia a quantidade especificada de cartas para cada naipe informado.\n"
            "• **Exemplo:** `&cartas sort 3c 2o` -> Sorteia 3 cartas de **copas** e 2 de **ouros**\n"
            "• Suporta múltiplos naipes na mesma mensagem.\n"
            "• Os números variam entre **1-13**.\n"
            "• **Naipes:** `c (copas) | o (ouros) | e (espadas) | p (paus)`\n"
        ),
        inline=False
    )
    embed.set_footer(text="Assimila - BOT • Digite os comandos corretamente para evitar erros.")
    await ctx.send(embed=embed)
@bot.command() #comando do bot
async def legenda(ctx):
    embed = discord.Embed(
            title="📝 LEGENDA",
            description="Segue abaixo a `legenda` das informações das cartas:",
            color=0x3498DB  #cor azul da barra lateral
        )
    embed.add_field(name="",
            value=(
                "**`J` -> Joaninha | `B` -> Cervo | `C` -> Coruja**\n"
                "**`D` -> Nível de Determinação | `d` -> Ponto de Determinação**\n"
                "**`A` -> Nível de Assimilação | `a` -> Ponto de Assimilação**\n"
                "**`S` -> Nível de Saúde | `s` -> Ponto de Saúde | `P` -> Penalidade**"
            ),
            inline=False
        )
    await ctx.send(embed=embed) 

@bot.command() #comando do bot
async def cartas(ctx, *, mensagem: str):
    msg = mensagem.lower()
    comandos = ["info", "sort"] 
    naipes = ["c", "o", "e", "p"]
    
    if (msg.find(comandos[0]) != -1): #trata as nuâncias do comando '&cartas info'
        msg = msg[msg.find(comandos[0]) + len(comandos[0]):].strip() #pega tudo após o comando 'info' e remove espaços em branco
        naipe = next((i for i in naipes if i in msg), None) #encontra o naipe na mensagem
        
        if (naipe is None): #trata se não encontrou um dos naipes 'c, o, e, p'
            await ctx.send("**ERRO DE DIGITAÇÃO: NAIPE INVÁLIDO!**") 
            return
       
        pos = msg.find(naipe)
        texto_numero = msg[:pos] #pega todo o texto que está antes do caractere do naipe
        
        if (not texto_numero.isdigit()): #verifica se a parte anterior é realmente um número
            await ctx.send("**ERRO DE DIGITAÇÃO: NÚMERO INVÁLIDO!**")
            return
        
        carta = int(texto_numero)
        
        if (carta < 1 or carta > 13): #valida se a carta está dentro do intervalo permitido (1 a 13)
            await ctx.send("**NÚMERO DA CARTA INVÁLIDO (USE DE 1 A 13)!!!**") 
            return
            
        caminho_img = _aux.escolhe_imagem_carta(naipes.index(naipe), carta)
        
        if not os.path.exists(caminho_img): #trata caso o arquivo da carta não exista
            await ctx.send("**ERRO: IMAGEM DA CARTA NÃO ENCONTRADA!**")
            return

        #envia diretamente a imagem da carta informada
        arq_carta = discord.File(caminho_img, filename="carta.png")
        await ctx.send(f"**Informações da `carta {carta}`**")
        await ctx.send(file=arq_carta)
        await ctx.send("**Se for necessário, digite `&legenda` para melhor compreensão das informações.**")
    
    elif (msg.find(comandos[1]) != -1): #trata as nuâncias do comando '&cartas sort'
        cartas_sorteadas = []
        msg = msg[msg.find(comandos[1]) + len(comandos[1]):] #pega tudo após o comando 'sort'
        
        if (len(msg) > 15): #trata tamanho máximo do comando (ex: '10c 11o 10e')
            await ctx.send("**ERRO DE DIGITAÇÃO!!!**")
            return
       
        naipes_presentes = [n for n in naipes if n in msg] #armazena todos os naipes digitados
        
        if not naipes_presentes: #trata se não encontrou um dos naipes 'c, o, e, p' 
            await ctx.send("**ERRO DE DIGITAÇÃO: NENHUM NAIPE ENCONTRADO!**")
            return
            
        for i in naipes_presentes:
            if (msg.count(i) > 1): # Verifica se o mesmo naipe foi digitado mais de uma vez
                await ctx.send(f"**ERRO DE DIGITAÇÃO: NAIPE `{i.upper()}` REPETIDO!**")
                return
            pos_naipe = msg.find(i) #encontra o naipe atual na mensagem
            texto_numero = msg[:pos_naipe].split()[-1] if msg[:pos_naipe].split() else "" #armazena o imediato valor que está anterior ao naipe
            if (texto_numero.isdigit()): #trata se há pelo menos um número antes do naipe (Ex: '3c')
                qtd_cartas = int(texto_numero)
                if (qtd_cartas < 1 or qtd_cartas > 13): #verifica se o número está dentro do limite
                    await ctx.send(f"**ERRO DE DIGITAÇÃO: NÚMERO INVÁLIDO DO NAIPE `{i}`!!!**")
                    return
                
                #adiciona o caminho das cartas sorteadas na lista principal
                resultado_sorteio = _aux.sorteia_carta(naipes.index(i), qtd_cartas)
                if isinstance(resultado_sorteio, list):
                    cartas_sorteadas.extend(resultado_sorteio)
                else:
                    cartas_sorteadas.append(resultado_sorteio)
                    
                msg = msg.replace(texto_numero+i,"") #retira o número de cartas sorteadas e o naipe(Ex: '2c3o' -> '3o')
            else:
                await ctx.send("**ERRO DE DIGITAÇÃO!!!**")
                return
            
        if cartas_sorteadas:
            #prepara a lista de arquivos para envio direto no Discord
            arquivos_envio = []
            for cont, caminho in enumerate(cartas_sorteadas):
                if os.path.exists(caminho):
                    #da um nome único para cada arquivo para evitar conflito
                    arquivos_envio.append(discord.File(caminho, filename=f"carta_{cont}.png"))
            
            if not arquivos_envio:
                await ctx.send("**ERRO: IMAGENS DAS CARTAS NÃO ENCONTRADAS!**")
                return

            #o Discord aceita no máximo 10 arquivos por mensagem, então enviamos em lotes se necessário
            for i in range(0, len(arquivos_envio), 10):
                lote = arquivos_envio[i:i+10]
                if (i == 0):
                    await ctx.send(f"🎴 {ctx.author.mention} **sorteou {len(cartas_sorteadas)} carta(s):**", files=lote)
                else:
                    await ctx.send(files=lote)
        await ctx.send("**Se for necessário, digite `&legenda` para melhor compreensão das informações.**")
   

@bot.command() #comando do bot
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
    #configuração da grade de dados (saída estilizada)
    if dados_rolados:
        TAMANHO_DADO = 67 #tamanho do dado (em pixels) considerando espaçamentos
        QTD_COLUNAS = 3 #tamanho máximo de dados em uma única linha
        qtd_linhas = (len(dados_rolados) // 3 + 1) if len(dados_rolados) % 3 != 0 else len(dados_rolados) // 3 #define quantas linhas estarão presentes na grade
        grade = Image.new('RGBA', (QTD_COLUNAS*TAMANHO_DADO, qtd_linhas*TAMANHO_DADO), (0,0,0,0)) #grade trasparente (sem fundo) para organizar os dados
        cont_coluna = 0
        cont_linha = 0
        
        for i in dados_rolados:
            img_dado = Image.open(i).convert('RGBA') #abre a imagem do dado
            grade.paste(img_dado, (TAMANHO_DADO*cont_coluna, TAMANHO_DADO*cont_linha), img_dado) #copia a imagem do dado na grade na posição ideal
            if (cont_coluna == QTD_COLUNAS-1): #verifica se acabou o espaço da linha e parte para próxima
                cont_coluna = 0
                cont_linha += 1
            else:
                cont_coluna += 1
        
        buffer = io.BytesIO()
        grade.save(buffer, format='PNG')  #salva a imagem combinada na memória RAM (sem criar arquivos no disco)
        buffer.seek(0)

        arq_final = discord.File(buffer, filename="resultados_dados.png")
        #envia um texto inicial mencionando quem rolou e mostra a grade com os dados
        await ctx.send(
                    f"🎲 {ctx.author.mention} **fez uma rolagem de {'+'.join(f'`{valor}{chave}`' for chave, valor in qtd_dados_rolados.items())}:**", 
                    file=arq_final)

bot.run(TOKEN)
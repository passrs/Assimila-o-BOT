# Assimila-o-BOT
BOT de Assimilação RPG feito para usar no discord, desenvolvido sem fins lucrativos para rolagens de dados e sorteio de cartas do sistema. O BOT é funcional para rodar no seu próprio dispositivo, seja ele *Windows*, *Linux* ou *Mac*, ou usando o link funcional do discord para adicioná-lo em seu servidor **(questão ainda em desenvolvimento)**.

## 📌 Seções e Guias
* [📖 Guia de Comandos](#-guia-de-comandos-assimila---bot)
* [⚙️ Pré-Requisitos para o Assimila - BOT rodar em seu dispositivo](#%EF%B8%8F-pr%C3%A9-requisitos-para-o-assimila---bot-rodar-em-seu-dispositivo)
* [🤖 Como criar o Bot no Discord e obter o Token](#-como-criar-o-bot-no-discord-e-obter-o-token-do-seu-bot)
* [🚀 Como Instalar e Rodar o Bot](#-como-instalar-e-rodar-o-bot-siga-as-instru%C3%A7%C3%B5es-passo-a-passo)

---
## ⚙️ Pré-Requisitos para o Assimila - BOT rodar em seu dispositivo

### Pré-requisitos
1. Você precisa de um Bot registrado na sua conta do discord.
2. Você precisa ter a linguagem de programação **Python** instalado no seu computador.
* [Baixar Python (site oficial)](https://www.python.org/downloads/) *(Ao instalar no Windows, marque a opção "Add Python to PATH")*.

---
## 🤖 Como criar o Bot no Discord e obter o Token do seu Bot

Para utilizar este projeto, você precisará registrar um Bot no `painel de desenvolvedores do Discord`, e isso possibilitará gerar o token de acesso do seu bot. 

Este guia vai ensinar como criar a aplicação do seu Bot no *portal de desenvolvedores do Discord*, gerar o token de acesso e convidá-lo para o seu servidor. O processo é simples, gratuito e rápido.

---

### Passo 1: Acessar o Portal de Desenvolvedores
1. Acesse o [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications) e faça login com a sua conta do Discord.
2. No canto superior direito, clique no botão **Nova Aplicação** (*New Application*).
3. Digite o nome do seu bot (ex: `Assimila Bot`) e clique em **Criar** (*Create*).

---

### Passo 2: Configurar o Bot e Permissões de Leitura
1. No menu lateral esquerdo, clique na aba **Bot**.
2. No campo **Nome de usuário** (*Username*), você pode personalizar a foto de perfil e o nome que aparecerá no Discord.
3. Role a página para baixo até a seção **Intenções de Gateway Privilegiadas** (*Privileged Gateway Intents*) e ative as seguintes opções:
   * **INTENÇÃO DE PRESENÇA** (*PRESENCE INTENT*)
   * **INTENÇÃO DE MEMBROS DO SERVIDOR** (*SERVER MEMBERS INTENT*)
   * **INTENÇÃO DE CONTEÚDO DE MENSAGEM** (*MESSAGE CONTENT INTENT*) *(Obrigatório para o bot conseguir ler comandos e mensagens)*
4. Clique em **Salvar alterações** (*Save Changes*) no rodapé da página.

---

### Passo 3: Gerar e Copiar o Token
1. Suba a página até a seção **Token** e clique no botão **Redefinir Token** (*Reset Token*).
2. Se a sua conta do Discord tiver autenticação em duas etapas (2FA), insira o código solicitado.
3. O seu **Token** será exibido na tela. Clique no botão **Copiar** (*Copy*).

> 🔒 **SEGURANÇA:** O Token funciona como a senha secreta do seu bot. Nunca o compartilhe com ninguém!
4. Cole esse Token em um lugar onde vc possa acessar e que seja seguro.

### Passo 5: Convidar o Bot Para Seu Servidor
1. Vá até a aba lateral e procure por **OAuth2**.
2. Depois, vá até a seção **Gerador de URL OAuth2** e marque a caixinha **Bot**.
3. Role a página para baixo e na seção **Permissões do bot** selecione **Administrador**.
4. Copie o link na caixa **URL Gerado** e convide seu bot normalmente, selecionando qual servidor você deseja convidá-lo.

---

### 🚀 Como Instalar e Rodar o Bot (SIGA AS INSTRUÇÕES PASSO A PASSO): 

**OBS:** O arquivo `.env` talvez não apareça na pasta. Para visualizá-lo, pesquise por *'como visualizar arquivos ocultos'* e veja como fazer tal alteração no seu dispositivo.

#### 💻 Se você usa Windows:
1. Baixe o arquivo `assimila-bot-windows.zip` e extraia a pasta.
2. Abra o arquivo `.env`, que se encontra na pasta `main`, com o *Bloco de Notas*. Em seguida, coloque seu token na linha `TOKEN_BOT=seu_token_aqui` e salve.
3. Dê dois cliques no arquivo `iniciar.bat` na pasta `setup`.

#### 🐧 Se você usa Linux / macOS:
1. Baixe o arquivo `assimila-bot-linux-mac.zip` e extraia a pasta.
2. Edite o arquivo `.env` na pasta `main` adicionando seu token na linha `TOKEN_BOT=seu_token_aqui` e salve.
3. Abra o terminal na pasta `setup` e execute:
   ```bash
   sed -i 's/\r$//' configurar.sh iniciar.sh && chmod +x configurar.sh iniciar.sh && ./configurar.sh && ./iniciar.sh

**Nas próximas vezes que você for iniciar o bot, é apenas necessário digitar `./iniciar.sh` no terminal.** 

---
🚨OBS: Enquanto a janela do terminal que for aberta no seu dispositivo estiver rodando, o bot funcionará!!!
---


## 📖 Guia de Comandos: Assimila - BOT
**🚨OBS: Se quiser ver a aba de comandos no próprio discord, digite o comando `&ajuda`**

Confira abaixo como utilizar os comandos de rolagens de dados e sorteio de cartas do bot:

### 🎲 Rolagem de Dados (`&dado`)
Para rolar dados, utilize o formato padrão **`xdy`**.

* **Exemplos:** `&dado 3d6+2d10` ou `&dado 4d12`
* Suporta múltiplos dados (máximo de **12** dados do mesmo tipo por rolagem).

---

### 🃏 Informações de Cartas (`&cartas info`)
Exibe a imagem de uma carta específica usando o **valor numérico** da carta e a **letra de seu naipe**.

* **Exemplo:** `&cartas info 10c` *(10 de Copas)*
* **Intervalo:** Números de **1 a 13**
* **Naipes:** 
  * `c` — Copas
  * `o` — Ouros
  * `e` — Espadas
  * `p` — Paus
* **Cartas Especiais:** `1` (Ás) | `11` (Valete) | `12` (Dama) | `13` (Rei)

---

### 🎴 Sorteio de Cartas (`&cartas sort`)
Sorteia a quantidade especificada de cartas para cada naipe informado.

* **Exemplo:** `&cartas sort 3c 2o` *(Sorteia 3 cartas de Copas e 2 de Ouros)*
* Suporta múltiplos naipes na mesma mensagem.
* **Intervalo:** Números de **1 a 13**
* **Naipes:** `c` (Copas) | `o` (Ouros) | `e` (Espadas) | `p` (Paus)

---
> 💡 **Dica:** Digite os comandos exatamente no formato indicado para evitar erros de execução.

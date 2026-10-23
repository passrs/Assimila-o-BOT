# Assimila-o-BOT
BOT de Assimilação RPG feito para usar no discord, desenvolvido sem fins lucrativos para rolagens de dados e sorteio de cartas do sistema. O BOT é funcional para rodar no seu próprio dispositivo, seja ele Windows ou Linux, ou usando o link funcional do discord para adicioná-lo em seu servidor(questão ainda em desenvolvimento).


## Como rodar o Bot em seu dispositivo

### Pré-requisitos
1. Você precisa de um Bot registrado na sua conta do discord.
2. Você precisa ter o **Python instalado** no seu computador.
* [Baixar Python (site oficial)](https://www.python.org/downloads/) *(Ao instalar no Windows, marque a opção "Add Python to PATH")*.

---
## 🤖 Como criar o Bot no Discord e obter o Token do seu Bot

Para utilizar este projeto, você precisará registrar um Bot no painel de desenvolvedores do Discord para gerar o token de acesso. O processo é gratuito e rápido.

Este guia vai ensinar como criar a aplicação do seu Bot no portal de desenvolvedores do Discord, gerar o token de acesso e convidá-lo para o seu servidor. O processo é simples, gratuito e lrápido.

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

### Passo 5: Convidar o Bot para seu servidor
1. Vá até a aba lateral e procure por **OAuth2**.
2. Depois, vá até a seção **Gerador de URL OAuth2** e marque a caixinha **Bot**.
3. Role a página para baixo e na seção **Permissões do bot** selecione **Administrador**.
4. Copie o link na caixa **URL Gerado** e convide seu bot normalmente, selecionando qual servidor você deseja convidá-lo.

---

## ⚙️ Passos de Instalação:
1. **Baixe o projeto:**
   * Baixe o arquivo na aba *Releases* ou [clique neste link](https://github.com/passrs/Assimila-o-BOT/releases/tag/v1.2) e extraia a pasta em qualquer lugar do computador.

2. **Adicione o Token do seu Bot:**
   * Abra o arquivo `.env` com o Bloco de Notas ou qualquer editor de texto. **OBS:** O arquivo `.env` talvez não apareça na pasta. Para visualizá-lo, pesquise por *'como visualizar arquivos ocultos'* e veja como fazer tal alteração no seu dispositivo.
   * Cole o token do seu bot na linha `DISCORD_TOKEN=seu_token_aqui` e salve o arquivo.

3. **Inicie o Bot:**
   * **No Linux / Mac:**
     1. Abra o terminal na pasta do projeto.
     2. Rode `./configurar.sh` (apenas na primeira vez).
     3. Rode `./iniciar.sh` para ligar o bot.
   * **No Windows:**
     * Dê **dois cliques** no arquivo `iniciar.bat`.

###OBS: Enquanto o seu terminal estiver aberto, o bot funcionará!!!

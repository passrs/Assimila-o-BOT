# Assimila-o-BOT
BOT do discord de assimilação RPG desenvolvido sem fins lucrativos para rolagens de dados e sorteio de cartas do sistema. O BOT é funcional para rodar no seu próprio dispositivo, seja ele Windows ou Linux, ou usando o link funcional do discord para adicioná-lo em seu servidor(questão ainda em desenvolvimento).


# Como rodar o Bot em seu dispositivo

### Pré-requisito
Você precisa ter o **Python instalado** no seu computador.
* [Baixar Python (site oficial)](https://www.python.org/downloads/) *(Ao instalar no Windows, marque a opção "Add Python to PATH")*.

---

### Passos de Instalação:

1. **Baixe o projeto:**
   * Clique no botão verde **Code** -> **Download ZIP** (ou baixe o arquivo na aba *Releases*) e extraia a pasta em qualquer lugar do computador.

2. **Adicione o Token do seu Bot:**
   * Abra o arquivo `.env` com o Bloco de Notas ou qualquer editor de texto.
   * Cole o token do seu bot na linha `DISCORD_TOKEN=seu_token_aqui` e salve o arquivo.

3. **Inicie o Bot:**
   * **No Linux / Mac:**
     1. Abra o terminal na pasta do projeto.
     2. Rode `./configurar.sh` (apenas na primeira vez).
     3. Rode `./iniciar.sh` para ligar o bot.
   * **No Windows:**
     * Dê **dois cliques** no arquivo `iniciar.bat`.

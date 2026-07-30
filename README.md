# YouTube Downloader Avançado (aTube Python Clone)

Um aplicativo de interface gráfica (GUI) moderno desenvolvido em Python para baixar vídeos e áudios do YouTube. O projeto utiliza uma arquitetura limpa (Clean Architecture), processamento em *threads* secundárias para evitar travamentos e organização automática de diretórios.

---

## Principais Funcionalidades

* **Múltiplas Qualidades e Formatos:** Escolha entre baixar apenas áudio (MP3) ou vídeos em diversas resoluções (com ou sem som embutido).
* **Acompanhamento em Tempo Real:** Barra de progresso visual mostrando a porcentagem exata do download.
* **Organização Inteligente:** O sistema separa automaticamente os arquivos baixados, criando as pastas `Audios` e `Videos` dentro da pasta "Vídeos" nativa do seu computador.
* **Acesso Rápido:** Botão "Abrir Pasta de Destino" na interface para acessar os arquivos baixados com um único clique (compatível com Windows, Mac e Linux).
* **Anti-Travamento:** Construído com *Multithreading*, garantindo que a tela não congele enquanto arquivos pesados são baixados.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x:** Linguagem base.
* **CustomTkinter:** Biblioteca para a interface gráfica moderna (Dark Mode nativo).
* **Pytubefix:** Biblioteca robusta para comunicação com a API do YouTube e extração de mídia.

---

## 📁 Estrutura do Projeto

O código foi desenhado aplicando o Princípio de Responsabilidade Única (SRP):

```text
meu_projeto/
├── main.py                 # Ponto de entrada que inicializa a aplicação
├── ui.py                   # Gerencia exclusivamente a interface gráfica, layout e eventos
├── downloader_service.py   # Lógica de negócio, download, filtros do YT e manipulação do SO
├── requirements.txt        # Lista de bibliotecas externas necessárias
└── README.md               # Documentação do projeto
```

---

## 🚀 Como Instalar e Executar

Siga o passo a passo abaixo para preparar o ambiente e rodar o software na sua máquina.

### 1. Pré-requisitos

Certifique-se de ter o **Python** instalado. Para verificar, abra o terminal e digite:

```bash
python --version
```

### 2. Preparando o Ambiente Virtual (Recomendado)

Para evitar conflitos com outras bibliotecas no seu sistema, crie um ambiente virtual na raiz do projeto:

```bash
# Cria o ambiente virtual chamado "venv"
python -m venv venv

# Ativa o ambiente virtual (Windows)
venv\Scripts\activate

# Ativa o ambiente virtual (Linux / macOS)
source venv/bin/activate

### 3. Instalando as Dependências

Com o ambiente ativado (indicado por `(venv)` no terminal), crie um arquivo `requirements.txt` com o conteúdo `customtkinter` e `pytubefix` (ou gere-o automaticamente) e instale:
```

```bash
pip install -r requirements.txt

```

*(Caso não tenha o arquivo, basta rodar: `pip install customtkinter pytubefix`)*

### 4. Executando o Software

Após a instalação das dependências, inicie o aplicativo executando o arquivo principal:

```bash
python main.py

```

---

## 🎯 Como Usar

1. **Cole a URL:** Com o aplicativo aberto, cole o link completo do vídeo do YouTube no campo de texto principal.
2. **Escolha o Formato:** Selecione uma das opções no menu suspenso:
* **Vídeo - Máx. Qualidade (Com Som):** Melhor qualidade possível que o YouTube fornece com áudio unificado (geralmente até 720p).
* **Vídeo - Baixa Qualidade (Com Som):** Opção mais leve para economizar espaço e internet.
* **Vídeo - 1080p ou Alta (Sem Som):** Alta resolução pura (o YouTube separa o áudio de resoluções muito altas).
* **Vídeo - 720p (Sem Som):** Apenas o canal de vídeo em HD.
* **Áudio (Melhor Qualidade - MP3):** Extrai a faixa de áudio e converte nativamente para `.mp3`.


3. **Inicie o Download:** Clique em **Baixar Agora**. Você poderá acompanhar o andamento pela barra de progresso em tempo real.
4. **Acesse os Arquivos:** Assim que concluir, clique em **Abrir Pasta de Destino**. O sistema operacional abrirá automaticamente a sua pasta nativa de Vídeos e direcionará para `YouTubeDownloader/Audios` ou `YouTubeDownloader/Videos`, dependendo do que foi baixado.
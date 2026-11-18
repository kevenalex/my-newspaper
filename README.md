Jornal Diário Pessoal
Sobre o projeto
Projeto J é um serviço que roda em servidor próprio, coleta notícias e outras informações ao longo do dia e, toda manhã, monta um jornal personalizado em PDF e o envia para a impressora. Inspirado no "The Karen Times", de Karen Cheng  [post] (https://x.com/VaibhavSisinty/status/2100133206070804742).
• Problema que resolve: Automação personalizada de resgate e consolidação de notícias ao decorrer do dia. 
• Para quem é: Indivíduos que querem personalizar a sua experiência de ler notícias.
• Estado atual: Em progresso.
Como funciona
1.  Coletor: a cada hora lê feeds RSS e APIs, remove duplicados e salva no banco.
2.  Detector de idioma: identifica se cada notícia está em inglês ou em português [biblioteca a definir] e grava o idioma no banco.
3.  Editor: de madrugada seleciona e ranqueia os itens do dia e gera manchetes e resumos em português. Notícias em português são resumidas direto; as em inglês são resumidas e o resumo é traduzido para português do Brasil.
4.  Diagramador: aplica o template de jornal e gera o PDF.
5.  Impressão: envia o PDF para a impressora; se falhar, o PDF fica salvo para imprimir depois.
Principais tecnologias
Camada
Tecnologia
Função
Linguagem
Python
Todo o código do serviço
Coleta
feedparser + requests
Ler feeds RSS e APIs
Banco de dados
SQLite
Catalogar as notícias do dia
Agendamento
systemd timer ou cron
Disparar coleta e edição
Resumos com IA
[API do Claude / outra / nenhuma]
Manchetes e resumos em português
Diagramação
Jinja2 + WeasyPrint [a confirmar]
Template HTML/CSS → PDF
Impressão
CUPS (lp) [a confirmar]
Enviar o PDF à impressora
Servidor
Ubuntu Server em notebook, SSH + Tailscale
Rodar tudo 24h
Pré-requisitos
• Servidor Linux com [versão do Python]
• Impressora configurada no CUPS: [modelo]
• Chave de API: [qual, se houver]
Instalação
git clone [url do repositório]
cd [pasta]
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
Configuração
Fontes, seções, horário e impressora ficam em um arquivo YAML:
fontes:
  - nome: [ex.: G1]
    url: [url do feed RSS]
    secao: [ex.: Brasil]
impressao:
  impressora: [nome no CUPS]
  horario: "06:00"
  paginas: [1 ou 2]
Uso
• Rodar a coleta manualmente: [comando]
• Gerar o jornal do dia: [comando]
• Imprimir: [comando]
Estrutura de pastas
[a definir após o primeiro protótipo]
Roadmap
[ ] Coletor de RSS com SQLite
[ ] Seleção e ranking das notícias do dia
[ ] Resumos em português
[ ] Template do jornal e geração do PDF
[ ] Impressão automática via CUPS
[ ] Agendamento no servidor
Referências
• "The Karen Times", de Karen Cheng (inspiração)
• O Matinal: github.com/cleiton-tavares/mydaily-newspaper
• Morning Paper: pypi.org/project/morning-paper
Licença e autor
[Licença] · [Seu nome]

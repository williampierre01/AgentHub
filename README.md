# AgentHub

Projeto de aprendizagem progressiva sobre FastAPI e APIs para sistemas de IA agentic.

O projeto crescerá durante o curso: começaremos com uma API pequena e bem estruturada e evoluiremos para uma plataforma com agentes, ferramentas, memória, persistência, autenticação, streaming e MCP.

## Objetivos

- Dominar os fundamentos e os recursos avançados do FastAPI.
- Projetar APIs tipadas, testáveis e organizadas em camadas.
- Compreender concorrência, `async` e streaming.
- Integrar bancos de dados, LLMs e ferramentas externas.
- Construir agentes com estado e memória.
- Preparar a aplicação para execução reproduzível e produção.
- Aprender Git durante a evolução real do projeto.

## Estado atual

Estamos no **Módulo 0 — Ambiente profissional e controle de versões**.

- [x] Diagnóstico inicial do Windows
- [x] Pasta permanente do projeto
- [x] Estrutura inicial de documentação
- [x] Repositório Git local
- [x] Instalação do Miniconda
- [x] Criação do ambiente `agenthub`
- [x] Seleção do interpretador no VS Code
- [x] Validação do ambiente reproduzível
- [ ] Primeira aplicação FastAPI

## Ambiente adotado

- Windows
- VS Code
- Miniconda 25.9.1
- Ambiente Conda: `agenthub`
- Python: série 3.12 (3.12.13 na validação inicial)
- pip 26.2.1 na validação inicial
- Git
- Docker em um módulo posterior

O Python global do Windows não será usado como ambiente do projeto. Dependências e atualizações serão feitas conscientemente dentro do ambiente `agenthub`.

Para reproduzir o ambiente em outra máquina:

```powershell
conda env create --file environment.yml
```

Nesta instalação, o plugin de termos do Conda consulta canais globais antes de aplicar o `nodefaults` do projeto. Por isso, a definição também foi validada em modo simulado com plugins externos desativados e o resolvedor clássico; nenhum termo de canal global foi aceito automaticamente.

## Estrutura inicial

```text
AgentHub/
├── app/                 # código da aplicação
├── tests/               # testes automatizados
├── docs/                # decisões e anotações permanentes
├── .gitignore
├── AGENTS.md            # orientação para futuras tarefas no Codex
├── environment.yml      # definição inicial do ambiente Conda
├── README.md
└── ROADMAP.md
```

## Próximo passo

Criar a primeira aplicação FastAPI, entendendo o papel do servidor ASGI, da instância da aplicação e de um endpoint antes de ampliar a arquitetura.

Para trabalhar no projeto em um terminal PowerShell com o Conda inicializado:

```powershell
conda activate agenthub
python --version
```

O executável esperado nesta máquina é `C:\Users\will\miniconda3\envs\agenthub\python.exe`. A configuração local do VS Code aponta para esse interpretador e não é versionada, pois caminhos de ambientes variam entre computadores.

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

O **Módulo 0 — Ambiente profissional e controle de versões** foi concluído. Estamos no **Módulo 1 — Fundamentos sólidos de FastAPI**.

- [x] Diagnóstico inicial do Windows
- [x] Pasta permanente do projeto
- [x] Estrutura inicial de documentação
- [x] Repositório Git local
- [x] Instalação do Miniconda
- [x] Criação do ambiente `agenthub`
- [x] Seleção do interpretador no VS Code
- [x] Validação do ambiente reproduzível
- [x] Primeira aplicação FastAPI
- [x] Primeiro endpoint `GET /`
- [x] Endpoint de disponibilidade `GET /health`
- [x] Resposta automática `404` para rotas desconhecidas
- [x] Organização das operações por tags no OpenAPI
- [x] Primeiro teste de endpoint
- [x] Validação com o servidor ASGI real

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

As primeiras dependências da API são:

- FastAPI 0.139.2 para declarar a aplicação e seus endpoints;
- Uvicorn 0.51.0 para servir a aplicação por meio do protocolo ASGI;
- HTTPX2 2.9.0 para simular requisições HTTP nos testes;
- pytest 9.1.1 para descobrir e executar os testes automatizados.

Para reproduzir o ambiente em outra máquina:

```powershell
conda env create --file environment.yml
```

Nesta instalação, o plugin de termos do Conda consulta canais globais antes de aplicar o `nodefaults` do projeto. Por isso, a definição também foi validada em modo simulado com plugins externos desativados e o resolvedor clássico; nenhum termo de canal global foi aceito automaticamente.

## Estrutura inicial

```text
AgentHub/
├── app/
│   ├── __init__.py
│   └── main.py         # instância FastAPI e endpoint inicial
├── tests/
│   ├── __init__.py
│   └── test_main.py    # teste HTTP do endpoint inicial
├── docs/                # decisões e anotações permanentes
├── .github/             # modelo de descrição dos pull requests
├── .gitignore
├── AGENTS.md            # orientação para futuras tarefas no Codex
├── environment.yml      # definição inicial do ambiente Conda
├── README.md
└── ROADMAP.md
```

## Executar a API

Em um novo terminal PowerShell:

```powershell
conda activate agenthub
python -m uvicorn app.main:app --reload
```

Em `app.main:app`, a primeira parte identifica o módulo Python `app/main.py`; a segunda identifica a variável que contém a instância `FastAPI`.

- API: <http://127.0.0.1:8000/>
- Disponibilidade: <http://127.0.0.1:8000/health>
- Documentação Swagger: <http://127.0.0.1:8000/docs>
- Esquema OpenAPI: <http://127.0.0.1:8000/openapi.json>

Para executar os testes:

```powershell
python -m pytest -q
```

## Próximo passo

Explorar parâmetros de caminho e de consulta, observando como o FastAPI os converte, valida e documenta antes de introduzir contratos Pydantic para corpos JSON.

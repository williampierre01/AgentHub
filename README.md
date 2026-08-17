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
- [ ] Instalação do Miniconda
- [ ] Criação do ambiente `agenthub`
- [ ] Seleção do interpretador no VS Code
- [ ] Validação do ambiente reproduzível
- [ ] Primeira aplicação FastAPI

## Ambiente adotado

- Windows
- VS Code
- Conda/Miniconda
- Ambiente Conda: `agenthub`
- Python: série 3.12
- Git
- Docker em um módulo posterior

O Python global do Windows não será usado como ambiente do projeto. Dependências e atualizações serão feitas conscientemente dentro do ambiente `agenthub`.

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

Instalar o Miniconda, criar o ambiente a partir de `environment.yml` e verificar que o terminal e o VS Code usam o Python correto.


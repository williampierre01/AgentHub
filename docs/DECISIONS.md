# Registro de decisões

Este arquivo registra decisões que devem continuar válidas entre diferentes aulas e tarefas.

## 001 — Um único projeto incremental

**Decisão:** desenvolver o AgentHub continuamente, em vez de criar projetos descartáveis para cada módulo.

**Motivo:** permite praticar manutenção, migrações, testes e evolução arquitetural em um sistema realista.

## 002 — Python isolado com Conda

**Decisão:** usar um ambiente chamado `agenthub`, inicialmente na série Python 3.12.

**Motivo:** separar o projeto do Python global do Windows e controlar atualizações do interpretador.

## 003 — Dependências adicionadas gradualmente

**Decisão:** o ambiente inicial contém apenas Python e pip. FastAPI e as demais bibliotecas serão adicionadas durante as aulas correspondentes.

**Motivo:** entender a função de cada dependência e registrar conscientemente suas versões.

## 004 — Framework de agentes somente após os fundamentos

**Decisão:** implementar primeiro os mecanismos essenciais com Python e FastAPI antes de introduzir LangGraph ou outra abstração agentic.

**Motivo:** compreender quais problemas o framework resolve e reduzir acoplamento prematuro.

## 005 — Pacotes Conda obtidos somente do conda-forge

**Decisão:** declarar `conda-forge` como canal do ambiente e usar `nodefaults` para impedir que canais da configuração global participem da resolução.

**Motivo:** tornar a origem dos pacotes previsível entre máquinas e evitar que uma configuração global altere silenciosamente o ambiente do projeto.

## 006 — Uma branch e um pull request por aula

**Decisão:** desenvolver cada aula em uma branch `codex/aula-NN-tema`, enviá-la ao GitHub e integrá-la em `main` por pull request com descrição completa.

**Motivo:** manter `main` estável e tornar o histórico do curso revisável, permitindo relacionar cada conjunto de mudanças ao objetivo e às verificações da aula.

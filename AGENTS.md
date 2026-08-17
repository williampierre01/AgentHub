# Orientações do projeto para o Codex

## Contexto

Este repositório é, ao mesmo tempo, um projeto de software e um curso prático de FastAPI aplicado a sistemas de IA agentic.

## Forma de trabalho

- Converse com o usuário em português do Brasil.
- Preserve o caráter pedagógico: explique conceitos e consequências das mudanças.
- Avance incrementalmente pelo roteiro em `ROADMAP.md`.
- Antes de alterar dependências, explique a finalidade e registre a versão escolhida.
- Use o ambiente Conda `agenthub` com Python 3.12 para comandos do projeto.
- Não use nem instale pacotes no Python global do Windows.
- Mantenha endpoints finos e regras de negócio fora da camada HTTP.
- Adicione ou atualize testes quando um comportamento for implementado.
- Rode verificações relevantes antes de declarar uma etapa concluída.
- Preserve mudanças existentes do usuário.

## Versionamento

- Mantenha `main` como branch estável e crie uma branch nova para cada aula antes de alterar arquivos.
- Nomeie branches de aula no formato `codex/aula-NN-tema`, com número de dois dígitos e tema curto em kebab-case.
- Use commits pequenos e descritivos.
- Prefira mensagens no padrão Conventional Commits, como `chore:`, `feat:`, `fix:`, `test:` e `docs:`.
- Ao concluir uma aula e suas verificações, envie a branch ao GitHub e abra um pull request para `main`.
- Ao criar um pull request, sempre preencha a descrição com o objetivo, um resumo das mudanças, as verificações executadas e observações ou riscos relevantes.
- Use o modelo em `.github/pull_request_template.md` como estrutura mínima da descrição do pull request.
- Nunca inclua arquivos `.env`, credenciais, tokens ou segredos no Git.
- Não atualize Python ou dependências automaticamente sem necessidade explícita.

## Documentação

- Mantenha `README.md` com o estado atual e os próximos passos.
- Mantenha decisões duráveis em `docs/DECISIONS.md`.
- Atualize `ROADMAP.md` quando o escopo ou a sequência do curso mudar.

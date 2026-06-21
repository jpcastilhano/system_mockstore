# Roadmap de Desenvolvimento: E-commerce Multi-Platform

Este documento serve como um guia de desenvolvimento iterativo para a construção do portfólio de e-commerce, garantindo uma evolução segura desde a modelagem de dados até a orquestração completa da infraestrutura.

---

## Fase 1: O Alicerce (Design e Contratos)
**Objetivo:** Definir as regras do jogo e a estrutura de dados antes de escrever qualquer código funcional.

* [x] **1.1. Modelo Entidade-Relacionamento (MER):**
    * ~~Mapear as tabelas principais: `Usuarios`, `Produtos`, `Categorias`, `Variações/SKUs` (Cor, Tamanho, Estoque) e `Imagens`.~~
    * ~~Definir os relacionamentos (1:N, N:N) e as chaves estrangeiras.~~
    * ~~*Ferramentas recomendadas:* dbdiagram.io, Draw.io ou MySQL Workbench.~~
    * Etapa realizada no dbdiagram. Será feito o posterior upload do código em /docs.
* [x] **1.2. O Contrato Central (API-First):**
    * ~~Criar o arquivo `openapi.yaml` (ou `.json`) na raiz do projeto (ex: na pasta `/contracts`).~~
    * ~~Documentar as rotas de CRUD essenciais (ex: `GET /products`, `POST /products`).~~
    * ~~Definir os payloads de requisição, respostas de sucesso e códigos de erro.~~
    * Etapa realizada com o SwaggerEditor. Caso for necessário atualizar a API com novos endpoints, será atualizado aqui primeiro.

---

## Fase 2: O Motor Inicial (Backend e Banco de Dados)
**Objetivo:** Levantar a persistência de dados e a primeira interface de comunicação de forma isolada.

* [x] **2.1. Dockerização Inicial (Apenas Banco de Dados):**
    * ~~Criar um `docker-compose.yml` contendo apenas um serviço do PostgreSQL.~~
    * ~~Configurar volumes para persistência de dados local e variáveis de ambiente (usuário, senha, banco).~~
    * Etapa configurada. O arquivo 'docker-compose' está na raíz do repositório.
* [ ] **2.2. A Primeira API (Python / FastAPI):**
    * Configurar o ambiente Python e as dependências (FastAPI, SQLAlchemy/SQLModel, Pydantic, Uvicorn).
    * Conectar a API ao container do PostgreSQL.
    * Implementar as rotas definidas no `openapi.yaml` garantindo a mesma estrutura de dados.
    * *Dica:* O FastAPI já gera uma documentação interativa nativamente, use isso para validar seu código contra o seu próprio contrato.

---

## Fase 3: Alimentando o Sistema (Frontend Administrativo)
**Objetivo:** Criar a interface para popular o banco de dados com dados reais, validando a API na prática.

* [ ] **3.1. Painel Admin (Next.js):**
    * Configurar o projeto Next.js (com TypeScript e TailwindCSS/ChakraUI).
    * Criar telas de Login, Dashboard, e formulários de CRUD (Categorias e Produtos).
    * Preparar a lógica de upload de imagens (integrando com Firebase Storage, AWS S3 ou simulando localmente).
* [ ] **3.2. Integração Admin <-> FastAPI:**
    * Consumir as rotas criadas na Fase 2.
    * Implementar JWT no backend e no frontend para proteger as rotas administrativas (RBAC).

---

## Fase 4: As Vitrines (O Core do Portfólio)
**Objetivo:** Desenvolver os clientes finais que exibirão os dados, demonstrando domínio em múltiplas plataformas.

* [ ] **4.1. Vitrine Web (Next.js):**
    * Criar a listagem pública de produtos.
    * **Core Feature:** Implementar a página de detalhes do produto, com atualização dinâmica de preço e imagem ao trocar o SKU (Cor/Tamanho) sem recarregar a tela.
* [ ] **4.2. Vitrine Mobile (React Native):**
    * Desenvolver o aplicativo mobile consumindo a mesma API (FastAPI).
    * Focar na navegação e na experiência do usuário em telas menores.
* [ ] **4.3. Vitrine Mobile (Flutter):**
    * *Opcional/Sequencial:* Replicar a mesma interface da vitrine React Native, provando a consistência independente do framework utilizado.

---

## Fase 5: O Desafio de Arquitetura e DevOps
**Objetivo:** Provar a senioridade do projeto, garantindo a intercambialidade e automatizando os processos.

* [ ] **5.1. O Segundo Backend (Node.js / NestJS):**
    * Desenvolver a mesma API usando NestJS, TypeScript, TypeORM/Prisma e `class-validator`.
    * **A Prova de Fogo:** Respeitar estritamente o `openapi.yaml`. Ao trocar a URL da API nos frontends de `localhost:8000` (FastAPI) para `localhost:3000` (NestJS), nada pode quebrar.
* [ ] **5.2. Orquestração Completa (Docker):**
    * Criar um `Dockerfile` para cada aplicação (FastAPI, NestJS, Admin, Web).
    * Atualizar o `docker-compose.yml` da raiz para levantar todo o ecossistema com um único comando `docker compose up`.
* [ ] **5.3. Pipelines de CI/CD (GitHub Actions):**
    * Configurar *workflows* no GitHub para rodar testes automatizados (Jest/PyTest) e linters em todo Pull Request aberto.
    * Aplicar *path filtering* para rodar apenas as pipelines correspondentes aos projetos alterados.

# StreamVibe ![image](https://github.com/user-attachments/assets/01ff50a1-93fd-45f2-9e95-c4ad00a67686)



# MovieSeriesHub - O Melhor Site para Filmes e Séries

O **MovieSeriesHub** é uma plataforma de streaming que permite aos usuários explorar uma vasta coleção de filmes e séries, com informações detalhadas, trailers, avaliações e muito mais. A ideia do projeto é oferecer uma experiência intuitiva para quem busca novos conteúdos para assistir.

## Índice

- [Descrição](#descrição)
- [Tecnologias Usadas](#tecnologias-usadas)
- [Como Rodar o Projeto](#como-rodar-o-projeto)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)

## Descrição

O **MovieSeriesHub** é um site desenvolvido para facilitar a busca por filmes e séries, com as seguintes funcionalidades principais:

- **Busca de Filmes e Séries**: Pesquisar por títulos, gêneros, atores, etc.
- **Detalhes de Conteúdo**: Visualizar informações completas sobre cada filme ou série, incluindo sinopse, elenco, avaliação e imagens.
- **Filtragem Avançada**: Filtrar filmes e séries por gênero, ano de lançamento, popularidade e mais.
- **Assistir Trailers**: Cada título possui um trailer que pode ser assistido diretamente no site.
- **Avaliação e Comentários**: Usuários podem avaliar e deixar comentários sobre filmes e séries.
- **Lista de Favoritos**: Adicione filmes e séries à sua lista de favoritos para ver depois.

Este projeto utiliza a **API do TMDb** (The Movie Database) para obter dados sobre filmes e séries, o que permite que o site se mantenha atualizado com os lançamentos mais recentes.

## Tecnologias Usadas

- **Frontend**:
  - HTML5, CSS3, JavaScript
  - Framework: React.js
  - Estilo: Bootstrap ou Tailwind CSS
  - Gerenciamento de Estado: Redux (ou Context API)
  
- **Backend** (se necessário):
  - Node.js com Express.js (para servir a aplicação ou se necessário para gerenciamento de autenticação)
  
- **API**:
  - The Movie Database (TMDb) API para dados de filmes e séries

- **Outras Ferramentas**:
  - Axios para requisições HTTP
  - React Router para navegação
  - LocalStorage para armazenar os favoritos do usuário
  
## Como Rodar o Projeto

### 1. Clonar o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/usuario/movieserieshub.git
cd movieserieshub

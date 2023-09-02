
# Desafio Fabrica - 2023.2

Api para shows\
CRUD - Create (Criar), Read (Ler), Update (Atualizar), Delete (Deletar): serve para a gestão de informações de forma simplificada com todas as ações citadas anteriormente em um banco de dados.\
Este CRUD tem o intuito de ajudar na gestão de uma agenda de shows.

## Objetos da API - Categoria, Artistas e Shows:
![Objetos](https://i.imgur.com/RoZYiTF.png)\
Todos os campos tem paginação de 2 em 2 items.\
Categorias (Apenas o campo "nome" - recebe string):\
![Categorias](https://i.imgur.com/o95xrA5.png)\
Artistas (Apenas o campo "nome" - recebe string):\
![Artistas](https://i.imgur.com/o95xrA5.png)\
Shows (Campos: "nome" - recebe string, "data" - recebe datetime, "categoria" - recebe objeto categoria e "artistas" recebe multiplos objetos artista):\
![Shows](https://i.imgur.com/jz90xvb.png)



## Database

Para definir sua informação do MYSQL vá ao arquivo acervo/settings.py

![DB](https://i.imgur.com/svujXHW.png)


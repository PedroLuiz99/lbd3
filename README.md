# Projeto de LBD III

API para o projeto de Laboratório de Banco de Dados

# Rodar com o docker

```bash
docker-compose up -d

docker exec -it lbd3_app_1 bash

python manage.py db migrate -m "Banco de dados final"
python manage.py db upgrade
```

# Projetão gostoso de LDB III

Quando eu estiver com saco preencho aqui

# Rodar com o docker

```bash
    docker-compose up -d

    docker exec -it lbd3_app_1 bash

    python manage.py db migrate -m "Uma mensagem legal aqui"
    python manage.py db upgrade
```

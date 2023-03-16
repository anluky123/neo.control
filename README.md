# TODO: 

#### Изменить файлы:

- [traefik.yml](compose%2Fproduction%2Ftraefik%2Ftraefik.yml)
- [.django](.envs%2F.production%2F.django)

*Нужно поменять хост* 


## Деплой и запуск:

1. Клонируем репозиторий и переходим в корневую директорию проекта:
```bash
git clone https://github.com/todd-sudo/neocontrol.git
cd neocontrol/
```

2. Билдим проект, выполняем миграции:
```bash
make build migrate
```

3. Создаем суперпользователя:
```bash
./scripts/manage_prod.sh createsuperuser
```

4. Запуск:
```bash
make up
```

5. Чтобы посмотреть логи (закрыть логи: Ctrl+C):
```bash
make logs
```

6. Чтобы остановить проект:
```bash
make down
```

7. Команда `make` без аргументов: остановит проект, обновится с гитхаба, перебилдит, поднимет и включит логи. Аналогично:
```bash
make down git_pull build up logs
```


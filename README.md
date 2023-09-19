# Пульт охраны банка

### Предметная область

Это сайт, который показывает охраннику все активные карты доступа. Также сайт показывает, кто находится в хранилище и все визиты человека


### Как установить
1. Создайте файл .env и все нужные ключи. Вот приммер, как должен выглядеть файл:
```sh
DB_PASSWORD=password
DB_USER=guard
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_HOST=checkpoint.devman.org
DB_PORT=5434
DB_NAME=checkpoint
DEBUG=False
ALLOWED_HOSTS=.localhost
SECRET_KEY=some_key
```
2. python3 должен быть установлен. Затем используйте ```pip``` для установки зависимостей
```sh
pip install -r requirements.txt
```
### Как запустить
Зайдите в терминал и запустите файл main.py
```sh
python3 manage.py runserver 
```
Далее переходите на локальные адрес вашего ПК: ```http://127.0.0.1:8000``` Там будет пульт охраны

### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

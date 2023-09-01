# Пульт охраны банка

### Предметная область

Это сайт, который показывает охраннику все активные карты доступа. Также сайт показывает, кто находится в хранилище и все визиты человека


### Как установить
1. Создайте файл .env и все нужные ключи. Вот приммер, как должен выглядеть файл:
```sh
PASSWORD=11111111
USER=test
ENGINE=engine
HOST=host
PORT=0000
NAME=name
SECRET_KEY=key
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

# ЯП - Спринт 11 - Проект «API для Yatube»

## Описание

API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, 
публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Стек технологий

* Python 3.11.3,
* Django 3.2.16,
* DRF,
* JWT + Djoser

Автор: 
* [Канцулин Данил](https://github.com/kekul78)
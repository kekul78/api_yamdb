<<<<<<< HEAD
# ЯП - Спринт 12 - Проект «Проект YaMDb»

## Описание

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:kekul78/api_yamdb.git
```

```
cd api_yambd
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

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
* JWT

Авторы: 
* [Канцулин Данил](https://github.com/kekul78)
* [Малич Денис](https://github.com/Denmais)
* [Даниил Кузнецов](https://github.com/Daniel-Ku3sovv)
=======
# api_yamdb
Совместный проект бибы, бобы и абобы
>>>>>>> 7dcf58a039a62e8ef197e873db63e86c01b298f5

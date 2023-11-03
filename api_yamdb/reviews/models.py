from django.db import models
from django.template.defaultfilters import truncatewords
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import validate_year
from users.models import UserModel

LENGHT_NAME = 256
LENGHT_SLUG = 50
TURN_CAT = 15


class Category(models.Model):
    """Класс категории."""
    name = models.CharField(
        verbose_name='Название',
        max_length=LENGHT_NAME
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        max_length=LENGHT_SLUG,
        unique=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Класс жанра."""
    name = models.CharField(
        verbose_name='Название',
        max_length=LENGHT_NAME
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        max_length=LENGHT_SLUG,
        unique=True
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Класс произведения."""
    name = models.CharField(
        verbose_name='Название',
        max_length=LENGHT_NAME,
        db_index=True
    )
    year = models.IntegerField(
        verbose_name='Дата выхода',
        validators=(validate_year,)
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        through='GenreTitle'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        default=None
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Класс жанра произведения."""
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE)
    genre = models.ForeignKey(
        Genre,
        verbose_name='Жанр',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Произведение и жанр'
        verbose_name_plural = 'Произведения и жанры'

    def __str__(self):
        return f'{self.title}, жанр - {self.genre}'


class AbstractModel(models.Model):

    class Meta:
        abstract = True

    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации отзыва',
        auto_now_add=True,
        db_index=True
    )
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )


class Review(AbstractModel):
    """Класс отзывов к произведениям."""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
    score = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        error_messages={'validators': 'Оценки могут быть от 1 до 10'}
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'],
                                    name='unique_review')
        ]
        default_related_name = 'reviews'

    def __str__(self):
        return truncatewords(self.text, TURN_CAT)


class Comment(AbstractModel):
    """Класс коментариев к отзывам."""
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'

    def __str__(self):
        return truncatewords(self.text, TURN_CAT)

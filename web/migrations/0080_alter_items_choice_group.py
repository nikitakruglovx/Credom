# Generated by Django 4.1 on 2022-08-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0079_alter_items_choice_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('scripts', 'Скрипты'), ('courses', 'Обучающие курсы'), ('desktopsoft', 'Десктоп софт'), ('sitesandweb', 'Сайты/Веб-приложения'), ('bots', 'Онлайн боты'), ('logotype', 'Логотипы'), ('androidapp', 'Мобильные приложения для Android'), ('books', 'Электронные книги'), ('treedmodels', '3D модели')], default='sitesandweb', max_length=50),
        ),
    ]

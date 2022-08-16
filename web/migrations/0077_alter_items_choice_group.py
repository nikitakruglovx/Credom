# Generated by Django 4.1 on 2022-08-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0076_alter_items_choice_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('courses', 'Обучающие курсы'), ('sitesandweb', 'Сайты/Веб-приложения'), ('scripts', 'Скрипты'), ('androidapp', 'Мобильные приложения для Android'), ('logotype', 'Логотипы'), ('desktopsoft', 'Десктоп софт'), ('treedmodels', '3D модели'), ('books', 'Электронные книги'), ('bots', 'Онлайн боты'), ('frontendtamplate', 'html/css/js Frontend Шаблоны')], default='sitesandweb', max_length=50),
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0072_alter_items_choice_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('bots', 'Онлайн боты'), ('desktopsoft', 'Десктоп софт'), ('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('logotype', 'Логотипы'), ('books', 'Электронные книги'), ('sitesandweb', 'Сайты/Веб-приложения'), ('treedmodels', '3D модели'), ('courses', 'Обучающие курсы'), ('androidapp', 'Мобильные приложения для Android'), ('scripts', 'Скрипты')], default='sitesandweb', max_length=50),
        ),
    ]

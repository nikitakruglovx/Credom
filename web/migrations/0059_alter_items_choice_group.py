# Generated by Django 4.0.3 on 2022-05-13 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0058_alter_items_choice_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('scripts', 'Скрипты'), ('logotype', 'Логотипы'), ('treedmodels', '3D модели'), ('desktopsoft', 'Десктоп софт'), ('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('bots', 'Онлайн боты'), ('sitesandweb', 'Сайты/Веб-приложения'), ('androidapp', 'Мобильные приложения для Android')], default='sitesandweb', max_length=50),
        ),
    ]

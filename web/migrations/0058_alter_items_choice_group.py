# Generated by Django 4.0.3 on 2022-05-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0057_alter_items_choice_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('desktopsoft', 'Десктоп софт'), ('scripts', 'Скрипты'), ('androidapp', 'Мобильные приложения для Android'), ('logotype', 'Логотипы'), ('sitesandweb', 'Сайты/Веб-приложения'), ('treedmodels', '3D модели'), ('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('bots', 'Онлайн боты')], default='sitesandweb', max_length=50),
        ),
    ]
# Generated by Django 4.0.3 on 2022-05-13 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0054_alter_items_choice_group_remove_profile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('sitesandweb', 'Сайты/Веб-приложения'), ('scripts', 'Скрипты'), ('treedmodels', '3D модели'), ('logotype', 'Логотипы'), ('bots', 'Онлайн боты'), ('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('androidapp', 'Мобильные приложения для Android'), ('desktopsoft', 'Десктоп софт')], default='sitesandweb', max_length=50),
        ),
    ]

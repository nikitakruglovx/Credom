# Generated by Django 4.0.3 on 2022-05-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0037_alter_items_choice_group_alter_items_file_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('logotype', 'Логотипы'), ('sitesandweb', 'Сайты/Веб-приложения'), ('desktopsoft', 'Десктоп софт'), ('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('bots', 'Онлайн боты'), ('treedmodels', '3D модели'), ('scripts', 'Скрипты'), ('androidapp', 'Мобильные приложения для Android')], default='sitesandweb', max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='text_item',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0038_alter_items_choice_group_alter_items_text_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('scripts', 'Скрипты'), ('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('logotype', 'Логотипы'), ('treedmodels', '3D модели'), ('bots', 'Онлайн боты'), ('desktopsoft', 'Десктоп софт'), ('sitesandweb', 'Сайты/Веб-приложения'), ('androidapp', 'Мобильные приложения для Android')], default='sitesandweb', max_length=50),
        ),
    ]

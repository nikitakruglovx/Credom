# Generated by Django 4.0.3 on 2022-05-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_items_avail_items_choice_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='avail',
        ),
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('sitesandweb', 'Сайты/Веб-приложения'), ('scripts', 'Скрипты'), ('androidapp', 'Мобильные приложения для андроид'), ('bots', 'Онлайн боты')], default='sitesandweb', max_length=50),
        ),
    ]

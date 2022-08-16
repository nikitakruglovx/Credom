# Generated by Django 4.0.3 on 2022-05-09 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_items_author_alter_items_choice_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('sitesandweb', 'Сайты/Веб-приложения'), ('bots', 'Онлайн боты'), ('androidapp', 'Мобильные приложения для андроид'), ('scripts', 'Скрипты')], default='sitesandweb', max_length=50),
        ),
    ]
# Generated by Django 4.0.3 on 2022-05-20 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0060_alter_items_choice_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='purchases',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.items'),
        ),
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('logotype', 'Логотипы'), ('scripts', 'Скрипты'), ('desktopsoft', 'Десктоп софт'), ('sitesandweb', 'Сайты/Веб-приложения'), ('bots', 'Онлайн боты'), ('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('treedmodels', '3D модели'), ('androidapp', 'Мобильные приложения для Android')], default='sitesandweb', max_length=50),
        ),
    ]

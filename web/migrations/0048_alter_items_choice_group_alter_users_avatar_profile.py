# Generated by Django 4.0.3 on 2022-05-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0047_alter_items_choice_group_alter_users_avatar_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('logotype', 'Логотипы'), ('sitesandweb', 'Сайты/Веб-приложения'), ('scripts', 'Скрипты'), ('desktopsoft', 'Десктоп софт'), ('androidapp', 'Мобильные приложения для Android'), ('frontendtamplate', 'html/css/js Frontend Шаблоны'), ('bots', 'Онлайн боты'), ('treedmodels', '3D модели')], default='sitesandweb', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar_profile',
            field=models.ImageField(blank=True, default='images/person.png', null=True, upload_to='avatar/'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_alter_items_choice_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='four_photo_item',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='items',
            name='tree_photo_item',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='items',
            name='two_photo_item',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='choice_group',
            field=models.CharField(choices=[('androidapp', 'Мобильные приложения для андроид'), ('bots', 'Онлайн боты'), ('sitesandweb', 'Сайты/Веб-приложения'), ('scripts', 'Скрипты')], default='sitesandweb', max_length=50),
        ),
    ]

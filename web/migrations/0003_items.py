# Generated by Django 4.0.3 on 2022-05-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_users_who_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_item', models.ImageField(blank=True, null=True, upload_to='')),
                ('name_item', models.CharField(max_length=200)),
                ('text_item', models.TextField()),
                ('price_item', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
            ],
        ),
    ]
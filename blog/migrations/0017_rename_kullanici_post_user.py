# Generated by Django 4.0.5 on 2022-06-05 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_post_kullanici'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='kullanici',
            new_name='user',
        ),
    ]

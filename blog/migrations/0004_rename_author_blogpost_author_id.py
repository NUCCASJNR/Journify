# Generated by Django 4.2.7 on 2023-12-02 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_sub_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='author',
            new_name='author_id',
        ),
    ]

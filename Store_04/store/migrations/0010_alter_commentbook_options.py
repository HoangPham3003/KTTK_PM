# Generated by Django 4.0.2 on 2022-05-18 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_book_commentbook_book_item_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentbook',
            options={'ordering': ('-comment_time',), 'verbose_name_plural': 'CommentBook'},
        ),
    ]

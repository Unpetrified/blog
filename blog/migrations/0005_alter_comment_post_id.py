# Generated by Django 4.0.5 on 2022-06-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.CharField(max_length=10000),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-30 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_post_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

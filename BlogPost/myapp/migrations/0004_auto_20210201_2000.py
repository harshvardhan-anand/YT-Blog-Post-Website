# Generated by Django 3.1.5 on 2021-02-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'PUBLISHED'), ('draft', 'DRAFT')], max_length=50),
        ),
    ]
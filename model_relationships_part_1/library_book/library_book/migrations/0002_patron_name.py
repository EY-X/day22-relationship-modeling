# Generated by Django 2.2.3 on 2019-08-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patron',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

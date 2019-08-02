# Generated by Django 2.2.3 on 2019-08-01 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_placed', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('renewed', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('hold_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_book.Hold')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_book.Loan')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=255)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_book.Loan')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_book.Book')),
            ],
        ),
    ]

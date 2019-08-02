# Generated by Django 2.2.3 on 2019-08-01 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wage', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker_shift.Shift')),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker_shift.Worker')),
            ],
        ),
    ]

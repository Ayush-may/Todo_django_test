# Generated by Django 5.1.2 on 2024-10-31 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('completed', 'completed'), ('pending', 'pending'), ('canceled', 'cancled')], default='pending', max_length=200)),
                ('time_stamp', models.TimeField()),
                ('is_completed', models.BooleanField()),
            ],
        ),
    ]

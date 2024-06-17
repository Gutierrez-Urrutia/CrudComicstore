# Generated by Django 5.0.6 on 2024-06-14 21:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999)])),
                ('img_path', models.CharField(max_length=200)),
            ],
        ),
    ]

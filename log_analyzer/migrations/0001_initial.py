# Generated by Django 5.0.6 on 2024-09-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysmonLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_data', models.JSONField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('has_threat', models.BooleanField(default=False)),
            ],
        ),
    ]

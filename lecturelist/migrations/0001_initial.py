# Generated by Django 3.0.5 on 2020-10-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecuture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_title', models.CharField(db_index=True, max_length=20)),
                ('lecture_summary', models.TextField(max_length=100)),
                ('lecture_detail', models.TextField(max_length=500)),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quran', '0008_delete_recitertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'TAFTAR'), (2, 'RECITER')])),
                ('count', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 3.0.8 on 2020-07-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quran', '0004_auto_20200714_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciter',
            name='r_mode',
            field=models.IntegerField(blank=True, choices=[(-1, 'Translate'), (0, 'Tartil'), (1, 'Mojawad'), (2, 'Moalem'), (3, 'Tahdir'), (4, 'WORD')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_ord',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_quality2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_quality3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_size2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_size3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_time',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_type',
            field=models.IntegerField(blank=True, choices=[(-1, 'Deleted'), (1, 'Show'), (2, 'Translate'), (3, 'Tafsir'), (4, 'WORD')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_url2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_url3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_withBesm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recitertype',
            name='mode',
            field=models.IntegerField(blank=True, choices=[(-1, 'Translate'), (0, 'Tartil'), (1, 'Mojawad'), (2, 'Moalem'), (3, 'Tahdir'), (4, 'WORD')], default=0, null=True),
        ),
    ]
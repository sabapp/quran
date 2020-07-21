# Generated by Django 3.0.8 on 2020-07-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quran', '0003_auto_20200714_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReciterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.IntegerField(choices=[(-1, 'Translate'), (0, 'Tartil'), (1, 'Mojawad'), (2, 'Moalem'), (3, 'Tahdir'), (4, 'WORD')], default=0, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='reciter',
            name='r_img',
            field=models.CharField(max_length=500, verbose_name='تصویر'),
        ),
        migrations.AddField(
            model_name='reciter',
            name='mm_mode',
            field=models.ManyToManyField(to='quran.ReciterType'),
        ),
    ]
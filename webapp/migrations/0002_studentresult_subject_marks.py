# Generated by Django 4.2.6 on 2023-11-30 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='subject_marks',
            field=models.CharField(default=78, max_length=200),
            preserve_default=False,
        ),
    ]

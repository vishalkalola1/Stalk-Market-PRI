# Generated by Django 3.0.4 on 2020-05-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrandAnalysisApp', '0007_auto_20200426_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercustom',
            name='uactivated',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 3.2 on 2022-02-26 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220227_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='app.category'),
            preserve_default=False,
        ),
    ]

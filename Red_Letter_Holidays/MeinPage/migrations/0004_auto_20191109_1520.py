# Generated by Django 2.2 on 2019-11-09 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0003_user_termsaccepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

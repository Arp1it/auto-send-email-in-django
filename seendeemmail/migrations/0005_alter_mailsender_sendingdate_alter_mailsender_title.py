# Generated by Django 5.0.1 on 2024-03-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seendeemmail', '0004_mailsender_title_alter_mailsender_sendingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailsender',
            name='sendingdate',
            field=models.CharField(default='<function now at 0x00000238E6348180>', max_length=30),
        ),
        migrations.AlterField(
            model_name='mailsender',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
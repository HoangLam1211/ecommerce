# Generated by Django 4.0.3 on 2022-04-15 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_order_transaction_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OderItem',
            new_name='OrderItem',
        ),
    ]

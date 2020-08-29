# Generated by Django 3.0.9 on 2020-08-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocodes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Promocodes',
            new_name='Promocode',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='pay_using',
            field=models.CharField(choices=[('CASH', 'Cash'), ('CARD', 'Card')], default='CARD', max_length=7),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment_for',
            field=models.CharField(choices=[('BILL', 'Bill'), ('SERVICE', 'Service')], default='BILL', max_length=40),
        ),
    ]
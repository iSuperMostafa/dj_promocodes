# Generated by Django 3.0.9 on 2020-08-29 01:38

import dj_promocodes.promocodes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField(default=100)),
                ('code', dj_promocodes.promocodes.models.TitleField(help_text='Unique title to identify this promocode (No spaces allowed. Lowercase letters)', max_length=20, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('frequency_of_use', models.PositiveIntegerField(default=100)),
                ('is_active', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)),
            ],
            options={
                'verbose_name': 'Promocode',
                'verbose_name_plural': 'Promocodes',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.CharField(editable=False, max_length=100, null=True)),
                ('payment_for', models.CharField(choices=[('BILL', 'Bill'), ('SUBSCRIPTION', 'Subscription'), ('BALANCE', 'Balance'), ('SERVICE', 'Service')], default='BILL', max_length=40)),
                ('pay_using', models.CharField(choices=[('CASH', 'Cash'), ('KIOSK', 'Kiosk'), ('CARD', 'Card')], default='CARD', max_length=7)),
                ('status', models.CharField(choices=[('SUCCESSFUL', 'Successful'), ('FAILED', 'Failed'), ('REFUNDED', 'Refunded'), ('VOIDED', 'Voided'), ('PENDING', 'Pending')], default='PENDING', max_length=10)),
                ('promocode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='promocodes.Promocodes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'ordering': ['-modified'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('transaction_uuid', models.CharField(editable=False, max_length=100)),
                ('promocode_title', models.CharField(blank=True, max_length=255, null=True)),
                ('promocode_code', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice', to='promocodes.Transaction')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoice',
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.IntegerField()),
                ('promocode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promocodes.Promocodes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

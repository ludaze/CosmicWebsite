# Generated by Django 5.0 on 2023-11-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmic', '0002_supplier_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='cosmic_order',
            fields=[
                ('order_no', models.TextField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('payment_type', models.TextField(blank=True, null=True)),
                ('measurement_type', models.TextField(blank=True, null=True)),
                ('transportation', models.TextField(blank=True, null=True)),
                ('shipment_type', models.TextField(blank=True, null=True)),
                ('approved_by', models.TextField(blank=True, null=True)),
                ('PR_before_vat', models.FloatField(blank=True, null=True)),
                ('status', models.TextField(blank=True, default='Pending', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cosmic_purchase',
            fields=[
                ('purchase_no', models.TextField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('measurement_type', models.TextField(blank=True, null=True)),
                ('transportation', models.TextField(blank=True, null=True)),
                ('shipment_type', models.TextField(blank=True, null=True)),
                ('payment_type', models.TextField(blank=True, null=True)),
                ('approved_by', models.TextField(blank=True, null=True)),
                ('before_vat', models.FloatField(blank=True, null=True)),
                ('status', models.TextField(blank=True, default='Pending', null=True)),
            ],
        ),
    ]

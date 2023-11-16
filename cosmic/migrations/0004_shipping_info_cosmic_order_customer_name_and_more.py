# Generated by Django 5.0 on 2023-11-13 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmic', '0003_cosmic_order_cosmic_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='shipping_info',
            fields=[
                ('agreement', models.TextField(blank=True, null=True)),
                ('PR_type', models.TextField(blank=True, null=True)),
                ('unique_no', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_date', models.DateField(blank=True, null=True)),
                ('port_of_loading', models.TextField(null=True)),
                ('port_of_discharge', models.TextField(blank=True, null=True)),
                ('final_destination', models.TextField(blank=True, null=True)),
                ('container_no', models.IntegerField(blank=True, null=True)),
                ('truck_waybill_no', models.TextField(blank=True, null=True)),
                ('country_of_origin', models.TextField(null=True)),
                ('customer_no', models.TextField(blank=True, null=True)),
                ('freight_amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cosmic_order',
            name='customer_name',
            field=models.ForeignKey(db_column='customer_name', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_related_to_customer', to='cosmic.customer_profile'),
        ),
        migrations.AddField(
            model_name='cosmic_order',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cosmic_purchase',
            name='supplier_name',
            field=models.ForeignKey(blank=True, db_column='supplier_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmic.supplier_profile'),
        ),
        migrations.AddField(
            model_name='cosmic_purchase',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
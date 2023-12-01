# Generated by Django 5.0 on 2023-12-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmic', '0008_remove_order_item_total_price_cosmic_order_consignee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping_info',
            name='PR_type',
        ),
        migrations.RemoveField(
            model_name='shipping_info',
            name='agreement',
        ),
        migrations.AddField(
            model_name='cosmic_order',
            name='country_of_origin',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cosmic_order',
            name='final_destination',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cosmic_order',
            name='port_of_discharge',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cosmic_order',
            name='port_of_loading',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shipping_info',
            name='total_gross_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shipping_info',
            name='total_net_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shipping_info',
            name='vessel',
            field=models.TextField(blank=True, null=True),
        ),
    ]
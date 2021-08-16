# Generated by Django 3.2.5 on 2021-08-14 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_item'),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employee_order', to='catalogue.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='item_collect',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='item_collect_order', to='catalogue.item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='item_delivery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='item_delivery_order', to='catalogue.item'),
            preserve_default=False,
        ),
    ]

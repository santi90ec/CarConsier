# Generated by Django 3.2.5 on 2021-08-15 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_item'),
        ('transaction', '0003_ordertracing'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertracing',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='state_order_tracing', to='catalogue.state'),
            preserve_default=False,
        ),
    ]
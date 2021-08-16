# Generated by Django 3.2.5 on 2021-08-13 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '0001_initial'),
        ('catalogue', '0007_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_collect', models.DateTimeField()),
                ('time_collect', models.CharField(max_length=20)),
                ('date_delivery', models.DateTimeField()),
                ('time_delivery', models.CharField(max_length=20)),
                ('decription', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address_collect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_collect_order', to='catalogue.address')),
                ('address_delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_delivery_order', to='catalogue.address')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_order', to='catalogue.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to='session.user')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_order', to='catalogue.vehicle')),
            ],
        ),
    ]

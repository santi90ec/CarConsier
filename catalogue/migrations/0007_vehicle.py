# Generated by Django 3.2.5 on 2021-08-13 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
        ('catalogue', '0006_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('decription', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_vehicle', to='catalogue.brand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_vehicle', to='catalogue.model')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_vehicle', to='catalogue.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_vehicle', to='session.user')),
            ],
        ),
    ]

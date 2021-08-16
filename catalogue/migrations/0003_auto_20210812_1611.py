# Generated by Django 3.2.5 on 2021-08-12 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_model', to='catalogue.state'),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_brand', to='catalogue.state')),
            ],
        ),
    ]

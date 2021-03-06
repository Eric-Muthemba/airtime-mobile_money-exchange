# Generated by Django 3.0.7 on 2021-03-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('A2M', 'A2M'), ('M2A', 'M2A')], max_length=30)),
                ('credit_amount', models.DecimalField(decimal_places=0, max_digits=10, max_length=255)),
                ('cash_amount', models.DecimalField(decimal_places=0, max_digits=10, max_length=255)),
                ('from_phoneNumber', models.DecimalField(decimal_places=0, max_digits=10, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]

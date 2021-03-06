# Generated by Django 3.2.13 on 2022-07-12 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0012_auto_20220704_2039'),
        ('basket', '0010_auto_20220704_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.PositiveBigIntegerField()),
                ('total_excl_tax', models.PositiveBigIntegerField()),
                ('pay_type', models.CharField(choices=[('PAYMENT', 'PANDING'), ('DEFERRED', 'DEFERRED'), ('AUTHENTICATE', 'AUTHENTICATE'), ('IN_TROUBLE_BUT_PAID', 'IN_TROUBLE_BUT_PAID')], default='PAYMENT', max_length=20)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.shippingaddress')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-21 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_caps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usercapsrelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='collection',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_caps.brand'),
        ),
        migrations.AddField(
            model_name='caps',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_caps.brand'),
        ),
        migrations.AddField(
            model_name='caps',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='caps',
            name='categories',
            field=models.ManyToManyField(related_name='caps', to='custom_caps.category'),
        ),
        migrations.AddField(
            model_name='caps',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_caps.collection'),
        ),
        migrations.AddField(
            model_name='caps',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shops', to='custom_caps.manufacturer', verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='caps',
            name='sizes',
            field=models.ManyToManyField(choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L'), ('eXtra Large', 'XL')], related_name='caps', to='custom_caps.size'),
        ),
        migrations.AddField(
            model_name='brand',
            name='categories',
            field=models.ManyToManyField(related_name='brands', to='custom_caps.category'),
        ),
    ]

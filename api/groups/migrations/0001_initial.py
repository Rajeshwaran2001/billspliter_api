# Generated by Django 4.1 on 2022-09-01 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_Name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=100)),
                ('group_icon', models.ImageField(upload_to='./group_icons')),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

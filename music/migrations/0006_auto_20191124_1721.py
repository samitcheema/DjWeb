# Generated by Django 2.2.4 on 2019-11-24 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0005_auto_20191124_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='albums',
            name='logo',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]

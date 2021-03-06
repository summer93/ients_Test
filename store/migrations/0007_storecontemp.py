# Generated by Django 2.0 on 2017-12-20 06:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20171215_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreConTemp',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Store', verbose_name='仓库')),
            ],
        ),
    ]

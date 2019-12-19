# Generated by Django 2.1.3 on 2019-12-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distro', '0004_auto_20191208_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferencePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('reg', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='dist',
            name='rp',
            field=models.CharField(max_length=100),
        ),
    ]

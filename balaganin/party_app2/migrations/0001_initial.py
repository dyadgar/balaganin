# Generated by Django 3.0.2 on 2020-01-15 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2020-01-15')),
                ('event_date', models.DateField(default='2020-01-15')),
                ('link', models.URLField(default='www.google.com')),
                ('venue', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='party_pics')),
                ('country', models.CharField(choices=[('MEXICO', 'MEXICO'), ('ISRAEL', 'ISRAEL'), ('FRANCE', 'FRANCE'), ('SPAIN', 'SPAIN'), ('GERMANY', 'GERMANY'), ('ENGLAND', 'ENGLAND')], default='MEXICO', max_length=20)),
                ('price', models.CharField(choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$'), ('$$$$', '$$$$')], default='$$$', max_length=10)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='party_app2.Category')),
            ],
            options={
                'ordering': ['event_date'],
            },
        ),
    ]

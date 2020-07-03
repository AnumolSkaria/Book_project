# Generated by Django 3.0.6 on 2020-06-24 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=50)),
                ('pages', models.IntegerField(default=60)),
                ('pub_date', models.DateField()),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vendor.Author')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vendor.Category')),
            ],
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowertypes', '0002_remove_flowersbouquets_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RosesBouquets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='flowertypes')),
            ],
            options={
                'verbose_name': 'Букеты из роз',
                'ordering': ['name'],
            },
        ),
    ]

# Generated by Django 4.0.2 on 2022-10-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(choices=[('elf', 'Elf'), ('dwarf', 'Dwarf'), ('human', 'Human'), ('ork', 'Ork')], max_length=255, unique=True),
        ),
    ]

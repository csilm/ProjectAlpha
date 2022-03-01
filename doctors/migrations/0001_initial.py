# Generated by Django 3.1.7 on 2021-03-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=50)),
                ('img', models.ImageField(default='default1.jpg', upload_to='doctor_pics')),
                ('email', models.EmailField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('Speciality', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=200)),
                ('experiance', models.CharField(max_length=200)),
            ],
        ),
    ]

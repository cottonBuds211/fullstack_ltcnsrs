# Generated by Django 4.2.6 on 2023-10-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('middleName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('address', models.CharField(default='Not specified', max_length=255)),
                ('pt', models.CharField(choices=[('permanent', 'Permanent'), ('temporary', 'Temporary')], default='', max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Not specified', max_length=10)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('bpe', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=10)),
                ('disability', models.CharField(default='', max_length=50)),
                ('parentName', models.CharField(default='Unknown', max_length=255)),
                ('occupation', models.CharField(default='Unknown', max_length=255)),
                ('relationship', models.CharField(choices=[('mother', 'Mother'), ('father', 'Father'), ('guardian', 'Guardian')], default='Not specified', max_length=200)),
                ('ethnicity', models.CharField(choices=[('Aggay', 'Aggay'), ('Akeanon/Aklanon', 'Akeanon/Aklanon'), ('Apayao/Yapayao', 'Apayao/Yapayao'), ('Ayangan', 'Ayangan'), ('Balangao/Baliwon', 'Balangao/Baliwon'), ('Bikol/Bicol', 'Bikol/Bicol'), ('Bisaya/Binisaya', 'Bisaya/Binisaya'), ('Bontok/Binontok', 'Bontok/Binontok'), ('Cebuano', 'Cebuano'), ('Hamtikanon', 'Hamtikanon'), ('Hiligaynon,Ilonggo', 'Hiligaynon,Ilonggo'), ('Ibaloi/Inibaloi', 'Ibaloi/Inibaloi'), ('Ibanag', 'Ibanag'), ('Ibontoc', 'Ibontoc'), ('Ifugao', 'Ifugao'), ('Kalanguya/Ikalahan', 'Kalanguya/Ikalahan'), ('Ilocano', 'Ilocano'), ('Iranon', 'Iranon'), ('Itneg', 'Itneg'), ('Kalinga', 'Kalinga'), ('Kankanai/Kankanaey', 'Kankanai/Kankanaey'), ('Kapampangan', 'Kapampangan'), ('Karao', 'Karao'), ('Kinalinga', 'Kinalinga'), ('Kiniray-a', 'Kiniray-a'), ('Maranao', 'Maranao'), ('Masbateno/Masbatean', 'Masbateno/Masbatean'), ('Pangasinan/Panggalato', 'Pangasinan/Panggalato'), ('Surigaonon', 'Surigaonon'), ('Tagalog', 'Tagalog'), ('Tausug', 'Tausug'), ('Waray', 'Waray'), ('Other Local Ethnicity', 'Other Local Ethnicity'), ('Chinese', 'Chinese'), ('American/English', 'American/English'), ('Other Foreign Ethnicity', 'Other Foreign Ethnicity'), ('Not Reported', 'Not Reported')], default='Not specified', max_length=200)),
                ('dow', models.DateField(blank=True, null=True)),
                ('weight', models.FloatField(default=0, max_length=255)),
                ('height', models.FloatField(default=0, max_length=255)),
                ('muac', models.FloatField(default=0, max_length=255)),
                ('purga', models.DateField(blank=True, null=True)),
                ('vac', models.DateField(blank=True, null=True)),
            ],
        ),
    ]

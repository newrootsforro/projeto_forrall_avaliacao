# Generated by Django 2.1.2 on 2018-10-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_pagamentos_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
                ('pontuacao_minima', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='pagamentos',
            name='data_pagamento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
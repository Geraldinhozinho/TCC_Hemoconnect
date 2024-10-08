# Generated by Django 5.1.1 on 2024-10-07 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_questionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='dias',
            field=models.CharField(choices=[('seg', 'Segunda'), ('ter', 'Terça'), ('qua', 'Quarta'), ('qui', 'Quinta'), ('sex', 'Sexta'), ('sab', 'Sábado'), ('dom', 'Domingo')], default=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='disponibilidade',
            field=models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], default=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='doenca',
            field=models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], default=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='doenca_det',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='fuma',
            field=models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], default=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='querer',
            field=models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], default=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='sexo',
            field=models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], default=True, max_length=9),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='tipo_sangue',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'), ('Não sei', 'Não sei')], default=True, max_length=10),
        ),
    ]

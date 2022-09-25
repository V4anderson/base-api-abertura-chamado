# Generated by Django 4.1.1 on 2022-09-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_os', models.CharField(max_length=6, verbose_name='Número da O.S')),
                ('nome_completo', models.CharField(max_length=50, verbose_name='Nome Completo')),
                ('cpf_cnpj', models.CharField(max_length=18, verbose_name='CPF/CNPJ')),
                ('endereco', models.CharField(max_length=250, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=120, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=120, verbose_name='Cidade')),
                ('telefone', models.CharField(max_length=14, verbose_name='Telefone')),
                ('tipo_de_servico', models.CharField(max_length=250, verbose_name='Tipo de Serviço')),
            ],
        ),
    ]
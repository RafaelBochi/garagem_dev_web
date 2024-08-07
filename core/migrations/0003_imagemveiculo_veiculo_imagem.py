# Generated by Django 5.0.6 on 2024-07-19 12:35

import core.models.imagem
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_acessorio_categoria_cor_marca_modelo_veiculo"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImagemVeiculo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(blank=True, null=True, upload_to=core.models.imagem.upload_image_fomater)),
            ],
        ),
        migrations.AddField(
            model_name="veiculo",
            name="imagem",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="veiculo",
                to="core.imagemveiculo",
            ),
        ),
    ]

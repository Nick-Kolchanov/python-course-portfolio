# Generated by Django 4.1.13 on 2024-03-30 06:33

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Изображение для демонстрации работы",
                        upload_to="images/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="Краткое описание выполненной работы",
                        max_length=255,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "detailed_description",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        help_text="Подробное описание выполненной работы",
                        verbose_name="Подробное описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "Выполненная работа",
                "verbose_name_plural": "Выполненные работы",
            },
        ),
    ]

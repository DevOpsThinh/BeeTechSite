# Generated by Django 4.0.3 on 2022-04-03 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postpage_rename_blog_blogpage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterUniqueTogether(
            name='postpageblogcategory',
            unique_together={('page', 'blog_category')},
        ),
    ]
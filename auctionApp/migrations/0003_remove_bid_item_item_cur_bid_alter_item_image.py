# Generated by Django 4.1.2 on 2022-12-16 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0002_alter_question_answer_alter_user_image_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='cur_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctionApp.bid'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='item_img'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-21 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lyrics', '0002_lyrics_musiclabel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='Movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.movie'),
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='MovieDirector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.moviedirector'),
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='MusicDirector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.musicdirector'),
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='Singer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.singer'),
        ),
    ]

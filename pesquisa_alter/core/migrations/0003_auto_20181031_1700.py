# Generated by Django 2.1.2 on 2018-10-31 20:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_person_cdalterdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_key', models.CharField(max_length=200, verbose_name='Chave da pesquisa')),
                ('researched', models.CharField(max_length=200, verbose_name='Entrevistado')),
                ('response', models.CharField(choices=[('V', 'Verdadeiro'), ('F', 'Falso'), ('I', 'Indefinido')], default='I', max_length=1, verbose_name='Resposta')),
                ('participation_on', models.DateField(default=django.utils.timezone.now, verbose_name='período dapesquisa')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='solicitado em')),
            ],
            options={
                'verbose_name': 'Pesquisa',
                'verbose_name_plural': 'Pesquisas',
                'ordering': ('-participation_on',),
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Pergunta')),
                ('level', models.CharField(choices=[('0', 'Indefinido'), ('1', 'Dependencia'), ('2', 'Confianca'), ('3', 'Comprometimento'), ('4', 'Preditiva'), ('5', 'Comprometimento')], default='0', max_length=15, verbose_name='Nível')),
            ],
            options={
                'verbose_name': 'Questão',
                'verbose_name_plural': 'Questões',
                'ordering': ('-level',),
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pessoa', to='core.Person'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pergunta', to='core.Questions'),
        ),
        migrations.AlterUniqueTogether(
            name='pesquisa',
            unique_together={('search_key', 'person', 'question')},
        ),
    ]

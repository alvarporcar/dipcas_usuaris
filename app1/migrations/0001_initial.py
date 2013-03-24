# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cursos'
        db.create_table('app1_cursos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contingut', self.gf('django.db.models.fields.TextField')()),
            ('pla', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('anny', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('dates', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('modalitat', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('projecte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Projectes'], null=True, blank=True)),
        ))
        db.send_create_signal('app1', ['Cursos'])

        # Adding model 'Organismes'
        db.create_table('app1_organismes', (
            ('codi', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True)),
            ('tipus', self.gf('django.db.models.fields.CharField')(default='AJ', max_length=2)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('adreca', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('poblacio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cp', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('email1', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('tel1', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('fax1', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('app1', ['Organismes'])

        # Adding model 'Carrecs'
        db.create_table('app1_carrecs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.TextField')(max_length='30')),
        ))
        db.send_create_signal('app1', ['Carrecs'])

        # Adding model 'Usuaris'
        db.create_table('app1_usuaris', (
            ('nif', self.gf('django.db.models.fields.CharField')(max_length=9, primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cognoms', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('usudipcas', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('email1', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('email2', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('tel1', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('carrec', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Carrecs'])),
            ('organisme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Organismes'])),
        ))
        db.send_create_signal('app1', ['Usuaris'])

        # Adding model 'UsuarisDeProjecte'
        db.create_table('app1_usuarisdeprojecte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuari', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Usuaris'])),
            ('projecte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Projectes'])),
        ))
        db.send_create_signal('app1', ['UsuarisDeProjecte'])

        # Adding unique constraint on 'UsuarisDeProjecte', fields ['usuari', 'projecte']
        db.create_unique('app1_usuarisdeprojecte', ['usuari_id', 'projecte_id'])

        # Adding model 'ProfessorDeCurs'
        db.create_table('app1_professordecurs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('professor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Usuaris'])),
            ('curs', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Cursos'])),
            ('hores', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('app1', ['ProfessorDeCurs'])

        # Adding unique constraint on 'ProfessorDeCurs', fields ['professor', 'curs']
        db.create_unique('app1_professordecurs', ['professor_id', 'curs_id'])

        # Adding model 'Matricula'
        db.create_table('app1_matricula', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumne', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Usuaris'])),
            ('curs', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Cursos'])),
            ('superat', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('app1', ['Matricula'])

        # Adding unique constraint on 'Matricula', fields ['alumne', 'curs']
        db.create_unique('app1_matricula', ['alumne_id', 'curs_id'])

        # Adding model 'Projectes'
        db.create_table('app1_projectes', (
            ('abrev', self.gf('django.db.models.fields.TextField')(max_length='10', primary_key=True)),
            ('nom', self.gf('django.db.models.fields.TextField')(max_length='30')),
            ('descripcio', self.gf('django.db.models.fields.TextField')(max_length='100')),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('responsable', self.gf('django.db.models.fields.related.ForeignKey')(related_name='responsable_de', to=orm['app1.Usuaris'])),
        ))
        db.send_create_signal('app1', ['Projectes'])


    def backwards(self, orm):
        # Removing unique constraint on 'Matricula', fields ['alumne', 'curs']
        db.delete_unique('app1_matricula', ['alumne_id', 'curs_id'])

        # Removing unique constraint on 'ProfessorDeCurs', fields ['professor', 'curs']
        db.delete_unique('app1_professordecurs', ['professor_id', 'curs_id'])

        # Removing unique constraint on 'UsuarisDeProjecte', fields ['usuari', 'projecte']
        db.delete_unique('app1_usuarisdeprojecte', ['usuari_id', 'projecte_id'])

        # Deleting model 'Cursos'
        db.delete_table('app1_cursos')

        # Deleting model 'Organismes'
        db.delete_table('app1_organismes')

        # Deleting model 'Carrecs'
        db.delete_table('app1_carrecs')

        # Deleting model 'Usuaris'
        db.delete_table('app1_usuaris')

        # Deleting model 'UsuarisDeProjecte'
        db.delete_table('app1_usuarisdeprojecte')

        # Deleting model 'ProfessorDeCurs'
        db.delete_table('app1_professordecurs')

        # Deleting model 'Matricula'
        db.delete_table('app1_matricula')

        # Deleting model 'Projectes'
        db.delete_table('app1_projectes')


    models = {
        'app1.carrecs': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Carrecs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {'max_length': "'30'"})
        },
        'app1.cursos': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Cursos'},
            'anny': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'contingut': ('django.db.models.fields.TextField', [], {}),
            'dates': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modalitat': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pla': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'professor': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'professor_de'", 'symmetrical': 'False', 'through': "orm['app1.ProfessorDeCurs']", 'to': "orm['app1.Usuaris']"}),
            'projecte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Projectes']", 'null': 'True', 'blank': 'True'})
        },
        'app1.matricula': {
            'Meta': {'unique_together': "(('alumne', 'curs'),)", 'object_name': 'Matricula'},
            'alumne': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Usuaris']"}),
            'curs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Cursos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'superat': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'app1.organismes': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Organismes'},
            'adreca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'codi': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'}),
            'cp': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'email1': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fax1': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'poblacio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tel1': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'tipus': ('django.db.models.fields.CharField', [], {'default': "'AJ'", 'max_length': '2'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'app1.professordecurs': {
            'Meta': {'unique_together': "(('professor', 'curs'),)", 'object_name': 'ProfessorDeCurs'},
            'curs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Cursos']"}),
            'hores': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Usuaris']"})
        },
        'app1.projectes': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Projectes'},
            'abrev': ('django.db.models.fields.TextField', [], {'max_length': "'10'", 'primary_key': 'True'}),
            'descripcio': ('django.db.models.fields.TextField', [], {'max_length': "'100'"}),
            'nom': ('django.db.models.fields.TextField', [], {'max_length': "'30'"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'responsable_de'", 'to': "orm['app1.Usuaris']"}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'app1.usuaris': {
            'Meta': {'ordering': "['organisme', 'cognoms']", 'object_name': 'Usuaris'},
            'carrec': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Carrecs']"}),
            'cognoms': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cursos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app1.Cursos']", 'through': "orm['app1.Matricula']", 'symmetrical': 'False'}),
            'email1': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'email2': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'nif': ('django.db.models.fields.CharField', [], {'max_length': '9', 'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organisme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Organismes']"}),
            'projectes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app1.Projectes']", 'through': "orm['app1.UsuarisDeProjecte']", 'symmetrical': 'False'}),
            'tel1': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'usudipcas': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'app1.usuarisdeprojecte': {
            'Meta': {'unique_together': "(('usuari', 'projecte'),)", 'object_name': 'UsuarisDeProjecte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projecte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Projectes']"}),
            'usuari': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Usuaris']"})
        }
    }

    complete_apps = ['app1']
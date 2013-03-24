# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UsuarisDeProjecte.alta'
        db.add_column('app1_usuarisdeprojecte', 'alta',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 24, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UsuarisDeProjecte.alta'
        db.delete_column('app1_usuarisdeprojecte', 'alta')


    models = {
        'app1.carrecs': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Carrecs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {'max_length': "'30'"})
        },
        'app1.cursos': {
            'Meta': {'ordering': "['anny', 'nom']", 'object_name': 'Cursos'},
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
            'Meta': {'ordering': "['usuari', 'projecte']", 'unique_together': "(('usuari', 'projecte'),)", 'object_name': 'UsuarisDeProjecte'},
            'alta': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 3, 24, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projecte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Projectes']"}),
            'usuari': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Usuaris']"})
        }
    }

    complete_apps = ['app1']
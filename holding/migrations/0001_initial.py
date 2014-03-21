# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HoldingBlock'
        db.create_table('holding_holdingblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.Page'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.Section'])),
        ))
        db.send_create_signal('holding', ['HoldingBlock'])

        # Adding model 'Holding'
        db.create_table('holding_holding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('moderate_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.ModerateState'])),
            ('date_moderated', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('user_moderated', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content', to=orm['holding.HoldingBlock'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('company', self.gf('django.db.models.fields.TextField')()),
            ('what_we_do', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100)),
        ))
        db.send_create_signal('holding', ['Holding'])

        # Adding unique constraint on 'Holding', fields ['block', 'moderate_state']
        db.create_unique('holding_holding', ['block_id', 'moderate_state_id'])

        # Adding model 'TitleBlock'
        db.create_table('holding_titleblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.Page'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.Section'])),
        ))
        db.send_create_signal('holding', ['TitleBlock'])

        # Adding model 'Title'
        db.create_table('holding_title', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('moderate_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.ModerateState'])),
            ('date_moderated', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('user_moderated', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content', to=orm['holding.TitleBlock'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('holding', ['Title'])

        # Adding unique constraint on 'Title', fields ['block', 'moderate_state']
        db.create_unique('holding_title', ['block_id', 'moderate_state_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Title', fields ['block', 'moderate_state']
        db.delete_unique('holding_title', ['block_id', 'moderate_state_id'])

        # Removing unique constraint on 'Holding', fields ['block', 'moderate_state']
        db.delete_unique('holding_holding', ['block_id', 'moderate_state_id'])

        # Deleting model 'HoldingBlock'
        db.delete_table('holding_holdingblock')

        # Deleting model 'Holding'
        db.delete_table('holding_holding')

        # Deleting model 'TitleBlock'
        db.delete_table('holding_titleblock')

        # Deleting model 'Title'
        db.delete_table('holding_title')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'block.moderatestate': {
            'Meta': {'object_name': 'ModerateState', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'block.page': {
            'Meta': {'object_name': 'Page', 'ordering': "['name']"},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'block.section': {
            'Meta': {'object_name': 'Section', 'ordering': "('name',)"},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'holding.holding': {
            'Meta': {'unique_together': "(('block', 'moderate_state'),)", 'object_name': 'Holding'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content'", 'to': "orm['holding.HoldingBlock']"}),
            'company': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'date_moderated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'moderate_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.ModerateState']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'user_moderated': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'what_we_do': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'})
        },
        'holding.holdingblock': {
            'Meta': {'object_name': 'HoldingBlock'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.Page']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.Section']"})
        },
        'holding.title': {
            'Meta': {'unique_together': "(('block', 'moderate_state'),)", 'object_name': 'Title'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content'", 'to': "orm['holding.TitleBlock']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'date_moderated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderate_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.ModerateState']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'user_moderated': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'holding.titleblock': {
            'Meta': {'object_name': 'TitleBlock'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.Page']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.Section']"})
        }
    }

    complete_apps = ['holding']
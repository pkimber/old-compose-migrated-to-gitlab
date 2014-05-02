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
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.PageSection'])),
        ))
        db.send_create_signal('holding', ['HoldingBlock'])

        # Adding model 'Holding'
        db.create_table('holding_holding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('moderate_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.ModerateState'])),
            ('date_moderated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('user_moderated', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='+', null=True, blank=True)),
            ('edit_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.EditState'])),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['holding.HoldingBlock'], related_name='content')),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('company', self.gf('django.db.models.fields.TextField')()),
            ('what_we_do', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('holding', ['Holding'])

        # Adding unique constraint on 'Holding', fields ['block', 'moderate_state']
        db.create_unique('holding_holding', ['block_id', 'moderate_state_id'])

        # Adding model 'TitleBlock'
        db.create_table('holding_titleblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.PageSection'])),
        ))
        db.send_create_signal('holding', ['TitleBlock'])

        # Adding model 'Title'
        db.create_table('holding_title', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('moderate_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.ModerateState'])),
            ('date_moderated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('user_moderated', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='+', null=True, blank=True)),
            ('edit_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.EditState'])),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['holding.TitleBlock'], related_name='content')),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'block.editstate': {
            'Meta': {'ordering': "['name']", 'object_name': 'EditState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'block.moderatestate': {
            'Meta': {'ordering': "['name']", 'object_name': 'ModerateState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'block.page': {
            'Meta': {'unique_together': "(('slug', 'slug_menu'),)", 'ordering': "['order', 'slug', 'slug_menu']", 'object_name': 'Page'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'slug_menu': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'block.pagesection': {
            'Meta': {'unique_together': "(('page', 'section'),)", 'ordering': "('page__slug', 'section__slug')", 'object_name': 'PageSection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.Page']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.Section']"})
        },
        'block.paginatedsection': {
            'Meta': {'object_name': 'PaginatedSection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_per_page': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'order_by_field': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'block.section': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Section'},
            'block_app': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'block_model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'create_url_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paginated': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.PaginatedSection']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'holding.holding': {
            'Meta': {'unique_together': "(('block', 'moderate_state'),)", 'object_name': 'Holding'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['holding.HoldingBlock']", 'related_name': "'content'"}),
            'company': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_moderated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edit_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.EditState']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'moderate_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.ModerateState']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'user_moderated': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'+'", 'null': 'True', 'blank': 'True'}),
            'what_we_do': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'holding.holdingblock': {
            'Meta': {'object_name': 'HoldingBlock'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'page_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.PageSection']"})
        },
        'holding.title': {
            'Meta': {'unique_together': "(('block', 'moderate_state'),)", 'object_name': 'Title'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['holding.TitleBlock']", 'related_name': "'content'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_moderated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'edit_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.EditState']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderate_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.ModerateState']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'user_moderated': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'+'", 'null': 'True', 'blank': 'True'})
        },
        'holding.titleblock': {
            'Meta': {'object_name': 'TitleBlock'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'page_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.PageSection']"})
        }
    }

    complete_apps = ['holding']
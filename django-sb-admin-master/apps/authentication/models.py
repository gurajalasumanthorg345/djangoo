from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=True)     #added new
    deletedAt = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'users'
        
class Files(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    alternative_text = models.CharField(max_length=255, null=True, blank=True)
    ext = models.CharField(max_length=255, null=True, blank=True)
    mime = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    contents = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    
    class Meta:
        db_table = 'files'

class ScannedContents(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    file_id = models.IntegerField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    document_source_type = models.CharField(max_length=255, null=True, blank=True)
    industry_type = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'scannedcontents'
        
class SequelizeMeta(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'sequelizemeta'
        
class Keywords(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    file_id = models.IntegerField(null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    polarity = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        db_table = 'keywords'
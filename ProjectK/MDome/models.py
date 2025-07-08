from django.db import models

# Create your models here.

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    class Meta:
        db_table="tbl_login"

class UInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    ph_no = models.BigIntegerField(null=True)
    email = models.CharField(max_length=100,null=True)


    class Meta:
        db_table= 'tbl_user'
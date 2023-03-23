from django.db import models

class contact_tb(models.Model):
	full_name=models.CharField(max_length=100,null=False)
	email=models.CharField(max_length=100,null=False)
	phone=models.CharField(max_length=100,null=False)
	subject=models.CharField(max_length=200,null=False)
	cn_message=models.CharField(max_length=400,null=False)

class admin_register_tb(models.Model):
	first_name=models.CharField(max_length=100,null=False)
	last_name=models.CharField(max_length=100,null=False)
	email=models.CharField(max_length=100,null=False)
	password=models.CharField(max_length=100,null=False)
	confirm_password=models.CharField(max_length=100,null=False)

class product_tb(models.Model):
	product_name=models.CharField(max_length=100,null=False)
	product_image=models.ImageField(upload_to="Userimage/")
	description=models.CharField(max_length=300,null=False)

class gallery_tb(models.Model):
	image=models.ImageField(upload_to="Userimage/")
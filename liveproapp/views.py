from django.shortcuts import render
from.models import *
from django.http import HttpResponseRedirect
import os
import random
import hashlib
import string
from django.conf import settings
from django.core.mail import send_mail


def index(request):
	data=product_tb.objects.all()[:3]
	return render(request,"index.html",{"data":data})

def about(request): 
	return render(request,"about.html")

def services(request):
	data=product_tb.objects.all()
	return render(request,"services.html",{"data":data})

def single(request):
	sid=request.GET['sid']
	data=product_tb.objects.filter(id=sid)
	return render(request,"single.html",{"data":data})
	

def gallery(request):
	data=gallery_tb.objects.all()
	return render(request,"gallery.html",{"data":data})

def contact(request):
	if request.method=="POST":
		full_name=request.POST['full_name']
		email=request.POST['email']
		phone=request.POST['phone']
		subject=request.POST['subject']
		cn_message=request.POST['message']

		add=contact_tb(full_name=full_name,email=email,phone=phone,subject=subject,cn_message=cn_message)
		add.save()

		x = ''.join(random.choices(full_name + string.digits, k=8))
		y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))

		subject = 'Welcome to Met Engineering and Metal Works'
		message = f'Hi {full_name}, thank you for writing to us. We have received your message and we will reply by email as soon as possible.'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email, ]
		send_mail( subject, message, email_from, recipient_list)
		subject = 'form details '
		message = f'A contact form from {full_name} and the message is {cn_message}'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [settings.EMAIL_HOST_USER , ]
		send_mail( subject, message, email_from, recipient_list)
		return render(request,"contact.html",{"msg":"Saved"})
	else:
		return render(request,"contact.html",{"error":" Not Saved"})




##################################################################################################################################

def admin_index(request):
	return render(request,"admin/index.html")

def admin_form_product(request):
	if request.method=="POST":
		product_name=request.POST['product_name']
		product_image=request.FILES['product_image']
		description=request.POST['description']
		check=product_tb.objects.filter(product_image=product_image)
		if check:
			return render(request,"admin/form_product.html",{"error":"Already Uploaded"})
		else:
			add=product_tb(product_name=product_name,product_image=product_image,description=description)
			add.save()
			return render(request,"admin/index.html",{"msg":"Saved"})
	else:
		return render(request,"admin/form_product.html",{"error":"Not saved"})

def admin_product_display(request):
	data=product_tb.objects.all()
	return render(request,"admin/product_display.html",{'data':data})


def admin_product_update(request):
	if request.method=="POST":
		product_name=request.POST['product_name']
		pid=request.GET['pid']
		imageupdate=request.POST['imgupdate']
		if imageupdate == "Yes":
			product_image=request.FILES['product_image']
			oldrec=product_tb.objects.filter(id=pid)
			updrec=product_tb.objects.get(id=pid)
			for x in oldrec:
				imgurl=x.product_image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.product_image=product_image
			updrec.save()
		description=request.POST['description']
		add=product_tb.objects.filter(id=pid).update(product_name=product_name,description=description)
		return HttpResponseRedirect("/admin_product_display/")
	else:
		pid=request.GET['pid']
		data=product_tb.objects.filter(id=pid)
		return render(request,"admin/product_update.html",{'data':data})

def admin_product_delete(request):
	pid=request.GET['pid']
	add=product_tb.objects.filter(id=pid).delete()
	return HttpResponseRedirect("/admin_product_display/")


def admin_signin(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['password']
		check=admin_register_tb.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session["admin_id"]=x.id
				request.session["admin_name"]=x.first_name
				return render(request,"admin/index.html",{"success":"Login Successful"})
		else:
			return render(request,"admin/sign-in.html",{"error":"Details are incorrect"})
	else:
		return render(request,"admin/sign-in.html")



def admin_signout(request):
	if request.session.has_key('admin_id'):
		del request.session['admin_id']
		del request.session['admin_name']
		return HttpResponseRedirect("/admin_signin/")


def admin_signup(request):
	if request.method=="POST":
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		password=request.POST['password']
		confirm_password=request.POST['confirm_password']
		check=admin_register_tb.objects.filter(email=email)
		if check:
			return render(request,"admin/sign-up.html",{"error":"Already registered"})
		else:
			add=admin_register_tb(first_name=first_name,last_name=last_name,email=email,password=password,confirm_password=confirm_password)
			add.save()
			return render(request,"admin/sign-in.html",{"success":"Registration Successful"})
	else:
		return render(request,"admin/sign-up.html")



def admin_form_gallery(request):
	if request.method=="POST":
		image=request.FILES['image']
		check=gallery_tb.objects.filter(image=image)
		if check:
			return render(request,"admin/form_gallery.html",{"error":"Already selected"})
		else:
			add=gallery_tb(image=image)
			add.save()
			return render(request,"admin/form_gallery.html",{"msg":"Saved"})
	else:
		return render(request,"admin/form_gallery.html")


def admin_gallery_display(request):
	data=gallery_tb.objects.all()
	return render(request,"admin/gallery_display.html",{'data':data})


def admin_gallery_update(request):
	if request.method=="POST":
		pid=request.GET['pid']
		imageupdate=request.POST['imgupdate']
		if imageupdate == "Yes":
			image=request.FILES['image']
			oldrec=gallery_tb.objects.filter(id=pid)
			updrec=gallery_tb.objects.get(id=pid)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.image=image
			updrec.save()
		add=gallery_tb.objects.filter(id=pid).update()
		return HttpResponseRedirect("/admin_gallery_display/")
	else:
		pid=request.GET['pid']
		data=gallery_tb.objects.filter(id=pid)
		return render(request,"admin/gallery_update.html",{'data':data})


def admin_gallery_delete(request):
	pid=request.GET['pid']
	add=gallery_tb.objects.filter(id=pid).delete()
	return HttpResponseRedirect("/admin_gallery_display/")


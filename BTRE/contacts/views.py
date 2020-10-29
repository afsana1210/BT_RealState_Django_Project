from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        user_id=request.POST['user_id']
        message=request.POST['message']
        realtor_email=request.POST['realtor_email']
        
        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,user_id=user_id,message=message)
        
        contact.save()

        messages.success(request,'Your request has been submitted,a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)










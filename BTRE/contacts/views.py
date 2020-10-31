from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
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
        
        # check if user already made an inquiry
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,user_id=user_id,message=message)
        
        contact.save()

        #send email
        send_mail(
            'Property listing Inquiry',
            'There has been an inquiry for '+listing+'.Sign into the admin panel for more infor',
            'abc@gmail.com',
            [realtor_email,'kyle@btrealestate.co'],
            fail_silently=False
        )

        messages.success(request,'Your request has been submitted,a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)










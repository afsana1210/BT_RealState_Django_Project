from django.shortcuts import render,get_object_or_404
from .models import Listing
from listings.choices import price_choices,bedroom_choices,state_choices
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def index(request):
    # listings=Listing.objects.all()
    # according to date it will show listing.used filter for listing is published or not if nor removed it.only published listing should show .
    listings=Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)

    context={
        'listing':listing

    }
    return render(request,'listings/listing.html',context)

def search(request):
    queryset_list=Listing.objects.order_by("-list_date")

    context={
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        'listings':queryset_list
    }
    return render(request,'listings/search.html',context)
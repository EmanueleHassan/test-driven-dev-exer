from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):

    return render(
        request,
        "home.html",

        # The third argument passes variables to templates.  Here you
        # pass the variable upon a post request.  We use dict.get to
        # supply a default value, for the case where we are doing a
        # normal GET request, when the POST dictionary is empty.
        {"new_item_text": request.POST.get("item_text", "")} 
    )


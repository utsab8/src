from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from utsab.models import Home, About, Service, Portfolio, Contact
from.forms import User_form

# Create your views here.

def home(request):
    home = Home.objects.all().last()
    abouts = About.objects.all().last()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    
    # if home.exists():
    #     home = home.last()
    
    return render(request, "home.html", {
    "home": home,    
    "about": abouts,
    "services": services,
    "portfolios": portfolios,    
               
                  
                  
                  })
def user_contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["number"]
        message = request.POST["message"]
        
        Contact.objects.create(name=name, email=email, number=mobile, message=message)
            
        return HttpResponseRedirect('/thanks/')
        
    else:
        form = User_form()
        
        
        
        
        
        
        # name = request.POST["user_name"]
        # email = request.POST["user_email"]
        # mobile = request.POST["user_mobile"]
        # # message = request.POST["user_message"]
        # contact = Contact(name=name, email=email,  )
        # contact.save
        
    return render(request, "home.html", {'form':form})




    
    

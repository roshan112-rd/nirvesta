from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .forms import *
# Create your views here.
def home(request):
    slider = Slider.objects.all().order_by("order")

    services = Service.objects.all()

    paginator = Paginator(services, 4)
    page = request.GET.get("page")
    services = paginator.get_page(page)

    testimonial = Testimonial.objects.all()

    partners = Partner.objects.all()
    team = Team.objects.all()
    paginator = Paginator(team, 3)
    page = request.GET.get("page")
    team = paginator.get_page(page)
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'slider':slider,
            'services':services,
            'testimonial':testimonial,
            'partners':partners,
            'team':team,
        }
    else:
        context = {
            'slider':slider,
            'services':services,
            'testimonial':testimonial,
            'partners':partners,
            'team':team,
        }
    return render(request,'index.html',context)


def about(request):
    testimonial = Testimonial.objects.all()
    partners = Partner.objects.all()
    team = Team.objects.all()
    faqs = Faqs.objects.all()
    files = Brochures.objects.all()
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'testimonial':testimonial,
            'partners':partners,
            'team':team,
            'faqs':faqs,
            'files':files,
        }
    else:
        context = {
            'testimonial':testimonial,
            'partners':partners,
            'team':team,
            'faqs':faqs,
            'files':files,
        }
    return render(request,'about.html',context)

def services(request):
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()

    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'services':services,
            'testimonial':testimonial,

        }
    else:
        context = {
            'services':services,
            'testimonial':testimonial,

        }
    return render(request,'service.html',context)

def service_detail(request,id):
    service_data = Service.objects.get(id=id)
    faqs = Faqs.objects.all()
    files = Brochures.objects.all()
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'service_data':service_data,
            'faqs':faqs,
            'files':files,
        }
    else:
        context = {
            'service_data':service_data,
            'faqs':faqs,
            'files':files,
        }
    return render(request,'service_detail.html',context)

def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 1)
    page = request.GET.get("page")
    blogs = paginator.get_page(page)
    files = Brochures.objects.all()
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'blogs':blogs,
            'files':files,

        }
    else:
        context = {
            'blogs':blogs,
            'files':files,

        }
    return render(request,'blog.html',context)

def blog_detail(request,id):
    blog_data = Blog.objects.get(id=id)
    faqs = Faqs.objects.all()
    files = Brochures.objects.all()
    blogs = Blog.objects.all()
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'blog_data':blog_data,
            'blogs':blogs,
            'faqs':faqs,
            'files':files,
        }
    else:
        context = {
            'blog_data':blog_data,
            'blogs':blogs,
            'faqs':faqs,
            'files':files,
        }
    return render(request,'blog_detail.html',context)


def contact(request):
    if request.method =='POST':
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        Contact.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        return redirect('contact')
    else:
        if CompanySetup.objects.filter()[:1].exists():
            company = CompanySetup.objects.filter()[:1].get()
            context = {
                'company':company,
            }
        else:
            context = {
            }
        return render(request,'contact.html',context)



def team(request):
    team = Team.objects.all()
    board = BoardMember.objects.all()
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'team':team,
            'board':board,
        }
    else:
        context = {
            'team':team,
            'board':board,
        }
    return render(request,'team.html',context)

def login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect("admin:index")

    elif request.user.is_authenticated:
        return redirect('dashboard')

    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user is None:
                messages.info(request, "Invalid credentials")
                return redirect("login")

            if user is not None and user.is_superuser:
                auth.login(request, user)
                messages.info(request, "Logged in successfully.")
                return redirect("admin:index")

            elif user is not None and not user.is_superuser:
                auth.login(request, user)
                messages.info(request, "Logged in successfully.")
                return redirect("dashboard")   
        else:
            if CompanySetup.objects.filter()[:1].exists():
                company = CompanySetup.objects.filter()[:1].get()
                context = {
                    'company':company,
                }
            else:
                context = {
                }
        return render(request,'login.html',context)


    
@login_required
def dashboard(request):
    user_data = Shareholder.objects.get(user=request.user)
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'user_data':user_data
        }
    else:
        context = {
            'user_data':user_data
        }
    return render(request, 'dashboard.html',context)


@login_required
def logout(request):
    django_logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("home")

@login_required
def apply_loan(request):
    form = LoanForm()
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')



    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'form':form
        }
    else:
        context = {
            'form':form
        }
    return render(request, 'apply_loan.html',context)

@login_required
def company_profile(request):
    company_data = CompanyProfile.objects.all()
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'company_data':company_data
        }
    else:
        context = {
            'company_data':company_data
        }
    return render(request, 'company_profile.html',context)

def shareholders(request):
    team = Shareholder.objects.all()
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
            'team':team,
        }
    else:
        context = {
            'team':team,
        }
    return render(request,'shareholders.html',context)
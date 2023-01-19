from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from nanoid import generate

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

    elif request.user.is_authenticated and not request.user.is_superuser and request.user.is_staff:
        return redirect('dashboard')
    
    elif request.user.is_authenticated and not request.user.is_superuser and not request.user.is_staff:
        return redirect('borrower_dashboard')

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

            elif user is not None and not user.is_superuser and  user.is_staff:
                auth.login(request, user)
                messages.info(request, "Logged in successfully.")
                return redirect("dashboard")
                  
            elif user is not None and not user.is_superuser and not user.is_staff:
                auth.login(request, user)
                messages.info(request, "Logged in successfully.")
                return redirect("borrower_dashboard")   
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


def apply_loan(request):
    if request.method == 'POST':
        desired_loan_amount = request.POST['desired_loan_amount']
        annual_income = request.POST['annual_income']
        use_of_loan = request.POST['use_of_loan']
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        marital_status = request.POST['marital_status']
        email = request.POST['email']
        phone = request.POST['phone']
        how_long_have_you_lived_in_your_given_address = request.POST['how_long_have_you_lived_in_your_given_address']
        address = request.POST['address']
        present_employer_name = request.POST['present_employer_name']
        occupation = request.POST['marital_status']
        years_of_experience = request.POST['years_of_experience']
        gross_monthly_income = request.POST['gross_monthly_income']
        monthly_rent = request.POST['monthly_rent']
        down_payment = request.POST['down_payment']
        comments = request.POST['comments']
        institution_name = request.POST['institution_name']
        saving_account_number = request.POST['saving_account_number']
        institution_address = request.POST['institution_address']
        phone_number = request.POST['phone_number']



        dob=date_of_birth.replace("-", "_")
        initial = name + '@'+ dob
        username = initial.replace(" ", "_").lower()
        password = generate(size=10)


         
        if User.objects.filter(username = username).first():
            messages.error(request, "This email is already taken")
            return redirect('apply_loan')
        first_name, last_name = name.split(" ", 1)
        user = User.objects.create_user(first_name = first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
        subject = 'User Account Creation'
        message = f"Hello {name}, thank you for becoming a member. Your username is {user.username} and your password is {password}"
        
        message = f"{message}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            email,
        ]
        send_mail(subject, message, email_from, recipient_list)
        messages.error(request, "Your Login credentials are sent to your email address. " + email + " Please check your inbox. ")

        Borrower.objects.create(user=user, name=name, email=email, contact=phone_number, address=address)

        Loan.objects.create(user=user, desired_loan_amount = desired_loan_amount,annual_income = annual_income ,use_of_loan = use_of_loan ,name = name ,
        date_of_birth = date_of_birth,marital_status = marital_status ,email = email ,phone = phone ,
        how_long_have_you_lived_in_your_given_address = how_long_have_you_lived_in_your_given_address ,
        address = address ,present_employer_name = present_employer_name ,occupation = occupation ,years_of_experience = years_of_experience ,
        gross_monthly_income = gross_monthly_income ,monthly_rent = monthly_rent, down_payment = down_payment ,comments = comments ,
        institution_name = institution_name ,saving_account_number = saving_account_number ,institution_address = institution_address ,phone_number = phone_number)
        return redirect('home')
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'company':company,
        }
    else:
        context = {
        }
    return render(request, 'loan_form.html',context)



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

def chat(request):
    if request.method =='POST':
        message = request.POST["message"]
        Chat.objects.create(message=message,sender_id=request.user.id)
        return redirect('chat')
    else:
        chat = Chat.objects.filter(sender = request.user)
        reply = Reply.objects.filter(sender = request.user)
        if CompanySetup.objects.filter()[:1].exists():
            company = CompanySetup.objects.filter()[:1].get()
            context = {
                'company':company,
                'chat':chat,
                'reply':reply,
                
            }
        else:
            context = {
                'chat':chat,
                'reply':reply,
                
            }
        return render(request,'chat.html',context)


def mail(request):
    if request.user.is_superuser:
        if request.method =='POST':
            email = request.POST["email"]
            subject = request.POST["subject"]
            message = request.POST["message"]

            subject = f"{subject}"
            message = f"{message}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [
                email,
            ]
            send_mail(subject, message, email_from, recipient_list)
            SentMail.objects.create(email=email,subject=subject,message=message)
            return redirect("mail")

        if CompanySetup.objects.filter()[:1].exists():
            company = CompanySetup.objects.filter()[:1].get()
            context = {
                'company':company,
            }
        else:
            context = {
            }
        return render(request,'send_mail.html',context)
    else:
        return redirect('login')

def bulk_mail(request):
    if request.user.is_superuser:
        if request.method =='POST':
            subject = request.POST["subject"]
            message = request.POST["message"]
            shareholders=Shareholder.objects.all()

            for shareholders in shareholders:
                subject = f"{subject}"
                message = f"{message}"
                email=shareholders.email
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [
                    email,
                ]
                send_mail(subject, message, email_from, recipient_list)
                SentMail.objects.create(email=email,subject=subject,message=message)

            return redirect("bulk_mail")
            
        if CompanySetup.objects.filter()[:1].exists():
            company = CompanySetup.objects.filter()[:1].get()
            context = {
                'company':company,
            }
        else:
            context = {
            }
        return render(request,'bulk_mail.html',context)
    else:
        return redirect('login')


# def selected_mail(request):
#     if request.user.is_superuser:
#         if request.method =='POST':
#             subject = request.POST["subject"]
#             message = request.POST["message"]
#             print(request.POST['selected'])
#             selected = ''
#             for request.POST['selected'] in selected:
#                 print(selected)
#             return redirect("selected_mail")
#         else:
#             if CompanySetup.objects.filter()[:1].exists():
#                 shareholders=Shareholder.objects.all()
#                 company = CompanySetup.objects.filter()[:1].get()
#                 context = {
#                     'company':company,
#                     'shareholders':shareholders,
#                 }
#             else:
#                 context = {
#                     'shareholders':shareholders,
#                 }
#             return render(request,'selected_mail.html',context)
#     else:
#         return redirect('login')



def selected_mail(request):
    if request.user.is_superuser:
        if request.method =='POST':
            subject = request.POST["subject"]
            message = request.POST["message"]
            email = request.POST.getlist("selected")

            print(email)
            for email in email:
                subject = f"{subject}"
                message = f"{message}"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [
                    email,
                ]
                send_mail(subject, message, email_from, recipient_list)
                SentMail.objects.create(email=email,subject=subject,message=message)
            return redirect("selected_mail")
        else:
            if CompanySetup.objects.filter()[:1].exists():
                shareholders=Shareholder.objects.all()
                company = CompanySetup.objects.filter()[:1].get()
                context = {
                    'company':company,
                    'shareholders':shareholders,
                }
            else:
                context = {
                    'shareholders':shareholders,
                }
            return render(request,'selected_mail.html',context)
    else:
        return redirect('login')




def page_not_found_view(request, exception):
    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
        'company':company,
        'shareholders':shareholders,
        }
    else:
        context = {
        'shareholders':shareholders,
        }
    return render(request, "error404.html", context)


@login_required
def borrower_dashboard(request):
    loan_data = Loan.objects.filter(user=request.user)

    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
        'company':company,
        'loan_data':loan_data,
        }
    else:
        context = {
        'loan_data':loan_data,
        }
    return render(request, "borrower_dashboard.html", context)

    
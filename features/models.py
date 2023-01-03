from django.db import models
from django.contrib.auth.models import User

class CompanySetup(models.Model):
    data_set = models.TextField()

    logo = models.ImageField(upload_to="company_images")
    location = models.TextField()
    contact = models.TextField()
    email = models.TextField()
    opening_hours = models.TextField()
    no_of_clients = models.TextField()
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    twitter_url = models.URLField()
    about_us_page_heading_text = models.TextField()
    about_us_page_content = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    company_profile_text = models.TextField()

    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "01. Company Setup" 

# Create your models here.
class Slider(models.Model):
    order = models.IntegerField()
    image = models.ImageField(upload_to='slider_images')
    text_1 = models.TextField(null=True,blank=True)
    text_2 = models.TextField(null=True,blank=True)
    text_3 = models.TextField(null=True,blank=True)
    button_text = models.TextField(null=True,blank=True)
    custom_link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.text_1
    class Meta:
        verbose_name_plural = "02. Slider" 


class Service(models.Model):
    title = models.TextField()
    description = models.TextField()
    icon = models.ImageField(upload_to='services')
    featured_image = models.ImageField(upload_to='services', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "03. Services" 

class Partner(models.Model):
    name = models.TextField()
    logo = models.ImageField(upload_to='partner_images')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "04. Partners"

class BoardMember(models.Model):
    name = models.TextField()
    position = models.TextField()
    image = models.ImageField(upload_to='team_images')
    facebook= models.URLField(null=True, blank=True)
    instagram= models.URLField(null=True, blank=True)
    twitter= models.URLField(null=True, blank=True)
    linkedin= models.URLField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "05. Board Members"
        
class Team(models.Model):
    name = models.TextField()
    position = models.TextField()
    image = models.ImageField(upload_to='team_images')
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "06. Team Members"

class Testimonial(models.Model):
    testimonial= models.TextField()
    name= models.TextField()
    company= models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "07. Testimonials"

class Faqs(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "08. FAQs"

class Brochures(models.Model):
    name = models.TextField()
    file = models.FileField(upload_to="brochures")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "09. Brochures"

class Shareholder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=200)
    no_of_share = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="shareholder_images/",null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name
    
    class Meta:
        verbose_name_plural = "10. Shareholders"

class Borrower(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "11. Borrowers"

class Blog(models.Model):
    title = models.TextField()
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/")
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "12. Blogs" 


class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "13. Borrowers"




class CompanyProfile(models.Model):
    company_name = models.TextField()
    invested_amount = models.IntegerField()
    investment_date = models.DateField()
    investment_duration = models.IntegerField()
    company_logo = models.ImageField(upload_to='company_profile')


    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name_plural = "14. Company Profile"



class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desired_loan_amount = models.IntegerField()
    annual_income = models.IntegerField()
    use_of_loan = models.TextField()

    name = models.TextField()
    date_of_birth = models.TextField()
    marital_status = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    address = models.TextField()
    how_long_have_you_lived_in_your_given_address = models.TextField()
   
    present_employer_name = models.TextField()
    occupation = models.TextField()
    years_of_experience = models.TextField()
    gross_monthly_income = models.TextField()
    monthly_rent = models.TextField()
    down_payment = models.TextField()
    comments = models.TextField()

    institution_name = models.TextField()
    saving_account_number = models.TextField()
    institution_address = models.TextField()
    phone_number = models.TextField()
    created = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "14. Loan Forms"


class Chat(models.Model):
    sender  = models.ForeignKey(User, on_delete=models.CASCADE)
    is_responded = models.BooleanField(default = 0)
    message= models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = "00. Chat"

class Reply (models.Model):
    sender  = models.ForeignKey(User, on_delete=models.CASCADE)
    message= models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = "0001. Reply"

class SentMail (models.Model):
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "18. Sent Mail"

from django.forms import ModelForm
from crispy_forms.helper import FormHelper, Layout
from .models import Loan
from django import forms
class LoanForm(forms.ModelForm):
	error_css_class='error-field'
	required_css_class='required-field'

	STATUS_CHOICES = (
        ('married', 'married'),
        ('unmarried', 'unmarried')
    )
	
	desired_loan_amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-input','placeholder': '100000'}))
	annual_income = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-input','placeholder': '100000'}))
	use_of_loan = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'business_purpose'}))

	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Alex Rodrigues'}))
	date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '100000'}))
	marital_status = forms.CharField( widget=forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-input'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Alex@gmail.com'}))
	phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '9841012145'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Baneshwor 8, Kathmandu'}))
	how_long_have_you_lived_in_your_given_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '2 Years'}))

	present_employer_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input' ,'placeholder': 'Nabil Corporation'}))
	occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Manager'}))
	years_of_experience = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '5'}))
	gross_monthly_income = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '50000'}))
	monthly_rent = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '20000'}))
	down_payment = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '50000'}))
	comments = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Write your comments.....'}))

	institution_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Global IME Bank'}))
	saving_account_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '1258455165145524'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'New- Baneshwor'}))
	phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': '01-1254541'}))
	class Meta:
		model = Loan
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
	
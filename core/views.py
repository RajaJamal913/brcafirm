from django.shortcuts import render
from django.http import HttpResponse
app_name = 'core'

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def audit_coordination(request):
    return render(request, 'core/audit_coordination.html')

def bookkeeping(request):
    return render(request, 'core/bookkeeping.html')

def external_audit(request):
    return render(request, 'core/external_audit.html')

def internal_audit(request):
    return render(request, 'core/internal_audit.html')

def advisory(request):
    return render(request, 'core/advisory.html')

def Taxation_services(request):
    return render(request, 'core/Taxationservices.html')

def program_support(request):
    return render(request, 'core/NTNRegistration.html')

def IncomeTax(request):
    return render(request, 'core/IncomeTax.html')

# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('core:contact')
        else:
            print(form.errors)  # Debugging: Print form errors
    else:
        form = ContactForm()

    return render(request, 'core/index.html', {'form': form})


def ngo_registration_licensing(request):
    return render(request, 'core/ngo_registration_licensing.html')

def corporate_registration_licensing(request):
    return render(request, 'core/corporate_registration_licensing.html')

def company_registration_withscep(request):
    return render(request, 'core/company_registration_withscep.html')
from urllib import request

from django.shortcuts import render, redirect

from company.models import Contact
from .models import About, Skill, Stat, Testimonial
from .models import Resume, Education, ProfessionalExperience, ResumeSkill


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.urls import reverse

# Create your views here.
# def home(request):
#     return render(request, 'index.html')



def contact_view(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()  # Save the data to the database
                messages.success(request, 'Your message has been sent. Thank you!')
                return redirect(reverse('index'))  # Redirect to the contact page or any other page
            else:
                messages.error(request, 'There was an error with your message. Please try again.')

        else:
            form = ContactForm()  # Empty form for GET request

        return render(request, 'contact.html', {'form': form})

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

# def resume(request):
#     return render(request, 'resume.html')

def services(request):
    return render(request, 'services.html')


# myapp/views.py


def about(request):
    about_info = About.objects.first()  # Assuming there's only one record for about info
    skills = Skill.objects.all()
    stats = Stat.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'about_info': about_info,
        'skills': skills,
        'stats': stats,
        'testimonials': testimonials,
    }

    return render(request, 'about.html', context)





def resume_view(request):
    resume = Resume.objects.first()  # Assuming only one resume
    education_list = Education.objects.all()
    experience_list = ProfessionalExperience.objects.all()
    skills = ResumeSkill.objects.all()  # Updated model name

    context = {
        'resume': resume,
        'education_list': education_list,
        'experience_list': experience_list,
        'skills': skills,
    }
    return render(request, 'resume.html', context)


from django.shortcuts import render
from .models import heroSection

def home_view(request):
    hero_section = heroSection.objects.first()  # Fetch the first HeroSection object
    context = {
        'hero': hero_section,
    }
    return render(request, 'index.html', context)


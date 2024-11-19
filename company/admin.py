from django.contrib import admin
from .models import Resume, Education, ProfessionalExperience,ResumeSkill
from .models import About, Skill, Stat, Testimonial, Contact
from .models import heroSection



# Register your models here.
# myapp/admin.py

admin.site.register(heroSection)

#contact
admin.site.register(Contact)

#About
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Stat)
admin.site.register(Testimonial)

#  resume
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(ProfessionalExperience)
admin.site.register(ResumeSkill)

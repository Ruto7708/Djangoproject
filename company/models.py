from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()


    def __str__(self):
        return f"Message from {self.name} ({self.email})"
# myapp/models.py


class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    degree = models.CharField(max_length=100)
    freelance_status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # 0 to 100 scale

    def __str__(self):
        return self.name

class Stat(models.Model):
    name = models.CharField(max_length=100)  # Example: "Clients", "Projects", etc.
    value = models.IntegerField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField()  # Rating from 1 to 5

    def __str__(self):
        return f"{self.client_name} - {self.position}"



#Resume
class Resume(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    institution = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.degree


class ProfessionalExperience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)  # Optional if still employed
    description = models.TextField()
    responsibilities = models.TextField()  # Store as a comma-separated string

    def responsibilities_list(self):
        return self.responsibilities.split(',')

    def __str__(self):
        return f"{self.title} at {self.company}"


class ResumeSkill(models.Model):  # Renamed model
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # Represented as a percentage (0–100)

    def __str__(self):
        return self.name




class heroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to='hero_images/')
    button_text = models.CharField(max_length=100)
    button_link = models.URLField()

    def __str__(self):
        return self.title

from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company_name}"

class Education(models.Model):
    title = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} in {self.speciality} at {self.organization}"

class Testimonial(models.Model):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonials/')
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return f"Testimonial by {self.full_name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    video = models.FileField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    video = models.FileField(upload_to='projects/', null=True, blank=True)

    def __str__(self):
        return self.title

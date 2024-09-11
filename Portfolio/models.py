from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    from_date = models.CharField(max_length=50)
    to_date = models.CharField(max_length=50)
    order = models.SmallIntegerField(auto_created=True)

class Certification(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    description = models.TextField()
    from_date = models.CharField(max_length=50)
    to_date = models.CharField(max_length=50)
    order = models.SmallIntegerField(auto_created=True)

class Skill(models.Model):
    class SkillType(models.TextChoices):
        PROGRAMMING = 'P',_('Programming')
        TOOL = 'T',_('Tool')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=SkillType.choices)
    order = models.SmallIntegerField(auto_created=True)

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to="projects/")
    order = models.SmallIntegerField(auto_created=True)

class Responsibility(models.Model):
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    order = models.SmallIntegerField(auto_created=True)

class Achievement(models.Model):
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    order = models.SmallIntegerField(auto_created=True)

class Media(models.Model):
    media = models.ImageField(upload_to="projects/media/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    order = models.SmallIntegerField(auto_created=True)

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="articles/")
    url = models.URLField()
    likes = models.IntegerField()
    views = models.IntegerField()
    created_at = models.DateField()
    order = models.SmallIntegerField(auto_created=True)

class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="about/", null=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.URLField()
    address = models.CharField(max_length=100)
    description = models.TextField()
    whatsapp = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()
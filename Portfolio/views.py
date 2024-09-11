from django.shortcuts import render
from .models import (
    About,
    Achievement,
    Article,
    Certification,
    Experience,
    Media,
    Project,
    Responsibility,
    Skill,
)


# Create your views here.
def index(request):
    about = About.objects.first()
    experiences = Experience.objects.all()
    certifications = Certification.objects.order_by("order").all()
    p_skills = Skill.objects.filter(type="P")
    t_skills = Skill.objects.filter(type="T")
    projects = Project.objects.all()
    for project in projects:
        project.Responsibilities = Responsibility.objects.filter(project_id=project.pk)
        project.Achievements = Achievement.objects.filter(project_id=project.pk)
        project.Media = Media.objects.filter(project_id=project.pk)
    articles = Article.objects.all()

    return render(
        request,
        "index.html",
        {
            "About": about,
            "Experiences": experiences,
            "Certifications": certifications,
            "PSkills": p_skills,
            "TSkills": t_skills,
            "Projects": projects,
            "Articles": articles,
        },
    )

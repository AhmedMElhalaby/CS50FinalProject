from django.contrib import admin
from .models import About, Article, Certification, Experience, Media, Project, Skill, Achievement, Responsibility
# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):        
    list_display = ('id','title','company_name','order')
admin.site.register(Experience,ExperienceAdmin)
class CertificationAdmin(admin.ModelAdmin):        
    list_display = ('id','title','organization','order')
admin.site.register(Certification,CertificationAdmin)
class SkillAdmin(admin.ModelAdmin):        
    list_display = ('id','name','type','order')
admin.site.register(Skill,SkillAdmin)
class ProjectAdmin(admin.ModelAdmin):        
    list_display = ('id','title','logo','order')
admin.site.register(Project,ProjectAdmin)
admin.site.register(Responsibility)
admin.site.register(Achievement)
admin.site.register(Media)
class ArticleAdmin(admin.ModelAdmin):        
    list_display = ('id','title','image','order')
admin.site.register(Article,ArticleAdmin)
class AboutAdmin(admin.ModelAdmin):        
    list_display = ('id','name','title','avatar')
admin.site.register(About,AboutAdmin)
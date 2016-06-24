from django.contrib import admin
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'desc', 'date_publish',)

admin.site.register(Article,ArticleAdmin)
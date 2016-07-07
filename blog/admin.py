from django.contrib import admin
from blog.models import Article, Contact, Banner


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'desc', 'date_publish',)

	class Media:
	    js = (
            '/static/scripts/kindeditor-4.1.10/kindeditor-min.js',
            '/static/scripts/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/scripts/kindeditor-4.1.10/config.js',
        )


class ContactAdmin(admin.ModelAdmin):
	list_display = ('subject', 'email', 'message')

class BannerAdmin(admin.ModelAdmin):
	list_display = ('name','url','img','index')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Banner,BannerAdmin)
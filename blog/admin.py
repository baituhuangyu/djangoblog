#-*- coding:utf-8-*-
from django.contrib import admin
from blog.models import *


#Register your model here.

class ArticleAdmin(admin.ModelAdmin):
    # list_display = ('title', 'desc', 'click_count',)
    # list_display_links = ('title', 'desc',)
    # list_editable = ('click_count',)
    # fieldsets = (
    #     (None,{
    #         'fields':('title', 'desc', 'content',)
    #     }),
    #     ('高级设置', {
    #         'classes': ('collapse',),
    #         'fields': ('click_count', 'is_recommend')
    #     }),
    # )
    class Media:
            js = (
                '/static/js/kindeditor-4.1.10/kindeditor-min.js',
                '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
                '/static/js/kindeditor-4.1.10/config.js',
            )
admin.site.register(User)
admin.site.register(Tag)
# admin.site.register(Article)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)


# class AuthorAdmin(admin.ModelAdmin):
# 	list_display = ('first_name', 'last_name')
# 	search_fields = ('first_name', 'last_name')
# 	# list_filter = ('publication_date',)
# 	# date_hierrchy = ('publication_date',)
#
# 	# ordering = ('-publication_date',)
# 	# fields = ('first_name',)
#
#
#
#
#
#
#
#
# admin.site.register(Author, AuthorAdmin)
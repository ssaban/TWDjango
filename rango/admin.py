from django.contrib import admin
from rango.models import Category, Page, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    pass

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)


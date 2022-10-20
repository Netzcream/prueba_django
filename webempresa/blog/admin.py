from django.contrib import admin
from .models import Category,Post
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published','post_categories','image')
    ordering = ('author','published') #si se quiere ordenar por 1 campo ('author',)
    search_fields = ('title','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('categories','author')

    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorías"

    def image(self, obj):
        return format_html('<image src="{}" />', obj.image)



admin.site.register(Category,CategoryAdmin)

admin.site.register(Post,PostAdmin)
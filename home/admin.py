from django.contrib import admin
from .models import News,Category,ContactMessage
admin.site.register(News)
admin.site.register(Category)
def mark_as_read(modeladmin, request, queryset):
    queryset.update(is_read=True)

mark_as_read.short_description = "Tanlangan xabarlarni 'o'qildi' deb belgilash"
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('name', 'text')

admin.site.register(ContactMessage, ContactMessageAdmin)
# Register your models here.

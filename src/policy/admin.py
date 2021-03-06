from django.contrib import admin

# Register your models here.
from .models import Policy


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('Program', 'Total_Graduate_Credits')
    search_fields = ('Program', 'Total_Graduate_Credits')

# 后台显示列名
admin.site.register(Policy, PolicyAdmin)
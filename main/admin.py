from django.contrib import admin
from .models import *


class AboutUsImgInline(admin.TabularInline):
    model = AboutUsImage
    extra = 0


class AboutUsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in AboutUs._meta.fields]
    inlines = [AboutUsImgInline]

    class Meta:
        model = AboutUs


admin.site.register(Slider)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(PublicOffer)
admin.site.register(Advantage)
admin.site.register(Help)
admin.site.register(Help_img)

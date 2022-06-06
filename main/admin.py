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
admin.site.register(Call_back)


class Footer_second_sideInline(admin.TabularInline):
    model = Footer_second_side
    extra = 0


class Footer_first_sideAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Footer_first_side._meta.fields]
    inlines =  [Footer_second_sideInline]

    class Meta:
        model = Footer_first_side

admin.site.register(Footer_first_side, Footer_first_sideAdmin)
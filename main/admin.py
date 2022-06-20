from django.contrib import admin
from .models import *


class AboutUsImgInline(admin.TabularInline):
    model = AboutUsImage
    max_num = 3
    extra = 3


class AboutUsAdmin (admin.ModelAdmin):
    """
    Открывает сразу редактор записи.
    """
    list_display = [field.name for field in AboutUs._meta.fields]
    inlines = [AboutUsImgInline]
    model = AboutUs

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.count() == 0:
            return super().add_view(request, extra_context)
        else:
            object = (self.model.objects.first()).id
            return super().change_view(request=request,
                                       extra_context=extra_context,
                                       object_id=str(object))

    class Meta:
        model = AboutUs


class PublicOfferAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.count() < 1:
            return super().add_view(request, extra_context)
        else:
            object = (self.model.objects.first()).id
            return super().change_view(request=request,
                                       extra_context=extra_context,
                                       object_id=str(object))

    class Meta:
        model = PublicOffer


class Footer_second_sideInline(admin.TabularInline):
    model = Footer_second_side
    extra = 0


class Footer_first_sideAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Footer_first_side._meta.fields]
    inlines = [Footer_second_sideInline]
    model = Footer_first_side

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.count() < 1:
            return super().add_view(request, extra_context)
        else:
            object = (self.model.objects.first()).id
            return super().change_view(request=request,
                                       extra_context=extra_context,
                                       object_id=str(object))

    class Meta:
        model = Footer_first_side


class Call_backAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'type', 'status', 'date')
    list_filter = ('status',)
    search_fields = ('name', 'phone_number')
    readonly_fields = ('date',)

    def has_add_permission(self, request):
        return False


class HelpInline(admin.StackedInline):
    model = Help
    extra = 0


class Help_imgAdmin(admin.ModelAdmin):
    inlines = [HelpInline]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.count() < 1:
            return super().add_view(request, extra_context)
        else:
            object = (self.model.objects.first()).id
            return super().change_view(request=request,
                                       extra_context=extra_context,
                                       object_id=str(object))


admin.site.register(Slider)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(PublicOffer, PublicOfferAdmin)
admin.site.register(Advantage)
admin.site.register(Help_img, Help_imgAdmin)
admin.site.register(Call_back, Call_backAdmin)
admin.site.register(Footer_first_side, Footer_first_sideAdmin)

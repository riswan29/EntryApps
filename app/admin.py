from django.contrib import admin
from .models import *
# Register your models here.


class KecamatanFilter(admin.SimpleListFilter):
    title = 'Kecamatan'
    parameter_name = 'kecamatan'

    def lookups(self, request, model_admin):
        kecamatans = Kecamatan.objects.all()
        return [(kecamatan.id, kecamatan.nama) for kecamatan in kecamatans]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(kecamatan__id=self.value())

class userPROF(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)


class KELURAHAN_g(admin.ModelAdmin):
    list_display = ('nama', 'kecamatan')
    list_filter = (KecamatanFilter,)
 

admin.site.register(UserProfile, userPROF)
admin.site.register(Kecamatan)
admin.site.register(Kelurahan, KELURAHAN_g)

from django.contrib import admin
from myapp.models import*

# Register your models here.
@admin.register(contect)
class contectadmin(admin.ModelAdmin):
    list_display=('fname','email','contect','day')


@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass


@admin.register(service)
class serviceadmin(admin.ModelAdmin):
    pass
    
@admin.register(serviceitem)
class serviceitemadmin(admin.ModelAdmin):
    pass

@admin.register(cusion)
class cusionadmin(admin.ModelAdmin):
    pass   

@admin.register(typecusion)
class typecusionadmin(admin.ModelAdmin):
    pass   

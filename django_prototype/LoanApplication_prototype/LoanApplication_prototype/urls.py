
from os import stat
from django.contrib import admin
from django.urls import path
from account_register import views

#For media
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view),  
    path('register/',views.register_account),
    path('personal_details/',views.register_personal_details)

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

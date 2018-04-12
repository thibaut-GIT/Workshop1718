from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginView),
    path('signup/', views.signup),
    path('login/',  views.loginView),
    path('homepageetudiant/',  views.homepageetudiant),
    path('equipe/<int:id>',  views.equipe, name='equipe'),
    path('homepageintervant/',  views.homepageintervant),
    path('invalid/',  views.invalid)

]

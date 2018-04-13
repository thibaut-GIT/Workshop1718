from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginView),
    path('signup/', views.signup),
    path('login/',  views.loginView),
    path('homepageetudiant/<int:idetudiant>',  views.homepageetudiant, name='homepageetudiant'),
    path('equipe/<int:idetudiant>/<int:idequipe>',  views.equipe, name='equipe'),
    path('ZoomEquipe/<int:idintervenant>/<int:idprojet>/<int:idequipe>',  views.ZoomEquipe, name='ZoomEquipe'),
    path('projet/<int:idintervenant>/<int:idprojet>',  views.projet, name='projet'),
    path('message/<int:idetudiant>/<int:idequipe>',  views.message, name='message'),
    path('messagesent/<int:idetudiant>/<int:idequipe>',  views.messagesent, name='messagesent'),
    path('homepageintervenant/<int:idintervenant>',  views.homepageintervenant, name='homepageintervenant'),
    path('invalid/',  views.invalid)

]

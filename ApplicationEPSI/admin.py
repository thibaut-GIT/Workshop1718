from django.contrib import admin
from .models import Equipe,Etudiant, Intervenant, Projet, Soutien
# Register your models here.
class EtudiantAdmin(admin.ModelAdmin):
    list_display   = ('Nom', 'Prenom', 'Mail' )
    list_filter    = ('Nom', 'Prenom', 'Mail')
    ordering       = ('Nom', )
    search_fields  = ('Nom', 'Mail')

class IntervenantAdmin(admin.ModelAdmin):
    list_display   = ('Nom', 'Prenom', 'Mail')
    list_filter    = ('Nom', 'Prenom', 'Mail')
    ordering       = ('Nom', )
    search_fields  = ('Nom', 'Mail')

class SoutienAdmin(admin.ModelAdmin):
    list_display   = ('Minutes','Intervenant', 'Projet', 'Equipe')
    list_filter    = ('Intervenant', 'Projet', 'Equipe')
    ordering       = ('Intervenant', )
    search_fields  = ('Intervenant')

class ProjetAdmin(admin.ModelAdmin):
    list_display   = ('Nom', 'Intervenant')

class EquipeAdmin(admin.ModelAdmin):
    list_display   = ('Nom', 'Projet')

admin.site.register(Projet, ProjetAdmin)
admin.site.register(Soutien)
admin.site.register(Intervenant, IntervenantAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Etudiant, EtudiantAdmin)

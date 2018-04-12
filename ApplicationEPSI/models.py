
from django.db import models

class Intervenant(models.Model):
    Nom   = models.CharField(max_length=100,null=True)
    Prenom   = models.CharField(max_length=100,null=True)
    Mail   = models.CharField(max_length=100,null=True)


    def __str__(self):
        template = '{0.Nom} {0.Prenom} {0.Mail}'
        return template.format(self)

class Projet(models.Model):
    Nom = models.CharField(max_length=100)
    Intervenant = models.ForeignKey('Intervenant',on_delete=models.CASCADE, null=True)
    TempsSoutienRestant = models.CharField(max_length=100, null=True)


    def __str__(self):
       return  self.Nom

class Soutien(models.Model):
    Minutes = models.CharField(max_length=100)
    Equipe = models.ForeignKey('Equipe',on_delete=models.CASCADE, null=True)
    Intervenant = models.ForeignKey('Intervenant',on_delete=models.CASCADE, null=True)

    def __str__(self):
       return  self.Intervenant, self.Projet, self.Equipe, self.Minutes

class Message(models.Model):
    Equipe = models.ForeignKey('Equipe',on_delete=models.CASCADE, null=True)
    Intervenant = models.ForeignKey('Intervenant',on_delete=models.CASCADE, null=True)
    Titre = models.CharField(max_length=100)
    Contenu = models.TextField(null=True)
    def __str__(self):
       return  self.Intervenant, self.Equipe, self.Titre, self.Contenu


class Equipe(models.Model):
    Nom = models.CharField(max_length=100)
    Projet = models.ForeignKey('Projet',on_delete=models.CASCADE, null=True)
    Etudiants = models.ManyToManyField('Etudiant', null=True)

    def __str__(self):
       return  self.Nom

class Etudiant(models.Model):
    Nom   = models.CharField(max_length=100,null=True)
    Prenom   = models.CharField(max_length=100,null=True)
    Mail   = models.CharField(max_length=100,null=True)


    def __str__(self):
        template = '{0.Nom} {0.Prenom} {0.Mail}'
        return template.format(self)

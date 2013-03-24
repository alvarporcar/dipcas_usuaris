# Create your models here.
#encoding:utf-8

from django.db import models
from datetime import date

modalitat_cursos = (('P','PRESENCIAL'),('O','ONLINE'),('M','MIXTE'))
pla_formacio = (('IN','INTERN'),('EX','EXTERN'),('AG','AGRUPAT'))

class Cursos(models.Model):
    nom = models.CharField(max_length=50)
    contingut = models.TextField()
    pla = models.CharField(max_length=2, choices= pla_formacio)
    anny = models.CharField(max_length=4)
    dates = models.CharField(max_length=20)
    modalitat = models.CharField(max_length=1,choices= modalitat_cursos)
    professor = models.ManyToManyField('Usuaris',related_name = 'professor_de',through='ProfessorDeCurs')
    projecte = models.ForeignKey('Projectes', to_field='abrev', blank=True, null=True)
    

    def __unicode__(self):
        return u'(%s) %s' %(self.anny,self.nom)

    class Meta:
        ordering = ["anny","nom"]
        verbose_name_plural = "Cursos"


tipus_organismes = (('AJ','AJUNTAMENT'),('MA','MANCOMUNITAT'),('DP','DIPUTACIÓ'),('CN','CONSELLERIA'),('MN','MINISTERI'),('EP','EMPRESA PUBLICA'))

class Organismes(models.Model):
    codi = models.CharField(max_length=6, primary_key=True)
    tipus = models.CharField(max_length=2,choices = tipus_organismes, default='AJ')
    nom = models.CharField(max_length=30)
    adreca = models.CharField(max_length=50)
    poblacio = models.CharField(max_length=30)
    cp = models.CharField(max_length=5)
    email1 = models.EmailField()
    web = models.URLField(blank=True)
    tel1 = models.CharField(max_length=9)
    fax1 = models.CharField(max_length=9, blank=True)
    notes = models.TextField(help_text="Escriu una nota ", verbose_name="Notes", blank=True)

    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ["nom"]
        verbose_name_plural = "Organismes"


class Carrecs(models.Model):
    nom = models.TextField(max_length="30")

    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ["nom"]
        verbose_name_plural = "Carrecs"

class Usuaris(models.Model):
    nif = models.CharField(max_length=9, primary_key=True)
    nom = models.CharField(max_length=30)
    cognoms = models.CharField(max_length=50)
    usudipcas = models.CharField(max_length=10, blank=True, null=True)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    tel1 = models.CharField(max_length=9, blank=True)
    imagen = models.ImageField(upload_to='fotos', verbose_name='Foto', blank=True)
    notes = models.TextField(help_text="Escriu una nota ", verbose_name="Notes", blank=True)
    carrec = models.ForeignKey(Carrecs)
    organisme = models.ForeignKey(Organismes)
    projectes = models.ManyToManyField('Projectes', through = 'UsuarisDeProjecte')
    cursos = models.ManyToManyField(Cursos,through='Matricula')
    
    def __unicode__(self):
        return u'%s %s  |   %s  |  %s ' %(self.cognoms,self.nom,self.carrec,self.organisme)

    class Meta:
        ordering = ["organisme","cognoms"]
        verbose_name_plural="Usuaris"

class UsuarisDeProjecte(models.Model):
    usuari = models.ForeignKey(Usuaris)
    projecte = models.ForeignKey('Projectes')
    alta = models.DateField(default = date.today()) 
    
    def  __unique__(self):
	return u'%s %s' %(self.usuari,self.projecte)

    class Meta:
        unique_together = (('usuari','projecte'),)
	ordering = ["usuari","projecte"]


class ProfessorDeCurs(models.Model):
    professor = models.ForeignKey(Usuaris)
    curs = models.ForeignKey(Cursos)
    hores = models.IntegerField(default=0)

    class Meta:
        unique_together = (('professor','curs'),)


class Matricula(models.Model):
    alumne = models.ForeignKey(Usuaris)
    curs = models.ForeignKey(Cursos)
    superat = models.BooleanField(default = True)
    notes = models.TextField(help_text="Escriu una nota ",verbose_name="Notes",blank=True)
	
    def __unique__(self):
	    return u'%s, %s, %s, %s' %(self.alumne,self.curs,self.superat,self.notes)

    class Meta:
        unique_together = (('alumne','curs'),)


class Projectes(models.Model):
    abrev = models.TextField(max_length="10", primary_key=True)
    nom = models.TextField(max_length="30")
    descripcio = models.TextField(max_length="100")
    web = models.URLField(blank=True)
    notes = models.TextField(help_text="Escriu una nota ", verbose_name="Notes", blank=True)
    responsable = models.ForeignKey(Usuaris,related_name='responsable_de')

    def __unicode__(self):
        return self.abrev

    class Meta:
        ordering = ["nom"]
        verbose_name_plural="Projectes"




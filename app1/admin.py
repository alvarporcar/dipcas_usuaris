from app1.models import Usuaris, Organismes, Projectes, Cursos, Carrecs, Matricula, ProfessorDeCurs, UsuarisDeProjecte
from django.contrib import admin


class UsuarisAdmin(admin.ModelAdmin):
    list_display= ('cognoms','nom', 'email1','email2','tel1','carrec','organisme','notes')
    list_filter= ('organisme','projectes','carrec','cursos')
    search_fields = ['cognoms']
    filter_horizontal = ['cursos','projectes']

class OrganismesAdmin(admin.ModelAdmin):
    list_display= ('nom', 'email1','tel1','fax1','web','notes')
    #list_filter = ('tipus')
    search_fields = ['nom']
  
class ProjectesAdmin(admin.ModelAdmin):
    list_display = ('nom','abrev','web', 'responsable','notes')
    search_fields = ['nom']

class CursosAdmin(admin.ModelAdmin):
    list_display = ('nom','pla','anny')
    list_filter = ('projecte','pla','anny')
    search_fields = ['nom']
    filter_horizontal = ['professor']
    #radio_fields = {"projecte":admin.VERTICAL}

class UsuarisDeProjecteAdmin(admin.ModelAdmin):
    list_display = ('projecte','usuari')
    list_filter = ('projecte','usuari__organisme')
    search_fields = ['usuari__cognoms','usuari__nom']

class ProfessorDeCursAdmin(admin.ModelAdmin):
	list_display = ('curs','professor')
	list_filter = ('curs__anny','curs','professor')
	search_fields = ['curs','professor']

class MatriculaAdmin(admin.ModelAdmin):
	list_display = ('alumne','curs','superat','notes')
	list_filter = ('curs__anny','curs__nom','superat')
	search_fields = ['alumne__nom','alumne__cognoms']

admin.site.register(Usuaris, UsuarisAdmin)
admin.site.register(Organismes,OrganismesAdmin)
admin.site.register(Projectes,ProjectesAdmin)
admin.site.register(Cursos,CursosAdmin)
admin.site.register(Carrecs)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(ProfessorDeCurs, ProfessorDeCursAdmin)
admin.site.register(UsuarisDeProjecte,UsuarisDeProjecteAdmin)


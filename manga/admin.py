from django.contrib import admin
from .models import Manga, Commentaire, Favories, Vue
# Register your models here.


admin.site.register(Manga)
admin.site.register(Commentaire)
admin.site.register(Favories)
admin.site.register(Vue)
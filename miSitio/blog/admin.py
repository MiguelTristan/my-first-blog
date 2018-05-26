from django.contrib import admin
from blog.models import Post

# Register your models here.
# para hacer visible el modelo en la pagina del 'admin'
admin.site.register(Post)
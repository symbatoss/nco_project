from django.contrib import admin

# Register your models here.
from nco.models import News, Laws, Posts, Favourites, Category, Photos

admin.site.register(News)
admin.site.register(Laws)
admin.site.register(Posts)
admin.site.register(Favourites)
admin.site.register(Category)
admin.site.register(Photos)



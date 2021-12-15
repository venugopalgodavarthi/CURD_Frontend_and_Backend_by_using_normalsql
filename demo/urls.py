from django.urls import path
from demo import views
app_name='demo'
urlpatterns=[  
    path("base/",views.base,name="base"),
    path("create/",views.create,name="create"),
    path('insert/',views.insert,name='insert'),
    path('select/',views.select,name='select'),
    path('update/',views.update,name='update'),
    path('update_value/',views.update_value,name='update_value'),
    path('delete_value/',views.delete_value,name='delete_value'),
    path('delete/',views.delete,name='delete'),
]
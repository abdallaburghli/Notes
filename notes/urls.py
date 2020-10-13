from django.urls import path
from . import views

urlpatterns = [
    path('',views.notes,name='notes'),
    path('addnote',views.addnote,name='addnote'),
    path('delete/<int:note_id>',views.delete,name='deleteNote'),
    path('edit/<int:note_id>',views.edit,name='editNote')
]
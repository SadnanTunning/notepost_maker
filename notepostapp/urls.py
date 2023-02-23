from django.urls import path
from .views import deleteNotepost, index, login, register, logout

urlpatterns = [
    path('', index, name="index"),
    path('delete-notepost/<int:id>/', deleteNotepost, name="deleteNotepost"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout, name="logout"),
]

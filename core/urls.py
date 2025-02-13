from django.urls import path
from . import views  # Ensure views.py is imported

urlpatterns = [
    path("", views.home, name="home"),
    path("chat/<int:problem_id>/", views.chat_room, name="chat_room"),
    path("api/active_problems/", views.active_problems, name="active_problems"),  # ✅ Add this line
]

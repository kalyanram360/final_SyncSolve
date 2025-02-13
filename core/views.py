from django.shortcuts import render


from django.http import JsonResponse
from core.consumers import active_users  # ✅ Import the active users dictionary

def home(request):
    return render(request, "core/home.html")

def chat_room(request, problem_id):
    return render(request, "core/chat.html", {"problem_id": problem_id})

from django.http import JsonResponse
from core.consumers import active_users  # ✅ Import the active users dictionary

def active_problems(request):
    """ ✅ Returns a list of active problems with active user counts """
    return JsonResponse({"active_problems": active_users})

from django.shortcuts import render
from was_practical.models import Message
# Create your views here.


def index(request):
    allMessages = Message.objects.all()
    context_dict = {}
    context_dict['messageList'] = allMessages
    print(context_dict)
    return render(request, 'index.html', context=context_dict)

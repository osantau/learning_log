from django.shortcuts import render
from .models import Topic,Entry

# Create your views here.


def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.all().order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html',context)

def topic(request, topic_id):
    """Show a topic details"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request, 'learning_logs/topic.html',context)
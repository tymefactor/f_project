from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.views import generic
from speeches.models import Speech,Speaker

# Create your views here.


def index(request):
    speeches = Speech.objects.all().order_by('published_date')
    context = {
        'speeches':speeches,
    }
    return render(request, 'speeches/index.html',context)
    paginate_by = 5

class SpeechListView(generic.ListView):
    model = Speech
    context_object_name = 'speech_list'
    queryset = Speech.objects.all()
    template_name = 'speeches/speech_list.html'
    
class SpeechDetailView(generic.DetailView):
    model = Speech
    
    def speech_detail_view(request, primary_key):
        speech = get_object_or_404(Speech, pk=primary_key)
        return render(request, 'speeches/speech_detail.html', context ={'speech': speech})

class SpeakerListView(generic.ListView):
    model = Speaker
    context_object_name = 'speaker'
    queryset = Speaker.objects.all()
    template_name = 'speakers/speaker_list.html'

class SpeakerDetailView(generic.DetailView):
    model = Speaker
    
    


from django.shortcuts import render

def home(request):
    context = {
        'video_url': '/media/videos/sample.mp4'  # Absoluter Pfad zur Videodatei
    }
    return render(request, 'home.html', context)

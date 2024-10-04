from django.shortcuts import render
from langdetect import detect, DetectorFactory

# Ensure consistent results
DetectorFactory.seed = 0

def home(request):
    detected_language = ""
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            detected_language = detect(text)
    return render(request, 'detector/home.html', {'detected_language': detected_language})
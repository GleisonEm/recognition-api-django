from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Translate
from .models import Photo
from .models import Audio
from .models import Greeting
import json
# from .models import Base64ToWavConverter

# Create your views here.


def index(request):
    return render(request, "index.html")

def sendPhoto(request):
    return render(request, "sendPhoto.html")

def sendPhotoAndView(request):
    return render(request, "sendPhotoAndView.html")

def viewTranslatePhoto(request):
    translation = translatePhoto(request)
    print(translation.split('\n'))
    return render(request, "viewTranslate.html", {"translateTexts": translation.split('\n')})

def translate(request):
    text = request.GET.get('text', '')
    translate = Translate()
    translation = translate.run(text)

    return render(request, "translate.html", {"translates": translation})

def extractText(request):
    if request.method == 'POST':
        imageFile = request.FILES.get('image')

        if imageFile:
            photo = Photo()
            text = photo.extractText(imageFile)
            text = text + "\nPlease choose the correct option below"
            print(text)
            return JsonResponse({'text': text})

        else:
            return JsonResponse({'message': 'No image file provided.'},  status=400)
    else:
        return JsonResponse({'message': "This view only accepts POST requests."}, status=500)

def save_json(request):
    if request.method == 'POST':
        try:
            # Carrega os dados do corpo da requisição
            request_data = json.loads(request.body)

            # Salva os dados em um arquivo JSON
            with open('data.json', 'w') as json_file:
                json.dump(request_data, json_file, indent=4)

            return JsonResponse({"message": "Dados salvos com sucesso."}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Erro ao decodificar JSON."}, status=400)
    else:
        return JsonResponse({"message": "Apenas requisições POST são aceitas."}, status=405)

def extractTextByAudio(request):
    if request.method == 'POST':
        audioFile = request.FILES.get('audio')
        audio = Audio()
        text = audio.extractText(audioFile)

        return JsonResponse({'text': text})

        # else:
        #     return JsonResponse({'message': 'No image file provided.'},  status=400)
    else:
        return JsonResponse({'message': "This view only accepts POST requests."}, status=500)

# def extractTextByAudio64(request):
#     if request.method == 'POST':
#         audiotext = request.POST.get('audiotext', '')
#         converter = Base64ToWavConverter(audiotext)
#         path = converter.convert('audio.opus')
#         audio = Audio()
#         print(path)
#         text = audio.extractText64(path)

#         return JsonResponse({'text': text})

#         # else:
#         #     return JsonResponse({'message': 'No image file provided.'},  status=400)
#     else:
#         return JsonResponse({'message': "This view only accepts POST requests."}, status=500)

# @csrf_exempt
def translatePhoto(request):
    if request.method == 'POST':
        imageFile = request.FILES.get('image')

        if imageFile:
            photo = Photo()
            extracted_text = photo.extractText(imageFile)
            translate = Translate()
            translation = translate.run(extracted_text)

            return translation[0].text
        else:
            return 'No image file provided.'
    else:
        return "This view only accepts POST requests."

def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

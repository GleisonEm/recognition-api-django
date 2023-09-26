from django.db import models
import requests, uuid, json
from PIL import Image
import pytesseract
import speech_recognition as sr

# class Base64ToOpusConverter:
#     def __init__(self, base64_string):
#         self.base64_string = base64_string

#     def convert(self, output_file):
#         try:
#             # Decodifique a string base64 para dados binários
#             binary_data = base64.b64decode(self.base64_string)

#             # Crie um arquivo .opus a partir dos dados binários
#             opus_data = opuslib.api.encoder_create(48000, 1, opuslib.api.OPUS_APPLICATION_AUDIO)
#             buffer = BytesIO()
#             with opuslib.api.Encoder(opus_data, 48000, 1, opuslib.api.OPUS_APPLICATION_AUDIO) as encoder:
#                 encoder.feed_pcm(binary_data)
#                 while True:
#                     opus_frame = encoder.get_opus()
#                     if not opus_frame:
#                         break
#                     buffer.write(opus_frame)

#             # Escreva os dados binários decodificados no arquivo .opus
#             with open(output_file, 'wb') as opus_file:
#                 opus_file.write(buffer.getvalue())

#             print(f"Arquivo .opus salvo como {output_file}")

#         except Exception as e:
#             print(f"Erro ao salvar o arquivo .opus: {str(e)}")

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Translation:
    def __init__(self, text, to):
        self.text = text
        self.to = to

class Translate:
    @staticmethod
    def run(text):
        key = "b85bc582c7dd499f990d204c717e064f"
        endpoint = "https://api.cognitive.microsofttranslator.com"

        location = "brazilsouth"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'from': 'en',
            'to': 'pt-br'
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': text
        }]

        try:
            response = requests.post(constructed_url, params=params, headers=headers, json=body)
            response.raise_for_status()
            result = response.json()
            print(result)
            translations = []
            for translation_data in result[0]['translations']:
                translation = Translation(text=translation_data['text'], to=translation_data['to'])
                translations.append(translation)

            return translations
        except requests.exceptions.RequestException as e:
            return [Translation(text='Error occurred', to='error')]

class Photo():
    @staticmethod
    def extractText(image):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        image = Image.open(image)
        return pytesseract.image_to_string(image)

class Audio():
    @staticmethod
    def extractText(audio_file):
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="pt-BR")
            print("Texto reconhecido: " + text)
            return text
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio")
        except sr.RequestError as e:
            print("Erro durante a requisição ao serviço de reconhecimento de fala: {0}".format(e))
    # def extractText64(source):
    #     recognizer = sr.Recognizer()
    #     audio_data = recognizer.record(source)

    #     try:
    #         text = recognizer.recognize_google(audio_data, language="pt-BR")
    #         print("Texto reconhecido: " + text)
    #         return text
    #     except sr.UnknownValueError:
    #         print("Não foi possível reconhecer o áudio")
    #     except sr.RequestError as e:
    #         print("Erro durante a requisição ao serviço de reconhecimento de fala: {0}".format(e))

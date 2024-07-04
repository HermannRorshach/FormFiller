import datetime
import hashlib
import os

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render

from .forms import IranPassportForm
from .main import main
from .models import IranPassport
from .template_creator import process_docx


class ProfileView(TemplateView):
    template_name = 'filler/profile.html'


class UploadSample(View):
    def get(self, request):
        return render(request, 'filler/upload_sample.html')

    def post(self, request):
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            fields = process_docx(uploaded_file)  # Передача загруженного файла в функцию
            print(fields)  # Вывод результата в консоль
            return HttpResponse('Файл успешно обработан')
        return HttpResponse('Файл не выбран', status=400)


def index(request):
    return redirect('filler:filler')


def get_file_hash(file_path):
    # Получаем хэш файла изображения (используем SHA256)
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def find_existing_image_path(image_hash, media_root):
    # Поиск существующего файла с заданным хэшем в папке медиа
    for root, dirs, files in os.walk(media_root):
        for filename in files:
            file_path = os.path.join(root, filename)
            if get_file_hash(file_path) == image_hash:
                return file_path
    return None


class IranPassportCreateView(CreateView):
    form_class = IranPassportForm
    template_name = 'filler/IranPassport.html'
    success_url = reverse_lazy('filler')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        image_file = self.request.FILES.get('image')
        # Создаем экземпляр IranPassport без сохранения в БД
        iran_passport_instance = IranPassport(**cleaned_data)
        cleaned_data['file_name'] = str(iran_passport_instance)
        if image_file:
            # Сохраняем загруженный файл во временное местоположение
            temp_image_path = self.save_uploaded_file(image_file)

            # Генерируем хэш файла изображения
            image_hash = get_file_hash(temp_image_path)

            # Определяем путь к файлу изображения в медиа
            date_path = datetime.datetime.now().strftime('%Y/%m/%d/')
            image_name = f'{date_path}{image_file.name}'
            image_path = os.path.join(settings.MEDIA_ROOT, image_name)

            # Проверяем, существует ли файл с таким хэшем в указанной папке
            existing_path = find_existing_image_path(image_hash, settings.MEDIA_ROOT)
            if existing_path:
                # Если найден существующий файл, используем его путь
                print('Функция во вьюхе. Найдена уже такая картинка, используем имеющуюся', existing_path)
                image_path = existing_path
            else:
                # Иначе сохраняем новый файл
                image_path = default_storage.save(image_name, ContentFile(open(temp_image_path, 'rb').read()))

            # Вызываем функцию main с очищенными данными и путем к изображению
            output_stream, file_name = main(cleaned_data, image_path=image_path)

            # Удаляем временный файл
            os.remove(temp_image_path)
        else:
            # Если изображение не загружено, вызываем main только с очищенными данными
            output_stream, file_name = main(cleaned_data)

        return FileResponse(output_stream, as_attachment=True, filename=f"{file_name}.docx")

    def save_uploaded_file(self, uploaded_file):
        # Сохраняем загруженный файл во временное местоположение на диске и возвращаем его путь
        temp_dir = os.path.join(settings.BASE_DIR, 'temp')  # Измените на BASE_DIR или другой временный путь
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_file_path, 'wb+') as temp_file:
            for chunk in uploaded_file.chunks():
                temp_file.write(chunk)
        return temp_file_path

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import IranPassportForm


def index(request):
    pass


class IranPassportCreateView(CreateView):
    form_class = IranPassportForm
    template_name = 'filler/IranPassport.html'
    success_url = reverse_lazy('filler')
    
    def get_context_data(self, **kwargs):
        print('Мы в гет контект')
        context = super().get_context_data(**kwargs)
        print('context =', context)
        return context
    
    def form_valid(self, form):
        cleaned_data = form.cleaned_data

        # Выводим данные в консоль
        print("Данные из формы:")
        print("Номер паспорта:", cleaned_data['passport_number'])
        print("Фамилия:", cleaned_data['surname'])
        print("Имя:", cleaned_data['name'])
        print("Имя отца:", cleaned_data['father_name'])
        print("Дата рождения:", cleaned_data['birthday'])
        print("Место рождения:", cleaned_data['place_of_birthday'])
        print("Пол:", cleaned_data['sex'])
        print("Дата выдачи:", cleaned_data['date_of_issue'])
        print("Действителен до:", cleaned_data['date_of_expiry'])
        print("Длинный номер:", cleaned_data['lond_number'])
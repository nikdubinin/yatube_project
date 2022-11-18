from django.shortcuts import render


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'

    context = {
        # В словарь можно передать переменную
        'title': title,
               }

    return render(request, template, context)


def group_posts(request, pk):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'

    context = {
        # В словарь можно передать переменную
        'title': title,
               }

    return render(request, template, context)

# Create your views here.

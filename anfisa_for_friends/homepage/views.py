from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Запроc-выборка с фильтрациёй
    # ==========================================
    # ice_cream_list = IceCream.objects.values(
    #     'id','title','description'
    # ).filter(
    #     is_published=True, is_on_main=True
    # ).order_by('title')[1:4]
    # ==========================================

    # JOIN c помощью метода .values()
    # возвращает список словарей, а не объектов.
    # В этом случае нужно использовать синтаксис
    # с двойным подчёркиванием, например, вот так:
    # {{ ice_cream.category__title }}.
    # ==========================================
    # ice_cream_list = IceCream.objects.values(
    #     'id', 'title', 'category__title', 'description'
    # )
    # ==========================================

    # JOIN c помощью .select_related()
    # возвращает QuerySet со списком объектов,
    # в которых содержатся все поля связанных моделей.
    # ==========================================
    # ice_cream_list = IceCream.objects.select_related(
    #     'category'
    # ).filter(
    #     category__is_published=True
    # )
    # ==========================================

    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description', 'output_order', 'category__title'
    ).filter(
        # Фильтруем выборку:
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации;
        # а сортировку можно указать в поисании самой модели
        # output_order — позиция для сортировки при выводе на страницу 
        # если порядок совпадает, то сортировать по названию.
    )

    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)

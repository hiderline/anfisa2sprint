# ice_cream/admin.py
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Topping, Wrapper


# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.

    # какие поля будут показаны на странице списка объектов
    # (свойство list_display, это кортеж);
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )

    # какие поля можно редактировать прямо на странице списка объектов
    # (свойство list_editable, кортеж);
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )

    # search_fields — кортеж с перечнем полей, по которым будет проводиться поиск.
    # Форма поиска отображается над списком элементов.
    search_fields = ('title',)

    # list_filter — кортеж с полями, по которым можно фильтровать записи.
    # Фильтры отобразятся справа от списка элементов.
    list_filter = ('is_published',)

    # В кортеже list_display_links указывают поля,
    # при клике на которые можно перейти на страницу просмотра и редактирования записи.
    # По умолчанию такой ссылкой служит первое отображаемое поле.
    list_display_links = ('title',)

    # Чтобы связанные записи можно было перекладывать из одного окошка в другое.
    filter_horizontal = ('toppings',)

    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выводиться строка "Не задано".
    # empty_value_display = 'Не задано'


# Все связанные записи на одной странице
# Интерфейс администратора можно настроить так, чтобы на странице редактирования
# определённой записи отображались связанные с ней записи другой модели.
# Например, на страницу редактирования категории можно подгрузить блок с информацией о связанных с ней сортах мороженого. 

# Такие блоки называют «вставки», для их настройки в Django есть классы admin.TabularInline и admin.StackedInline.
# Разница между этими классами заключается лишь в способе отображения связанных записей:
# TabularInline отображает поля вставки в строку, а StackedInline — столбом, одно под другим.

# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):
    model = IceCream
    # Поле extra - добавляет определённое кол-во дополнительных пустых полей ддля редактирования/создания нового объекта
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = (IceCreamInline,)
    list_display = ('title',)

# Регистрируем новый класс: 
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно использовать класс IceCreamAdmin 
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Topping)
admin.site.register(Wrapper)

# Переопределить отображение пустых полей можно и на уровне приложения.
# Тогда во всех моделях приложения пустые поля будут отображаться одинаково:
admin.site.empty_value_display = 'Не задано' 
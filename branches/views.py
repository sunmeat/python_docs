
"""Представлення Django для керування сторінками філій компанії.

Модуль містить клас Branch для зберігання інформації про філії
та функції-представлення для відображення списку філій
і сторінок окремих представництв компанії.

Філії компанії розташовані в Україні, Франції та Індії.
"""

from django.shortcuts import render, reverse


class Branch:
    """Представляє філію компанії та її основні характеристики.

    Клас використовується для формування карток філій
    на вебсайті компанії. Зберігає інформацію про
    місцезнаходження, призначення, послуги, зображення
    та посилання на сторінку філії.

    Attributes:
        city (str): Місто та країна розташування філії.
        role (str): Призначення філії в структурі компанії.
        services (list[str]): Перелік послуг філії.
        detail_url (str): URL сторінки з детальною інформацією.
        detail_text (str): Текст посилання на сторінку філії.
        image_path (str): Відносний шлях до зображення філії.

    Example:
        >>> branch = Branch(
        ...     city="Одеса, Україна",
        ...     role="Головний офіс",
        ...     services=["Логістика", "Митне оформлення"],
        ...     url_name="odesa",
        ...     detail_text="Детальніше",
        ...     image_path="img/branch-odesa.png"
        ... )
        >>> branch.city
        'Одеса, Україна'

    Note:
        Для створення detail_url використовується
        django.urls.reverse(), тому відповідне ім'я
        маршруту повинно бути визначене в urls.py.
        Приклад потребує налаштованого Django.
    """

    def __init__(
        self,
        city,
        role,
        services,
        url_name,
        detail_text,
        image_path
    ):
        """Ініціалізує об'єкт філії компанії.

        Args:
            city (str): Назва міста та країни.
            role (str): Основна роль філії.
            services (list[str]): Послуги, які надає філія.
            url_name (str): Ім'я маршруту Django для філії.
            detail_text (str): Текст посилання на сторінку.
            image_path (str): Шлях до зображення відносно
                каталогу статичних файлів.

        Raises:
            django.urls.exceptions.NoReverseMatch:
                Якщо маршрут із заданим url_name не існує.
        """
        self.city = city
        self.role = role
        self.services = services
        self.detail_url = reverse(url_name)
        self.detail_text = detail_text
        self.image_path = image_path


def branches_list(request):
    """Відображає сторінку зі списком усіх філій компанії.

    Створює колекцію об'єктів Branch для представництв
    компанії в Одесі, Орлеані та Нью-Делі.

    Передає сформований список до HTML-шаблону,
    де кожна філія відображається окремою карткою.

    Args:
        request (HttpRequest): HTTP-запит від користувача.

    Returns:
        HttpResponse: Сформована HTML-сторінка зі списком
        філій компанії.

    Note:
        Для відображення використовується шаблон
        branches_list.html.

        Контекст шаблону містить:
            - title: Заголовок сторінки.
            - branches: Список об'єктів Branch.
    """
    branches = [
        Branch(
            city="Одеса, Україна",
            role="Головний офіс та логістичний хаб",
            services=[
                "Приймання та відправка вантажів по всій Україні",
                "Митне оформлення експорт",
                "Консолідація дрібних вантажів",
                "Склад тимчасового зберігання",
            ],
            url_name="odesa",
            detail_text="Детальніше про філію в Одесі",
            image_path="img/branch-odesa.png"
        ),
        Branch(
            city="Орлеан, Франція",
            role="Представництво в ЄС",
            services=[
                "Митне оформлення імпорт до ЄС",
                "Доставка по всій Франції та країнах ЄС",
                "Розконсолідація та адресна доставка",
                "Супровід зворотних вантажів",
            ],
            url_name="orleans",
            detail_text="Детальніше про філію в Орлеані",
            image_path="img/branch-orleans.png"
        ),
        Branch(
            city="Нью-Делі, Індія",
            role="Представництво в Азії",
            services=[
                "Митне оформлення імпорт до ЄС",
                "Доставка по всій Індії та країнах ЄС",
                "Розконсолідація та адресна доставка",
                "Супровід зворотних вантажів",
            ],
            url_name="deli",
            detail_text="Детальніше про філію в Нью-Делі",
            image_path="img/deli.webp"
        )
    ]

    context = {
        'title': 'Філії',
        'branches': branches,
    }

    return render(request, 'branches_list.html', context)


def odesa(request):
    """Відображає сторінку головного офісу компанії в Одесі.

    Args:
        request (HttpRequest): HTTP-запит користувача.

    Returns:
        HttpResponse: HTML-сторінка філії в Одесі.

    Note:
        Використовує шаблон odesa.html.
    """
    return render(
        request,
        'odesa.html',
        {'title': 'Філія в Одесі'}
    )


def deli(request):
    """Відображає сторінку представництва компанії в Індії.

    Args:
        request (HttpRequest): HTTP-запит користувача.

    Returns:
        HttpResponse: HTML-сторінка філії в Нью-Делі.

    Note:
        Використовує шаблон deli.html.
    """
    return render(
        request,
        'deli.html',
        {'title': 'Філія в Індії'}
    )


def orleans(request):
    """Відображає сторінку представництва компанії у Франції.

    Args:
        request (HttpRequest): HTTP-запит користувача.

    Returns:
        HttpResponse: HTML-сторінка філії в Орлеані.

    Note:
        Використовує шаблон orleans.html.
    """
    return render(
        request,
        'orleans.html',
        {'title': 'Філія в Орлеані'}
    )

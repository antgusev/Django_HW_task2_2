from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
def rec_calc_omlet(request):
    servings_multiply = float(request.GET.get('servings', 1))
    recipe_data = {}
    for dish, ingredients in DATA.items():
        if dish == 'omlet':
            for ingredient, amount in ingredients.items():
                recipe_data.setdefault(ingredient, [])
                recipe_data[ingredient].append(amount * servings_multiply)
        else:
            continue

# В качестве контекста должен быть передан словарь с рецептом:
    context = {
      'recipe': recipe_data
    }
# Результат - 
    return render(request, 'calculator/index.html', context)


def rec_calc_pasta(request):
    servings_multiply = float(request.GET.get('servings', 1))
    recipe_data = {}
    for dish, ingredients in DATA.items():
        if dish == 'pasta':
            for ingredient, amount in ingredients.items():
                recipe_data.setdefault(ingredient, [])
                recipe_data[ingredient].append(amount * servings_multiply)
        else:
            continue

# В качестве контекста должен быть передан словарь с рецептом:
    context = {
      'recipe': recipe_data
    }
# Результат - 
    return render(request, 'calculator/index.html', context)


def rec_calc_buter(request):
    servings_multiply = float(request.GET.get('servings', 1))
    recipe_data = {}
    for dish, ingredients in DATA.items():
        if dish == 'buter':
            for ingredient, amount in ingredients.items():
                recipe_data.setdefault(ingredient, [])
                recipe_data[ingredient].append(amount * servings_multiply)
        else:
            continue

# В качестве контекста должен быть передан словарь с рецептом:
    context = {
      'recipe': recipe_data
    }
# Результат - 
    return render(request, 'calculator/index.html', context)

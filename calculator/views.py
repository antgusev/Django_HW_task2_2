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
def rec_calc(request):
    recipe = request.GET.get("recipe")
    servings = request.GET.get("servings", 1)
    recipe_resp = DATA[recipe]
    recipe_resp.update((key, value * servings) for key, value in recipe_resp.items())
    # for ingredient, amount in recipe.items

# В качестве контекста должен быть передан словарь с рецептом:
    context = {
      'recipe': recipe_resp
    }
# Результат - 
    return render(request, 'calculator/index.html', context)
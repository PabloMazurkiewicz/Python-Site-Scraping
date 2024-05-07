def number_range(number):
    start = (number - 1) * 20 + 1
    end = start + 19
    return start - 1, end - 1

def select_emoji(category: str):
    categories =  {
        'electro': "🔌",
        'hogar y textil': "🪑",
        'tempo libre': "🏡",
        'bebes y ninos': "👶",
        'almacen': "🥫",
        'bebidas': "🍷",
        'frutas y verduras': "🥕",
        'carnes': "🥩",
        'lácteos': "🥛",
        'quesos y fiambres': "🧀",
        'congelados': "❄️",
        'panadería y repostería': "🥖",
        'comidas preparadas': "🍽",
        'perfumeria': "🧴"
        }
    
    return categories[category.lower()]
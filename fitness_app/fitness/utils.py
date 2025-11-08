from rapidfuzz import fuzz


class FitnessMixin:

    def get_mixin_context(self, context, **kwargs):
        context['selected_menu'] = 'Workout'
        context.update(kwargs)
        return context

    # fitness/utils.py
def compare_programs(a, b, criteria):
    """Порівняння двох програм за заданими критеріями"""
    better, worse = False, False

    for field, direction in criteria.items():
        va, vb = getattr(a, field), getattr(b, field)

        # Обробка текстових критеріїв як впорядкованих рівнів
        order = {
            'difficulty': {'beginner': 1, 'intermediate': 2, 'advanced': 3},
            'duration': {'short': 1, 'medium': 2, 'long': 3}
        }

        # Перетворення текстових полів у числові для порівняння
        if field in order:
            va, vb = order[field].get(va, 0), order[field].get(vb, 0)

        if va == vb:
            continue

        if direction == "min":
            if va < vb:
                better = True
            else:
                worse = True
        elif direction == "max":
            if va > vb:
                better = True
            else:
                worse = True

    if better and not worse:
        return "dominates"
    elif worse and not better:
        return "dominated"
    else:
        return "incomparable"


def apply_skyline_filter(qs, criteria):
    """Вибирає недоміновані програми"""
    skyline = []

    for obj in qs:
        dominated = False
        for other in skyline.copy():
            result = compare_programs(obj, other, criteria)
            if result == "dominated":
                dominated = True
                break
            elif result == "dominates":
                skyline.remove(other)
        if not dominated:
            skyline.append(obj)

    return skyline





FUZZY_KEYWORDS = {
    # запит → ступені належності до категорій
    "beginner":     {"beginner": 1.0, "intermediate": 0.6, "advanced": 0.2},
    "intermediate": {"beginner": 0.5, "intermediate": 1.0, "advanced": 0.5},
    "advanced":     {"beginner": 0.2, "intermediate": 0.6, "advanced": 1.0},

    "low":      {"short": 1.0, "medium": 0.7, "long": 0.3},
    "moderate": {"short": 0.6, "medium": 1.0, "long": 0.6},
    "high":     {"short": 0.3, "medium": 0.7, "long": 1.0},
}

def parse_fuzzy_query(query: str):
    query = query.lower()
    fuzzy_weights = {}

    for keyword, mapping in FUZZY_KEYWORDS.items():
        if fuzz.partial_ratio(keyword, query) > 70:
            # додаємо/оновлюємо ваги
            for k, v in mapping.items():
                fuzzy_weights[k] = max(fuzzy_weights.get(k, 0), v)

    return fuzzy_weights
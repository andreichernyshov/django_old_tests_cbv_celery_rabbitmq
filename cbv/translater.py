trantab = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
                'д': 'd', 'е': 'e', 'ё': 'e', 'з': 'z', 'и': 'i',
                'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
                'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
                'ф': 'f', 'х': 'h', 'ц': 'c', 'э': 'e', 'ь': '`',
                'ы': 'ui', 'ъ': '`', 'ю': 'yu', 'я': 'ya', 'ж': 'zh',
                'ч': 'ch', 'ш': 'sh', 'щ': 'shch', ' ': ' ', 'і': 'i',
                'ї': 'y', 'й': 'iy', 'к': 'k', 'є': 'е'}


def city_name_to_eng(text: str):
    text = text.lower()
    tab_city = text.maketrans(trantab)
    return text.translate(tab_city)


def prof_name_to_eng(text: str):
    text = text.lower()
    tab_prof = text.maketrans(trantab)
    return text.translate(tab_prof)


def comp_name_to_eng(text: str):
    text = text.lower()
    tab_comp = text.maketrans(trantab)
    return text.translate(tab_comp)

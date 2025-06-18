from jinja2 import Environment, FileSystemLoader, select_autoescape

import random
import os


def create_card(races, classes):
    clases_base = {
        'Волшебник': {
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': 15,
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'skills': [
                'Стрела ледяного огня',
                'Снятие проклятия',
                'Огненный взрыв',
                'Обледенение',
                'Ледяное копье',
                'Конус холода',
                'Прилив сил',
                'Морозный доспех'
            ],
            'img': 'images/wizard.png',
        },
        'Воин': {
            'strength': 15,
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'skills': [
                'Блок щитом',
                'Казнь',
                'Рывок',
                'Боевой крик',
                'Вихрь',
                'Парирование',
                'Мощный удар',
                'Глубокие раны'
            ],
            'img': 'images/warrior.png',
        },
        'Бард': {
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': 15,
            'skills': [
                'Аккорды ветра',
                'Аккорды воды',
                'Исцеление',
                'Соната жизни',
                'Пауза',
                'Плач сирен',
                'Песнь ветра',
                'Реквием'
            ],
            'img': 'images/bard.webp',
        },
        'Ассасин': {
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': 15,
            'temper': random.randint(1, 3),
            'skills': [
                'Отравление',
                'Взлом замка',
                'Подлый трюк',
                'Исчезновение',
                'Ложный выпад',
                'Внезапный удар',
                'Ошеломление',
                'Спринт'
            ],
            'img': 'images/assasin.png',
        },
        'Лучник': {
            'strength': random.randint(1, 3),
            'agility': 15,
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'skills': [
                'Верный выстрел',
                'Чародейский выстрел',
                'Стенающая стрела',
                'Стрелы ветра',
                'Призыв питомца',
                'Глаз зверя',
                'Осветительная ракета',
                'Приручение животного'
            ],
            'img': 'images/archer.png',
        },
    }

    character_name = input('Введите имя персонажа: ').capitalize()
    character_race = races[int(input(f'Введите номер расы от 1 до {len(races)}(расы: {races}): '))-1]
    character_class = classes[(int(input(f'Введите номер класса от 1 до {len(classes)}(классы: {classes}): ')))-1]
    skills = random.sample(clases_base[character_class]['skills'], 3)

    character_date = {
        'name': character_name,
        'race': character_race,
        'class': character_class,
        'skills': skills
    }

    return character_date, clases_base


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    races = [
        'Орк',
        'Хоббит',
        'Эльф',
        'Гном'
    ]
    classes = [
        'Волшебник',
        'Воин',
        'Бард',
        'Ассасин',
        'Лучник'
    ]
    dir_name = 'characters'

    os.makedirs(dir_name, exist_ok=True)

    quantity_cards = int(input("Сколько карточек нужно создать: "))

    for num in range(0, quantity_cards):
        character, clases_base = create_card(template, races, classes)
        character_class = character['class']
        rendered_page = template.render(
            name = character['name'],
            race = character['race'],
            character_class = character_class,
            image = clases_base[character_class]['img'],
            strength = clases_base[character_class]['strength'],
            agility = clases_base[character_class]['agility'],
            intelligence = clases_base[character_class]['intelligence'],
            luck = clases_base[character_class]['luck'],
            temper = clases_base[character_class]['temper'],
            first_skill = character['skills'][0],
            second_skill = character['skills'][1],
            third_skill = character['skills'][2],
        )
        with open(f'{dir_name}/index_{num+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == "main":
    main()
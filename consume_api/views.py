from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.template import loader
from PIL import Image

# Create your views here.


def main_page(request):
    response_breaking = requests.get(
        'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/?series=Breaking+Bad'
    )
    response = response_breaking.json()
    temporadas_breaking = list()
    for resp in response:
        temporada = resp['season']
        if temporada not in temporadas_breaking:
            temporadas_breaking.append(temporada)
    temporadas_breaking.sort()

    response_seul = requests.get(
      '  https://tarea-1-breaking-bad.herokuapp.com/api/episodes/?series=Better+Call+Saul'
    )
    response = response_seul.json()
    temporadas_saul = list()
    for resp in response:
        temporada = resp['season']
        if temporada not in temporadas_saul:
            temporadas_saul.append(temporada)
    temporadas_saul.sort()
    context = {
        'temporadas_breaking': temporadas_breaking,
        'temporadas_saul': temporadas_saul
    }

    return render(request, 'consume_api/home.html', context)


def breakin_seasons(request):
    response_breaking = requests.get(
        'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/?series=Breaking+Bad'
    )
    response = response_breaking.json()
    temporadas = list()
    for resp in response:
        temporada = resp['season']
        if temporada not in temporadas:
            temporadas.append(temporada)
    temporadas.sort()
    context = {
        'response': response,
        'temporadas': temporadas
    }
    return render(request, 'consume_api/seasons.html', context)


def seul_seasons(request):
    response_seul = requests.get(
      '  https://tarea-1-breaking-bad.herokuapp.com/api/episodes/?series=Better+Call+Saul'
    )
    response = response_seul.json()
    temporadas = list()
    for resp in response:
        temporada = resp['season']
        print(temporada)
        if temporada not in temporadas:
            temporadas.append(temporada)
    temporadas.sort()
    context = {
        'response': response,
        'temporadas': temporadas
    }
    return render(request, 'consume_api/seasons.html', context)


def breaking_episodes(request, season):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad'
    response = requests.get(url)
    response = response.json()
    content = list()
    for r in response:     
        if r['season'] == season:
            content.append(r)

    context = {
        'content': content
    }
    return render(request, 'consume_api/episodes.html', context)


def seul_episodes(request, season):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul'
    response = requests.get(url)
    response = response.json()
    content = list()
    for r in response:     
        if r['season'] == season:
            content.append(r)

    context = {
        'content': content
    }
    return render(request, 'consume_api/episodes.html', context)


def get_character(request, id):
    url = f'https://tarea-1-breaking-bad.herokuapp.com/api/characters/{id}'
    character_details = requests.get(url)
    character_details = character_details.json()[0]
    name = character_details['name']
    name = name.replace(' ', '+')
    url_quote = f'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={name}'
    character_quotes = requests.get(url_quote)
    character_quotes = character_quotes.json()
    context = {
        'name': character_details['name'],
        'occupation': character_details['occupation'],
        'status': character_details['status'],
        'nickname': character_details['nickname'],
        'appearance': character_details['appearance'],
        'portrayed': character_details['portrayed'],
        'category': character_details['category'],
        'better_call_saul_appearance': character_details['better_call_saul_appearance'],
        'quotes': character_quotes,
        'img': character_details['img']
    }
    return render(request, 'consume_api/character.html', context)


def get_episode(request, id):
    url = f'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/{id}'
    episode_detail = requests.get(url)
    episode_detail = episode_detail.json()[0]
    phone_book = dict()
    for personaje in episode_detail['characters']:
        name = personaje.replace(' ', '+')
        url_personaje = f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={name}'
        personaje = requests.get(url_personaje)
        personaje = personaje.json()[0]
        phone_book[personaje['char_id']] = personaje['name']
    context = {
        'title': episode_detail['title'],
        'season': episode_detail['season'],
        'air_date': episode_detail['air_date'],
        'characters': episode_detail['characters'],
        'episode': episode_detail['episode'],
        'series': episode_detail['series'],
        'phone_book': phone_book
    }
    return render(request, 'consume_api/episode_detail.html', context)


def search_character(request):
    search = request.GET['query']
    search = search.replace(' ', '+')
    url = f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={search}'
    characters = requests.get(url)
    characters = characters.json()
    personajes = list()
    for character in characters:
        personajes.append(character)

    context = {
        'personajes': personajes
    }
    return render(request, 'consume_api/search.html', context)

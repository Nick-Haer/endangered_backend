from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

from django.http import HttpResponse

from .models import Animal

from django.http import JsonResponse
from django.core import serializers


def index(request):
    return HttpResponse("Server for Endangered")


def getAllAnimals(request):
    animals = list(Animal.objects.values())
    return JsonResponse({"data": animals})


def getWikiData():
    animals = Animal.objects.all()

    for animal in animals:
        wikiReadyAnimalName = animal.name.capitalize().replace(" ", "_")
        wikiUrl = "https://en.wikipedia.org/w/api.php?action=query&format=json&titles={}&prop=pageimages|extracts&format=json&pithumbsize=100&exsentences=10&exlimit=1&explaintext=1".format(
            wikiReadyAnimalName)
        wikiPage = requests.get(wikiUrl).json()
        print(wikiPage['query']["pages"])
        if (type(wikiPage['query']["pages"]) is dict):
            if ('thumbnail' in list(wikiPage['query']["pages"].values())[0]):

                print(list(wikiPage['query']["pages"].values())[
                    0]["thumbnail"]["source"])

                animal.image_url = list(wikiPage['query']["pages"].values())[
                    0]["thumbnail"]["source"]
            if ('extract' in list(wikiPage['query']["pages"].values())[0]):

                print(list(wikiPage['query']["pages"].values())[
                    0]["extract"])

                animal.description = list(wikiPage['query']["pages"].values())[
                    0]["extract"]
            animal.save()
            print(animal.description)


def getMatchingCharities():
    queryString = "https://api.data.charitynavigator.org/v2/Organizations?app_id=d7b095ba&app_key=9f6820071629919514265b3843172891"
    PARAMS = {'app_id': "d7b095ba",
              "app_key": "9f6820071629919514265b3843172891"}
    charities = requests.get(queryString, PARAMS)


def getWWFAnimalsData():
    page = requests.get(
        'https://www.worldwildlife.org/species/directory')

    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.table

    rows = table.find_all("tr")

    for row in rows:
        name = row.a.contents[0]
        latin_name = ''
        status = ''

        if (row.find("em") and len(row.find("em")) != 0):
            latin_name = row.em.contents[0]
        else:
            latin_name = "none"

        tableCellsFound = (row.find_all("td") and len(row.find_all("td")) != 0)

        if (tableCellsFound and row.find_all("td")[2].text):
            status = row.find_all("td")[2].text
        else:
            status = "none"

        print(bool(status))

        a = Animal(name=name, latin_name=latin_name, status=status)
        a.save()
        print(a.id)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

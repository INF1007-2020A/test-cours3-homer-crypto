#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    # TODO completer la fonction
    mots_miniscules = ['and']
    for i in range(capitalized_words):
        test_str = test_str.replace(capitalized_words[i],capitalized_words[i].capitalize())
    return nom


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    # TODO completer la fonction
    mots_miniscules = ['and']
    nom.capitalize()
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

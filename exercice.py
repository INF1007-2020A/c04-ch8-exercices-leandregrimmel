#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75],
                        "F": [0, 70]}
from os import path
import pickle
from recettes import add_recipes, print_recipe


# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def exercice1(file1, file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        for index, line1 in enumerate(f1):
            line2 = f2.readline()

            if line1 != line2:
                print(f"les fichiers sont différents! À la ligne {index + 1}, on a:")
                print(line1)
                print("Et on a:")
                print(line2)


def exercice2(input_file, output_file):
    with open(input_file, encoding="utf-8") as in_file, open(output_file, 'w', encoding="utf-8") as out_file:
        for line in in_file:
            out_file.write(line.replace(" ", "   "))


def exercice3(file_path, result_file_path):
    with open(file_path, encoding="utf-8") as f:
        note_percent = f.read().splitlines()

    with open(result_file_path, 'w', encoding="utf-8") as f:
        for note in note_percent:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] <= int(note) < value[1]:
                    f.write(note + "\t" + key + "\n")
                    break


def delete_recipe(recipes):
    name = input("Entrez le nom de la recette que vous voulez supprimer. \n")
    if name in recipes:
        del recipes[name]
        print("La recette est supprimée!. \n")
    else:
        print("Cette recette n'existe pas.\n")

    return recipes


def exercice4(file_path="./recipe.p"):
    if path.exists(file_path):
        recipes = pickle.load(open(file_path, "rb"))
    else:
        recipes = dict()
    while True:
        choice = input(
            "Choisissez une opiton: \n a) Ajouter une recette \n b) Modifier une recette \n c) Supprimer une recette "
            "\n d) Afficher une recette \n e) Quitter le programme \n").strip()
        if choice == 'a':
            recipes = add_recipes(recipes)
        elif choice == "b":
            recipes = add_recipes(recipes)
        elif choice == "c":
            recipes = delete_recipe(recipes)
        elif choice == "d":
            print_recipe(recipes)
        elif choice == "e":
            break
        else:
            print("Le choix n'est pas valide")

    pickle.dump(recipes, open(file_path, "wb"))


if __name__ == '__main__':
    # TODO: Appelez vos
    #  fonctions ici
    # exercice1("./exemple.txt", "./exemple2.txt")
    # exercice2("./exemple.txt", "./exemple_copy.txt")
    # exercice3("./notes.txt", "./notes_lettre.txt")
    exercice4()

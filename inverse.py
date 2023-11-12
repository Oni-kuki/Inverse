# Fonction pour inverser les lignes d'un fichier
def inverser_lignes(fichier_entree, fichier_sortie):
    try:
        # Lecture du fichier d'entrée
        with open(fichier_entree, 'r') as f_entree:
            lignes = f_entree.readlines()

        # Inversion de l'ordre des lignes
        lignes_inversees = reversed(lignes)

        # Écriture du résultat dans le fichier de sortie
        with open(fichier_sortie, 'w') as f_sortie:
            f_sortie.writelines(lignes_inversees)

        print("Inversion des lignes terminée avec succès.")

    except FileNotFoundError:
        print("Le fichier d'entrée spécifié n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
fichier_entree = 'photo.png'  # Remplacez cela par le chemin de votre fichier
fichier_sortie = 'fichier_inverse.png'

inverser_lignes(fichier_entree, fichier_sortie)

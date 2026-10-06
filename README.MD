
```markdown
# Convertisseur de Nombres en Lettres

Un outil en ligne de commande écrit en Python qui lit un fichier texte, identifie tous les nombres entiers et ajoute automatiquement leur traduction en toutes lettres juste à côté.

Le script a été conçu pour être **sûr** : il ne modifie jamais le fichier d'origine, mais génère un nouveau fichier avec le suffixe `_traduit`.

##  Fonctionnalités
- Détection automatique des nombres via des expressions régulières (Regex).
- Conversion des nombres en lettres (géré par le module `convert_number_sting.py`).
- Gestion de l'encodage UTF-8.
- Création d'un fichier de sortie sécurisé (aucun écrasement de données).


##   Prérequis
- Python 3.10 doit être installé sur votre machine.

## 🛠️ Installation
1. Clonez ce dépôt sur votre machine :
   ```bash
   git clone https://github.com/zymel-prog/convertisseur_lettres.git
```

2. Accédez au dossier du projet :
   ```bash
   cd convertisseur_lettres
   ```

(Aucune dépendance externe n'est requise, le script utilise uniquement les bibliothèques standard de Python).

🚀 Utilisation

Ouvrez un terminal (CMD, PowerShell ou Bash) dans le dossier du projet et exécutez la commande suivante :

```bash
python main.py "chemin_vers_votre_fichier.txt"
```

Exemple concret :

```bash
python main.py "C:\Users\Documents\convertisseur_lettres\text.txt"
```

📝 Résultat attendu

Si votre fichier source text.txt contient :

J'ai 25 pommes et 35 poires.

Le script générera un nouveau fichier text_traduit.txt contenant :

J'ai 25 (vingt-cinq) pommes et 35 (trente cinq) poires.

📁 Structure du projet

· main.py : Le script principal qui lit le fichier, trouve les nombres et gère les entrées/sorties.
· convert_number_sting.py : Le module contenant la logique de conversion des nombres en lettres.
· .gitignore : Fichier de configuration Git pour ignorer les fichiers inutiles (caches, environnements virtuels, etc.).

👤 Auteur : zymel-prog

📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

```




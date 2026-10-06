import os
import sys
import re
import convert_number_sting as CL


 
if len(sys.argv) <2:
    print("Utilisation : " \
    "python de convret and replace number.py "
    "< chemin_du_fichier>")

    sys.exit()

chemin = sys.argv[1]

# duplication du fichier
nom_base, extension = os.path.splitext(chemin)
chemin_sortie = nom_base + "_traduit" + extension

#fichier source ouvert en lecture et fichier de sortie en ecriture
with open(chemin, encoding = 'utf-8') as f, open(chemin_sortie, "w", encoding='utf-8') as f_out:
    for line in f:
        nombre = re.findall(r"[-+]?\d+(?:[.,]\d+)?", line)
        if nombre :
            resultat = line
            for i in nombre :
                resort = CL.convert(i)
                chaine_nombre = " ".join(resort)

                resultat = resultat.replace(i, 
                                            i + " (" + chaine_nombre +") ", 
                                            1
                                            )

            f_out.write(resultat)
        else :
            f_out.write(line)

print(f" Termié ! Le resultat enregistré dans :{chemin_sortie} ")


            
chiffres = {0:'zero',1:'un',2:'deux',3:'trois',4:'quatre',5:'cinq',6:'six',7:'sept',8:'huit',9:'neuf',10:'dix'}
vingtaine = {11:'onze',12:'douze',13:'treize',14:'quatorze',15:'quinze',16:'seize',17:'dix sept',18:'dix huit',19:'dix neuf',10:'dix'}
vingtaine_special = {1:'onze',2:'douze',3:'treize',4:'quatorze',5:'quinze',6:'seize',7:'dix sept',8:'dix huit',9:'dix neuf'}
dizaines = {2:'vingt',3:'trente',4:'quarante',5:'cinquante',6:'soixante',7:'soixante',8:'quatre vingt',9:'quatre vingt',0:""}


def taille_1(d):
    result = []
    if d == '0':
        result.append(chiffres[0])
    else:
        result.append(chiffres[int(d[0])])
    
    return result

    
def taille_2(d):
    result = []
    if d == '00':
        return result
    if d[0] in ['2','3','4','5','6','8']:
      result.append(dizaines[int(d[0])])
      if d[1] == '0':
        return result
      
      result.append(chiffres[int(d[1])])
      
          # cas des 70,,, et 90,,,
    elif d[0] in ['7','9']:
      result.append(dizaines[int(d[0])])
      if d[1] == '0':
        result.append('dix')
        return result
      else:
        result.append(vingtaine_special[int(d[1])])
        return result
      
    elif d[0] == '1':
      if d[1] == '0':
        result.append(chiffres[10])
        
      else:
        result.append(vingtaine[int(d)])
        
    else :
           result.append(vingtaine[int(d)])
           
    return result

def taille_3(d):
    result = []
    if d == '000':
        return result

    if d[0] == '1':
        result.append('cent')
        if d[1] == '0':
            if d[2] != '0':
                result.append(chiffres[int(d[2])])
            return result
        # cas où la dizaine est 1 (ex: 111 -> 'cent onze')
        if d[1] == '1':
            # d[1:] vaut '10'..'19' -> utiliser la table vingtaine
            result.append(vingtaine[int(d[1:])])
            return result
        if d[1] in ['7','9']:
            result.append(dizaines[int(d[1])])
            if d[2] == '0':
                result.append('dix')
            else:
                result.append(vingtaine_special[int(d[2])])
        else :
           result.append(dizaines[int(d[1])])
           if d[2] != '0':
               result.append(chiffres[int(d[2])])
    else:
        result.append(chiffres[int(d[0])])
        result.append('cent')
        if d[1] == '0':
            if d[2] != '0':
                result.append(chiffres[int(d[2])])
            return result
         # cas particulier
        if d[1] in ['7','9']:
            result.append(dizaines[int(d[1])])
      
            # gestion des cas 70 et 90 
            if d[2] == '0':
                result.append('dix')
      
              # gestion des cas restant
            else:
                  result.append(vingtaine_special[int(d[2])])
        elif d[1] in ['1']:
            if d[2] == '0':
                result.append('dix')
            else:
                result.append(vingtaine_special[int(d[2])])
      
        else :
            result.append(dizaines[int(d[1])])
            if d[2] != '0':
                result.append(chiffres[int(d[2])])
   
    return result

def millier(d):
    result = []

    if len(d) == 4:
        if d[0] == '1' and d[1:] == '000':
            result.append('mille')
        else:
            if d[0] == '1':
                result.append('mille')
            else:
                result.append(chiffres[int(d[0])])
            result.append('mille')
            de = d[1:]
            if de != '000':
                r = taille_3(de)
                result.extend(r)

    if len(d) == 5:
        d1 = d[0:2]
        d2 = taille_2(d1)
        result.extend(d2)
        if d[2:] == '000':
            return result + ['mille']
        result.append('mille')
        de = d[2:]
        if de != '000':
            r = taille_3(de)
            result.extend(r)

    if len(d) == 6:
        d1 = d[0:3]
        d2 = taille_3(d1)
        result.extend(d2)
        if d[3:] == '000':
            return result + ['mille']
        result.append('mille')
        de = d[3:]
        if de != '000':
            r = taille_3(de)
            result.extend(r)
    return result


#d=input("entrer un nombre et nous le traduirons en lettres : ")
results=[]
def convert(d):
    match len(d):
        case 1:
            results = taille_1(d)
            return results

        case 2:
            results = taille_2(d)
            return results

        case 3:
            results = taille_3(d)
            return results

        case 4 | 5 | 6:
            results = millier(d)
            return results

    

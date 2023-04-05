# Un premier algorithme naif de recherche textuelle


def correspondance(texte, motif, p, i):
    ...
    return (True, decalage)


def rechercher_motif(texte, motif):
    ''' fonction qui renvoie le nombre d'occurences de la
        chaine "cle" dans la  chaine "texte"
        texte : str
        cle : str
    '''
    nb_occur = 0
    ...
    return nb_occur



texte = 'abracadabra'
motif_1 = 'bra'
motif_2 = 'bac'
motif_3 = 'abracadabra'
motif_4 = 'abracadabracadabra'

assert(rechercher_motif(texte, motif_1) == 2)
assert(rechercher_motif(texte, motif_2) == 0)
assert(rechercher_motif(texte, motif_3) == 1)
assert(rechercher_motif(texte, motif_4) == -1)
print("Tests réalisés avec succès !")
print()

print("Recherche d'un triplet de bases azotées dans un brin d'ADN :")
    
brin = "CAAGCGCACAAGACGCGGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTTGCTGTATGTTCCATGGTGGCCAATCCGTCTCTTTTCGACAGCACGGCCAATTCTCCTAGGAAGCCAGCTCAATTTCAACGAAGTCGGCTGTTGAACAGCGAGGTATGGCGTCGGTGGCTCTATTAGTGGTGAGCGAATTGAAATTCGGTGGCCTTACTTGTACCACAGCGATCCCTTCCCACCATTCTTATGCGTCGTCTGTTACCTGGCTTGGCAT"
triplet = "ACG"

print(rechercher_motif(brin, triplet))
print()

print("Recherche d'un mot dans le roman de Stendhal :")

fichier = open('Le_rouge_et_le_noir.txt','r', encoding="utf-8")
stendhal = fichier.read()
fichier.close()
mot = "Julien"

print(rechercher_motif(stendhal, mot))

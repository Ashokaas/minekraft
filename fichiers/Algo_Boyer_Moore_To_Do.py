# Une mise en oeuvre de l'algorithme de Boyer-Moore
# dans la version simplifiée de Horspool


def remplir_table_decalage(motif, p, dico_deca):
    # remplit (partiellement) un dictionnaire pour donner
    # les positions les plus à droite de chaque caractère
    # présents dans le motif
    ...

        
def calculer_decalage(c, dico_deca):
    # renvoie -1 si c n'est pas dans le motif ou sinon aDroite[c]
    ...
    

def correspondance(texte, motif, p, i, dico_deca):
    ...
    return (True, 1)


def rechercher_motif_BM(texte, motif):
    ''' fonction qui renvoie le nombre d'occurences de la
        chaine "cle" dans la  chaine "texte" en utilisant
        l'algorithme de Boyer-Moore
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

assert(rechercher_motif_BM(texte, motif_1) == 2)
assert(rechercher_motif_BM(texte, motif_2) == 0)
assert(rechercher_motif_BM(texte, motif_3) == 1)
assert(rechercher_motif_BM(texte, motif_4) == -1)
print("Tests réalisés avec succès !")
print()

print("Recherche d'un triplet de bases azotées dans un brin d'ADN :")
    
brin = "CAAGCGCACAAGACGCGGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTTGCTGTATGTTCCATGGTGGCCAATCCGTCTCTTTTCGACAGCACGGCCAATTCTCCTAGGAAGCCAGCTCAATTTCAACGAAGTCGGCTGTTGAACAGCGAGGTATGGCGTCGGTGGCTCTATTAGTGGTGAGCGAATTGAAATTCGGTGGCCTTACTTGTACCACAGCGATCCCTTCCCACCATTCTTATGCGTCGTCTGTTACCTGGCTTGGCAT"
triplet = "ACG"

print(rechercher_motif_BM(brin, triplet))
print()

print("Recherche d'un mot dans le roman de Stendhal :")

fichier = open('Le_rouge_et_le_noir.txt','r', encoding="utf-8")
stendhal = fichier.read()
fichier.close()
mot = "Julien"

print(rechercher_motif_BM(stendhal, mot))

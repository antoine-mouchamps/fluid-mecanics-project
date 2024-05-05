Ce dossier contient:
    - les simulations effectuées (steady & transient) pour l'étude préliminaire (sous NX22)
    - les simulations effectuées pour les 4 régimes d'écoulement considérés (un pour chaque Re)
      pour l'étude détaillée (NX18)

Pour les simulations de l'étude détaillée, les différents AR sont traités en changeant le paramètre
du même nom dans les expressions du fichier .prt, et en updatant le .fem. Interchanger les AR entre
0.25, 0.5, 1 ne pose aucun problème mais, en mettant AR=0 NX supprime (sans raison) 4 mesh sur 
les 14 ainsi que 2 mesh controls, qu'il est donc nécessaire de refaire. A cause des mesh supprimés, 
certaines conditions limites (au niveau de l'obstacle) doivent également être remises (AR=0 est le seul
à poser ce problème). 

Comme expliqué dans le rapport, selon le AR choisit, nous avons adapté certains mesh control afin 
d'ajouter plus d'éléments sur les côtés qui s'allongent, et ainsi maintenir la même taille d'éléments.

# SAÉ Graphes-IHM : Optimisation des parcours en supermarché

> **EN:** BUT1 project — two Python GUI apps to lay out supermarket products on a floor plan and compute optimal shopping paths.  
> **FR:** Projet BUT1 — deux applications Python pour positionner des produits en magasin et calculer un parcours de courses optimal.

Ce projet a été développé dans le cadre de la SAÉ IHM du BUT1 Informatique à l'IUT du Littoral Côte d'Opale.

## Contexte

L'objectif de ce projet est de créer deux applications permettant d'optimiser les parcours dans un supermarché. La première application permet de positionner les produits sur un plan de magasin, tandis que la seconde calcule le chemin optimal pour collecter une liste de courses.

## Équipe de développement

**Groupe 16**
- **Application 1** : Marwa Kime (Mapbaya), Frédéric Gobfert (Karadoc)
- **Application 2** : Neda Khelifi, Mathys Levitre

**Encadrement** : L. Conoir (responsable), R. Cozot, J. Hermilier

## Fonctionnalités développées

### Application 1 : Positionnement des produits (Terminée)

Cette application permet de créer et gérer des projets de positionnement de produits dans un magasin.

**Fonctionnalités principales :**
- Création et gestion complète des projets (création, ouverture, suppression)
- Chargement et affichage de plans de magasin
- Système de quadrillage paramétrable
- Positionnement des produits avec respect des contraintes métier (rayons, limite par case)
- Sauvegarde automatique des configurations
- Interface avec zoom et navigation intuitive

**Fonctionnalités avancées implémentées :**
- Contraintes de rayonnage (les produits ne peuvent être placés que dans leur rayon correspondant)
- Limitation à 5 produits maximum par case
- Barre d'état avec raccourcis d'accès rapide
- Gestion d'erreurs avec notifications utilisateur
- Notice d'utilisation intégrée

### Application 2 : Calcul de parcours optimal (App2)

Application de liste de courses avec calcul de parcours (`App2/`). Lancement :

```bash
python App2/mainApp2.py
```

## Architecture technique

Le projet respecte l'architecture MVC (Modèle-Vue-Contrôleur) imposée dans les consignes. Nous utilisons exclusivement les bibliothèques autorisées des modules R2-02 et R2-07.

**Technologies utilisées :**
- Python
- Format JSON pour la persistence des données
- Git pour le versioning avec branches dédiées (`appli_1MF`, `appli_2NM`)

## Installation et utilisation

### Prérequis
- Python 3.x
- Bibliothèques des modules R2-02 et R2-07

### Lancement

**Application 1** (positionnement des produits) :

```bash
git clone https://github.com/Mapbaya/magasin_projet_ihm.git
cd magasin_projet_ihm
python App1/main.py
```

**Application 2** (liste de courses et parcours) :

```bash
python App2/mainApp2.py
```

L'application 1 dispose d'une notice d'utilisation intégrée accessible depuis l'interface.


## Tests et validation

L'application 1 a été testée avec :
- Listes de produits variées (minimum 20 produits comme spécifié)
- Scénarios d'erreur utilisateur
- Tests de performance sur le système de sauvegarde

## Livrables

- Code source complet de l'application 1 (commenté et documenté)
- Code source de l'application 2
- Plans de magasin utilisés pour les tests
- Exemples de projets créés avec l'application
- Notice d'utilisation intégrée à l'application

## État d'avancement

**Application 1** : ✅ Terminée et validée
- Toutes les fonctionnalités requises implémentées
- Fonctionnalités bonus ajoutées
- Tests effectués et validés

**Application 2** : ✅ Livrable (liste de courses, algorithme de parcours)
- Code dans `App2/`
- Améliorations possibles (voir `suiviTravail.md`)

## Notes techniques

### Choix d'implémentation
- Utilisation du format JSON pour la flexibilité et la lisibilité
- Architecture MVC strictement respectée pour la maintenabilité
- Interface graphique optimisée pour l'utilisabilité

### Contraintes respectées
- Limitation aux bibliothèques autorisées
- Architecture MVC imposée
- Sauvegarde des projets selon le format spécifié

---

**Projet réalisé dans le cadre du BUT Informatique - IUT du Littoral Côte d'Opale**  
**Année universitaire 2024-2025**

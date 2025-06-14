"""
Module de gestion des projets de magasin.

Ce module gère les opérations suivantes :
- Création de nouveaux projets
- Sauvegarde des modifications
- Chargement des projets existants
- Suppression des projets

Utilise un fichier config.json pour chaque projet
afin d'assurer une organisation structurée des données.
"""

import os
import json
import shutil
from config import DOSSIER_PROJETS

class GestionProjet:
    """
    Classe de gestion des projets de magasin.
    
    Gère l'ensemble des opérations liées aux fichiers
    et à la persistance des données.
    """
    
    def __init__(self):
        """Initialisation des variables de classe."""
        self.projet_actuel = None
        
    def creer_projet(self, nom, magasin, auteur, plan):
        """
        Crée un nouveau projet avec les informations fournies.
        
        Vérifie les conditions suivantes :
        - Unicité du nom de projet
        - Existence du fichier plan
        - Présence de tous les champs requis
        """
        # Validation des champs requis
        if not all([nom, magasin, auteur, plan]):
            raise ValueError("Données incomplètes pour la création du projet")
            
        # Validation du nom
        nom = nom.strip()
        if not nom:
            raise ValueError("Le nom du projet est requis")
            
        # Vérification de l'unicité du projet
        mon_dossier = os.path.join(DOSSIER_PROJETS, nom)
        if os.path.exists(mon_dossier):
            raise ValueError(f"Un projet nommé '{nom}' existe déjà")
            
        # Vérification de l'existence du plan
        if not os.path.isfile(plan):
            raise ValueError(f"Le fichier plan spécifié est introuvable : {plan}")
            
        # Création du dossier projet
        os.makedirs(mon_dossier)
        
        # Copie du fichier plan avec chemin normalisé
        extension = os.path.splitext(plan)[1]
        mon_plan = os.path.join("App1", "projets", nom, f"plan{extension}")
        mon_plan = os.path.normpath(mon_plan)
        shutil.copy2(plan, mon_plan)
        
        # Conversion des backslashes en forward slashes pour la compatibilité
        mon_plan = mon_plan.replace("\\", "/")
        
        # Configuration du projet
        ma_config = {
            "nom": nom,
            "magasin": magasin,
            "auteur": auteur,
            "chemin_plan": mon_plan,
            "produits": {}
        }
        
        # Sauvegarde de la configuration
        mon_fichier = os.path.join(mon_dossier, "config.json")
        with open(mon_fichier, "w", encoding="utf-8") as f:
            json.dump(ma_config, f, indent=4, ensure_ascii=False)
            
        # Mise à jour du projet actuel
        self.projet_actuel = ma_config
        
    def charger_projet(self, nom):
        """
        Charge un projet existant.
        Vérifie l'ensemble des données du projet.
        """
        # Vérification de l'existence du projet
        mon_dossier = os.path.join(DOSSIER_PROJETS, nom)
        if not os.path.isdir(mon_dossier):
            raise ValueError(f"Le projet '{nom}' est introuvable")
            
        # Chargement de la configuration
        mon_fichier = os.path.join(mon_dossier, "config.json")
        try:
            with open(mon_fichier, "r", encoding="utf-8") as f:
                ma_config = json.load(f)
        except Exception as e:
            raise ValueError(f"Erreur lors du chargement de la configuration : {str(e)}")
            
        # Validation et normalisation de la structure
        champs_requis = ["nom", "magasin", "auteur", "chemin_plan"]
        if not all(champ in ma_config for champ in champs_requis):
            raise ValueError("Configuration du projet invalide ou incomplète")
            
        # Normalisation du chemin du plan
        ma_config["chemin_plan"] = os.path.normpath(ma_config["chemin_plan"]).replace("\\", "/")
        
        # Gestion de la compatibilité des produits
        if "produits_par_case" in ma_config:
            ma_config["produits"] = ma_config.pop("produits_par_case")
        elif "produits" not in ma_config:
            ma_config["produits"] = {}
        elif isinstance(ma_config["produits"], list):
            ma_config["produits"] = {}  # Conversion d'une liste vide en dictionnaire vide
            
        # Mise à jour du projet actuel
        self.projet_actuel = ma_config
        return ma_config
        
    def supprimer_projet(self, nom):
        """
        Supprime un projet et ses fichiers associés.
        Cette opération est irréversible.
        """
        mon_dossier = os.path.join(DOSSIER_PROJETS, nom)
        if not os.path.isdir(mon_dossier):
            raise ValueError(f"Le projet '{nom}' est introuvable")
            
        # Suppression du dossier projet
        try:
            shutil.rmtree(mon_dossier)
        except Exception as e:
            raise ValueError(f"Erreur lors de la suppression : {str(e)}")
            
        # Réinitialisation du projet actuel si nécessaire
        if self.projet_actuel and self.projet_actuel["nom"] == nom:
            self.projet_actuel = None
            
    def sauvegarder(self):
        """
        Sauvegarde les modifications du projet actuel.
        """
        if not self.projet_actuel:
            raise ValueError("Aucun projet actif à sauvegarder")
            
        # Sauvegarde de la configuration
        mon_dossier = os.path.join(DOSSIER_PROJETS, self.projet_actuel["nom"])
        mon_fichier = os.path.join(mon_dossier, "config.json")
        
        try:
            with open(mon_fichier, "w", encoding="utf-8") as f:
                json.dump(self.projet_actuel, f, indent=4, ensure_ascii=False)
        except Exception as e:
            raise ValueError(f"Erreur lors de la sauvegarde : {str(e)}")
            
    def obtenir_produits_case(self, case):
        """
        Récupère la liste des produits d'une case donnée.
        """
        if not self.projet_actuel:
            return []
            
        return self.projet_actuel["produits"].get(case, [])
        
    def definir_produits_case(self, case, produits):
        """
        Met à jour la liste des produits d'une case.
        """
        if not self.projet_actuel:
            raise ValueError("Aucun projet actif")
            
        if produits:
            self.projet_actuel["produits"][case] = produits
        elif case in self.projet_actuel["produits"]:
            del self.projet_actuel["produits"][case]
            
        self.sauvegarder()
        
    def obtenir_tous_produits_places(self):
        """
        Retourne la liste complète des produits placés
        sur le plan.
        """
        if not self.projet_actuel:
            return []
            
        tous_produits = []
        for produits in self.projet_actuel["produits"].values():
            tous_produits.extend(produits)
        return tous_produits
        
    def trouver_case_produit(self, produit):
        """
        Recherche la case contenant un produit donné.
        """
        if not self.projet_actuel:
            return None
            
        for case, produits in self.projet_actuel["produits"].items():
            if produit in produits:
                return case
        return None 
    
    
    
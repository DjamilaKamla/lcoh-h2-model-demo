# LCOH Hydrogen Model – Demo

Ce projet illustre un **modèle simplifié de calcul du LCOH** (Levelized Cost of Hydrogen),
utilisé pour évaluer la compétitivité de projets hydrogène.

⚠️ Les données sont fictives, le but est de montrer la **logique économique** et la
capacité de modélisation, pas de reproduire un modèle industriel.

---

## 1. Objectif

- Calculer un **LCOH** à partir de :
  - CAPEX
  - OPEX
  - durée de vie
  - facteur de charge
  - coût du capital (WACC)
- Comparer plusieurs **scénarios (Bas / Central / Haut)**.
- Réaliser une **analyse de sensibilité** sur une variable clé (ex : CAPEX).

---

## 2. Contenu

Le script `lcoh_model_demo.py` :

1. Définit un ensemble d’hypothèses économiques.
2. Implémente une fonction générique de calcul du LCOH.
3. Compare plusieurs scénarios.
4. Affiche les résultats et une interprétation business simple.

---

## 3. Usage

```bash
python lcoh_model_demo.py

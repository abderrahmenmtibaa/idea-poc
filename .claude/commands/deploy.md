# /deploy

Prépare et exécute le déploiement du projet.

## Usage

```
/deploy [environnement: dev|staging|prod]
```

## Instructions

1. **Vérifications pré-déploiement** :
   - Tests passent (`/test`)
   - Pas de secrets hardcodés
   - Variables d'environnement configurées
   - Build réussi

2. **Déploiement** :
   - Exécute le pipeline approprié pour l'environnement cible
   - Confirme toujours avant de déployer en **production**

3. **Post-déploiement** :
   - Vérifie que le service répond
   - Contrôle les logs pour détecter des erreurs

> ⚠️ Demander confirmation explicite avant tout déploiement en production.

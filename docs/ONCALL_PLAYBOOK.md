# ONCALL PLAYBOOK

## Introduction
Ce playbook est destiné à fournir des directives claires pour les interventions d'urgence concernant le système SIEM. Il est essentiel que tous les membres de l'équipe soient familiarisés avec ces procédures afin de garantir une réponse rapide et efficace en cas d'incident.

## Objectifs
- Identifier et résoudre rapidement les incidents de sécurité.
- Minimiser l'impact des incidents sur les opérations.
- Documenter les incidents et les réponses pour une analyse future.

## Procédures d'Intervention

### 1. Identification de l'Incident
- Surveillez les alertes générées par le système SIEM.
- Vérifiez les logs pour identifier les événements suspects.
- Utilisez les tableaux de bord Grafana et Kibana pour visualiser les données.

### 2. Évaluation de l'Incident
- Déterminez la gravité de l'incident (faible, moyen, élevé).
- Identifiez les systèmes et données affectés.
- Évaluez l'impact potentiel sur l'organisation.

### 3. Containment (Confinement)
- Isoler les systèmes compromis pour éviter la propagation.
- Désactiver les comptes utilisateurs suspects.
- Bloquer les adresses IP malveillantes au niveau du pare-feu.

### 4. Eradication
- Supprimez les logiciels malveillants ou les accès non autorisés.
- Appliquez les correctifs nécessaires aux systèmes affectés.
- Changez les mots de passe des comptes compromis.

### 5. Récupération
- Restaurez les systèmes à partir de sauvegardes fiables.
- Surveillez les systèmes pour détecter toute activité suspecte post-récupération.
- Réactivez les services et les comptes utilisateurs de manière contrôlée.

### 6. Documentation
- Documentez chaque étape de l'incident, y compris les décisions prises et les actions effectuées.
- Rédigez un rapport d'incident détaillé pour l'analyse post-incident.

### 7. Analyse Post-Incident
- Organisez une réunion de retour d'expérience pour discuter de l'incident.
- Identifiez les leçons apprises et les améliorations à apporter aux procédures.
- Mettez à jour les règles d'alerte et les configurations si nécessaire.

## Contacts d'Urgence
- **Responsable de la Sécurité**: [Nom, Email, Téléphone]
- **Équipe IT**: [Nom, Email, Téléphone]
- **Support Technique**: [Nom, Email, Téléphone]

## Conclusion
Ce playbook doit être régulièrement mis à jour pour refléter les changements dans l'environnement de sécurité et les leçons apprises lors des incidents précédents. Assurez-vous que tous les membres de l'équipe ont accès à ce document et comprennent leur rôle dans le processus d'intervention.
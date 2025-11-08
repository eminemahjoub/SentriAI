#!/bin/bash

# Script pour déployer le système SIEM en local

# Vérification des dépendances
dependencies=("python3" "pip3" "docker" "docker-compose")

for dep in "${dependencies[@]}"; do
    if ! command -v $dep &> /dev/null; then
        echo "$dep n'est pas installé. Veuillez l'installer avant de continuer."
        exit 1
    fi
done

# Installation des dépendances Python
pip3 install -r requirements.txt

# Lancement des services avec Docker Compose
docker-compose up -d

# Vérification du statut des services
if [ $? -eq 0 ]; then
    echo "Les services ont été lancés avec succès."
else
    echo "Échec du lancement des services."
    exit 1
fi

# Instructions supplémentaires
echo "Le système SIEM est maintenant déployé en local."
echo "Vous pouvez accéder à l'API et au tableau de bord via les ports configurés dans docker-compose.yml."
import logging

logger = logging.getLogger(__name__)

def appliquer_remise(prix_ht, remise):
    if remise < 0 or remise > 1:
        logger.error("Remise invalide : %s", remise)
        raise ValueError("Remise doit être entre 0 et 1")
    nouveau_prix = prix_ht * (1 - remise)
    logger.info("Remise appliquée : %s -> %s", prix_ht, nouveau_prix)
    return nouveau_prix
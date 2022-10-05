from odoo import fields, models

class Responsable(models.Model):
    _name="stage.responsable"
    nom=fields.Char("Nom du personnel", required=True)
    prenom=fields.Char("Prenom du personnel", required=True)
    departement=fields.Char("Département", required=True)
    telephone=fields.Integer("Numéro de telephone", required=True)

class Stagiaire(models.Model):
    _name="stage.stagiaire"
    nom=fields.Char("Nom du stagiaire", required=True)
    prenom=fields.Char("Prenom du stagiaire", required=True)
    theme=fields.Char("Thème de stage", required=True)
    dateDebut=fields.Date("date de début de stage", required=True)
    dateFin=fields.Date("date de fin de stage", required=True)
    reponsable=fields.Many2one("stage.responsable","Responsable",required=True)

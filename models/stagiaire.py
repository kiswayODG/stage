from odoo import fields, models

class Stagiaire(models.Model):
    _name="stage.stagiaire"
    nom=fields.Char("Nom du stagiaire", required=True)
    prenom=fields.Char("Prenom du stagiaire", required=True)
    theme=fields.Char("Thème de stage", required=True)
    dateDebut=fields.Date("date de début de stage", required=True)
    dateFin=fields.Date("date de fin de stage", required=True)
    reponsable=fields.Many2One(comodel_name="stage.responsable", string="Responsable", onDelete=cascade)

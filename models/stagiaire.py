from odoo import fields, models

class Stagiaire(models.Model):
    _name="stage.stagiaire"
    name=fields.Char("Nom du stagiaire", required=True)
    
    prenom=fields.Char("Prenom du stagiaire", required=True)
    theme=fields.Char("Thème de stage", required=True)
    dateDebut=fields.Date("date de début de stage", required=True)
    dateFin=fields.Date("date de fin de stage", required=True)
    x_responsable_id=fields.Many2one("stage.responsable",string="Responsable")
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cities(models.Model):
    _name = 'address.cities'
    _description = 'Address Cities'
    _rec_name = 'name'

    # Fields ======================================================
    name = fields.Char(string="City", translate=True, required=True)
    state_id = fields.Many2one('res.country.state', string="State", required=True, domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string="Country", required=True)

    # Constraint ======================================================
    _sql_constraints = [
        ('name_city_uniq', 'unique(name, state_id, country_id)', 'The city of the state must be unique by country !')
    ]

    # Onchange State =====================================================
    @api.onchange('state_id')
    def _onchange_country_id(self):
        if self.state_id.country_id:
            self.country_id = self.state_id.country_id

# Country State Translate=====================================================
class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    name = fields.Char(translate=True)
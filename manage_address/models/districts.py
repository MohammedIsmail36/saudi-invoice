# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Districts(models.Model):
    _name = 'address.districts'
    _description = 'Address Districts'
    _rec_name = 'name'

    # Fields ======================================================
    city_id = fields.Many2one('address.cities', string="City", required=True, domain="[('state_id', '=?', state_id), ('country_id', '=?', country_id)]")
    state_id = fields.Many2one('res.country.state', string="State", required=True, domain="[('country_id', '=?', country_id)]")
    name = fields.Char(string="District", translate=True, required=True)
    country_id = fields.Many2one('res.country', string="Country", required=True)

    # Constraint ======================================================
    _sql_constraints = [
        ('name_District_uniq', 'unique(name, city_id, state_id, country_id)', 'The District of the City must be unique by State and country !')
    ]

    # Onchange City =====================================================
    @api.onchange('city_id')
    def _onchange_city_id(self):
        if self.city_id.state_id:
            self.state_id = self.city_id.state_id

    # Onchange State =====================================================
    @api.onchange('state_id')
    def _onchange_district(self):
        if self.state_id.country_id:
            self.country_id = self.state_id.country_id

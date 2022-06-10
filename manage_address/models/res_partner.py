# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'


    # Fields ======================================================
    district_id = fields.Many2one('address.districts', string="District", domain="[('city_id', '=?', city_id), ('state_id', '=?', state_id), ('country_id', '=?', country_id)]")
    city_id = fields.Many2one('address.cities', string="City", ondelete='restrict', domain="[('state_id', '=?', state_id), ('country_id', '=?', country_id)]")
    building_no = fields.Char(string='Building No')
    additional_no = fields.Char(string='Additional No')
    other_id = fields.Char(string='Other ID')

    # Override Onchange Country ==================================================
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id and self.country_id != self.state_id.country_id:
            self.state_id = False
            self.city_id = False
            self.district_id = False

    # Override Onchange State ==================================================
    @api.onchange('state_id')
    def _onchange_state(self):
        if self.state_id and self.state_id != self.city_id.state_id:
            self.city_id = False
        return super(ResPartner, self)._onchange_state()

    # Onchange City =====================================================
    @api.onchange('city_id')
    def _onchange_city(self):
        if self.city_id and self.city_id != self.district_id.city_id:
            self.district_id = False
        if self.city_id.state_id:
            self.state_id = self.city_id.state_id

    # Onchange District ===================================================
    @api.onchange('district_id')
    def _onchange_district(self):
        if self.district_id.city_id:
            self.city_id = self.district_id.city_id

    # Override Address Fields Function ================================================
    @api.model
    def _address_fields(self):
        """Returns the list of address fields that are synced from the parent."""
        return super(ResPartner, self)._address_fields() + ['district_id', 'city_id', 'building_no', 'additional_no', 'other_id']

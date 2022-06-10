# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Company(models.Model):
    _inherit = 'res.company'

    # Set value in Field District ======================================================
    @api.depends('district_id')
    def set_district(self):
        self.district = self.district_id.name

    # Fields ======================================================
    district_id = fields.Many2one('address.districts', string="District", inverse='_inverse_district', ondelete='restrict', domain="[('city_id', '=?', city_id), ('state_id', '=?', state_id), ('country_id', '=?', country_id)]")
    city_id = fields.Many2one('address.cities', string="City", inverse='_inverse_city_id', ondelete='restrict', domain="[('state_id', '=?', state_id), ('country_id', '=?', country_id)]")
    building_no = fields.Char(string='Building No', inverse='_inverse_building_no')
    additional_no = fields.Char(string='Additional No',  inverse='_inverse_additional_no')
    other_id = fields.Char(string='Other ID', inverse='_inverse_other_id')
    district = fields.Char(compute=set_district, store=True)

    # Onchange District ======================================================
    @api.onchange('district_id')
    def _onchange_company_district(self):
        if self.district_id.city_id:
            self.city_id = self.district_id.city_id
            self.city = self.city_id.name

    # Onchange City ======================================================
    @api.onchange('city_id')
    def _onchange_city_id(self):
        if self.city_id and self.city_id != self.district_id.city_id:
            self.district_id = False
        if self.city_id.state_id:
            self.state_id = self.city_id.state_id

    # Onchange State ======================================================
    @api.onchange('state_id')
    def _onchange_state(self):
        if self.state_id and self.state_id != self.city_id.state_id:
            self.city_id = False
        return super(Company, self)._onchange_state()

    # Onchange Country ======================================================
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id and self.country_id != self.state_id.country_id:
            self.state_id = False
            self.city_id = False
            self.district_id = False
        return super(Company, self)._onchange_country_id()

    # Inverse to partner's contact address ==============================
    # Inverse City ======================================================
    def _inverse_city_id(self):
        for company in self:
            company.partner_id.city_id = company.city_id

    # Inverse District ======================================================
    def _inverse_district(self):
        for company in self:
            company.partner_id.district_id = company.district_id

    # Inverse Building No ======================================================
    def _inverse_building_no(self):
        for company in self:
            company.partner_id.building_no = company.building_no

    # Inverse Additional No ======================================================
    def _inverse_additional_no(self):
        for company in self:
            company.partner_id.additional_no = company.additional_no

    # Inverse Other Id ======================================================
    def _inverse_other_id(self):
        for company in self:
            company.partner_id.other_id = company.other_id
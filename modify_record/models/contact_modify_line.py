# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contact_modify_line(models.Model):
    _name = "contact.modify.line"
    _description = "联系人修改单元"


    record_id = fields.Many2one("contact.modify", string="修改记录")
    # field = fields.Selection(selection="_fields_contacts", string="字段")
    field = fields.Many2one("ir.model.fields", string="字段")
    value = fields.Char(string="值")
    csq = fields.Char(string="结果")

    # @api.model
    # def _fields_contacts(self):
    #     field_list = self.env['ir.model.fields'].search(['model_id.model','=','res.partner'])
    #     return [(f.name, f.field_description) for f in field_list]
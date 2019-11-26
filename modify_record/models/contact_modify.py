# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contact_modify(models.Model):
    _name = "contact.modify"
    _description = "联系人修改记录"

    name = fields.Char(string="单号", default="New", readonly=True)
    apply_time = fields.Datetime(default=fields.Datetime.now(), readonly=True, string="提交时间")
    field_lines = fields.One2many("contact.modify.line", "record_id", string="字段")
    # model_id = fields.Many2one("ir.model", string="模型")
    record = fields.Many2one("res.partner", string="联系人")
    state = fields.Many2one("modify.state", string="联系人")
    # record = fields.Reference(selection="related_records", string="记录")
    # model_id = fields.Reference(selection="_selection_target_model", string="模型")
    applier = fields.Many2one(comodel_name="res.users", default=lambda self: self.env.user, string="申请人", readonly=True)
    approver = fields.Many2one(comodel_name="res.users", string="审批人")

    # @api.model
    # def _selection_target_model(self):
    #     models = self.env['ir.model'].search([])
    #     return [(model.model, model.name) for model in models]

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('contact.modify') or '/'
        return super(contact_modify, self).create(vals)

    def exec_modify(self):
        vals = {}
        line.csq = "成功"
        for line in self.field_lines:
            if line.field.ttype == 'many2one':
                obj_val = self.env[line.field.relation].search([('name','ilike',line.value)])
                if obj_val:
                    vals[line.field.name] = obj_val[0].id
                else:
                    line.csq = "失败，找不到相关记录"
            else:
                vals[line.field.name] = line.value
        return self.record.write(vals)


class modify_tate(models.Model):
    _name = "modify.state"
    _description = "工单状态"

    name = fields.Char(string="状态")
    end_state = fields.Boolean(default=False, string="最终状态")
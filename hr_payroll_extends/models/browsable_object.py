#-*- coding:utf-8 -*-

from odoo.addons.hr_payroll.models.browsable_object import Payslips

def get_loans_amount(self, partner_id=None):
    return self.dict.get_loans_amount(partner_id=partner_id)

def get_savings_amount(self, partner_id=None):
    return self.dict.get_savings_amount(partner_id=partner_id)

Payslips.get_loans_amount = get_loans_amount
Payslips.get_savings_amount = get_savings_amount
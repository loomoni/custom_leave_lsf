from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from io import BytesIO
import base64
from datetime import *
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from dateutil.relativedelta import relativedelta
from odoo.addons import decimal_precision as dp


class LeaveWizardReport(models.TransientModel):
    _name = 'leave.wizard.report'
    _description = 'Leave Wizard report excel'

    employee_id = fields.Many2one('hr.employee', string="Staff Name")
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    company = fields.Many2one('res.company', default=lambda self: self.env['res.company']._company_default_get(),
                              string="Company")

    @api.multi
    def get_excel_report(self):

        domain = []

        employee_id = self.employee_id

        if employee_id:
            domain += [('employee_id', '=', employee_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('requested_date', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('requested_date', '<=', date_to)]
        staff_leave = self.env['hr.leave'].search_read(domain)
        data = {
            'all_leave': staff_leave,
            'form_data': self.read()[0]
        }
        return self.env.ref('custom_leaves.leave_report_xls').report_action(self, data=data)

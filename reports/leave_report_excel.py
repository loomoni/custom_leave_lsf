import base64
import io
from odoo import models, fields, api, _


class LeaveReportExcel(models.AbstractModel):
    _name = 'report.custom_leaves.leave_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        print("Well done and good job alot I like the work done", data['all_leave'])
        sheet = workbook.add_worksheet('Staff Leave')
        bold = workbook.add_format({'bold': True})
        sheet.set_column('A:A', 8)
        sheet.set_column('B:B', 23)
        sheet.set_column('C:C', 18)
        sheet.set_column('D:D', 32)
        sheet.set_column('E:E', 20)
        sheet.set_column('F:F', 18)
        sheet.set_column('G:G', 18)
        sheet.set_column('H:H', 13)
        sheet.set_column('I:I', 17)
        sheet.set_column('J:J', 17)

        row = 0
        col = 0

        sheet.write(row, col, 'Staff ID', bold)
        sheet.write(row, col + 1, 'Staff Name', bold)
        sheet.write(row, col + 2, 'Department', bold)
        sheet.write(row, col + 3, 'Designation', bold)
        sheet.write(row, col + 4, 'Type Of Leave', bold)
        sheet.write(row, col + 5, 'Start Date', bold)
        sheet.write(row, col + 6, 'End Date', bold)
        sheet.write(row, col + 7, 'Requested On', bold)
        sheet.write(row, col + 8, 'Days/hr Requested', bold)
        sheet.write(row, col + 9, 'HR Decision', bold)

        for leave in data['all_leave']:
            row += 1
            sheet.write(row, col, leave['staff_id_inherit'])
            sheet.write(row, col + 1, leave['employee_id'][1])
            sheet.write(row, col + 2, leave['department_id'][1])
            sheet.write(row, col + 3, leave['job_id_inherit'])
            sheet.write(row, col + 4, leave['holiday_status_id'][1])
            sheet.write(row, col + 5, leave['date_from'])
            sheet.write(row, col + 6, leave['date_to'])
            sheet.write(row, col + 7, leave['requested_date'])
            sheet.write(row, col + 8, leave['duration_display'])
            sheet.write(row, col + 9, leave['state'])


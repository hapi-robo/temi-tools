# -*- coding: utf-8 -*-
""" Simple report generator

References:
    https://xlsxwriter.readthedocs.io/

"""
import xlsxwriter


# constants
DEFAULT_FIELD_WIDTH = 20


class SimpleReport:
    """ Generate simple reports

    """

    def __init__(self, workbook_name, fields):
        """ Constructor

        Args:
            workbook_name (str): Name of the workbook without extension
            fields ([str]): List of all fields

        """
        self._fields = fields

        # create a new excel file and add a worksheet
        self._workbook = xlsxwriter.Workbook(workbook_name + ".xlsx")
        self._worksheet = self._workbook.add_worksheet()

        # formatting
        format_bold = self._workbook.add_format({"bold": True})

        # headers
        for idx, field_name in enumerate(fields):
            self._worksheet.set_column(idx, idx, DEFAULT_FIELD_WIDTH)
            self._worksheet.write(0, idx, field_name, format_bold)

    def add(self, field_name, row, value, lst=None):
        """ Add value (text or number) to the report

        Args:
            field_name (str): Name of the field
            row (int): Row of spreadsheet
            value (*): Cell value
            lst ([]): Data validation list

        """
        col = self._fields.index(field_name)
        self._worksheet.write(row, col, value)

        if lst:
            self._worksheet.data_validation(
                row,
                col,
                row,
                col,
                {"validate": "list", "source": lst, "error_type": "information"},
            )

    def add_date(self, field_name, row, value, lst=None):
        """ Add date to the report

        Args:
            field_name (str): Name of the field
            row (int): Row of spreadsheet
            value (*): Cell value
            lst ([]): Data validation list

        """
        col = self._fields.index(field_name)

        format_date = self._workbook.add_format({"num_format": "yyyy/mm/dd"})
        self._worksheet.write(row, col, value, format_date)

        if lst:
            self._worksheet.data_validation(
                row,
                col,
                row,
                col,
                {"validate": "list", "source": lst, "error_type": "information"},
            )

    def add_url(self, field_name, row, value):
        """ Add URL to the report

        Args:
            field_name (str): Name of the field
            row (int): Row of spreadsheet
            value (*): Cell value
            lst ([]): Data validation list

        """
        col = self._fields.index(field_name)
        self._worksheet.write_url(row, col, value)

    def close(self):
        """ Safely close expense report

        """
        self._workbook.close()


if __name__ == "__main__":
    FIELDS = ["Date", "Cost", "Company", "Category", "File Path", "Warning"]

    REPORT = SimpleReport("expenses", FIELDS)
    REPORT.add("Date", 1, 1)
    REPORT.add("Cost", 1, 2)
    REPORT.add("Company", 1, 3, [1, 2, 3])
    REPORT.add("Category", 2, 4, [1, 2, 3, 4, 5])
    REPORT.add("File Path", 2, 5)
    REPORT.add("Warning", 2, "Warning")
    REPORT.close()

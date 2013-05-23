from xlrd import open_workbook

book = open_workbook('d:/test/abc.xls')
first_index = book.sheet_by_index(0)
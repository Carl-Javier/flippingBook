import xlsxwriter

class ExportExcelFile:
    def __init__(self, data):
        self.data = data
        self.workbook = xlsxwriter.Workbook("./scraper/file/flipbookDatas.xlsx")
        self.worksheet = self.workbook.add_worksheet('PERFORMANCE')

    def generate_excel(self):
        self.worksheet.write(0, 0, "#")
        self.worksheet.write(0, 1, "Book Name")
        self.worksheet.write(0, 2, "Views")
        self.worksheet.write(0, 3, "Visitors")
        self.worksheet.write(0, 4, "Downloads")
        for index, entry in enumerate(self.data):
            print(entry["book_name"])
            self.worksheet.write(index+1, 0, str(index))
            self.worksheet.write(index+1, 1, entry["book_name"])
            self.worksheet.write(index+1, 2, entry["views"])
            self.worksheet.write(index+1, 3, entry["visitors"])
            self.worksheet.write(index+1, 4, entry["downloads"])
        
        self.workbook.close()
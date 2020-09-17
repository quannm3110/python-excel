import openpyxl
from openpyxl import load_workbook
import pandas as pd

def load_data_openpyxl(file_path):
    book = load_workbook(file_path)
    writer = pd.ExcelWriter(file_path, engine='openpyxl') 
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    return writer

def load_data_pandas(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name)

def modify(data):
    data['new_column'] = 0
    return data

def save(data, writer, sheet_name):
    data.to_excel(writer, sheet_name)
    writer.save()

def process():
    file_path = './data.xlsx'
    sheet_name = 'SalesOrders'
    writer = load_data_openpyxl(file_path)
    data = load_data_pandas(file_path, sheet_name)
    data = modify(data)
    save(data, writer, sheet_name)

if __name__=='__main__':
    process()
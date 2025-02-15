import pandas as pd
import xlwings as xw
import os
import datetime

now = datetime.datetime.now()
formatted_time = now.strftime("%Y_%m_%d_%H_%M_%S")

path = os.getcwd()
path = path + r"/data/sales_data"

xlxs_file_lists = []
file_extension = ".xlsx"

for root,dirs,files in os.walk(path):
    for name in files:
        if name.endswith(file_extension):
            file_path = os.path.join(root,name)
            #print(file_path)
            xlxs_file_lists.append(file_path)
xlxs_file_list_sorts = []

month_order = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}
def extract_month(file_path):
    month_name = file_path.split("\\")[-1].split(".")[0] 
    return month_order[month_name]

sorted_file_paths = sorted(xlxs_file_lists, key=extract_month, reverse=True)

for path in sorted_file_paths:
    #print(path)
    xlxs_file_list_sorts.append(path)

template = xw.Book()
app = xw.apps.active
sheet_1 = template.sheets["Sheet1"]

for file in xlxs_file_list_sorts:
    df = pd.read_excel(file)
    file_name = file.split("\\")[-1].split(".")[0]
    df['date'] = pd.to_datetime(df['transaction_date'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df = df[df["year"] == 2024]
    pivot = pd.pivot_table(df,index="transaction_date",columns="store",values="amount",aggfunc="sum",margins=True,margins_name="Total")
    template.sheets.add(file_name)
    sheet = template.sheets[file_name]
    sheet["A1"].value = f'SALE AMOUNT REPORT BY DAILY AT {file_name}'
    sheet["A1"].api.Font.Bold = True
    sheet["A1"].font.size = 15
    sheet["A1"].font.name = "Arial"
    sheet["A1"].font.color = (0,0,255)
    sheet["A3"].value = pivot

sheet_1.delete()
template.save(f"export\sale_amount_by_daily_12_month_{formatted_time}.xlsx")
template.close() # close workbook
app.kill() # close app
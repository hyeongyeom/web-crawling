from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook
from itertools import chain

workbook = Workbook()
spreadsheet = workbook.active


driver = webdriver.Chrome()
driver.get("https://www.coupang.com/np/categories/417869?listSize=120&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=417769&rating=0")
imgs = driver.find_elements_by_css_selector('.image img')
count = 1
for img in imgs:
    time.sleep(0.2)
    imgUrl_list = []
    imgUrl = img.get_attribute('src')
    imgUrl_list.append(imgUrl)
    rows = imgUrl_list
    spreadsheet.append(rows)
    count = count+1
    print(imgUrl_list)
workbook.save(filename="infant-hat.xlsx")

# //excel reading
# # book = Workbook('infant.xlsx')
# # sheet = book.active

# # rows = sheet.rows
# # headers = [cell.value for cell in next(rows)]
# # all_rows = []


# # for row in rows:
# #     data = {}
# #     for title, cell in zip(headers, row)
# #     data[title] = cell.value

# # all_rows.append(data)
# # print(all_rows)

# excel_data_df = pandas.read_excel('infant-hat.xlsx', sheet_name='Sheet')
# print(excel_data_df.tolist())
webdriver.close()

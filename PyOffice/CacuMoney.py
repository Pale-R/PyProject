"""
 @file : CacuMoney
 @Author : Pale.R
 @Date : 2022/10/10
"""

import xlwt
import xlrd
import datetime
from time import strftime

now = datetime.datetime.now()
updateDate = now.strftime("%Y-%m-%d")
colHeads = ['bank', 'Money', 'Date']
bankMoney = {'zhonghang': '2182', 'jianhang': '1500', 'zhaohang': '12068', 'wechat': '400'}

print(len(bankMoney.keys()))



bankObjs = [
    {
        'bank': 'zhonghang',
        'money': 2182,
        'data': updateDate
    },
    {
        'bank': 'jianhang',
        'money': 1500,
        'data': updateDate
    },
    {
        'bank': 'zhaohang',
        'money': 12068,
        'data': updateDate
    },
    {
        'bank': 'wechat',
        'money': 400,
        'data': updateDate
    },
    {
        'bank': 'total',
        'money': 0,
        'data': updateDate
    }
]


print(bankObjs[len(bankObjs)-1]['money'])

def calculateMoney(bankObjs):
    rowNum = len(bankObjs)
    totalMoney = 0
    for j in range(rowNum):
        totalMoney += bankObjs[j]['money']
    bankObjs[len(bankObjs) - 1]['money'] = totalMoney


# 写入excel
def writeInExcel(colHeads, bankObjs, date):
    # 创建新的workbook（其实就是创建新的excel）
    workbook = xlwt.Workbook(encoding='utf-8')

    # 创建新的sheet表
    worksheet = workbook.add_sheet("MoneyAbout")

    # 初始化样式
    headStyle = xlwt.XFStyle()
    cellStyle = xlwt.XFStyle()

    # 为样式创建字体
    font = xlwt.Font()
    # font.name = 'Times New Roman'  # 字体
    font.bold = True  # 加粗

    # 设置样式
    headStyle.font = font




    # 设置行高
    # style = xlwt.easyxf('font:height 360;')  # 18pt,类型小初的字号
    # row = worksheet.row(0)
    # row.set_style(style)

    # 设置边框样式
    borders = xlwt.Borders()

    # May be:   NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR,
    #           MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
    #           MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
    # DASHED虚线
    # NO_LINE没有
    # THIN实线
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40

    headStyle.borders = borders  # Add Borders to Style
    cellStyle.borders = borders

    # 设置对齐
    al = xlwt.Alignment()
    # VERT_TOP = 0x00       上端对齐
    # VERT_CENTER = 0x01    居中对齐（垂直方向上）
    # VERT_BOTTOM = 0x02    低端对齐
    # HORZ_LEFT = 0x01      左端对齐
    # HORZ_CENTER = 0x02    居中对齐（水平方向上）
    # HORZ_RIGHT = 0x03     右端对齐
    al.horz = 0x02  # 设置水平居中
    al.vert = 0x01  # 设置垂直居中
    headStyle.alignment = al
    cellStyle.alignment = al

    # 设置列宽
    # 往表格写入表头
    colNum = len(colHeads)
    for i in range(colNum):
        worksheet.col(i).width = 256 * 20
        worksheet.write(0, i, colHeads[i], headStyle)
        # 往表格写入内容

    calculateMoney(bankObjs)
    rowNum = len(bankObjs)
    for j in range(rowNum):
        column = 0
        print(bankObjs[j])
        for k in bankObjs[j]:
            worksheet.write(j + 1, column, bankObjs[j][k], cellStyle)
            column += 1


    # 保存
    workbook.save("calculateMoney.xls")



writeInExcel(colHeads, bankObjs, updateDate)
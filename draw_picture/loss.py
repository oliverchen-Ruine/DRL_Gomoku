''''
@Time:2022/5/15 15:05       
@Author:OliverCHen
@Project: DRL_Gomoku   
@Description: 展示loss函数值变化


'''
import xlrd
import matplotlib as mpl
import matplotlib.pyplot as plt

file_name = xlrd.open_workbook('./policy_loss_6_6_4.xls')
table = file_name.sheets()[0]
# 创建一个空列表，存储Excel的数据
tables = []


def import_excel(excel):
    for rown in range(1, excel.nrows):
        array = {"kl": table.cell_value(rown, 0), "lr_multiplier": table.cell_value(rown, 1),
                 "loss": table.cell_value(rown, 2), "entropy": table.cell_value(rown, 3),
                 "explained_var_old": table.cell_value(rown, 4), "explained_var_new": table.cell_value(rown, 5)}
        tables.append(array)


if __name__ == '__main__':
    import_excel(table)
    '''
    for i in tables:
        print(i["loss"])
    '''
    k = 0
    plt.figure(figsize=(20, 10))  # 画布大小
    for i in tables:
        plt.plot(k, i["loss"], 'b', lw=1.5)  # 蓝色的线
        plt.plot(k, i["loss"], 'ro')  # 离散的点
        k += 1
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('Loss function trends')

    plt.show()


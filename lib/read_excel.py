import xlrd
import requests
import unittest
import json

# wb = xlrd.open_workbook("test_user_data.xlsx")  #打开表格
# sh = wb.sheet_by_name("testuserlogin")  #定位工作表
# print("有效行数:%s"%sh.nrows)
# print("有效列数：%s"%sh.ncols)
# print(sh.cell(0,0).value)
# print(sh.row_values(1))
#
# #数据和标题封装成字典
# now_data = dict(zip(sh.row_values(0),sh.row_values(1)))
# print(now_data)


class fengzhuang(object):
    '''封装Excel'''
    def excel_to_list(data_file,sheet):
        data_list = []  #空列表承装所有数据
        wb = xlrd.open_workbook(data_file)  #d打开Excel表格
        sh = wb.sheet_by_name(sheet)  #获取工作表格
        header = sh.row_values(0)  #获取标题行数据
        for i in range(1,sh.nrows): #跳过标题行，从第二行开始抓取数据
            d = dict(zip(header,sh.row_values(i)))  #将标题和每行数据组装成为字典
            data_list.append(d)  #将遍历的值加入到定义的空列表里
            print(data_list)
        return data_list  #列表里嵌套字典格式

    def get_test_data(data_list,case_name):
        for case_data in data_list:
            if case_name == case_data['case_name']:  #如果字典数据中的case_name与参数一致
                print(case_data)
                return case_data


class Testuserloin(unittest.TestCase):
    @classmethod

    def setUpClass(cls):  #整个测试类只执行一次

        cls.data_list = fengzhuang.excel_to_list('test_user_data.xlsx','testuserlogin')  #读取改类的所有测试用例

    def test_userlogin(self):
        case_data = fengzhuang.get_test_data(self.data_list,'userlogin')  #从数据列表中查询到该用例数据
        if not case_data:  #有可能用例为空返回null
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        res = requests.post(url = url,data = json.loads(data))
        print(res.text)
        #self.assertEqual(res.text,expect_res)  #断言判断返回值








if __name__ == '__main__':
    unittest.main(verbosity=2)



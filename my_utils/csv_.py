import csv
from datetime import datetime



class HandleCSV:
    filename = (r"C:\Users\Admin\Downloads\csvfile_data\employees.csv")

    @classmethod
    def read_as_dict(cls):
        with open(cls.filename) as csvfile:
            data = csv.reader(csvfile)
            headers = next(data)
            return [dict(zip(headers, i)) for i in data]

    @classmethod
    def list_data(cls):
        list_ = cls.read_as_dict()
        list2 = []
        for i in list_:
            if int(i.get('SALARY')) > 9000:
                list2.append({'name': i.get('FIRST_NAME') + ' ' + i.get('LAST_NAME'), 'email': i.get('EMAIL'),
                              'phone_number': i.get('PHONE_NUMBER').replace('.', '')})
        return list2

    @classmethod
    def task_two(cls):
        list3 = []
        list_1 = cls.read_as_dict()
        for i in list_1:
            if int(i.get('SALARY')) > 4000 and 30 <= int(i.get('DEPARTMENT_ID')) <= 110:
                list3.append({datetime.strptime(i.get('HIRE_DATE'), "%d-%b-%y"): i.get('FIRST_NAME') + ' ' + i.get('LAST_NAME')})
        return list3


if __name__ == '__main__':
    var = HandleCSV()
    var1 = var.list_data()
    print(var1)
    var2 = var.task_two()
    print(var2)

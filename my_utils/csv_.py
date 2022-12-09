import csv
from datetime import datetime
from typing import Dict, List


class HandleCSV:
    """
    to read data from csv file & perform operation as per task one & task two
    """

    filename = r"C:\Users\Admin\PycharmProjects\pythonProject\pythonProject\pythonProject\HRConnect\employees.csv"

    @classmethod
    def read_as_dict(cls) -> List:
        """
        read csv file and return data in dict format
        :return: Dictionary format data from csv file
        """
        with open(cls.filename) as csvfile:
            data = csv.reader(csvfile)
            # reader function return csv data in list of rows
            # header taken in variable
            headers = next(data)
            return [dict(zip(headers, i)) for i in data]

    @classmethod
    def task_one(cls) -> List:
        """
        return name, email, phone number of employees whose salary is greate than 9000
        :return:
        """
        list_ = cls.read_as_dict()
        list2 = []
        for i in list_:
            # get is the Dict attribute
            if int(i.get('SALARY')) > 9000:
                list2.append({'name': i.get('FIRST_NAME') + ' ' + i.get('LAST_NAME'), 'email': i.get('EMAIL'),
                              'phone_number': i.get('PHONE_NUMBER').replace('.', '')})
        return list2

    @classmethod
    def date_convert(cls, date) -> str:
        """
        convert received date in date format
        :param date: date in format '21-Jun-07'
        :return: date in format yyyy-mm-dd
        """
        date_format = "%d-%b-%y"   # date format for '21-Jun-07'
        hire_date = datetime.strptime(date, date_format)  # return 2018-12-31 00:00:00
        hire_date = hire_date.date()  # convert into 2018-12-31
        return str(hire_date)

    @classmethod
    def task_two(cls) -> Dict:
        """
        fetch data whose depart id in between 30 & 110 and salary is greater than 4200
        :return: grouping data based on hire date
        """
        emp_details = {}
        for i in cls.read_as_dict():
            if 30 <= int(i.get('DEPARTMENT_ID')) <= 110 and int(i.get('SALARY')) > 4200:
                hire_date = cls.date_convert(i.get('HIRE_DATE'))
                name = i.get('FIRST_NAME') + ' ' + i.get('LAST_NAME')
                if emp_details.get(hire_date) is None:   # if hire date not in dict
                    emp_details.setdefault(hire_date, [name])
                else:
                    emp_details[hire_date].append(name)  # is hire date is in dict then appending name values list
        return emp_details


if __name__ == '__main__':
    var = HandleCSV()
    print(var.read_as_dict())
    var1 = var.task_one()
    print(var1)
    var2 = var.task_two()
    print(var2)


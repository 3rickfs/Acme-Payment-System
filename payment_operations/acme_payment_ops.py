from abc import ABC, abstractmethod
import sys
sys.path.insert(0, "..")
from utils.utils import *

def list_day_and_hours_of_work_by_employee(employee_name, day_hour_str):
	return day_hour_str.split(employee_name + "=")[1].split(",")

class PaymentOps():
	'''Operations to calculate employee payment'''
	
	@abstractmethod
	def operation():
		pass

class LoadTxtInput(PaymentOps):
	'''Load the input especified by -input args'''

	def operation(input_file_path):
		f = open(input_file_path,'r')
		loaded_txt_input = f.readlines()
		#print(f"f type: {f.type()}")
		#f.closed()
		return loaded_txt_input

class GetSetsNumberOfEmployeeData(PaymentOps):
	'''Extract employee sets from txt file. It is possible to find out more than
	one dataset, that is one or more employees considering name, days and 
	worked hours'''

	def operation(txt_file_list):
		return [len(txt_file_list), txt_file_list]

class GetEmployeesNames(PaymentOps):
	'''From the txt file get the employees name'''

	def operation(*args):
		employees_num, txt_file_list = args[0]
		employees_names = []
		for i in range(employees_num):
			employees_names.append(txt_file_list[i].split("=")[0])
		return [employees_names, txt_file_list]

class GetEmpDayOfWork(PaymentOps):
	'''Get days of work of employees in the txt file'''

	def operation(*args):
		names, txt_file_list = args[0]
		em_days_of_work = []
		for i, name in enumerate(names):
			raw_day_list = list_day_and_hours_of_work_by_employee(name, txt_file_list[i])
			days_of_work = []
			for raw_day in raw_day_list:
				days_of_work.append(raw_day[:2])
			em_days_of_work.append(days_of_work)

		return [em_days_of_work, names, txt_file_list]

class GetEmpWorkTime(PaymentOps):
	'''Get days of work of employees in the txt file'''

	def operation(*args):
		em_days_of_work, names, txt_file_list = args[0]
		em_hours_of_work = []
		for i, name in enumerate(names):
			raw_day_list = list_day_and_hours_of_work_by_employee(name, txt_file_list[i])
			hours_of_work = []
			for j, day_of_work in enumerate(em_days_of_work[i]):
				raw_hours = raw_day_list[j].split(day_of_work)[1]
				raw_bt, raw_et = raw_hours.split("-") #raw begining and ending time
				hours_of_work.append((int(raw_bt.split(":")[0]), int(raw_et.split(":")[0])))	
			em_hours_of_work.append(hours_of_work)

		return [em_hours_of_work, em_days_of_work, names, txt_file_list]

class GenerateEmployeeDict(PaymentOps):
	'''Structure employee work hours input information into a dictionary'''

	def operation(*args):
		em_hours_of_work, em_days_of_work, names, txt_file_list = args[0]
		employee_dict = {}
		for i, name in enumerate(names):
			pdict = {}
			for j, em_day_of_work in enumerate(em_days_of_work[i]):
				pdict[em_day_of_work] = {"BT":em_hours_of_work[i][j][0],"ET":em_hours_of_work[i][j][1]} #beginning and ending time
			employee_dict[name] = pdict
		return employee_dict

class CalculateEmPaymentByDay(PaymentOps):
	'''Calculate payment by day and put it all into a list'''

	def operation(employee_dict):
		em_payment_by_day = {}
		for employee_name in employee_dict:
			payment_by_day = {}
			for day in employee_dict[employee_name]:
				bt = employee_dict[employee_name][day]["BT"]
				et = employee_dict[employee_name][day]["ET"]
				intrvl = get_groups_and_intervals_of_belonging(bt, et)
				hours_by_interval = calculate_hours_by_interval(bt, et, intrvl)
				payment_by_day[day] = calculate_payment_by_day(hours_by_interval, day)
			em_payment_by_day[employee_name] = payment_by_day
		return em_payment_by_day

class CalculateEmTotalPayment(PaymentOps):
	'''Calculate employee total payment'''

	def operation(em_payment_by_day):
		em_total_payment = {}
		for employee_name in em_payment_by_day:
			total_payment = calculate_total_payment(em_payment_by_day[employee_name])
			em_total_payment[employee_name] = total_payment
		return em_total_payment

class GenerateTotalPaymentOutputMsg(PaymentOps):
	'''Generate the output message for an employee to know how much will be paid'''

	def operation(em_total_payment):
		output_msgs = []
		for employee_name in em_total_payment:
			output_msgs.append(f"The amount to pay {employee_name} is: {em_total_payment[employee_name]} USD")
		return output_msgs

class EmployeePayment():
	'''Main class to operate all classes inheriting from PaymentOps and get the 
	final payment for the employees'''

	@abstractmethod
	def get_employees_payment(txt_file):
		res = txt_file
		for operation in PaymentOps.__subclasses__():
			res = operation.operation(res)

		return res
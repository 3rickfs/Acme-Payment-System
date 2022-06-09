import unittest
import sys
sys.path.insert(0, "..")
from payment_operations.acme_payment_ops import *

input_1 = r'C:/Users/hjara/OneDrive/Proyectos/IOET/acme_app/inputs/input1.txt'
input_2 = r'C:/Users/hjara/OneDrive/Proyectos/IOET/acme_app/inputs/input2.txt'

class tdd_cases(unittest.TestCase):

	def test_read_txt_file(self):
		txtfile = LoadTxtInput.operation(input_1)
		self.assertIsNotNone(txtfile)

	def test_extract_sets_of_data_from_txt_returns_2(self):
		txtfile = LoadTxtInput.operation(input_1)
		sod = GetSetsNumberOfEmployeeData.operation(txtfile)
		self.assertEqual(2, sod[0])

	def test_extract_employee_name_returns_rene_and_astrid(self):
		txtfile = LoadTxtInput.operation(input_1)
		sod = GetSetsNumberOfEmployeeData.operation(txtfile)
		names = GetEmployeesNames.operation(sod)
		names_are_correct = False
		if names[0][0] == "RENE" and names[0][1] == "ASTRID": names_are_correct = True
		self.assertTrue(names_are_correct)

	def test_extract_employees_days_of_work_for_rene_and_astrid(self):
		txtfile = LoadTxtInput.operation(input_1)
		sod = GetSetsNumberOfEmployeeData.operation(txtfile)
		names = GetEmployeesNames.operation(sod)
		em_days_of_work = GetEmpDayOfWork.operation(names)
		rene_dow = ["MO", "TU", "TH", "SA", "SU"]
		astrid_dow = ["MO", "TH", "SU"]
		self.assertTrue(rene_dow == em_days_of_work[0][0] and astrid_dow == em_days_of_work[0][1])

	def test_extract_employees_work_time_for_rene_and_astrid(self):
		txtfile = LoadTxtInput.operation(input_1)
		sod = GetSetsNumberOfEmployeeData.operation(txtfile)
		names = GetEmployeesNames.operation(sod)
		em_days_of_work = GetEmpDayOfWork.operation(names)
		em_hours_of_work = GetEmpWorkTime.operation(em_days_of_work)
		rene_how = [(10,12), (10,12), (1,3), (14,18), (20,21)]
		astrid_how = [(10,12), (12,14), (20,21)]
		self.assertTrue(rene_how == em_hours_of_work[0][0] and astrid_how == em_hours_of_work[0][1])
	
	def test_generate_employee_work_dict_with_rene_and_astrid_info(self):
		txtfile = LoadTxtInput.operation(input_1)
		sod = GetSetsNumberOfEmployeeData.operation(txtfile)
		names = GetEmployeesNames.operation(sod)
		em_days_of_work = GetEmpDayOfWork.operation(names)
		em_hours_of_work = GetEmpWorkTime.operation(em_days_of_work)
		emwore_dict = GenerateEmployeeDict.operation(em_hours_of_work)
		emwore_dicti = {"RENE":{"MO":{"BT":10,
									  "ET":12},
								"TU":{"BT":10,
									  "ET":12},
								"TH":{"BT":1,
									  "ET":3},
								"SA":{"BT":14,
									  "ET":18},
								"SU":{"BT":20,
									  "ET":21}},
						"ASTRID":{"MO":{"BT":10,
									    "ET":12},
								  "TH":{"BT":12,
									    "ET":14},
								  "SU":{"BT":20,
									    "ET":21}}}
		self.assertEqual(emwore_dicti, emwore_dict)

	def test_calculate_employee_payment_by_day_for_rene_and_astrid(self):
		txtfile = LoadTxtInput.operation(input_1)
		sod = GetSetsNumberOfEmployeeData.operation(txtfile)
		names = GetEmployeesNames.operation(sod)
		em_days_of_work = GetEmpDayOfWork.operation(names)
		em_hours_of_work = GetEmpWorkTime.operation(em_days_of_work)
		emwore_dict = GenerateEmployeeDict.operation(em_hours_of_work)
		#em_works_hours_by_day = CalculateEmWorkHoursByDay.operation(emwore_dict)
		em_payment_by_day = CalculateEmPaymentByDay.operation(emwore_dict)
		em_pbd = {"RENE":{"MO":30,  #2*15 USD
				     	  "TU":30,  #2*15 USD
						  "TH":50,  #2*25 USD
						  "SA":80,  #4*20 USD
						  "SU":25}, #1*25 USD
				  "ASTRID":{"MO":30,  #2*15 USD
					   	    "TH":30,  #2*15 USD
							"SU":25}} #1*25 USD
		self.assertEqual(em_pbd, em_payment_by_day)

	def test_calculate_employee_total_payment_for_rene_and_astrid(self):
		txtfile = LoadTxtInput.operation(input_1)
		sod = GetSetsNumberOfEmployeeData.operation(txtfile)
		names = GetEmployeesNames.operation(sod)
		em_days_of_work = GetEmpDayOfWork.operation(names)
		em_hours_of_work = GetEmpWorkTime.operation(em_days_of_work)
		emwore_dict = GenerateEmployeeDict.operation(em_hours_of_work)
		#em_works_hours_by_day = CalculateEmWorkHoursByDay.operation(emwore_dict)
		em_payment_by_day = CalculateEmPaymentByDay.operation(emwore_dict)
		em_total_payment = CalculateEmTotalPayment.operation(em_payment_by_day)
		em_tp = {"RENE":215,"ASTRID":85}
		self.assertEqual(em_tp, em_total_payment)

	def test_output_message_of_employee_total_payment_for_rene_and_astrid(self):
		txtfile = LoadTxtInput.operation(input_1)
		sod = GetSetsNumberOfEmployeeData.operation(txtfile)
		names = GetEmployeesNames.operation(sod)
		em_days_of_work = GetEmpDayOfWork.operation(names)
		em_hours_of_work = GetEmpWorkTime.operation(em_days_of_work)
		emwore_dict = GenerateEmployeeDict.operation(em_hours_of_work)
		#em_works_hours_by_day = CalculateEmWorkHoursByDay.operation(emwore_dict)
		em_payment_by_day = CalculateEmPaymentByDay.operation(emwore_dict)
		em_total_payment = CalculateEmTotalPayment.operation(em_payment_by_day)
		em_total_payment_output_msg = GenerateTotalPaymentOutputMsg.operation(em_total_payment)
		tpom = ["The amount to pay RENE is: 215 USD",
				"The amount to pay ASTRID is: 85 USD"]
		self.assertEqual(em_total_payment_output_msg, tpom)

	def test_to_get_employees_payment_operations_input1(self):
		em_total_payment_output_msg = EmployeePayment.get_employees_payment(input_1)
		tpom = ["The amount to pay RENE is: 215 USD",
				"The amount to pay ASTRID is: 85 USD"]
		self.assertEqual(tpom, em_total_payment_output_msg)

	def test_to_get_employees_payment_operations_input2(self):
		em_total_payment_output_msg = EmployeePayment.get_employees_payment(input_2)
		tpom = ["The amount to pay DIANA is: 275 USD",
				"The amount to pay KARL is: 325 USD",
				"The amount to pay MARK is: 730 USD",
				"The amount to pay AMELIA is: 1250 USD"]
		self.assertEqual(tpom, em_total_payment_output_msg)

if __name__ == '__main__':
	unittest.main()
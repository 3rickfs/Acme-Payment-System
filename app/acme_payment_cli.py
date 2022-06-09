import sys
sys.path.insert(0, "..")
from payment_operations.acme_payment_ops import EmployeePayment
from utils.utils import start_parser

txt_file_path = start_parser()
em_total_payment_output_msg = EmployeePayment.get_employees_payment(txt_file_path)
print(em_total_payment_output_msg)


class hospital:
    def __init__(self):
        self.admin_name=str(input("Enter the admin name"))
        self.doctor_name=str(input("Enter the doctor name"))
        self.sister_name=str(input("Enter the sister name"))
        self.dept_name=str(input("Enter the department name"))
class patient_ward:
    def patient(self):
        self.patient_id=str(input("Enter the patient ID"))
        self.patient_name=str(input("Enter the patient name"))
        self.patient_age=int(input("Enter the age of patient"))
        self.patient_disease=str(input("Enter the name of disease"))
    def display_patient(self):
        print("\n....Patient details....")
        print("Patient Name:", self.patient_name)
        print("Patient ID:", self.patient_id)
        print("Patient age:", self.patient_age)
        print("Patient disease:", self.patient_disease)
class department(hospital, patient_ward):
    def display_hos(self):
        print("\n.....Hospital details.....")
        print("Admin Name:", self.admin_name)
        print("Doctor Name:", self.doctor_name)
        print("Sister Name:", self.sister_name)
        print("Department Name:", self.dept_name)
obj_dep= department()
obj_dep.patient()
obj_dep.display_hos()
obj_dep.display_patient()


import json 
from queue import PriorityQueue 
 
class Patient: 
    def __init__(self, name, surname, id_number, priority): 
        self.name = name 
        self.surname = surname 
        self.id_number = id_number 
        self.priority = priority 
        self.status = None 
         
    def __lt__(self, other):   
        return self.priority < other.priority 
     
    def print_info(self): 
        print(f"Name: {self.name}, Surname: {self.surname}, ID: {self.id_number}, 
Priority: {self.priority}, Status: {self.status}") 
         
 
class Scheduler: 
    def __init__(self): 
        self.patients = PriorityQueue() 
         
    def add_patient(self, patient): 
        self.patients.put(patient) 
         
    def retrieve_next_patient(self): 
5 | Page 
 
        if not self.patients.empty(): 
            return self.patients.get() 
        return None 
     
    def print_waiting_list(self): 
        temp_queue = PriorityQueue() 
        while not self.patients.empty(): 
            patient = self.patients.get() 
            temp_queue.put(patient) 
            patient.print_info() 
             
        self.patients = temp_queue 
         
    def save_consultations_to_file(self, filename): 
        consultations = [] 
        while not self.patients.empty(): 
            patient = self.patients.get() 
            consultations.append({ 
                'name': patient.name, 
                'surname': patient.surname, 
                'id_number': patient.id_number, 
                'priority': patient.priority, 
                'status': patient.status 
            }) 
         
        with open(filename, 'w') as f: 
            json.dump(consultations, f) 
             
    def read_patient_consultations(self, filename): 
        try: 
6 | Page 
 
            with open(filename, 'r') as f: 
                consultations = json.load(f) 
                for consultation in consultations: 
                    print(consultation) 
        except FileNotFoundError: 
            print("No consultations were discovered! Please add patients") 
             
 
class MainMenu: 
    def __init__(self): 
        self.scheduler = Scheduler() 
         
    def display_menu(self): 
        while True: 
            print("\n ER Visit Scheduler") 
            print("1. Add Patient") 
            print("2. Consult Next Patient") 
            print("3. Print Waiting List") 
            print("4. Save Patient Consultations to File") 
            print("5. Read Patient Consultations from File") 
            print("6. Exit") 
            choice = input("Select an option: ") 
             
            if choice == '1': 
                self.add_patient() 
            elif choice == '2': 
                self.retrieve_next_patient() 
            elif choice == '3': 
                self.scheduler.print_waiting_list() 
            elif choice == '4': 
7 | Page 
 
                self.scheduler.save_consultations_to_file("consultations.txt") 
            elif choice == '5': 
                self.scheduler.read_patient_consultations("consultations.txt")  
            elif choice == '6': 
                print("Exiting the application.") 
                break 
            else: 
                print("Invalid option! Please try again.") 
                 
    def add_patient(self): 
        name = input("Enter patient's name: ") 
        surname = input("Enter patient's surname: ") 
        id_number = input("Enter patient's ID number: ") 
        priority = int(input("Enter patient's priority (1-5): ")) 
        patient = Patient(name, surname, id_number, priority) 
        self.scheduler.add_patient(patient) 
        print("Patient has been added successfully") 
         
    def retrieve_next_patient(self): 
        patient = self.scheduler.retrieve_next_patient()  
        if patient: 
            patient.status = input(f"Enter status for {patient.name} {patient.surname}: ") 
            print(f"Consulted {patient.name} {patient.surname}. Status: {patient.status}") 
        else: 
            print("There are no patients in the queue") 
            
 
if __name__ == "__main__": 
    menu = MainMenu() 
    menu.display_menu() 

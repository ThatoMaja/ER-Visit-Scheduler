# ER Visit Scheduler

A Python console-based application designed to help doctors efficiently manage patient consultations in their emergency room using priority-based scheduling. This scheduler ensures that patients with the most critical conditions are treated first.

---

## Project Overview

**Scenario**:  
In an emergency room, patients arrive with varying levels of urgency and must be scheduled for consultation based on priority (1-5, with 5 being most urgent). After consultation, a status is assigned to each patient, and all consultations are stored for later review.

---

## Features

- Add new patients with name, surname, ID number, and priority level.
- Automatically schedules patients based on priority using a **Priority Queue**.
- Retrieve and consult the next patient in the queue.
- Assign and save patient consultation status.
- Display the full waiting list.
- Save all consultation data to a file.
- Read saved consultations from file.
- Menu-based interface with continuous loop until exit.

---

## System Components

### `Patient` Class 
Stores:
- Name
- Surname
- ID number
- Priority
- Status (added after consultation)

Includes a method:
- `print_info()` – to display patient details.

### `Scheduler` Class 
Handles:
- Adding patients to the **Priority Queue**
- Retrieving the next patient
- Printing the current waiting list
- Saving consultations to a `.txt` file using JSON
- Reading and displaying past consultations

### Data Structure 
Uses `queue.PriorityQueue` to:
- Ensure highest priority patients (larger numbers) are seen first.
- Maintain the order of patients waiting.

### `MainMenu` Class 
Interactive CLI menu with options:
1. Add Patient  
2. Consult Next Patient  
3. Print Waiting List  
4. Save Patient Consultations  
5. Read Saved Consultations  
6. Exit  
Uses a sentinel loop to persist until user exits.

---

## How It Works

1. **Adding a Patient**: Captures name, surname, ID, and priority level.
2. **Consultation**: Retrieves patient with the highest priority, prompts for consultation status.
3. **Storage**: Saves consultations to a JSON-formatted `.txt` file.
4. **Viewing**: Displays waiting patients or reads from saved consultations file.



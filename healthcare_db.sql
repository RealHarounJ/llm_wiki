/* 
   Metropolitan Healthcare System - SQL DDL Script 
   Academic Level: University (Conceptual -> Logical -> Physical)
*/

-- 1. Medical Staff (Base for ISA Hierarchy)
CREATE TABLE MEDICAL_STAFF (
    staff_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_joined DATE NOT NULL
);

-- 2. Doctor (Subclass of Medical Staff)
CREATE TABLE DOCTOR (
    staff_id INT PRIMARY KEY,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    supervisor_id INT, -- Recursive FK
    FOREIGN KEY (staff_id) REFERENCES MEDICAL_STAFF(staff_id) ON DELETE CASCADE,
    FOREIGN KEY (supervisor_id) REFERENCES DOCTOR(staff_id) ON DELETE SET NULL
);

-- 3. Nurse (Subclass of Medical Staff)
CREATE TABLE NURSE (
    staff_id INT PRIMARY KEY,
    shift_type VARCHAR(20) CHECK (shift_type IN ('Day', 'Night', 'Swing')),
    FOREIGN KEY (staff_id) REFERENCES MEDICAL_STAFF(staff_id) ON DELETE CASCADE
);

-- 4. Hospital
CREATE TABLE HOSPITAL (
    hospital_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    address VARCHAR(200),
    manager_id INT NOT NULL, -- Mandatory 1:1 Manager
    FOREIGN KEY (manager_id) REFERENCES DOCTOR(staff_id)
);

-- 5. Patient
CREATE TABLE PATIENT (
    ssn CHAR(16) PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- 6. Patient Phones (Handling Multi-valued Attribute)
CREATE TABLE PATIENT_PHONES (
    ssn CHAR(16),
    phone_number VARCHAR(20),
    PRIMARY KEY (ssn, phone_number),
    FOREIGN KEY (ssn) REFERENCES PATIENT(ssn) ON DELETE CASCADE
);

-- 7. Admission (Weak Entity Mapping)
CREATE TABLE ADMISSION (
    patient_ssn CHAR(16),
    hospital_id INT,
    admission_date DATE,
    room_number VARCHAR(10),
    PRIMARY KEY (patient_ssn, hospital_id, admission_date),
    FOREIGN KEY (patient_ssn) REFERENCES PATIENT(ssn) ON DELETE CASCADE,
    FOREIGN KEY (hospital_id) REFERENCES HOSPITAL(hospital_id) ON DELETE CASCADE
);

-- 8. Medications
CREATE TABLE MEDICATIONS (
    med_code VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- 9. Prescribes (Ternary Relationship Mapping)
CREATE TABLE PRESCRIBES (
    patient_ssn CHAR(16),
    doctor_id INT,
    med_code VARCHAR(20),
    admission_date DATE, -- Link to specific admission
    hospital_id INT,     -- Link to specific admission
    frequency VARCHAR(50),
    dosage VARCHAR(50),
    PRIMARY KEY (patient_ssn, doctor_id, med_code, admission_date),
    FOREIGN KEY (doctor_id) REFERENCES DOCTOR(staff_id),
    FOREIGN KEY (med_code) REFERENCES MEDICATIONS(med_code),
    FOREIGN KEY (patient_ssn, hospital_id, admission_date) 
        REFERENCES ADMISSION(patient_ssn, hospital_id, admission_date)
);

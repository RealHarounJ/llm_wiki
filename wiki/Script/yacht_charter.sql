-- =========================================================================
-- DATABASE CREATION: LUXURY YACHT CHARTER SYSTEM (LYCS)
-- Mappatura Relazionale basata sullo schema EER dell'Esercizio
-- =========================================================================

-- 1. Tabella Superclasse Yacht
CREATE TABLE YACHT (
    yacht_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    daily_rate DECIMAL(10, 2) NOT NULL,
    year_built INT NOT NULL
);

-- 2. Tabella Sottoclasse Sailing Yacht (Ereditarietà Option 8A)
CREATE TABLE SAILING_YACHT (
    yacht_id VARCHAR(50) PRIMARY KEY,
    sail_area DECIMAL(6, 2) NOT NULL,
    FOREIGN KEY (yacht_id) REFERENCES YACHT(yacht_id) ON DELETE CASCADE
);

-- 3. Tabella Sottoclasse Motor Yacht (Ereditarietà Option 8A)
CREATE TABLE MOTOR_YACHT (
    yacht_id VARCHAR(50) PRIMARY KEY,
    fuel_capacity DECIMAL(8, 2) NOT NULL,
    FOREIGN KEY (yacht_id) REFERENCES YACHT(yacht_id) ON DELETE CASCADE
);

-- 4. Tabella Capitani
CREATE TABLE CAPTAIN (
    license VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    exper_years INT NOT NULL
);

-- 5. Tabella Clienti con Relazione Ternaria Fusa (Cardinalità massima 1 per il cliente)
CREATE TABLE CUSTOMER (
    customer_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    credit_card VARCHAR(50) NOT NULL,
    
    -- Campi della Relazione Ternaria (CHARTER) fusa in CUSTOMER
    license_captain VARCHAR(50) NULL,
    yacht_id VARCHAR(50) NULL,
    start_date DATE NULL,
    end_date DATE NULL,
    total_paid DECIMAL(10, 2) NULL,
    
    FOREIGN KEY (license_captain) REFERENCES CAPTAIN(license) ON DELETE SET NULL,
    FOREIGN KEY (yacht_id) REFERENCES YACHT(yacht_id) ON DELETE SET NULL,
    
    -- Vincolo logico: se il cliente noleggia, deve specificare capitano, yacht, date e pagamento
    CONSTRAINT chk_charter_integrity CHECK (
        (license_captain IS NULL AND yacht_id IS NULL AND start_date IS NULL AND end_date IS NULL AND total_paid IS NULL) OR
        (license_captain IS NOT NULL AND yacht_id IS NOT NULL AND start_date IS NOT NULL AND end_date IS NOT NULL AND total_paid IS NOT NULL)
    )
);

-- 6. Tabella Multivalore per i Numeri di Telefono del Cliente
CREATE TABLE CUSTOMER_PHONE (
    customer_id VARCHAR(50),
    phone_number VARCHAR(30),
    PRIMARY KEY (customer_id, phone_number),
    FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id) ON DELETE CASCADE
);

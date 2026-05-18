-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Apr 03, 2026 alle 12:44
-- Versione del server: 10.4.32-MariaDB
-- Versione PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ikea_project`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `contact_mechanism`
--

CREATE TABLE `contact_mechanism` (
  `contact_mechanism_id` varchar(50) NOT NULL,
  `contact_type` varchar(50) NOT NULL,
  `e_mail` varchar(100) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `via` varchar(100) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `cap` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `contact_mechanism`
--

INSERT INTO `contact_mechanism` (`contact_mechanism_id`, `contact_type`, `e_mail`, `phone_number`, `via`, `city`, `cap`) VALUES
('C-01', 'INDIRIZZO', NULL, NULL, 'Via Roma 1', 'Milano', '20100'),
('C-02', 'INDIRIZZO', NULL, NULL, 'Via Napoli 2', 'Roma', '00100'),
('C-03', 'EMAIL', 'info@azienda.it', NULL, NULL, NULL, NULL),
('C-04', 'TELEFONO', NULL, '333-1234567', NULL, NULL, NULL),
('C-05', 'INDIRIZZO', NULL, NULL, 'Via Torino 5', 'Torino', '10100');

-- --------------------------------------------------------

--
-- Struttura della tabella `customer`
--

CREATE TABLE `customer` (
  `PARTY` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `customer`
--

INSERT INTO `customer` (`PARTY`) VALUES
('P-01'),
('P-06'),
('P-07'),
('P-08'),
('P-09');

-- --------------------------------------------------------

--
-- Struttura della tabella `employee`
--

CREATE TABLE `employee` (
  `PARTY` varchar(50) NOT NULL,
  `security_number` varchar(50) DEFAULT NULL,
  `hire_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `employee`
--

INSERT INTO `employee` (`PARTY`, `security_number`, `hire_date`) VALUES
('P-01', 'EMP-001', '2020-01-15'),
('P-02', 'EMP-002', '2021-03-10'),
('P-03', 'EMP-003', '2022-06-20'),
('P-04', 'EMP-004', '2023-01-05'),
('P-05', 'EMP-005', '2023-11-01');

-- --------------------------------------------------------

--
-- Struttura della tabella `facility`
--

CREATE TABLE `facility` (
  `facility_id` varchar(50) NOT NULL,
  `facility_type` varchar(50) DEFAULT NULL,
  `facility_name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `facility`
--

INSERT INTO `facility` (`facility_id`, `facility_type`, `facility_name`) VALUES
('FAC-1', 'WAREHOUSE', 'Magazzino Nord'),
('FAC-2', 'WAREHOUSE', 'Magazzino Centro'),
('FAC-3', 'STORE', 'Negozio Milano'),
('FAC-4', 'STORE', 'Negozio Roma'),
('FAC-5', 'WAREHOUSE', 'Polo Logistico Sud');

-- --------------------------------------------------------

--
-- Struttura della tabella `facility_location`
--

CREATE TABLE `facility_location` (
  `FACILITY` varchar(50) NOT NULL,
  `level_id` varchar(20) NOT NULL,
  `section_id` varchar(20) NOT NULL,
  `aisle_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `facility_location`
--

INSERT INTO `facility_location` (`FACILITY`, `level_id`, `section_id`, `aisle_id`) VALUES
('FAC-1', 'L1', 'S1', 'A1'),
('FAC-1', 'L1', 'S2', 'A1'),
('FAC-2', 'L1', 'S1', 'A2'),
('FAC-3', 'L2', 'S1', 'A1'),
('FAC-4', 'L1', 'S3', 'A5');

-- --------------------------------------------------------

--
-- Struttura della tabella `inventory_item`
--

CREATE TABLE `inventory_item` (
  `PRODUCT` varchar(50) NOT NULL,
  `inventory_seq` int(11) NOT NULL,
  `FACILITY` varchar(50) NOT NULL,
  `inventory_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `inventory_item`
--

INSERT INTO `inventory_item` (`PRODUCT`, `inventory_seq`, `FACILITY`, `inventory_type`) VALUES
('PR-CAVO', 1, 'FAC-1', 'NON_SERIALIZED'),
('PR-CAVO', 2, 'FAC-2', 'NON_SERIALIZED'),
('PR-MOUSE', 1, 'FAC-5', 'NON_SERIALIZED'),
('PR-PC', 1, 'FAC-2', 'SERIALIZED'),
('PR-PC', 2, 'FAC-2', 'SERIALIZED'),
('PR-PC', 3, 'FAC-2', 'SERIALIZED'),
('PR-TV', 1, 'FAC-1', 'SERIALIZED'),
('PR-TV', 2, 'FAC-1', 'SERIALIZED'),
('PR-VITI', 1, 'FAC-3', 'NON_SERIALIZED'),
('PR-VITI', 2, 'FAC-4', 'NON_SERIALIZED');

-- --------------------------------------------------------

--
-- Struttura della tabella `invoice`
--

CREATE TABLE `invoice` (
  `invoice_id` varchar(50) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `invoice`
--

INSERT INTO `invoice` (`invoice_id`, `date`) VALUES
('INV-01', '2026-04-02'),
('INV-02', '2026-04-03'),
('INV-03', '2026-04-04'),
('INV-04', '2026-04-05'),
('INV-05', '2026-04-06');

-- --------------------------------------------------------

--
-- Struttura della tabella `invoice_item`
--

CREATE TABLE `invoice_item` (
  `INVOICE` varchar(50) NOT NULL,
  `invoice_item_seq` int(11) NOT NULL,
  `ORDER` varchar(50) NOT NULL,
  `ORDER_SEQ` int(11) NOT NULL,
  `INVENTORY_PRODUCT` varchar(50) NOT NULL,
  `INVENTORY_SEQ` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `amount` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `invoice_item`
--

INSERT INTO `invoice_item` (`INVOICE`, `invoice_item_seq`, `ORDER`, `ORDER_SEQ`, `INVENTORY_PRODUCT`, `INVENTORY_SEQ`, `quantity`, `amount`) VALUES
('INV-01', 1, 'ORD-1', 1, 'PR-TV', 1, 1, 500.00),
('INV-01', 2, 'ORD-1', 2, 'PR-CAVO', 1, 2, 19.98),
('INV-02', 1, 'ORD-2', 1, 'PR-PC', 1, 1, 1200.00),
('INV-03', 1, 'ORD-3', 1, 'PR-VITI', 1, 100, 500.00),
('INV-04', 1, 'ORD-4', 1, 'PR-MOUSE', 1, 10, 150.00);

-- --------------------------------------------------------

--
-- Struttura della tabella `non_serialized_inventory_item`
--

CREATE TABLE `non_serialized_inventory_item` (
  `PRODUCT` varchar(50) NOT NULL,
  `INVENTORY_SEQ` int(11) NOT NULL,
  `quantity_on_hand` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `non_serialized_inventory_item`
--

INSERT INTO `non_serialized_inventory_item` (`PRODUCT`, `INVENTORY_SEQ`, `quantity_on_hand`) VALUES
('PR-CAVO', 1, 300),
('PR-CAVO', 2, 150),
('PR-MOUSE', 1, 80),
('PR-VITI', 1, 10000),
('PR-VITI', 2, 5000);

-- --------------------------------------------------------

--
-- Struttura della tabella `order`
--

CREATE TABLE `order` (
  `order_id` varchar(50) NOT NULL,
  `order_date` date NOT NULL,
  `PARTY` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `order`
--

INSERT INTO `order` (`order_id`, `order_date`, `PARTY`) VALUES
('ORD-1', '2026-04-01', 'P-01'),
('ORD-2', '2026-04-02', 'P-06'),
('ORD-3', '2026-04-03', 'P-07'),
('ORD-4', '2026-04-04', 'P-08'),
('ORD-5', '2026-04-05', 'P-09');

-- --------------------------------------------------------

--
-- Struttura della tabella `order_facility`
--

CREATE TABLE `order_facility` (
  `ORDER` varchar(50) NOT NULL,
  `FACILITY` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `order_facility`
--

INSERT INTO `order_facility` (`ORDER`, `FACILITY`) VALUES
('ORD-1', 'FAC-1'),
('ORD-2', 'FAC-2'),
('ORD-3', 'FAC-3'),
('ORD-4', 'FAC-4'),
('ORD-5', 'FAC-5');

-- --------------------------------------------------------

--
-- Struttura della tabella `order_item`
--

CREATE TABLE `order_item` (
  `ORDER` varchar(50) NOT NULL,
  `order_item_seq` int(11) NOT NULL,
  `PRODUCT` varchar(50) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `order_item`
--

INSERT INTO `order_item` (`ORDER`, `order_item_seq`, `PRODUCT`, `quantity`, `unit_price`) VALUES
('ORD-1', 1, 'PR-TV', 1, 500.00),
('ORD-1', 2, 'PR-CAVO', 2, 9.99),
('ORD-2', 1, 'PR-PC', 5, 1200.00),
('ORD-3', 1, 'PR-VITI', 100, 5.00),
('ORD-4', 1, 'PR-MOUSE', 10, 15.00);

-- --------------------------------------------------------

--
-- Struttura della tabella `organization`
--

CREATE TABLE `organization` (
  `PARTY` varchar(50) NOT NULL,
  `social_reason` varchar(100) DEFAULT NULL,
  `vat_number` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `organization`
--

INSERT INTO `organization` (`PARTY`, `social_reason`, `vat_number`) VALUES
('P-06', 'TechCorp SRL', 'IT123456789'),
('P-07', 'Forniture ABC', 'IT987654321'),
('P-08', 'Logistica Express', 'IT112233445'),
('P-09', 'Global Import', 'IT556677889'),
('P-10', 'B2B Solutions', 'IT998877665');

-- --------------------------------------------------------

--
-- Struttura della tabella `party`
--

CREATE TABLE `party` (
  `party_id` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `party`
--

INSERT INTO `party` (`party_id`, `type`) VALUES
('P-01', 'PERSON'),
('P-02', 'PERSON'),
('P-03', 'PERSON'),
('P-04', 'PERSON'),
('P-05', 'PERSON'),
('P-06', 'ORGANIZATION'),
('P-07', 'ORGANIZATION'),
('P-08', 'ORGANIZATION'),
('P-09', 'ORGANIZATION'),
('P-10', 'ORGANIZATION');

-- --------------------------------------------------------

--
-- Struttura della tabella `party_contact_mech`
--

CREATE TABLE `party_contact_mech` (
  `PARTY` varchar(50) NOT NULL,
  `CONTACT_MECHANISM` varchar(50) NOT NULL,
  `purpose_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `party_contact_mech`
--

INSERT INTO `party_contact_mech` (`PARTY`, `CONTACT_MECHANISM`, `purpose_type`) VALUES
('P-01', 'C-01', 'SHIPPING'),
('P-06', 'C-02', 'BILLING'),
('P-07', 'C-03', 'INVOICE_EMAIL'),
('P-08', 'C-04', 'MOBILE'),
('P-09', 'C-05', 'SHIPPING');

-- --------------------------------------------------------

--
-- Struttura della tabella `person`
--

CREATE TABLE `person` (
  `PARTY` varchar(50) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `person`
--

INSERT INTO `person` (`PARTY`, `first_name`, `last_name`) VALUES
('P-01', 'Mario', 'Rossi'),
('P-02', 'Luca', 'Neri'),
('P-03', 'Anna', 'Bianchi'),
('P-04', 'Giulia', 'Verdi'),
('P-05', 'Marco', 'Gialli');

-- --------------------------------------------------------

--
-- Struttura della tabella `product`
--

CREATE TABLE `product` (
  `product_id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `product_type` varchar(50) DEFAULT NULL,
  `introduction_date` date DEFAULT NULL,
  `sales_discontinuation_date` date DEFAULT NULL,
  `support_discontinuation_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `product`
--

INSERT INTO `product` (`product_id`, `name`, `description`, `product_type`, `introduction_date`, `sales_discontinuation_date`, `support_discontinuation_date`) VALUES
('PR-CAVO', 'Cavo HDMI 2m', NULL, 'ACCESSORI', NULL, NULL, NULL),
('PR-MOUSE', 'Mouse Wireless', NULL, 'ACCESSORI', NULL, NULL, NULL),
('PR-PC', 'Laptop Pro', NULL, 'ELETTRONICA', NULL, NULL, NULL),
('PR-TV', 'Smart TV 55', NULL, 'ELETTRONICA', NULL, NULL, NULL),
('PR-VITI', 'Scatola Viti 5mm', NULL, 'FERRAMENTA', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Struttura della tabella `product_category`
--

CREATE TABLE `product_category` (
  `category_id` varchar(50) NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `product_category`
--

INSERT INTO `product_category` (`category_id`, `description`) VALUES
('CAT-1', 'Home Cinema'),
('CAT-2', 'Informatica'),
('CAT-3', 'Periferiche'),
('CAT-4', 'Bricolage'),
('CAT-5', 'Cavi');

-- --------------------------------------------------------

--
-- Struttura della tabella `product_category_assignment`
--

CREATE TABLE `product_category_assignment` (
  `PRODUCT` varchar(50) NOT NULL,
  `PRODUCT_CATEGORY` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `product_category_assignment`
--

INSERT INTO `product_category_assignment` (`PRODUCT`, `PRODUCT_CATEGORY`) VALUES
('PR-CAVO', 'CAT-5'),
('PR-MOUSE', 'CAT-3'),
('PR-PC', 'CAT-2'),
('PR-TV', 'CAT-1'),
('PR-VITI', 'CAT-4');

-- --------------------------------------------------------

--
-- Struttura della tabella `product_feature`
--

CREATE TABLE `product_feature` (
  `product_feature_id` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  `product_feature_type` varchar(50) DEFAULT NULL,
  `uom_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `product_feature`
--

INSERT INTO `product_feature` (`product_feature_id`, `description`, `product_feature_type`, `uom_id`) VALUES
('F-4K', 'Risoluzione 4K', 'DISPLAY', 'PX'),
('F-5MM', 'Diametro 5mm', 'DIMENSIONE', 'MM'),
('F-BLK', 'Nero', 'COLORE', NULL),
('F-RED', 'Rosso', 'COLORE', NULL),
('F-WIFI', 'WiFi 6', 'CONNETTIVITA', NULL);

-- --------------------------------------------------------

--
-- Struttura della tabella `product_feature_applicability`
--

CREATE TABLE `product_feature_applicability` (
  `PRODUCT` varchar(50) NOT NULL,
  `PRODUCT_FEATURE` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `product_feature_applicability`
--

INSERT INTO `product_feature_applicability` (`PRODUCT`, `PRODUCT_FEATURE`) VALUES
('PR-CAVO', 'F-BLK'),
('PR-MOUSE', 'F-BLK'),
('PR-PC', 'F-WIFI'),
('PR-TV', 'F-4K'),
('PR-VITI', 'F-5MM');

-- --------------------------------------------------------

--
-- Struttura della tabella `product_price`
--

CREATE TABLE `product_price` (
  `PRODUCT` varchar(50) NOT NULL,
  `PRODUCT_PRICE_TYPE` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `currency` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `product_price`
--

INSERT INTO `product_price` (`PRODUCT`, `PRODUCT_PRICE_TYPE`, `price`, `currency`) VALUES
('PR-CAVO', 'SCONTO', 9.99, 'EUR'),
('PR-MOUSE', 'INGROSSO', 15.00, 'EUR'),
('PR-PC', 'LISTINO', 1200.00, 'EUR'),
('PR-TV', 'LISTINO', 500.00, 'EUR'),
('PR-VITI', 'LISTINO', 5.00, 'EUR');

-- --------------------------------------------------------

--
-- Struttura della tabella `product_price_type`
--

CREATE TABLE `product_price_type` (
  `product_price_type_id` varchar(50) NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `product_price_type`
--

INSERT INTO `product_price_type` (`product_price_type_id`, `description`) VALUES
('COSTO', 'Costo di produzione'),
('DIPENDENTE', 'Prezzo per staff'),
('INGROSSO', 'Prezzo B2B'),
('LISTINO', 'Prezzo al pubblico'),
('SCONTO', 'Prezzo in promozione');

-- --------------------------------------------------------

--
-- Struttura della tabella `serialized_inventory_item`
--

CREATE TABLE `serialized_inventory_item` (
  `PRODUCT` varchar(50) NOT NULL,
  `INVENTORY_SEQ` int(11) NOT NULL,
  `serial_number` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `serialized_inventory_item`
--

INSERT INTO `serialized_inventory_item` (`PRODUCT`, `INVENTORY_SEQ`, `serial_number`) VALUES
('PR-PC', 1, 'SN-PC-001'),
('PR-PC', 2, 'SN-PC-002'),
('PR-PC', 3, 'SN-PC-003'),
('PR-TV', 1, 'SN-TV-001'),
('PR-TV', 2, 'SN-TV-002');

-- --------------------------------------------------------

--
-- Struttura della tabella `supplier`
--

CREATE TABLE `supplier` (
  `PARTY` varchar(50) NOT NULL,
  `standard_lead_time` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `supplier`
--

INSERT INTO `supplier` (`PARTY`, `standard_lead_time`) VALUES
('P-06', 5),
('P-07', 10),
('P-08', 2),
('P-09', 15),
('P-10', 7);

-- --------------------------------------------------------

--
-- Struttura della tabella `supplier_product`
--

CREATE TABLE `supplier_product` (
  `PARTY` varchar(50) NOT NULL,
  `PRODUCT` varchar(50) NOT NULL,
  `supplier_product_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `supplier_product`
--

INSERT INTO `supplier_product` (`PARTY`, `PRODUCT`, `supplier_product_id`) VALUES
('P-06', 'PR-TV', 'SUP-TV-01'),
('P-07', 'PR-PC', 'SUP-PC-99'),
('P-08', 'PR-VITI', 'SUP-VT-55'),
('P-09', 'PR-MOUSE', 'SUP-MS-11'),
('P-10', 'PR-CAVO', 'SUP-CV-22');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `contact_mechanism`
--
ALTER TABLE `contact_mechanism`
  ADD PRIMARY KEY (`contact_mechanism_id`);

--
-- Indici per le tabelle `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`PARTY`);

--
-- Indici per le tabelle `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`PARTY`);

--
-- Indici per le tabelle `facility`
--
ALTER TABLE `facility`
  ADD PRIMARY KEY (`facility_id`);

--
-- Indici per le tabelle `facility_location`
--
ALTER TABLE `facility_location`
  ADD PRIMARY KEY (`FACILITY`,`level_id`,`section_id`,`aisle_id`);

--
-- Indici per le tabelle `inventory_item`
--
ALTER TABLE `inventory_item`
  ADD PRIMARY KEY (`PRODUCT`,`inventory_seq`),
  ADD KEY `FACILITY` (`FACILITY`);

--
-- Indici per le tabelle `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`invoice_id`);

--
-- Indici per le tabelle `invoice_item`
--
ALTER TABLE `invoice_item`
  ADD PRIMARY KEY (`INVOICE`,`invoice_item_seq`),
  ADD KEY `ORDER` (`ORDER`,`ORDER_SEQ`),
  ADD KEY `INVENTORY_PRODUCT` (`INVENTORY_PRODUCT`,`INVENTORY_SEQ`);

--
-- Indici per le tabelle `non_serialized_inventory_item`
--
ALTER TABLE `non_serialized_inventory_item`
  ADD PRIMARY KEY (`PRODUCT`,`INVENTORY_SEQ`);

--
-- Indici per le tabelle `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `PARTY` (`PARTY`);

--
-- Indici per le tabelle `order_facility`
--
ALTER TABLE `order_facility`
  ADD PRIMARY KEY (`ORDER`,`FACILITY`),
  ADD KEY `FACILITY` (`FACILITY`);

--
-- Indici per le tabelle `order_item`
--
ALTER TABLE `order_item`
  ADD PRIMARY KEY (`ORDER`,`order_item_seq`),
  ADD KEY `PRODUCT` (`PRODUCT`);

--
-- Indici per le tabelle `organization`
--
ALTER TABLE `organization`
  ADD PRIMARY KEY (`PARTY`);

--
-- Indici per le tabelle `party`
--
ALTER TABLE `party`
  ADD PRIMARY KEY (`party_id`);

--
-- Indici per le tabelle `party_contact_mech`
--
ALTER TABLE `party_contact_mech`
  ADD PRIMARY KEY (`PARTY`,`CONTACT_MECHANISM`,`purpose_type`),
  ADD KEY `CONTACT_MECHANISM` (`CONTACT_MECHANISM`);

--
-- Indici per le tabelle `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`PARTY`);

--
-- Indici per le tabelle `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indici per le tabelle `product_category`
--
ALTER TABLE `product_category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indici per le tabelle `product_category_assignment`
--
ALTER TABLE `product_category_assignment`
  ADD PRIMARY KEY (`PRODUCT`,`PRODUCT_CATEGORY`),
  ADD KEY `PRODUCT_CATEGORY` (`PRODUCT_CATEGORY`);

--
-- Indici per le tabelle `product_feature`
--
ALTER TABLE `product_feature`
  ADD PRIMARY KEY (`product_feature_id`);

--
-- Indici per le tabelle `product_feature_applicability`
--
ALTER TABLE `product_feature_applicability`
  ADD PRIMARY KEY (`PRODUCT`,`PRODUCT_FEATURE`),
  ADD KEY `PRODUCT_FEATURE` (`PRODUCT_FEATURE`);

--
-- Indici per le tabelle `product_price`
--
ALTER TABLE `product_price`
  ADD PRIMARY KEY (`PRODUCT`,`PRODUCT_PRICE_TYPE`),
  ADD KEY `PRODUCT_PRICE_TYPE` (`PRODUCT_PRICE_TYPE`);

--
-- Indici per le tabelle `product_price_type`
--
ALTER TABLE `product_price_type`
  ADD PRIMARY KEY (`product_price_type_id`);

--
-- Indici per le tabelle `serialized_inventory_item`
--
ALTER TABLE `serialized_inventory_item`
  ADD PRIMARY KEY (`PRODUCT`,`INVENTORY_SEQ`);

--
-- Indici per le tabelle `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`PARTY`);

--
-- Indici per le tabelle `supplier_product`
--
ALTER TABLE `supplier_product`
  ADD PRIMARY KEY (`PARTY`,`PRODUCT`),
  ADD KEY `PRODUCT` (`PRODUCT`);

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`PARTY`) REFERENCES `party` (`party_id`);

--
-- Limiti per la tabella `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`PARTY`) REFERENCES `party` (`party_id`);

--
-- Limiti per la tabella `facility_location`
--
ALTER TABLE `facility_location`
  ADD CONSTRAINT `facility_location_ibfk_1` FOREIGN KEY (`FACILITY`) REFERENCES `facility` (`facility_id`);

--
-- Limiti per la tabella `inventory_item`
--
ALTER TABLE `inventory_item`
  ADD CONSTRAINT `inventory_item_ibfk_1` FOREIGN KEY (`PRODUCT`) REFERENCES `product` (`product_id`),
  ADD CONSTRAINT `inventory_item_ibfk_2` FOREIGN KEY (`FACILITY`) REFERENCES `facility` (`facility_id`);

--
-- Limiti per la tabella `invoice_item`
--
ALTER TABLE `invoice_item`
  ADD CONSTRAINT `invoice_item_ibfk_1` FOREIGN KEY (`INVOICE`) REFERENCES `invoice` (`invoice_id`),
  ADD CONSTRAINT `invoice_item_ibfk_2` FOREIGN KEY (`ORDER`,`ORDER_SEQ`) REFERENCES `order_item` (`ORDER`, `order_item_seq`),
  ADD CONSTRAINT `invoice_item_ibfk_3` FOREIGN KEY (`INVENTORY_PRODUCT`,`INVENTORY_SEQ`) REFERENCES `inventory_item` (`PRODUCT`, `inventory_seq`);

--
-- Limiti per la tabella `non_serialized_inventory_item`
--
ALTER TABLE `non_serialized_inventory_item`
  ADD CONSTRAINT `non_serialized_inventory_item_ibfk_1` FOREIGN KEY (`PRODUCT`,`INVENTORY_SEQ`) REFERENCES `inventory_item` (`PRODUCT`, `inventory_seq`);

--
-- Limiti per la tabella `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`PARTY`) REFERENCES `party` (`party_id`);

--
-- Limiti per la tabella `order_facility`
--
ALTER TABLE `order_facility`
  ADD CONSTRAINT `order_facility_ibfk_1` FOREIGN KEY (`ORDER`) REFERENCES `order` (`order_id`),
  ADD CONSTRAINT `order_facility_ibfk_2` FOREIGN KEY (`FACILITY`) REFERENCES `facility` (`facility_id`);

--
-- Limiti per la tabella `order_item`
--
ALTER TABLE `order_item`
  ADD CONSTRAINT `order_item_ibfk_1` FOREIGN KEY (`ORDER`) REFERENCES `order` (`order_id`),
  ADD CONSTRAINT `order_item_ibfk_2` FOREIGN KEY (`PRODUCT`) REFERENCES `product` (`product_id`);

--
-- Limiti per la tabella `organization`
--
ALTER TABLE `organization`
  ADD CONSTRAINT `organization_ibfk_1` FOREIGN KEY (`PARTY`) REFERENCES `party` (`party_id`);

--
-- Limiti per la tabella `party_contact_mech`
--
ALTER TABLE `party_contact_mech`
  ADD CONSTRAINT `party_contact_mech_ibfk_1` FOREIGN KEY (`PARTY`) REFERENCES `party` (`party_id`),
  ADD CONSTRAINT `party_contact_mech_ibfk_2` FOREIGN KEY (`CONTACT_MECHANISM`) REFERENCES `contact_mechanism` (`contact_mechanism_id`);

--
-- Limiti per la tabella `person`
--
ALTER TABLE `person`
  ADD CONSTRAINT `person_ibfk_1` FOREIGN KEY (`PARTY`) REFERENCES `party` (`party_id`);

--
-- Limiti per la tabella `product_category_assignment`
--
ALTER TABLE `product_category_assignment`
  ADD CONSTRAINT `product_category_assignment_ibfk_1` FOREIGN KEY (`PRODUCT`) REFERENCES `product` (`product_id`),
  ADD CONSTRAINT `product_category_assignment_ibfk_2` FOREIGN KEY (`PRODUCT_CATEGORY`) REFERENCES `product_category` (`category_id`);

--
-- Limiti per la tabella `product_feature_applicability`
--
ALTER TABLE `product_feature_applicability`
  ADD CONSTRAINT `product_feature_applicability_ibfk_1` FOREIGN KEY (`PRODUCT`) REFERENCES `product` (`product_id`),
  ADD CONSTRAINT `product_feature_applicability_ibfk_2` FOREIGN KEY (`PRODUCT_FEATURE`) REFERENCES `product_feature` (`product_feature_id`);

--
-- Limiti per la tabella `product_price`
--
ALTER TABLE `product_price`
  ADD CONSTRAINT `product_price_ibfk_1` FOREIGN KEY (`PRODUCT`) REFERENCES `product` (`product_id`),
  ADD CONSTRAINT `product_price_ibfk_2` FOREIGN KEY (`PRODUCT_PRICE_TYPE`) REFERENCES `product_price_type` (`product_price_type_id`);

--
-- Limiti per la tabella `serialized_inventory_item`
--
ALTER TABLE `serialized_inventory_item`
  ADD CONSTRAINT `serialized_inventory_item_ibfk_1` FOREIGN KEY (`PRODUCT`,`INVENTORY_SEQ`) REFERENCES `inventory_item` (`PRODUCT`, `inventory_seq`);

--
-- Limiti per la tabella `supplier`
--
ALTER TABLE `supplier`
  ADD CONSTRAINT `supplier_ibfk_1` FOREIGN KEY (`PARTY`) REFERENCES `party` (`party_id`);

--
-- Limiti per la tabella `supplier_product`
--
ALTER TABLE `supplier_product`
  ADD CONSTRAINT `supplier_product_ibfk_1` FOREIGN KEY (`PARTY`) REFERENCES `supplier` (`PARTY`),
  ADD CONSTRAINT `supplier_product_ibfk_2` FOREIGN KEY (`PRODUCT`) REFERENCES `product` (`product_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

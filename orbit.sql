-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: orbit_db
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `category_name` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES ('4eb77e32-6fef-4586-b36c-820cc6bd462f','2023-01-31 18:58:00','Traditionals','Traditional dishes'),('5229e972-82d2-4b03-a98c-470d0d1adf96','2023-01-31 18:57:19','Main Dish','Main meals'),('c7869754-b6ea-4b4d-b696-7893c6e681d9','2023-02-01 09:12:39','Beverage','Hot beverages'),('dfc36ea7-c308-4f09-9b42-07016ea22057','2023-01-31 18:43:35','Snacks','Snacky items'),('e9217bdf-96a3-4d0b-b4f5-268f2c7bf793','2023-02-01 10:48:03','Beveragess','dgfgm');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `counters`
--

DROP TABLE IF EXISTS `counters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `counters` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `counter_name` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `counter_name` (`counter_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `counters`
--

LOCK TABLES `counters` WRITE;
/*!40000 ALTER TABLE `counters` DISABLE KEYS */;
/*!40000 ALTER TABLE `counters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_numbers`
--

DROP TABLE IF EXISTS `document_numbers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `document_numbers` (
  `last_number` int NOT NULL,
  PRIMARY KEY (`last_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_numbers`
--

LOCK TABLES `document_numbers` WRITE;
/*!40000 ALTER TABLE `document_numbers` DISABLE KEYS */;
INSERT INTO `document_numbers` VALUES (1114);
/*!40000 ALTER TABLE `document_numbers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grn_stockitems`
--

DROP TABLE IF EXISTS `grn_stockitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grn_stockitems` (
  `quantity` int NOT NULL,
  `amount` int NOT NULL,
  `grn_id` varchar(100) NOT NULL,
  `stock_item_id` varchar(100) NOT NULL,
  `rate` int DEFAULT '0',
  PRIMARY KEY (`grn_id`,`stock_item_id`),
  KEY `stock_item_id` (`stock_item_id`),
  CONSTRAINT `grn_stockitems_ibfk_1` FOREIGN KEY (`grn_id`) REFERENCES `grns` (`id`),
  CONSTRAINT `grn_stockitems_ibfk_2` FOREIGN KEY (`stock_item_id`) REFERENCES `stock_items` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grn_stockitems`
--

LOCK TABLES `grn_stockitems` WRITE;
/*!40000 ALTER TABLE `grn_stockitems` DISABLE KEYS */;
INSERT INTO `grn_stockitems` VALUES (70,10500,'123afe68-36b4-4d89-8bd9-3bba949b2f9f','001',150),(50,2500,'123afe68-36b4-4d89-8bd9-3bba949b2f9f','002',50),(13,273,'308fb126-0670-4b23-b3e1-91fc5f442afd','001',21),(6,36,'43557598-7350-485f-bf9d-ed96aeb7f4b1','002',6),(7,49,'43557598-7350-485f-bf9d-ed96aeb7f4b1','914afe24-1a9d-40ee-b7e7-d194a641c152',7),(45,3015,'46424cdf-2383-4439-a3e6-6ce1c33da02b','001',67),(3,9,'4690b74d-80fe-4009-9aec-5a8163847410','001',3),(5,20,'4690b74d-80fe-4009-9aec-5a8163847410','002',4),(10,100,'4a089d3c-4669-44a2-a30d-661e3273749b','001',10),(20,400,'4a089d3c-4669-44a2-a30d-661e3273749b','002',20),(30,900,'4a089d3c-4669-44a2-a30d-661e3273749b','914afe24-1a9d-40ee-b7e7-d194a641c152',30),(40,1600,'4a089d3c-4669-44a2-a30d-661e3273749b','ecaa3a3a-44e2-4a4e-bb5a-7bfc3c25a3df',40),(1,1,'546aec50-640f-4776-ab7c-5aa666a9863b','914afe24-1a9d-40ee-b7e7-d194a641c152',1),(22,484,'67a535eb-33ff-44dd-9097-98fce854e65c','001',22),(33,330,'67a535eb-33ff-44dd-9097-98fce854e65c','002',10),(3,9,'6b855b0d-4130-4996-8cc7-923c4214cfdf','002',3),(56,4368,'733f7f63-bc51-405a-ae72-e14175497c73','001',78),(789,3156,'733f7f63-bc51-405a-ae72-e14175497c73','e7f6ce6a-b6a9-4197-a03b-0ff061b93947',4),(5,25,'b2468c4f-d22e-4a5c-9bb3-d083440e87fe','001',5),(6,396,'b2468c4f-d22e-4a5c-9bb3-d083440e87fe','002',66),(50,5000,'b265e127-49f8-4c61-a297-74a81f034e38','914afe24-1a9d-40ee-b7e7-d194a641c152',100),(600,24000,'b265e127-49f8-4c61-a297-74a81f034e38','ecaa3a3a-44e2-4a4e-bb5a-7bfc3c25a3df',40),(10,10000,'bc148fd7-1610-4804-ac6d-9e243f47f134','914afe24-1a9d-40ee-b7e7-d194a641c152',1000),(5,500,'bc148fd7-1610-4804-ac6d-9e243f47f134','ecaa3a3a-44e2-4a4e-bb5a-7bfc3c25a3df',100),(100,100000,'c3035198-79f0-4d24-bab1-2d708ded6cc9','001',1000),(67,5963,'c3035198-79f0-4d24-bab1-2d708ded6cc9','002',89),(3,18,'caea3e86-1139-45c8-bc57-ff73187ed114','e7f6ce6a-b6a9-4197-a03b-0ff061b93947',6),(10,550,'cebf2118-b8c4-4f7d-a1e1-30446d4b5d9c','001',55),(56,5600,'d96730dd-5790-4970-a439-ad821d65a0af','e7f6ce6a-b6a9-4197-a03b-0ff061b93947',100),(6,5400,'d96730dd-5790-4970-a439-ad821d65a0af','ecaa3a3a-44e2-4a4e-bb5a-7bfc3c25a3df',900),(1,1,'da2d2291-efaa-435d-94a4-cfc4b34d8b80','001',1);
/*!40000 ALTER TABLE `grn_stockitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grns`
--

DROP TABLE IF EXISTS `grns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grns` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `grn_no` varchar(100) NOT NULL,
  `amount` int NOT NULL,
  `supplier_name` varchar(100) NOT NULL,
  `reference_no` varchar(100) DEFAULT '0',
  `is_invoiced` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `supplier_name` (`supplier_name`),
  CONSTRAINT `grns_ibfk_1` FOREIGN KEY (`supplier_name`) REFERENCES `suppliers` (`supplier_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grns`
--

LOCK TABLES `grns` WRITE;
/*!40000 ALTER TABLE `grns` DISABLE KEYS */;
INSERT INTO `grns` VALUES ('123afe68-36b4-4d89-8bd9-3bba949b2f9f','2023-08-24 15:19:29','GRN/1059',13000,'Msee wa Jaba','0',1),('308fb126-0670-4b23-b3e1-91fc5f442afd','2023-08-25 09:10:22','GRN/1073',273,'JogooLimited','0',1),('43557598-7350-485f-bf9d-ed96aeb7f4b1','2023-08-25 08:35:48','GRN/1063',85,'JogooLimited','0',0),('46424cdf-2383-4439-a3e6-6ce1c33da02b','2023-08-29 09:01:37','GRN/1084',3015,'Msee wa Jaba','q34',0),('4690b74d-80fe-4009-9aec-5a8163847410','2023-08-25 09:44:12','GRN/1079',29,'JogooLimited','0',0),('4a089d3c-4669-44a2-a30d-661e3273749b','2023-08-24 12:23:02','GRN/1055',3000,'JogooLimited','0',0),('546aec50-640f-4776-ab7c-5aa666a9863b','2023-08-25 08:59:07','GRN/1068',1,'JogooLimited','0',0),('67a535eb-33ff-44dd-9097-98fce854e65c','2023-08-25 09:34:12','GRN/1074',814,'JogooLimited','0',0),('6b855b0d-4130-4996-8cc7-923c4214cfdf','2023-08-25 09:06:25','GRN/1070',9,'JogooLimited','0',0),('733f7f63-bc51-405a-ae72-e14175497c73','2023-08-24 12:32:46','GRN/1057',7524,'JogooLimited','0',0),('b2468c4f-d22e-4a5c-9bb3-d083440e87fe','2023-08-25 08:57:48','GRN/1066',421,'Msee wa Jaba','0',0),('b265e127-49f8-4c61-a297-74a81f034e38','2023-08-29 14:45:07','GRN/1087',29000,'Msee wa Jaba','1111',0),('bc148fd7-1610-4804-ac6d-9e243f47f134','2023-08-29 14:42:07','GRN/1086',10500,'Msee wa Jaba','5678909',NULL),('c3035198-79f0-4d24-bab1-2d708ded6cc9','2023-08-25 10:24:50','GRN/1081',105963,'JogooLimited','456',0),('caea3e86-1139-45c8-bc57-ff73187ed114','2023-08-25 15:57:30','GRN/1083',18,'Msee wa Jaba','45678',0),('cebf2118-b8c4-4f7d-a1e1-30446d4b5d9c','2023-08-25 09:09:16','GRN/1072',550,'JogooLimited','0',0),('d96730dd-5790-4970-a439-ad821d65a0af','2023-09-01 08:57:13','GRN/1112',11000,'Msee wa Jaba','9876',0),('da2d2291-efaa-435d-94a4-cfc4b34d8b80','2023-08-24 15:23:36','GRN/1061',1,'JogooLimited','0',0);
/*!40000 ALTER TABLE `grns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ledger_groups`
--

DROP TABLE IF EXISTS `ledger_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ledger_groups` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `group_name` varchar(100) NOT NULL,
  `description` varchar(250) DEFAULT NULL,
  `nature_of_group` enum('asset','liability','income','expense') NOT NULL,
  PRIMARY KEY (`id`,`group_name`),
  KEY `idx_group_name` (`group_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ledger_groups`
--

LOCK TABLES `ledger_groups` WRITE;
/*!40000 ALTER TABLE `ledger_groups` DISABLE KEYS */;
INSERT INTO `ledger_groups` VALUES ('001','2023-08-03 07:25:40','Accounts payable','','liability'),('002','2023-08-03 07:26:40','Accounts receivable','','asset'),('003','2023-08-03 07:27:40','Cash-in-hand','','asset'),('004','2023-08-03 07:28:40','Bank account','','asset'),('005','2023-08-03 07:29:40','Duties and taxes','','liability'),('006','2023-08-03 07:30:40','Mobile money(MPESA)','','asset'),('007','2023-08-03 07:31:40','Direct expenses','','expense'),('008','2023-08-03 07:32:40','Indirect expenses','','expense'),('009','2023-08-03 07:33:40','Fixed assets','','asset'),('010','2023-08-03 07:34:40','Direct income','','asset'),('011','2023-08-03 07:35:40','Indirect income','','asset'),('012','2023-08-03 07:36:40','Loans and advances(Asset)','','asset'),('013','2023-08-03 07:37:40','Loan(Liability)','','liability'),('014','2023-08-03 07:38:40','Misc Expenses','','expense'),('015','2023-08-03 07:39:40','Purchase accounts','','expense');
/*!40000 ALTER TABLE `ledger_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ledgers`
--

DROP TABLE IF EXISTS `ledgers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ledgers` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `account_no` varchar(100) NOT NULL,
  `ledger_name` varchar(100) NOT NULL,
  `ledger_opening_amount` int NOT NULL,
  `group_name` varchar(100) NOT NULL,
  `dr` int DEFAULT NULL,
  `cr` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ledger_name` (`ledger_name`),
  KEY `group_name` (`group_name`),
  CONSTRAINT `ledgers_ibfk_1` FOREIGN KEY (`group_name`) REFERENCES `ledger_groups` (`group_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ledgers`
--

LOCK TABLES `ledgers` WRITE;
/*!40000 ALTER TABLE `ledgers` DISABLE KEYS */;
INSERT INTO `ledgers` VALUES ('1c2f0fe2-e475-4f1a-9d7f-8592a30fe242','2023-08-04 14:19:13','0juu9','ssstttkkkl',1000,'Bank account',0,1000),('274ed836-91bf-4245-a276-c890fede8300','2023-08-04 14:10:40','0juu5','sssttt',999,'Bank account',0,999),('49cfa5f4-bc81-4bce-b39c-022bb71c87ba','2023-08-04 13:03:19','00test2345','hellno',1000,'Accounts payable',0,1000),('5e2d5ea2-4af5-4387-9f10-012b2202e8fe','2023-08-04 12:46:40','00test234','hell',1000,'Accounts payable',0,1000),('6d02e63e-3cf6-4592-8e91-8ecc16cc94fb','2023-08-04 14:23:04','0979889','oduo',800,'Duties and taxes',800,0),('756f7f17-950b-44e5-8c20-4e1b5a9af2e5','2023-08-04 12:36:36','00test23','tyvioou',1000,'Accounts payable',0,1000),('8bb2c17e-5cc5-439f-bc49-9f92bf3fcee6','2023-08-04 13:54:42','pot','',999,'Bank account',0,999),('aec0e1b3-b920-49ee-b94b-baf3f24e02cd','2023-08-04 14:17:26','0juu5','ssstttkk',999,'Bank account',0,999),('b35f172e-b867-4887-85df-2b8a65cabfdd','2023-08-04 10:57:30','00test','test',1000,'Accounts payable',0,1000),('d83be7cf-98ee-4b73-a3c3-ebb5c35002af','2023-08-04 14:05:16','0juu','klo',999,'Bank account',0,999),('f3c2fba7-2a21-4b8c-84fd-c87873b585cc','2023-08-04 14:21:10','09798','gee',80,'Duties and taxes',0,80),('fa609ce9-9d4f-48e5-abe1-aeba6200ce1f','2023-08-04 14:06:19','0juu','sss',999,'Bank account',0,999);
/*!40000 ALTER TABLE `ledgers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ledgers_transactions`
--

DROP TABLE IF EXISTS `ledgers_transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ledgers_transactions` (
  `ledger_id` varchar(100) NOT NULL,
  `transaction_id` varchar(100) NOT NULL,
  PRIMARY KEY (`ledger_id`,`transaction_id`),
  KEY `transaction_id` (`transaction_id`),
  CONSTRAINT `ledgers_transactions_ibfk_1` FOREIGN KEY (`ledger_id`) REFERENCES `ledgers` (`id`),
  CONSTRAINT `ledgers_transactions_ibfk_2` FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ledgers_transactions`
--

LOCK TABLES `ledgers_transactions` WRITE;
/*!40000 ALTER TABLE `ledgers_transactions` DISABLE KEYS */;
/*!40000 ALTER TABLE `ledgers_transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_items`
--

DROP TABLE IF EXISTS `menu_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu_items` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `item_name` varchar(100) NOT NULL,
  `price` int NOT NULL,
  `category_id` varchar(100) DEFAULT NULL,
  `uom_id` varchar(100) DEFAULT NULL,
  `state` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`,`item_name`),
  KEY `category_id` (`category_id`),
  KEY `uom_id` (`uom_id`),
  KEY `item_name_index` (`item_name`),
  CONSTRAINT `menu_items_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `menu_items_ibfk_2` FOREIGN KEY (`uom_id`) REFERENCES `uom` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_items`
--

LOCK TABLES `menu_items` WRITE;
/*!40000 ALTER TABLE `menu_items` DISABLE KEYS */;
INSERT INTO `menu_items` VALUES ('25407613-1346-4232-bc2a-fe22f58e35dd','2023-02-01 09:14:09','Beef',500,'5229e972-82d2-4b03-a98c-470d0d1adf96','46506f63-3abf-40b8-a1bb-cde6b5a6bd96','Active','provided','Red meet'),('27ea9a68-bdc8-46c7-95e5-5cf2da1fb255','2023-01-31 18:58:35','chicken fry',750,'5229e972-82d2-4b03-a98c-470d0d1adf96','926868c8-b82b-48d1-984f-20067dd50a40','Active','provided','Chicken broiler fry'),('3a7a0cc6-c2e0-4622-b0ca-1ba7d0fe8d89','2023-01-31 18:59:52','coffee',150,'5229e972-82d2-4b03-a98c-470d0d1adf96','7183ef55-206b-414f-a5d1-f3c5861cfb3c','Active','provided','Black highland coffee'),('4bb35b0c-9b9e-4531-9b90-3224c5682105','2023-01-31 19:00:22','Managu',300,'4eb77e32-6fef-4586-b36c-820cc6bd462f','46506f63-3abf-40b8-a1bb-cde6b5a6bd96','Active','provided','Traditional vegetable'),('9bed9e5a-5321-4d26-9dfa-0591b2e83563','2023-02-01 10:48:58','Fish',450,'5229e972-82d2-4b03-a98c-470d0d1adf96','926868c8-b82b-48d1-984f-20067dd50a40','Active','provided','fish'),('b995e763-2a4e-42f2-bdb5-5a06e9c2bbbe','2023-01-31 18:44:07','chapo',100,'dfc36ea7-c308-4f09-9b42-07016ea22057','926868c8-b82b-48d1-984f-20067dd50a40','Active','provided','White Chapati');
/*!40000 ALTER TABLE `menu_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_menuitem`
--

DROP TABLE IF EXISTS `order_menuitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_menuitem` (
  `item_name` varchar(100) NOT NULL,
  `order_number` int NOT NULL,
  `quantity` int NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`item_name`,`order_number`),
  KEY `order_number` (`order_number`),
  CONSTRAINT `order_menuitem_ibfk_1` FOREIGN KEY (`item_name`) REFERENCES `menu_items` (`item_name`),
  CONSTRAINT `order_menuitem_ibfk_2` FOREIGN KEY (`order_number`) REFERENCES `orders` (`order_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_menuitem`
--

LOCK TABLES `order_menuitem` WRITE;
/*!40000 ALTER TABLE `order_menuitem` DISABLE KEYS */;
INSERT INTO `order_menuitem` VALUES ('Beef',1009,1,500),('Beef',1010,1,500),('Beef',1011,2,1000),('Beef',1012,1,500),('Beef',1015,2,1000),('Beef',1016,1,500),('Beef',1017,1,500),('chapo',1002,1,100),('chapo',1003,1,100),('chapo',1005,3,300),('chapo',1006,3,300),('chapo',1013,1,100),('chapo',1014,1,100),('chicken fry',1003,1,750),('chicken fry',1004,1,750),('chicken fry',1005,2,1500),('chicken fry',1006,1,750),('chicken fry',1007,1,750),('chicken fry',1008,1,750),('chicken fry',1009,2,1500),('chicken fry',1010,2,1500),('chicken fry',1013,1,750),('chicken fry',1014,1,750),('chicken fry',1015,1,750),('chicken fry',1016,1,750),('chicken fry',1018,1,750),('chicken fry',1019,1,750),('coffee',1004,1,150),('coffee',1005,1,150),('coffee',1008,1,150),('coffee',1009,1,150),('coffee',1010,2,300),('coffee',1012,1,150),('coffee',1015,2,300),('coffee',1019,1,150),('coffee',1020,1,150),('coffee',1021,1,150),('Fish',1021,2,900),('Fish',1022,1,450),('Managu',1003,1,300),('Managu',1004,1,300),('Managu',1005,2,600),('Managu',1007,1,300),('Managu',1014,1,300),('Managu',1020,1,300),('Managu',1021,2,600),('Managu',1022,1,300);
/*!40000 ALTER TABLE `order_menuitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `order_number` int NOT NULL,
  `customer` varchar(100) NOT NULL,
  `waiter` varchar(100) NOT NULL,
  `table` varchar(100) NOT NULL,
  `counter` varchar(100) NOT NULL,
  `tender` varchar(100) NOT NULL,
  `total` int NOT NULL,
  `isPaid` varchar(100) DEFAULT NULL,
  `is_served` int DEFAULT '0',
  PRIMARY KEY (`id`,`order_number`),
  KEY `order_menuitem_ibfk_2` (`order_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('04f3bf3d-c339-4f25-aa00-c0f9db01d1ab','2023-02-01 05:16:21',1008,'0707607537','Gerald','T10','Billing Counter','CASH',900,'False',1),('103d1d2f-4e64-4d17-b7ae-0e71d3e83b1c','2023-07-23 16:41:55',1020,'0707607536','Gerald','T10','Billing Counter','CASH',450,'False',1),('15806085-43f3-4324-8074-3cc8b969947c','2023-07-26 12:09:32',1022,'0707607536','Gerald','T10','Billing Counter','CASH',750,'False',1),('2d2a4b83-f012-4901-a1fc-37452d9d32b6','2023-01-31 18:52:26',1002,'0707607527','Gerald','T10','Billing Counter','CASH',100,'False',1),('2e3a0932-3963-4a67-b9a2-73221636b4b6','2023-04-19 12:13:17',1013,'0707607527','Gerald','T10','Billing Counter','CASH',850,'False',1),('43ce829d-de27-46d3-963b-7c28ce2d8c72','2023-01-31 19:00:58',1003,'0700000000','Gerald','T10','Billing Counter','CASH',1150,'True',0),('599f559f-9ae9-4d1d-adcd-309755b2f7cd','2023-02-16 06:35:21',1011,'0707607527','Bobo','Table 5','Billing Counter','MPESA',1000,'False',0),('5f805abe-fdee-4397-a1b4-dc2b9c1d4ae5','2023-07-22 18:38:55',1017,'0707607527','Gerald','T10','Billing Counter','CASH',500,'False',1),('6d339615-27cc-4546-a44f-28e7158230f9','2023-07-26 08:31:13',1021,'0707607536','Gerald','T10','Billing Counter','CASH',1650,'False',1),('6d61f0b2-df74-4f8b-9985-de9f08646c8a','2023-07-03 02:17:37',1015,'0707607527','Gerald','T10','Billing Counter','CASH',2050,'False',1),('791b378a-62ca-4c2f-b2b2-7f1c3d6e115c','2023-02-01 09:17:41',1009,'0707607527','Gerald','T10','Billing Counter','CASH',2150,'False',0),('81b2b8d5-1fbe-4c6e-ae67-1b98d212bff8','2023-04-18 14:00:56',1012,'0707607527','Gerald','T10','Billing Counter','CASH',650,'False',0),('84ce343a-3c7a-4b58-8627-dce066216421','2023-07-23 16:13:34',1019,'0707607536','Gerald','T10','Billing Counter','CASH',900,'False',1),('9c89396e-0855-452d-8473-67ec36ec5804','2023-01-31 19:37:42',1004,'0707607527','Gerald','T10','Billing Counter','MPESA',1200,'False',1),('b1134469-6e6d-448a-ae14-c3487f3b9db2','2023-01-31 18:48:46',1001,'0707607527','Gerald','T10','Billing Counter','CASH',100,'True',0),('b5eb0946-f1e6-4112-af31-e16e6fc589c5','2023-01-31 23:20:40',1006,'0707607537','Gerald','T10','Billing Counter','CASH',1050,'False',1),('be5fc2da-1167-432a-9b6b-400837cda334','2023-01-31 19:39:57',1005,'0707607536','Gerald','T10','Billing Counter','CASH',2550,'True',0),('f0da7464-0331-4efb-9211-9e15db752d07','2023-07-22 18:40:05',1018,'0707607536','Gerald','T10','Billing Counter','CASH',750,'False',1),('f64bb63a-559f-4a11-b899-a8d5c278d6ca','2023-02-01 05:15:44',1007,'0707607527','Gerald','T10','Billing Counter','CASH',1050,'False',1),('fda8603c-28ac-4d39-84c0-5f2f825e3c17','2023-02-01 10:53:15',1010,'0707607536','Gerald','T10','Billing Counter','MPESA',2300,'False',1),('ff55c66a-ad82-4723-8c66-9c3cff7b3450','2023-07-03 02:18:47',1016,'0707607527','Gerald','T10','Billing Counter','CASH',1250,'False',0),('ffcd760d-90cf-412c-8a92-89944ed5608b','2023-04-19 15:50:59',1014,'0707607527','Bobo','Table 5','Billing Counter','CASH',1150,'False',0);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `amount_paid` int NOT NULL,
  `order_number` int NOT NULL,
  `transaction_id` varchar(100) NOT NULL,
  `tender_type` varchar(100) DEFAULT NULL,
  `user` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_number` (`order_number`),
  UNIQUE KEY `transaction_id` (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_invoice`
--

DROP TABLE IF EXISTS `purchase_invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_invoice` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `invoice_no` varchar(100) NOT NULL,
  `supplier_invoice_date` date DEFAULT NULL,
  `grn_no` varchar(100) NOT NULL,
  `supplier_name` varchar(100) NOT NULL,
  `reference_no` varchar(100) NOT NULL,
  `narration` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `grn_no` (`grn_no`),
  KEY `supplier_name` (`supplier_name`),
  CONSTRAINT `purchase_invoice_ibfk_1` FOREIGN KEY (`grn_no`) REFERENCES `grns` (`id`),
  CONSTRAINT `purchase_invoice_ibfk_2` FOREIGN KEY (`supplier_name`) REFERENCES `suppliers` (`supplier_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_invoice`
--

LOCK TABLES `purchase_invoice` WRITE;
/*!40000 ALTER TABLE `purchase_invoice` DISABLE KEYS */;
INSERT INTO `purchase_invoice` VALUES ('461825a3-881a-47d4-8d80-56707c6b81ae','2023-09-01 08:52:19','INV/1111','2023-09-01','123afe68-36b4-4d89-8bd9-3bba949b2f9f','Msee wa Jaba','0','lkjh/'),('d0c00fd6-a787-4ed4-9359-31e5ec23346b','2023-09-01 11:06:26','INV/1113','2023-09-01','308fb126-0670-4b23-b3e1-91fc5f442afd','JogooLimited','0','1073/');
/*!40000 ALTER TABLE `purchase_invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases`
--

DROP TABLE IF EXISTS `purchases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchases` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `transaction_no` varchar(100) NOT NULL,
  `grn_no` varchar(100) NOT NULL,
  `amount` int NOT NULL,
  `supplier_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grn_no` (`grn_no`),
  KEY `supplier_name` (`supplier_name`),
  CONSTRAINT `purchases_ibfk_1` FOREIGN KEY (`grn_no`) REFERENCES `grns` (`id`),
  CONSTRAINT `purchases_ibfk_2` FOREIGN KEY (`supplier_name`) REFERENCES `suppliers` (`supplier_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases`
--

LOCK TABLES `purchases` WRITE;
/*!40000 ALTER TABLE `purchases` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases_stockitems`
--

DROP TABLE IF EXISTS `purchases_stockitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchases_stockitems` (
  `quantity` int NOT NULL,
  `amount` int NOT NULL,
  `purchase_id` varchar(100) NOT NULL,
  `stockitems_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`purchase_id`),
  KEY `stockitems_id` (`stockitems_id`),
  CONSTRAINT `purchases_stockitems_ibfk_1` FOREIGN KEY (`purchase_id`) REFERENCES `purchases` (`id`),
  CONSTRAINT `purchases_stockitems_ibfk_2` FOREIGN KEY (`stockitems_id`) REFERENCES `stock_items` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases_stockitems`
--

LOCK TABLES `purchases_stockitems` WRITE;
/*!40000 ALTER TABLE `purchases_stockitems` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchases_stockitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_items`
--

DROP TABLE IF EXISTS `stock_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock_items` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `part_no` varchar(100) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `item_description` varchar(100) DEFAULT NULL,
  `base_unit` enum('pcs','dozen','bars','litres','boxes','kgs','ml') NOT NULL,
  `quantity` int DEFAULT '10',
  PRIMARY KEY (`id`),
  UNIQUE KEY `part_no` (`part_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_items`
--

LOCK TABLES `stock_items` WRITE;
/*!40000 ALTER TABLE `stock_items` DISABLE KEYS */;
INSERT INTO `stock_items` VALUES ('001','2023-01-31 18:56:42','UJ-2KG','Jogoo','Unga','pcs',10),('002','2023-01-31 18:56:50','CO-2L','Fresh Fry','Cooking Oil','pcs',10),('914afe24-1a9d-40ee-b7e7-d194a641c152','2023-08-08 09:27:55','water-500','500ml water','drinking water','boxes',10),('e7f6ce6a-b6a9-4197-a03b-0ff061b93947','2023-08-09 06:42:49','test-1','test','test item','pcs',10),('ecaa3a3a-44e2-4a4e-bb5a-7bfc3c25a3df','2023-08-08 09:07:18','s-0001','Soap','qwest','pcs',10);
/*!40000 ALTER TABLE `stock_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `account_no` varchar(100) NOT NULL,
  `supplier_name` varchar(100) NOT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `dr` int DEFAULT NULL,
  `cr` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `supplier_name` (`supplier_name`),
  KEY `idx_supplier_name` (`supplier_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES ('00s1','2023-01-31 18:57:48','s-001','JogooLimited','0707607527',0,0),('00s2','2023-01-31 18:57:49','s-002','Msee wa Jaba','0707607527',0,0);
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tables`
--

DROP TABLE IF EXISTS `tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tables` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `table_name` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `capacity` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_name` (`table_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tables`
--

LOCK TABLES `tables` WRITE;
/*!40000 ALTER TABLE `tables` DISABLE KEYS */;
INSERT INTO `tables` VALUES ('1','2023-01-11 06:10:29','T10','Roof Top',5),('6cc2724b-5ad2-42a4-affa-5a62c5cae1a0','2023-02-01 09:10:02','Table 5','Balcony',2),('6e9fa52b-d3ee-4102-af74-eaa6708eefdb','2023-02-16 06:27:47','t5','qwer',2),('838c2de8-4767-4af9-9282-9c359b678284','2023-02-01 10:45:27','Table 20','Balcony',2);
/*!40000 ALTER TABLE `tables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tender_types`
--

DROP TABLE IF EXISTS `tender_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tender_types` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `tender_name` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tender_name` (`tender_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tender_types`
--

LOCK TABLES `tender_types` WRITE;
/*!40000 ALTER TABLE `tender_types` DISABLE KEYS */;
INSERT INTO `tender_types` VALUES ('1','2023-01-10 06:10:29','CASH','Cash'),('2','2023-01-10 06:14:29','MPESA','Mobile Money');
/*!40000 ALTER TABLE `tender_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `date` date NOT NULL,
  `transaction_number` varchar(100) DEFAULT NULL,
  `amount` int NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `transaction_type` enum('dr','cr') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unique_numbers`
--

DROP TABLE IF EXISTS `unique_numbers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unique_numbers` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `number` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unique_numbers`
--

LOCK TABLES `unique_numbers` WRITE;
/*!40000 ALTER TABLE `unique_numbers` DISABLE KEYS */;
INSERT INTO `unique_numbers` VALUES ('1','2023-01-13 06:14:29','orders',1023);
/*!40000 ALTER TABLE `unique_numbers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uom`
--

DROP TABLE IF EXISTS `uom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uom` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `symbol` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uom`
--

LOCK TABLES `uom` WRITE;
/*!40000 ALTER TABLE `uom` DISABLE KEYS */;
INSERT INTO `uom` VALUES ('46506f63-3abf-40b8-a1bb-cde6b5a6bd96','2023-01-31 18:56:42','plt','plate'),('7183ef55-206b-414f-a5d1-f3c5861cfb3c','2023-01-31 18:56:55','cup','cup'),('7f2ea7cf-ff17-4c80-9bed-54f93cd86386','2023-02-16 06:30:40','yuii','dfg'),('926868c8-b82b-48d1-984f-20067dd50a40','2023-01-31 18:43:13','pcs','pieces'),('c8ec7b94-7919-4020-870a-776f52a40c78','2023-02-01 10:47:30','pckts','packets'),('ec53925b-6046-4523-8727-e3b41ecde069','2023-02-01 09:12:10','tst','test');
/*!40000 ALTER TABLE `uom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email_address` varchar(100) NOT NULL,
  `phone_number` int NOT NULL,
  `password` varchar(100) NOT NULL,
  `account_balance` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('14778603-cd9a-47fa-ba2b-e93e10482b37','2023-02-16 06:26:07','Gerald','Oduo','abc@gmail.com',707607527,'sha256$stQTZTZNgYiGYwqS$83e1b516d16f953e285087c30b9429f378051cfab0ebe42aecba92025c85a677',NULL),('6caaa6c8-3337-4d8d-a3c2-49edb342a642','2023-01-31 18:42:56','Gerald','Oduo','geraldoduo@gmail.com',707607527,'sha256$2YTlzC5qo2L3iawb$0e68443817d9edde8c0db92aec5cd1ff20384e0a0f40e4646db6ae5b7b10b4de',NULL),('b173f8ec-95ce-4a27-b7d4-7b87cc02b940','2023-02-01 09:05:07','musa','juma','musa@gmail.com',707070707,'sha256$ElT6C93vsh8ah967$29557bd264a0efd21652358a38e2acc1d041a6281eb5d481b26a0b7b39f120bc',NULL),('e32800bd-1776-461e-80d0-e82d9965d0e0','2023-02-01 10:43:55','musa','juma','jumamusa@gmail.com',707607527,'sha256$Yxjl5DbywvPzu0aA$ef694294d7a642153d20e83f79333040ec69dec5a481a9bd41b30391cf5bd290',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `waiter_table`
--

DROP TABLE IF EXISTS `waiter_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `waiter_table` (
  `waiter_id` varchar(60) NOT NULL,
  `table_id` varchar(60) NOT NULL,
  PRIMARY KEY (`waiter_id`,`table_id`),
  KEY `table_id` (`table_id`),
  CONSTRAINT `waiter_table_ibfk_1` FOREIGN KEY (`waiter_id`) REFERENCES `waiters` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `waiter_table_ibfk_2` FOREIGN KEY (`table_id`) REFERENCES `tables` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waiter_table`
--

LOCK TABLES `waiter_table` WRITE;
/*!40000 ALTER TABLE `waiter_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `waiter_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `waiters`
--

DROP TABLE IF EXISTS `waiters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `waiters` (
  `id` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email_address` varchar(100) NOT NULL,
  `phone_number` int NOT NULL,
  `passcode` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waiters`
--

LOCK TABLES `waiters` WRITE;
/*!40000 ALTER TABLE `waiters` DISABLE KEYS */;
INSERT INTO `waiters` VALUES ('1','2023-01-11 06:10:29','Gerald','Ochieng','gerald@gmail.com',707607527,'123'),('17d9ba1c-1587-479e-8d5e-33820e56b4b4','2023-02-01 10:46:43','Bobo','wangoi','bobo@gmail.com',707607527,'sha256$2I43VMkhfupk3s43$1980fa53a9d7e056a3b30fa5731c303d665647b84c7f8cda1d7da37b4c031c8e'),('cab7f099-500e-4224-970f-ef61cc54a5db','2023-02-01 09:11:06','Mary','Wangui','wangui@gmail.com',789045769,'sha256$rTwzoTuYirXiJZzG$cc2322a9b718655903bdf04e60bc0bb519e8e170d804d1dced77011a31eea921');
/*!40000 ALTER TABLE `waiters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-11 16:22:37

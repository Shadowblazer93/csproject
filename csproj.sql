-- MariaDB dump 10.19  Distrib 10.6.12-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: csproj
-- ------------------------------------------------------
-- Server version	10.6.12-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `rooms`
--
DROP DATABASE IF EXISTS `csproj`;
CREATE DATABASE `csproj`;
USE `csproj`;

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rooms` (
  `room` int(11) NOT NULL,
  `status` enum('vacant','occupied') DEFAULT NULL,
  `guest` varchar(100) DEFAULT NULL,
  `checkin` date DEFAULT NULL,
  `checkout` date DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `tab` int(11) DEFAULT NULL,
  PRIMARY KEY (`room`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES (101,'vacant',NULL,NULL,NULL,NULL,0),(102,'occupied','trump','2023-09-28','2023-09-29',15000,140),(103,'occupied','obama','2023-09-28','2023-09-30',5000,85),(201,'occupied','sussy backr','2023-11-21','2023-11-24',7500,285),(202,'occupied','rasam','2023-10-21','2023-10-23',5000,325),(203,'vacant',NULL,NULL,NULL,NULL,0),(301,'vacant',NULL,NULL,NULL,NULL,0),(302,'vacant',NULL,NULL,NULL,NULL,0),(303,'vacant',NULL,NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms_backup`
--

DROP TABLE IF EXISTS `rooms_backup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rooms_backup` (
  `room` int(11) NOT NULL,
  `status` enum('vacant','occupied') DEFAULT NULL,
  `guest` varchar(100) DEFAULT NULL,
  `checkin` date DEFAULT NULL,
  `checkout` date DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `tab` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms_backup`
--

LOCK TABLES `rooms_backup` WRITE;
/*!40000 ALTER TABLE `rooms_backup` DISABLE KEYS */;
INSERT INTO `rooms_backup` VALUES (101,'occupied','Azm','2023-09-28','2023-10-05',15000,60),(102,'occupied','azrrea','2023-09-28','2023-09-29',15000,140),(103,'occupied','arrerareoatuie','2023-09-28','2023-09-30',5000,85),(201,'occupied','sussy backr','2023-11-21','2023-11-24',7500,0),(202,'occupied','modi','2023-09-28','2023-09-30',5000,0),(203,'vacant',NULL,NULL,NULL,NULL,0),(301,'vacant',NULL,NULL,NULL,NULL,0),(302,'vacant',NULL,NULL,NULL,NULL,0),(303,'vacant',NULL,NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `rooms_backup` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-21 15:52:07

-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: videostream
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adminlogin`
--

DROP TABLE IF EXISTS `adminlogin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `adminlogin` (
  `adminid` int(11) NOT NULL,
  `emailid` varchar(45) NOT NULL,
  `adminname` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`adminid`,`emailid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adminlogin`
--

LOCK TABLES `adminlogin` WRITE;
/*!40000 ALTER TABLE `adminlogin` DISABLE KEYS */;
INSERT INTO `adminlogin` VALUES (100,'ss@gmail.com','Harry','123'),(200,'kk@gmail.com','Peter','123');
/*!40000 ALTER TABLE `adminlogin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `category` (
  `categoryid` int(11) NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(100) DEFAULT NULL,
  `description` text,
  `icon` text,
  PRIMARY KEY (`categoryid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (5,'Hindi Movies','Movies','bollywood.jpg'),(6,'English Movies','Movie','Hollywood.jpg'),(7,'TV Shows','TV Shows','Tvshows.jpg'),(8,'Sports','Sports','Sports.jpg');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientdetails`
--

DROP TABLE IF EXISTS `clientdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `clientdetails` (
  `mobilenumber` varchar(45) NOT NULL,
  `username` varchar(45) DEFAULT NULL,
  `age` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT 'deactivate',
  PRIMARY KEY (`mobilenumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientdetails`
--

LOCK TABLES `clientdetails` WRITE;
/*!40000 ALTER TABLE `clientdetails` DISABLE KEYS */;
INSERT INTO `clientdetails` VALUES ('9300003085','Foo','22','Female','deactivate'),('9301123085','Sandeep Sappal','44','Female','deactivate'),('9301123086','Hero','14','Male','deactivate'),('9301123087','Geeta','22','Female','deactivate'),('9301123089','James','22','Male','deactivate'),('9301123090','Chetan','22','Male','deactivate'),('9301123666','Harry','56','Male','activate'),('9752576100','Egg','22','Female','deactivate'),('9752576101','Spam','44','Female','deactivate'),('9752576105','Chetan','44','Male','deactivate');
/*!40000 ALTER TABLE `clientdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `episode`
--

DROP TABLE IF EXISTS `episode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `episode` (
  `episodeid` int(11) NOT NULL AUTO_INCREMENT,
  `categoryid` int(11) DEFAULT NULL,
  `showid` int(11) DEFAULT NULL,
  `episodenumber` int(11) DEFAULT NULL,
  `description` text,
  `poster` text,
  `trailer` text,
  `video` text,
  PRIMARY KEY (`episodeid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `episode`
--

LOCK TABLES `episode` WRITE;
/*!40000 ALTER TABLE `episode` DISABLE KEYS */;
INSERT INTO `episode` VALUES (4,7,14,1,'The Hunt','1.jpg','1.jpg','1.jpg'),(5,7,14,2,'The Hunt-Car Racing','1.jpg','1.jpg','1.jpg'),(6,7,15,1,'Crime in Mumbai','2.jpg','2.jpg','2.jpg');
/*!40000 ALTER TABLE `episode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shows`
--

DROP TABLE IF EXISTS `shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `shows` (
  `categoryid` int(11) NOT NULL,
  `showid` int(11) NOT NULL AUTO_INCREMENT,
  `showname` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `rating` varchar(45) DEFAULT NULL,
  `artist` text,
  `status` varchar(45) DEFAULT NULL,
  `showstatus` varchar(45) DEFAULT NULL,
  `episodes` int(11) DEFAULT NULL,
  `poster` text,
  `trailerurl` text,
  `videourl` text,
  PRIMARY KEY (`showid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shows`
--

LOCK TABLES `shows` WRITE;
/*!40000 ALTER TABLE `shows` DISABLE KEYS */;
INSERT INTO `shows` VALUES (5,3,'Tanaji','Action','Tanaji','2020','4','Ajay Devgan, Kajol etc','Trending','Active',1,'M1.jpg','M1.jpg','M1.jpg'),(5,4,'Baaghi 3','Action','Baaghi 3','2020','4','Tiger Shroff, Shraddha Kapoor','Trending','Active',1,'M2.jpg','1.mp4','1.mp4'),(5,5,'Housefull 4','Comedies','Housefull 4','2019','4','Akshay Kumar,Kiriti Senon,Kirti Karbanda etc','Trending','Active',1,'M3.jpg','M3.jpg','M3.jpg'),(5,6,'Chichhorre','Dramas','Chichhorre','2019','5','Shushant Singh,Shraddha Kapoor etc','Trending','Active',1,'M4.jpg','M4.jpg','M4.jpg'),(5,7,'Angreji Medium','Comedies','Angreji Medium','2020','5','Irfaan Khan,Kareena Kapoor','Trending','Active',1,'M5.jpg','2.mp4','2.mp4'),(5,8,'Mission Mangal','Dramas','Mission Mangal','2020','4','Akshay Kumar,Vidhya Balan etc','Trending','Active',1,'M6.jpg','M6.jpg','M6.jpg'),(5,9,'Dil Bechara','Romantic','Dil Bechara','2020','4','Shushant Singh, Sanjana  etc','Trending','Active',1,'M10.jpg','M10.jpg','M10.jpg'),(5,10,'Arjun Reddy','Romantic','Arjun Reddy','2020','4','Vijay, Alice Etc','Trending','Active',1,'M11.jpg','M11.jpg','M11.jpg'),(5,11,'Big Bull','Dramas','','2021','4','Abhishek Bachan, Vidhya Etc','Trending','Active',1,'M14.jpg','M14.jpg','M14.jpg'),(5,12,'Ms Dhoni','Dramas','Ms Dhoni','2019','5','','Trending','Active',1,'M12.jpg','M12.jpg','M12.jpg'),(5,13,'Total Dhamaal','Comedies','Total Dhamaal','2019','3','etc','Trending','Active',1,'M8.jpg','M8.jpg','M8.jpg'),(7,14,'The Hunt','Thriller','The Hunt','2021','3','James','New','Active',10,'1.jpg','1.jpg','1.jpg'),(7,15,'Crime Next Door','Thriller','Crime Next Door','2021','4','Akshay Kumar,Vidhya Balan etc','New','Active',6,'2.jpg','2.jpg','2.jpg'),(7,16,'Risky Ishq','Romantic','Risky Ishq','2021','4','James','Most Watched','Active',1,'3.jpg','3.jpg','3.jpg'),(7,17,'Murder Meri Jaan','Thriller','Murder Meri Jaan','2021','4','etc','New','Active',1,'4.jpg','4.jpg','4.jpg');
/*!40000 ALTER TABLE `shows` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-01 16:05:38

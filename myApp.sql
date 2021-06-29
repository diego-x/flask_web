-- MySQL dump 10.13  Distrib 5.5.61, for Linux (x86_64)
--
-- Host: localhost    Database: myApp
-- ------------------------------------------------------
-- Server version	5.5.61

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_active` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','pbkdf2:sha256:150000$uCa81Wug$53aa5eaabe785847af632583418551867a679cad62e2e92f8db5ae9b235bae3d',1);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picture`
--

DROP TABLE IF EXISTS `picture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picture` (
  `picture_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `index_src` varchar(128) NOT NULL,
  `real_Path` varchar(128) NOT NULL,
  `downloadurl` varchar(200) NOT NULL,
  `size` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`picture_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picture`
--

LOCK TABLES `picture` WRITE;
/*!40000 ALTER TABLE `picture` DISABLE KEYS */;
INSERT INTO `picture` VALUES (3,'测试图片','/static/user/bizhi/70eff4ae2c473da9213fde0b18c516c7.png','/static/upload/011028d760ec6090c9f53eaa68138cfb.jpg','/static/upload/011028d760ec6090c9f53eaa68138cfb.jpg','3840  x  2560','Sun Jun 27 18:48:34 2021'),(4,'测试图片','/static/user/bizhi/219cd10e60e29b12fdca121c1373ab77.png','/static/upload/b9d1cb8665a30600d040fb0cea206d0b.png','/static/upload/b9d1cb8665a30600d040fb0cea206d0b.png','3360  x  2100','Sun Jun 27 18:48:38 2021'),(6,'测试图片','/static/user/bizhi/12ebb21449dd58d9a12117b82276071f.png','/static/upload/834ef4068f268dee51507b377a8654ac.jpg','/static/upload/834ef4068f268dee51507b377a8654ac.jpg','2000  x  1332','Sun Jun 27 18:48:46 2021'),(8,'测试图片','/static/user/bizhi/a6661b31293acd46b8ba2d635c160854.png','/static/upload/7a0099add37b5137a8ef917b09f9acd6.jpg','/static/upload/7a0099add37b5137a8ef917b09f9acd6.jpg','5472  x  3648','Sun Jun 27 18:50:07 2021'),(9,'测试图片','/static/user/bizhi/fc7fd1652065392ea8bf58fcbf8be132.png','/static/upload/78b0c365dfef07c24991e8d64daf7998.png','/static/upload/78b0c365dfef07c24991e8d64daf7998.png','2560  x  1600','Sun Jun 27 18:50:12 2021'),(10,'测试图片','/static/user/bizhi/c828b007a5d5d9c3df0f9236204a2950.png','/static/upload/decf8c394de7cb799c05dc824f49838a.jpg','/static/upload/decf8c394de7cb799c05dc824f49838a.jpg','2000  x  1414','Sun Jun 27 18:50:35 2021'),(13,'测试图片','/static/user/bizhi/a572a0a1304538ea72594623eedd66fe.png','/static/upload/9f4e74f329fe415ddb1e2d9581af2ed7.jpg','/static/upload/9f4e74f329fe415ddb1e2d9581af2ed7.jpg','3840  x  2400','Sun Jun 27 18:50:52 2021'),(14,'测试图片','/static/user/bizhi/20c0cfc0aa86c7f22a44eea49547b0ab.png','/static/upload/03b3d45bb63f3f46e3c5413f75a4f080.jpg','/static/upload/03b3d45bb63f3f46e3c5413f75a4f080.jpg','2560  x  1600','Sun Jun 27 18:50:56 2021'),(17,'测试图片','/static/user/bizhi/5b9a791cf112c32e8046468d1565e80a.png','/static/upload/e2970f6ee1e098ea593036f5058c87ba.jpg','/static/upload/e2970f6ee1e098ea593036f5058c87ba.jpg','1200  x  750','Sun Jun 27 18:51:13 2021'),(19,'测试图片','/static/user/bizhi/a7ac22f2197d9df937c30a575eacbb0f.png','/static/upload/8009c522ed9e9119f0d259aef7a61359.jpg','/static/upload/8009c522ed9e9119f0d259aef7a61359.jpg','2560  x  1600','Sun Jun 27 18:54:22 2021'),(20,'测试图片','/static/user/bizhi/eafb8b557016c89d71248076e10944ef.png','/static/upload/6a318e52a787dba98a7191114749ddf8.jpg','/static/upload/6a318e52a787dba98a7191114749ddf8.jpg','3840  x  2560','Sun Jun 27 18:54:30 2021'),(21,'测试图片','/static/user/bizhi/8cc83c6fc14eb4fd7962839f7899d864.png','/static/upload/c402368874c7541accbdabf19e6010e0.jpg','/static/upload/c402368874c7541accbdabf19e6010e0.jpg','1920  x  1200','Sun Jun 27 18:54:37 2021'),(22,'测试图片','/static/user/bizhi/33615147b1ae825e952f21c754eff384.png','/static/upload/2ba09721869167037ff1ad2d06245f16.jpg','/static/upload/2ba09721869167037ff1ad2d06245f16.jpg','2723  x  1716','Sun Jun 27 18:54:42 2021'),(23,'测试图片','/static/user/bizhi/fda5d7af0a7fca51f8330d7c988bc82b.png','/static/upload/bb39271863a09e9b1af1d930d40ef130.jpg','/static/upload/bb39271863a09e9b1af1d930d40ef130.jpg','5120  x  3200','Sun Jun 27 18:54:51 2021'),(24,'测试图片','/static/user/bizhi/bf1f5738d861a4d3bb5ec4eb94759013.png','/static/upload/6f087b0731ef8bc8abbc26e23f0eab60.jpg','/static/upload/6f087b0731ef8bc8abbc26e23f0eab60.jpg','3648  x  2736','Sun Jun 27 18:54:56 2021'),(25,'测试图片','/static/user/bizhi/a0f508b01a9ea85e9105049d591d1811.png','/static/upload/3af722a6fea42fa1c79d1ac65b921ff1.jpg','/static/upload/3af722a6fea42fa1c79d1ac65b921ff1.jpg','2921  x  1873','Sun Jun 27 18:55:01 2021'),(26,'测试图片','/static/user/bizhi/f5ab6667e366c00186d146a40dcba5ab.png','/static/upload/2ab05c4e81c28f8bd42de4121f0e8d1a.jpg','/static/upload/2ab05c4e81c28f8bd42de4121f0e8d1a.jpg','1920  x  1200','Sun Jun 27 18:55:11 2021'),(28,'测试图片','/static/user/bizhi/7d03297dcf8df688b615567bad8fd8ba.png','/static/upload/7a0099add37b5137a8ef917b09f9acd6.jpg','/static/upload/7a0099add37b5137a8ef917b09f9acd6.jpg','5472  x  3648','Sun Jun 27 18:56:16 2021'),(30,'测试图片','/static/user/bizhi/a1670331ba57290f498871632de51d8c.png','/static/upload/7252045678e1901b18fe6853f85d301e.jpg','/static/upload/7252045678e1901b18fe6853f85d301e.jpg','2048  x  1367','Sun Jun 27 18:56:35 2021'),(31,'测试图片','/static/user/bizhi/3eaf2799ee076a0dc5ae17fd92ce79bb.png','/static/upload/4f7690acc4244a3a88675aedd22e0eec.jpg','/static/upload/4f7690acc4244a3a88675aedd22e0eec.jpg','1920  x  1200','Sun Jun 27 18:56:40 2021'),(32,'测试图片','/static/user/bizhi/3f00719a55fc8ea6e224c12234d41e16.png','/static/upload/ee92ba04e5e7ba3151e683b64aa8a796.jpg','/static/upload/ee92ba04e5e7ba3151e683b64aa8a796.jpg','5021  x  3200','Sun Jun 27 18:56:48 2021'),(33,'测试图片','/static/user/bizhi/baff444a9f88d340c1bbdf83f4acada2.png','/static/upload/b2ff06dbebf3d772a3e6e574919024b4.png','/static/upload/b2ff06dbebf3d772a3e6e574919024b4.png','1920  x  1200','Sun Jun 27 18:56:54 2021'),(34,'测试图片','/static/user/bizhi/590706749173b65a751c27d9b41031aa.png','/static/upload/f2cc5d3450236a331298ddc5a15f376f.jpg','/static/upload/f2cc5d3450236a331298ddc5a15f376f.jpg','8000  x  4988','Sun Jun 27 18:57:06 2021'),(35,'测试图片','/static/user/bizhi/714c68afd98787d660dd2187fd23f9d3.png','/static/upload/46542b3764d43134a41b87070bbea45c.jpg','/static/upload/46542b3764d43134a41b87070bbea45c.jpg','1200  x  750','Sun Jun 27 18:57:20 2021'),(36,'测试图片','/static/user/bizhi/4a7bc0fcf861789cd1a7e2600db142a9.png','/static/upload/3fbb28c590d726906efb4f3f319bfce0.jpg','/static/upload/3fbb28c590d726906efb4f3f319bfce0.jpg','2560  x  1600','Sun Jun 27 18:57:27 2021'),(37,'测试图片','/static/user/bizhi/f5a1e83b35679c78c14586d3ce31f7d0.png','/static/upload/7a5d2a1d92a1f280c4fc3f2188afb284.jpg','/static/upload/7a5d2a1d92a1f280c4fc3f2188afb284.jpg','2048  x  1365','Sun Jun 27 18:58:47 2021'),(38,'测试图片','/static/user/bizhi/cd59889de34d0e9c098dbdcefea6527b.png','/static/upload/a8248b1d0ec92d6199b5f83c57df11ad.jpg','/static/upload/a8248b1d0ec92d6199b5f83c57df11ad.jpg','1920  x  1200','Sun Jun 27 18:58:55 2021'),(40,'测试图片','/static/user/bizhi/92ad4415b7ce6adce62076497384d933.png','/static/upload/583b8c10612ca4f00de250b5553020d6.jpg','/static/upload/583b8c10612ca4f00de250b5553020d6.jpg','4096  x  2404','Sun Jun 27 18:59:14 2021'),(41,'测试图片','/static/user/bizhi/a2db11dc6ef2b5bdb774070b838bda9a.png','/static/upload/0624026dc12d07a556fbd2d60b6f03ef.jpg','/static/upload/0624026dc12d07a556fbd2d60b6f03ef.jpg','1920  x  1200','Sun Jun 27 18:59:23 2021'),(42,'测试图片','/static/user/bizhi/c4aebb8cf14b0c512432d7f6dce8f887.png','/static/upload/7a5d2a1d92a1f280c4fc3f2188afb284.jpg','/static/upload/7a5d2a1d92a1f280c4fc3f2188afb284.jpg','2048  x  1365','Sun Jun 27 18:59:31 2021'),(44,'测试图片','/static/user/bizhi/4515a88e12b6e55c95495c11a6b59b33.png','/static/upload/a143f8187eaabdf2052ac1394e3330fb.png','/static/upload/a143f8187eaabdf2052ac1394e3330fb.png','3000  x  2400','Sun Jun 27 18:59:54 2021'),(47,'测试图片','/static/user/bizhi/b07453c69a5a03078029816265998bbd.png','/static/upload/6dd08a0939ebc8bee1f9eeeb5419c5a9.jpg','/static/upload/6dd08a0939ebc8bee1f9eeeb5419c5a9.jpg','4435  x  2951','Sun Jun 27 19:00:41 2021'),(48,'测试图片','/static/user/bizhi/1bcc2509d7f09a5be260357ec4d68530.png','/static/upload/38ac8e51c06a2321ff38e3b362c30fbc.jpg','/static/upload/38ac8e51c06a2321ff38e3b362c30fbc.jpg','2880  x  1800','Sun Jun 27 19:00:50 2021'),(49,'测试图片','/static/user/bizhi/87d557fd171e3ea2ef9db8744e01d1f5.png','/static/upload/ff6648b3ef4d4d4d3360139498ea25f0.jpg','/static/upload/ff6648b3ef4d4d4d3360139498ea25f0.jpg','1920  x  1200','Sun Jun 27 19:00:59 2021'),(50,'测试图片','/static/user/bizhi/4f6066d7d1a78edc40b18c253e066bcb.png','/static/upload/d2a703954bb187aba65c6e61b66db47b.jpg','/static/upload/d2a703954bb187aba65c6e61b66db47b.jpg','2560  x  1600','Sun Jun 27 19:01:08 2021'),(51,'测试图片','/static/user/bizhi/851dff5057abb73dbd08d60906b907e5.png','/static/upload/6ae616a2682442a5d04679d9c41ddf09.png','/static/upload/6ae616a2682442a5d04679d9c41ddf09.png','1920  x  1250','Sun Jun 27 19:01:16 2021'),(52,'样例图','/static/user/bizhi/90c49659db213d9c90b65da0f0e20e8c.png','/static/upload/5fa1583babe1454d60d83fa8722c5d15.jpg','/static/upload/5fa1583babe1454d60d83fa8722c5d15.jpg','1920  x  1280','Sun Jun 27 19:04:40 2021'),(53,'样例图','/static/user/bizhi/f46b513e86bba57fc7cf06db43d12818.png','/static/upload/142f62d45adca3438072b020434a27a2.png','/static/upload/142f62d45adca3438072b020434a27a2.png','2598  x  1966','Sun Jun 27 19:04:49 2021'),(54,'样例图','/static/user/bizhi/513183d0d9fb8a3be640e2c70ec5dfb9.png','/static/upload/f7b3cd9264ecd09a094ea8b59178e760.jpg','/static/upload/f7b3cd9264ecd09a094ea8b59178e760.jpg','2500  x  1765','Sun Jun 27 19:04:58 2021'),(55,'样例图','/static/user/bizhi/1df8b596b097dcb06fb10fedea76a726.png','/static/upload/bd6deebfde09b39979acd5f37f13f730.jpg','/static/upload/bd6deebfde09b39979acd5f37f13f730.jpg','2000  x  1500','Sun Jun 27 19:05:11 2021');
/*!40000 ALTER TABLE `picture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_active` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'pictureadmin','pbkdf2:sha256:150000$uCa81Wug$53aa5eaabe785847af632583418551867a679cad62e2e92f8db5ae9b235bae3d',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-27 11:07:40

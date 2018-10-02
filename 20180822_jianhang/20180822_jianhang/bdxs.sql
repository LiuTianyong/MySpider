/*
Navicat MySQL Data Transfer

Source Server         : localdb
Source Server Version : 80003
Source Host           : localhost:3306
Source Database       : scrapyspider

Target Server Type    : MYSQL
Target Server Version : 80003
File Encoding         : 65001

Date: 2018-08-01 22:16:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bdxs
-- ----------------------------
DROP TABLE IF EXISTS `bdxs`;
CREATE TABLE `bdxs` (
  `title` varchar(255) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `abstract` varchar(255) DEFAULT NULL,
  `publish` varchar(255) DEFAULT NULL,
  `cite` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

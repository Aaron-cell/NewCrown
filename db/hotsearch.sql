/*
Navicat MySQL Data Transfer

Source Server         : NewCrown
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : newcrown

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2020-08-29 19:18:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for hotsearch
-- ----------------------------
DROP TABLE IF EXISTS `hotsearch`;
CREATE TABLE `hotsearch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt` datetime NOT NULL COMMENT '更新时间',
  `content` varchar(255) NOT NULL COMMENT '热搜数据',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

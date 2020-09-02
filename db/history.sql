/*
Navicat MySQL Data Transfer

Source Server         : NewCrown
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : newcrown

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2020-08-23 02:46:08
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history` (
  `ds` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '日期',
  `confirm` int(11) DEFAULT NULL COMMENT '累计确诊',
  `confirm_add` int(11) DEFAULT NULL COMMENT '当日新增确诊',
  `now_confirm` int(11) DEFAULT NULL COMMENT '现有确诊',
  `heal` int(11) DEFAULT NULL COMMENT '累计治愈',
  `heal_add` int(11) DEFAULT NULL COMMENT '当日新增治愈',
  `dead` int(11) DEFAULT NULL COMMENT '累计死亡',
  `dead_add` int(11) DEFAULT NULL COMMENT '当日新增死亡',
  PRIMARY KEY (`ds`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

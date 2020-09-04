/*
Navicat MySQL Data Transfer

Source Server         : NewCrown
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : newcrown

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2020-09-04 11:24:19
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
  `search_num` int(10) unsigned zerofill NOT NULL COMMENT '搜索次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

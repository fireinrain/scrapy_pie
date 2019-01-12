/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : javbus_db

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 12/01/2019 15:26:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for film_cover
-- ----------------------------
DROP TABLE IF EXISTS `film_cover`;
CREATE TABLE `film_cover`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `film_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '影片名',
  `film_code` tinytext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '番号',
  `film_url` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '影片url',
  `film_pub_date` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '发行日期',
  `film_cover_url` tinytext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT 'mini封面图',
  `extends1` int(11) NULL DEFAULT NULL COMMENT '扩展字段1',
  `extends2` tinytext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '扩展字段2',
  `create_date` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建时间',
  `update_date` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新时间',
  `enable_flag` int(11) NULL DEFAULT NULL COMMENT '是否可见 默认为1',
  `logic_delete` int(11) NULL DEFAULT NULL COMMENT '逻辑删除 默认为0，不是逻辑删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '影片封面' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

/*
 Navicat Premium Data Transfer

 Source Server         : Local
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : cmm

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 01/08/2019 18:36:05
*/

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for qrcode
-- ----------------------------
DROP TABLE IF EXISTS `leitores_qrcode`;
CREATE TABLE `leitores_qrcode`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `leitor_1` varchar(100)  NULL,
  `leitor_2` varchar(100)  NULL,
  `leitor_3` varchar(100)  NULL,
  `leitor_4` varchar(100)  NULL,
  `leitor_5` varchar(100)  NULL,
  `leitor_6` varchar(100)  NULL,
  `leitor_7` varchar(100)  NULL,
  `leitor_8` varchar(100)  NULL,
  `leitor_9` varchar(100)  NULL,
  `leitor_10` varchar(100)  NULL,
  `leitor_11` varchar(100)  NULL,
  `leitor_12` varchar(100)  NULL,
  `leitor_13` varchar(100)  NULL,
  `leitor_14` varchar(100)  NULL,
  `leitor_15` varchar(100)  NULL,
  `leitor_16` varchar(100)  NULL,
  `portao_1` varchar(100)  NULL,
  `portao_2` varchar(100)  NULL,
  `portao_3` varchar(100)  NULL,
  `portao_4` varchar(100)  NULL,
  `portao_5` varchar(100)  NULL,
  `portao_6` varchar(100)  NULL,
  `portao_7` varchar(100)  NULL,
  `portao_8` varchar(100)  NULL,
  `portao_9` varchar(100)  NULL,
  `portao_10` varchar(100)  NULL,
  `portao_11` varchar(100)  NULL,
  `portao_12` varchar(100)  NULL,
  `portao_13` varchar(100)  NULL,
  `portao_14` varchar(100)  NULL,
  `portao_15` varchar(100)  NULL,
  `portao_16` varchar(100)  NULL,
  `mensagem_1` varchar(100)  NULL,
  `mensagem_2` varchar(100)  NULL,
  `mensagem_3` varchar(100)  NULL,
  `mensagem_4` varchar(100)  NULL,
  `mensagem_5` varchar(100)  NULL,
  `mensagem_6` varchar(100)  NULL,
  `mensagem_7` varchar(100)  NULL,
  `mensagem_8` varchar(100)  NULL,
  `mensagem_9` varchar(100)  NULL,
  `mensagem_10` varchar(100)  NULL,
  `mensagem_11` varchar(100)  NULL,
  `mensagem_12` varchar(100)  NULL,
  `mensagem_13` varchar(100)  NULL,
  `mensagem_14` varchar(100)  NULL,
  `mensagem_15` varchar(100)  NULL,
  `mensagem_16` varchar(100)  NULL,
  PRIMARY KEY (`id`)
);

SET FOREIGN_KEY_CHECKS = 1;

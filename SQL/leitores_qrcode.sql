-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 24-Ago-2019 às 08:58
-- Versão do servidor: 10.1.38-MariaDB-0+deb9u1
-- PHP Version: 7.0.33-0+deb9u3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `CMM`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `leitores_qrcode`
--

CREATE TABLE `leitores_qrcode` (
  `id` int(11) NOT NULL,
  `leitor_1` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_2` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_3` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_4` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_5` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_6` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_7` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_8` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_9` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_10` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_11` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_12` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_13` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_14` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_15` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `leitor_16` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_1` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_2` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_3` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_4` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_5` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_6` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_7` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_8` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_9` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_10` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_11` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_12` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_13` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_14` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_15` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `portao_16` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_1` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_2` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_3` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_4` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_5` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_6` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_7` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_8` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_9` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_10` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_11` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_12` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_13` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_14` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_15` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mensagem_16` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `leitores_qrcode`
--

INSERT INTO `leitores_qrcode` (`id`, `leitor_1`, `leitor_2`, `leitor_3`, `leitor_4`, `leitor_5`, `leitor_6`, `leitor_7`, `leitor_8`, `leitor_9`, `leitor_10`, `leitor_11`, `leitor_12`, `leitor_13`, `leitor_14`, `leitor_15`, `leitor_16`, `portao_1`, `portao_2`, `portao_3`, `portao_4`, `portao_5`, `portao_6`, `portao_7`, `portao_8`, `portao_9`, `portao_10`, `portao_11`, `portao_12`, `portao_13`, `portao_14`, `portao_15`, `portao_16`, `mensagem_1`, `mensagem_2`, `mensagem_3`, `mensagem_4`, `mensagem_5`, `mensagem_6`, `mensagem_7`, `mensagem_8`, `mensagem_9`, `mensagem_10`, `mensagem_11`, `mensagem_12`, `mensagem_13`, `mensagem_14`, `mensagem_15`, `mensagem_16`) VALUES
(1, '172.20.9.111', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'social', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'arquivo_1.mp3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `leitores_qrcode`
--
ALTER TABLE `leitores_qrcode`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `leitores_qrcode`
--
ALTER TABLE `leitores_qrcode`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

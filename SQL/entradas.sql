-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 24-Ago-2019 às 08:57
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
-- Estrutura da tabela `entradas`
--

CREATE TABLE `entradas` (
  `id` int(11) NOT NULL,
  `in1` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `in2` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `in3` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `in4` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `in5` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `in6` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `in7` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `in8` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `a` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `b` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `c` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `d` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp1` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp2` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp3` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp4` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp5` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp6` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp7` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp8` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp9` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp10` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp11` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp12` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp13` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp14` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp15` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exp16` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `entradas`
--

INSERT INTO `entradas` (`id`, `in1`, `in2`, `in3`, `in4`, `in5`, `in6`, `in7`, `in8`, `a`, `b`, `c`, `d`, `exp1`, `exp2`, `exp3`, `exp4`, `exp5`, `exp6`, `exp7`, `exp8`, `exp9`, `exp10`, `exp11`, `exp12`, `exp13`, `exp14`, `exp15`, `exp16`) VALUES
(1, 'pm_social_externo', 'pm_social_interno', 'botao_saida_social_externo', '', '', '', '', '', '', '', '', '', 'garagem_terreo', 'gar_subsolo_1', 'gar_subsolo_3', '', '', '', '', '', '', '', '', '', '', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `entradas`
--
ALTER TABLE `entradas`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 24-Ago-2019 às 08:59
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
-- Estrutura da tabela `saidas`
--

CREATE TABLE `saidas` (
  `id` int(11) NOT NULL,
  `out1` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out2` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out3` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out4` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out5` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out6` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out7` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out8` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out9` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out10` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out11` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out12` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out13` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out14` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out15` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `out16` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `saidas`
--

INSERT INTO `saidas` (`id`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11`, `out12`, `out13`, `out14`, `out15`, `out16`) VALUES
(1, 'abre_social_externo', 'abre_social_interno', 'iluminacao_automatica_eclusa', '', '', '', '', '', '', '', '', '', '', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `saidas`
--
ALTER TABLE `saidas`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

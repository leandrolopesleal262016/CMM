-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 24-Ago-2019 às 09:00
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
-- Estrutura da tabela `status`
--

CREATE TABLE `status` (
  `in1` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `in2` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `in3` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `in4` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `in5` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `in6` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `in7` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `in8` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `inA` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `inB` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `inC` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `inD` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out1` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out2` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out3` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out4` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out5` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out6` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out7` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out8` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out9` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out10` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out11` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out12` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out13` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out14` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out15` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `out16` varchar(1) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `status`
--

INSERT INTO `status` (`in1`, `in2`, `in3`, `in4`, `in5`, `in6`, `in7`, `in8`, `inA`, `inB`, `inC`, `inD`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11`, `out12`, `out13`, `out14`, `out15`, `out16`) VALUES
('1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`in1`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

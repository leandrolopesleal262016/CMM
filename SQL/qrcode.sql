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
-- Estrutura da tabela `qrcode`
--

CREATE TABLE `qrcode` (
  `ID` varchar(20) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `apartamento` varchar(10) NOT NULL,
  `bloco` varchar(10) NOT NULL,
  `cond` varchar(10) NOT NULL,
  `hora_inicio` time(6) NOT NULL,
  `hora_final` time(6) NOT NULL,
  `data_inicio` date NOT NULL,
  `data_final` date NOT NULL,
  `dias_semana` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `qrcode`
--

INSERT INTO `qrcode` (`ID`, `nome`, `apartamento`, `bloco`, `cond`, `hora_inicio`, `hora_final`, `data_inicio`, `data_final`, `dias_semana`) VALUES
('36966957', 'Leandro', '11', 'B', '5410', '06:00:00.000000', '23:00:00.000000', '2019-02-18', '2019-12-29', '1111111');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `qrcode`
--
ALTER TABLE `qrcode`
  ADD PRIMARY KEY (`ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

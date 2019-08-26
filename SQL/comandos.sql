-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 24-Ago-2019 às 08:56
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
-- Estrutura da tabela `comandos`
--

CREATE TABLE `comandos` (
  `id` int(11) NOT NULL,
  `abre_social_externo` int(11) DEFAULT NULL,
  `abre_social_interno` int(11) DEFAULT NULL,
  `abre_garagem` int(11) DEFAULT NULL,
  `abre_subsolo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `comandos`
--

INSERT INTO `comandos` (`id`, `abre_social_externo`, `abre_social_interno`, `abre_garagem`, `abre_subsolo`) VALUES
(1, 1, 0, 1, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comandos`
--
ALTER TABLE `comandos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comandos`
--
ALTER TABLE `comandos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

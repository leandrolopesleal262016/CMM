-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 29-Nov-2019 às 08:07
-- Versão do servidor: 10.1.38-MariaDB-0+deb9u1
-- PHP Version: 7.0.33-0+deb9u6

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
  `abre_garagem1` int(11) DEFAULT NULL,
  `abre_garagem2` int(11) DEFAULT NULL,
  `abre_garagem3` int(11) NOT NULL,
  `reset` int(11) NOT NULL,
  `mudanca` int(11) NOT NULL,
  `audio` int(11) NOT NULL,
  `eventos` int(11) NOT NULL,
  `notifica` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `comandos`
--

INSERT INTO `comandos` (`id`, `abre_social_externo`, `abre_social_interno`, `abre_garagem1`, `abre_garagem2`, `abre_garagem3`, `reset`, `mudanca`, `audio`, `eventos`, `notifica`) VALUES
(1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `config`
--

CREATE TABLE `config` (
  `id` int(11) NOT NULL,
  `fechadura` varchar(20) DEFAULT NULL,
  `periodo` int(11) DEFAULT NULL,
  `audio` int(11) NOT NULL,
  `cliente` varchar(20) NOT NULL,
  `nome_cliente` varchar(20) NOT NULL,
  `ip_cliente` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `config`
--

INSERT INTO `config` (`id`, `fechadura`, `periodo`, `audio`, `cliente`, `nome_cliente`, `ip_cliente`) VALUES
(1, 'magnetica', 0, 1, '0054', 'Soho', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `entradas`
--

CREATE TABLE `entradas` (
  `id` int(11) NOT NULL DEFAULT '1',
  `in1` varchar(100) DEFAULT NULL,
  `in2` varchar(100) DEFAULT NULL,
  `in3` varchar(100) DEFAULT NULL,
  `in4` varchar(100) DEFAULT NULL,
  `in5` varchar(100) DEFAULT NULL,
  `in6` varchar(100) DEFAULT NULL,
  `in7` varchar(100) DEFAULT NULL,
  `in8` varchar(100) DEFAULT NULL,
  `a` varchar(100) DEFAULT NULL,
  `b` varchar(100) DEFAULT NULL,
  `c` varchar(100) DEFAULT NULL,
  `d` varchar(100) DEFAULT NULL,
  `exp1` varchar(100) DEFAULT NULL,
  `exp2` varchar(100) DEFAULT NULL,
  `exp3` varchar(100) DEFAULT NULL,
  `exp4` varchar(100) DEFAULT NULL,
  `exp5` varchar(100) DEFAULT NULL,
  `exp6` varchar(100) DEFAULT NULL,
  `exp7` varchar(100) DEFAULT NULL,
  `exp8` varchar(100) DEFAULT NULL,
  `exp9` varchar(100) DEFAULT NULL,
  `exp10` varchar(100) DEFAULT NULL,
  `exp11` varchar(100) DEFAULT NULL,
  `exp12` varchar(100) DEFAULT NULL,
  `exp13` varchar(100) DEFAULT NULL,
  `exp14` varchar(100) DEFAULT NULL,
  `exp15` varchar(100) DEFAULT NULL,
  `exp16` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `entradas`
--

INSERT INTO `entradas` (`id`, `in1`, `in2`, `in3`, `in4`, `in5`, `in6`, `in7`, `in8`, `a`, `b`, `c`, `d`, `exp1`, `exp2`, `exp3`, `exp4`, `exp5`, `exp6`, `exp7`, `exp8`, `exp9`, `exp10`, `exp11`, `exp12`, `exp13`, `exp14`, `exp15`, `exp16`) VALUES
(1, 'pm_social_interno', '', 'abre_social_externo', 'abre_social_interno', 'pm_social_externo', 'quebra_vidro_interno_eclusa', '', '', '', '', '', '', 'garagem1', 'garagem2', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `intertravamento`
--

CREATE TABLE `intertravamento` (
  `id` int(11) NOT NULL,
  `habilitado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `intertravamento`
--

INSERT INTO `intertravamento` (`id`, `habilitado`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `leitores_qrcode`
--

CREATE TABLE `leitores_qrcode` (
  `id` int(11) NOT NULL,
  `leitor_1` varchar(100) DEFAULT NULL,
  `leitor_2` varchar(100) DEFAULT NULL,
  `leitor_3` varchar(100) DEFAULT NULL,
  `leitor_4` varchar(100) DEFAULT NULL,
  `leitor_5` varchar(100) DEFAULT NULL,
  `leitor_6` varchar(100) DEFAULT NULL,
  `leitor_7` varchar(100) DEFAULT NULL,
  `leitor_8` varchar(100) DEFAULT NULL,
  `leitor_9` varchar(100) DEFAULT NULL,
  `leitor_10` varchar(100) DEFAULT NULL,
  `leitor_11` varchar(100) DEFAULT NULL,
  `leitor_12` varchar(100) DEFAULT NULL,
  `leitor_13` varchar(100) DEFAULT NULL,
  `leitor_14` varchar(100) DEFAULT NULL,
  `leitor_15` varchar(100) DEFAULT NULL,
  `leitor_16` varchar(100) DEFAULT NULL,
  `portao_1` varchar(100) DEFAULT NULL,
  `portao_2` varchar(100) DEFAULT NULL,
  `portao_3` varchar(100) DEFAULT NULL,
  `portao_4` varchar(100) DEFAULT NULL,
  `portao_5` varchar(100) DEFAULT NULL,
  `portao_6` varchar(100) DEFAULT NULL,
  `portao_7` varchar(100) DEFAULT NULL,
  `portao_8` varchar(100) DEFAULT NULL,
  `portao_9` varchar(100) DEFAULT NULL,
  `portao_10` varchar(100) DEFAULT NULL,
  `portao_11` varchar(100) DEFAULT NULL,
  `portao_12` varchar(100) DEFAULT NULL,
  `portao_13` varchar(100) DEFAULT NULL,
  `portao_14` varchar(100) DEFAULT NULL,
  `portao_15` varchar(100) DEFAULT NULL,
  `portao_16` varchar(100) DEFAULT NULL,
  `mensagem_1` varchar(100) DEFAULT NULL,
  `mensagem_2` varchar(100) DEFAULT NULL,
  `mensagem_3` varchar(100) DEFAULT NULL,
  `mensagem_4` varchar(100) DEFAULT NULL,
  `mensagem_5` varchar(100) DEFAULT NULL,
  `mensagem_6` varchar(100) DEFAULT NULL,
  `mensagem_7` varchar(100) DEFAULT NULL,
  `mensagem_8` varchar(100) DEFAULT NULL,
  `mensagem_9` varchar(100) DEFAULT NULL,
  `mensagem_10` varchar(100) DEFAULT NULL,
  `mensagem_11` varchar(100) DEFAULT NULL,
  `mensagem_12` varchar(100) DEFAULT NULL,
  `mensagem_13` varchar(100) DEFAULT NULL,
  `mensagem_14` varchar(100) DEFAULT NULL,
  `mensagem_15` varchar(100) DEFAULT NULL,
  `mensagem_16` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `leitores_qrcode`
--

INSERT INTO `leitores_qrcode` (`id`, `leitor_1`, `leitor_2`, `leitor_3`, `leitor_4`, `leitor_5`, `leitor_6`, `leitor_7`, `leitor_8`, `leitor_9`, `leitor_10`, `leitor_11`, `leitor_12`, `leitor_13`, `leitor_14`, `leitor_15`, `leitor_16`, `portao_1`, `portao_2`, `portao_3`, `portao_4`, `portao_5`, `portao_6`, `portao_7`, `portao_8`, `portao_9`, `portao_10`, `portao_11`, `portao_12`, `portao_13`, `portao_14`, `portao_15`, `portao_16`, `mensagem_1`, `mensagem_2`, `mensagem_3`, `mensagem_4`, `mensagem_5`, `mensagem_6`, `mensagem_7`, `mensagem_8`, `mensagem_9`, `mensagem_10`, `mensagem_11`, `mensagem_12`, `mensagem_13`, `mensagem_14`, `mensagem_15`, `mensagem_16`) VALUES
(1, '172.18.37.246', '172.18.37.245', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'eclusa', 'social', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `qrcode`
--

CREATE TABLE `qrcode` (
  `id` varchar(20) NOT NULL,
  `nome` varchar(20) DEFAULT NULL,
  `apartamento` varchar(10) DEFAULT NULL,
  `bloco` varchar(10) DEFAULT NULL,
  `cond` varchar(20) DEFAULT NULL,
  `hora_inicio` time(6) DEFAULT NULL,
  `hora_final` time(6) DEFAULT NULL,
  `data_inicio` date DEFAULT NULL,
  `data_final` date DEFAULT NULL,
  `dias_semana` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `qrcode`
--

INSERT INTO `qrcode` (`id`, `nome`, `apartamento`, `bloco`, `cond`, `hora_inicio`, `hora_final`, `data_inicio`, `data_final`, `dias_semana`) VALUES
('12345678', 'Leandro', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `qr_utilizado`
--

CREATE TABLE `qr_utilizado` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `qr_utilizado`
--

INSERT INTO `qr_utilizado` (`id`) VALUES
(12345678),
(13275502),
(23329063),
(35398440),
(40021293),
(66416765),
(88118448),
(90909135);

-- --------------------------------------------------------

--
-- Estrutura da tabela `saidas`
--

CREATE TABLE `saidas` (
  `id` int(11) NOT NULL,
  `out1` varchar(100) DEFAULT NULL,
  `out2` varchar(100) DEFAULT NULL,
  `out3` varchar(100) DEFAULT NULL,
  `out4` varchar(100) DEFAULT NULL,
  `out5` varchar(100) DEFAULT NULL,
  `out6` varchar(100) DEFAULT NULL,
  `out7` varchar(100) DEFAULT NULL,
  `out8` varchar(100) DEFAULT NULL,
  `out9` varchar(100) DEFAULT NULL,
  `out10` varchar(100) DEFAULT NULL,
  `out11` varchar(100) DEFAULT NULL,
  `out12` varchar(100) DEFAULT NULL,
  `out13` varchar(100) DEFAULT NULL,
  `out14` varchar(100) DEFAULT NULL,
  `out15` varchar(100) DEFAULT NULL,
  `out16` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `saidas`
--

INSERT INTO `saidas` (`id`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11`, `out12`, `out13`, `out14`, `out15`, `out16`) VALUES
(1, 'abre_social_externo', 'abre_social_interno', 'impede_abertura_externo', 'impede_abertura_interno', '', '', '', 'sirene', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `status`
--

CREATE TABLE `status` (
  `in1` varchar(1) NOT NULL,
  `in2` varchar(1) DEFAULT NULL,
  `in3` varchar(1) DEFAULT NULL,
  `in4` varchar(1) DEFAULT NULL,
  `in5` varchar(1) DEFAULT NULL,
  `in6` varchar(1) DEFAULT NULL,
  `in7` varchar(1) DEFAULT NULL,
  `in8` varchar(1) DEFAULT NULL,
  `inA` varchar(1) DEFAULT NULL,
  `inB` varchar(1) DEFAULT NULL,
  `inC` varchar(1) DEFAULT NULL,
  `inD` varchar(1) DEFAULT NULL,
  `out1` varchar(1) DEFAULT NULL,
  `out2` varchar(1) DEFAULT NULL,
  `out3` varchar(1) DEFAULT NULL,
  `out4` varchar(1) DEFAULT NULL,
  `out5` varchar(1) DEFAULT NULL,
  `out6` varchar(1) DEFAULT NULL,
  `out7` varchar(1) DEFAULT NULL,
  `out8` varchar(1) DEFAULT NULL,
  `out9` varchar(1) DEFAULT NULL,
  `out10` varchar(1) DEFAULT NULL,
  `out11` varchar(1) DEFAULT NULL,
  `out12` varchar(1) DEFAULT NULL,
  `out13` varchar(1) DEFAULT NULL,
  `out14` varchar(1) DEFAULT NULL,
  `out15` varchar(1) DEFAULT NULL,
  `out16` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `status`
--

INSERT INTO `status` (`in1`, `in2`, `in3`, `in4`, `in5`, `in6`, `in7`, `in8`, `inA`, `inB`, `inC`, `inD`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11`, `out12`, `out13`, `out14`, `out15`, `out16`) VALUES
('1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `user` varchar(60) DEFAULT NULL,
  `password` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `user`, `password`) VALUES
(1, 'admin', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comandos`
--
ALTER TABLE `comandos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `config`
--
ALTER TABLE `config`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `entradas`
--
ALTER TABLE `entradas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `intertravamento`
--
ALTER TABLE `intertravamento`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `leitores_qrcode`
--
ALTER TABLE `leitores_qrcode`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `qrcode`
--
ALTER TABLE `qrcode`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `qr_utilizado`
--
ALTER TABLE `qr_utilizado`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `saidas`
--
ALTER TABLE `saidas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`in1`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

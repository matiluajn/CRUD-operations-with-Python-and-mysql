-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 24-10-2022 a las 17:03:54
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.3.21
-- Issue : 3 - Santillan, Maximo Leandro

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `future`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

DROP TABLE IF EXISTS `estado`;
CREATE TABLE IF NOT EXISTS `estado` (
  `Id_Estado` int(4) NOT NULL AUTO_INCREMENT,
  `Nombre_Estado` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Estado`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `estado`
--

INSERT INTO `estado` (`Id_Estado`, `Nombre_Estado`) VALUES
(1, 'Venta'),
(2, 'Alquiler'),
(3, 'Prestamo'),
(4, 'Cesion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operatoriacomercial`
--

DROP TABLE IF EXISTS `operatoriacomercial`;
CREATE TABLE IF NOT EXISTS `operatoriacomercial` (
  `Id_OperatoriaComercial` int(4) NOT NULL AUTO_INCREMENT,
  `Nombre_OperatoriaComercial` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_OperatoriaComercial`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


--
-- Volcado de datos para la tabla `operatoriacomercial`
--

INSERT INTO `operatoriacomercial` ( `Nombre_OperatoriaComercial`) VALUES
('Sin_Operatoria'),
( 'Vendida'),
( 'Alquilada'),
( 'Prestada'),
( 'Cedida');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `propiedad`
--

DROP TABLE IF EXISTS `propiedad`;
CREATE TABLE IF NOT EXISTS `propiedad` (
  `Id_Propiedad` int(6) NOT NULL AUTO_INCREMENT,
  `Id_Tipo` int(4) NOT NULL,
  `Id_Estado` int(4) NOT NULL,
  `Id_OperatoriaComercial` int(4) NOT NULL,
  `Id_Propietario` int(6) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `Contacto` varchar(100) NOT NULL,
  PRIMARY KEY (`Id_Propiedad`),
  KEY `FK_Tipo` (`Id_Tipo`),
  KEY `FK_Estado` (`Id_Estado`),
  KEY `FK_OperatoriaComercial` (`Id_OperatoriaComercial`),
  KEY `FK_Propietario` (`Id_Propietario`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `propietario`
--

DROP TABLE IF EXISTS `propietario`;
CREATE TABLE IF NOT EXISTS `propietario` (
  `Id_Propietario` int(6) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `Contacto` varchar(100) NOT NULL,
  PRIMARY KEY (`Id_Propietario`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo`
--

DROP TABLE IF EXISTS `tipo`;
CREATE TABLE IF NOT EXISTS `tipo` (
  `Id_Tipo` int(4) NOT NULL AUTO_INCREMENT,
  `Nombre_Tipo` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Tipo`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo`
--

INSERT INTO `tipo` (`Id_Tipo`, `Nombre_Tipo`) VALUES
(1, 'Casa'),
(2, 'Departamento'),
(3, 'Campo'),
(4, 'Quinta'),
(5, 'Lote'),
(6, 'Galpon');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

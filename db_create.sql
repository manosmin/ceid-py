-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Φιλοξενητής: 127.0.0.1:3306
-- Χρόνος δημιουργίας: 09 Ιουν 2022 στις 14:33:01
-- Έκδοση διακομιστή: 5.7.26
-- Έκδοση PHP: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `python2022ceidcompilers`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `graph1`
--

DROP TABLE IF EXISTS `graph1`;
CREATE TABLE IF NOT EXISTS `graph1` (
  `date` varchar(255) DEFAULT NULL,
  `total_in_tons` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Άδειασμα δεδομένων του πίνακα `graph1`
--

INSERT INTO `graph1` (`date`, `total_in_tons`) VALUES
('2014', 213944),
('2015', 156190),
('2016', 147764),
('2017', 146914),
('2018', 149180),
('2019', 152221),
('2020', 152815),
('2021', 153065),
('2022', 16008);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `graph2`
--

DROP TABLE IF EXISTS `graph2`;
CREATE TABLE IF NOT EXISTS `graph2` (
  `type` varchar(255) DEFAULT NULL,
  `total_in_tons` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Άδειασμα δεδομένων του πίνακα `graph2`
--

INSERT INTO `graph2` (`type`, `total_in_tons`) VALUES
('Asphalt Debris', 60000),
('Bottle Bill', 30749),
('Curb Garbage', 763669),
('Curb Recycling', 134191),
('E-Waste', 3165),
('Haz Waste', 117),
('Misc. Garbage', 133025),
('Misc. Recycling', 41348),
('Recycled Tires', 2174),
('Scrap Metal', 33778),
('Sidewalk Debris', 5004),
('Yard Waste', 80881);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `graph3`
--

DROP TABLE IF EXISTS `graph3`;
CREATE TABLE IF NOT EXISTS `graph3` (
  `month` varchar(255) DEFAULT NULL,
  `total_in_tons` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Άδειασμα δεδομένων του πίνακα `graph3`
--

INSERT INTO `graph3` (`month`, `total_in_tons`) VALUES
('April', 104891),
('August', 110220),
('December', 179989),
('February', 78466),
('January', 89025),
('July', 105019),
('June', 113166),
('March', 86833),
('May', 120301),
('November', 92835),
('October', 102808),
('September', 104548);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

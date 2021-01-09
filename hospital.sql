

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `hospital`
--

-- --------------------------------------------------------

--
-- Структура таблицы `accounts`
--

-- IF NOT EXISTS `hospital`.`accounts`

CREATE TABLE IF NOT EXISTS `hospital`.`accounts` (
  `login` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `accounts`
--
CREATE user 'admin'@'%' identified by '123456';
GRANT SELECT, INSERT, DELETE, UPDATE, CREATE user on *.* TO 'admin'@'%';
FLUSH PRIVILEGES;
CREATE user 'basalai'@'%' identified by '654321';
GRANT SELECT on mydb.* TO 'basalai'@'%';
FLUSH PRIVILEGES;

INSERT INTO `accounts` (`login`, `password`, `role`) VALUES
('admin', '123456', 'admin'),
('basalai', '654321', 'regis');

-- --------------------------------------------------------

--
-- Структура таблицы `adress_area`
--

CREATE TABLE IF NOT EXISTS `hospital`.`adress_area` (
  `STREET` varchar(255) NOT NULL,
  `AREA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `adress_area`
--

INSERT INTO `adress_area` (`STREET`, `AREA`) VALUES
('Ленина', 1),
('Солнечная', 2),
('Ульяновская', 2);

-- --------------------------------------------------------

--
-- Структура таблицы `area`
--

CREATE TABLE IF NOT EXISTS `hospital`.`area` (
  `AREA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `area`
--

INSERT INTO `area` (`AREA`) VALUES
(1),
(2);

-- --------------------------------------------------------

--
-- Структура таблицы `description_disease`
--

CREATE TABLE IF NOT EXISTS `hospital`.`description_disease` (
  `DIAGNOSIS` varchar(255) NOT NULL,
  `SYMPTOMS` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `description_disease`
--

INSERT INTO `description_disease` (`DIAGNOSIS`, `SYMPTOMS`) VALUES
('Ветряная оспа ', 'Сыпь'),
('ОРВИ', 'Боль в горле'),
('ОРВИ', 'заложенность носа, насморк, выделения из носа');

-- --------------------------------------------------------

--
-- Структура таблицы `diagnos`
--

CREATE TABLE IF NOT EXISTS `hospital`.`diagnos` (
  `DIAGNOSIS` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `diagnos`
--

INSERT INTO `diagnos` (`DIAGNOSIS`) VALUES
('Ветряная оспа '),
('ОРВИ');

-- --------------------------------------------------------

--
-- Структура таблицы `diagnosis_of_the_patient`
--

CREATE TABLE IF NOT EXISTS `hospital`.`diagnosis_of_the_patient` (
  `FIO` varchar(255) NOT NULL,
  `DIAGNOSIS` varchar(255) NOT NULL,
  `DATE` datetime DEFAULT current_timestamp(),
  `patients_ID` int(11) NOT NULL,
  `patients_FIO` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `diagnosis_of_the_patient`
--

INSERT INTO `diagnosis_of_the_patient` (`FIO`, `DIAGNOSIS`, `DATE`, `patients_ID`, `patients_FIO`) VALUES
('Ветряная оспа ', 'Ветрянка', '2020-12-12 15:27:48', 0, 'Шмаков Леонид Васильевич'),
('ОРВИ', 'ОРВИ', '2020-12-08 21:18:47', 0, 'Матюх Арсений Иванович'),
('ОРВИ', 'ОРВИ', '2020-12-12 15:39:26', 0, 'Млынчик Дмитрий Иванович');

-- --------------------------------------------------------

--
-- Структура таблицы `doctors`
--

CREATE TABLE IF NOT EXISTS `hospital`.`doctors` (
  `AREA` int(11) NOT NULL,
  `DOCTOR_FIO` varchar(255) NOT NULL,
  `OFFICE` int(11) NOT NULL,
  `WORKTIME` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `doctors`
--

INSERT INTO `doctors` (`AREA`, `DOCTOR_FIO`, `OFFICE`, `WORKTIME`) VALUES
(2, 'Иванов Иван Иванович', 211, '8.00-13.00'),
(1, 'Хрящев Иван Петрович', 204, '8.00-13.00');

-- --------------------------------------------------------

--
-- Структура таблицы `medicaments`
--

CREATE TABLE IF NOT EXISTS `hospital`.`medicaments` (
  `DIAGNOSIS` varchar(255) NOT NULL,
  `MEDICINE` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `medicaments`
--

INSERT INTO `medicaments` (`DIAGNOSIS`, `MEDICINE`) VALUES
('Ветряная оспа ', 'Ацикловир'),
('ОРВИ', 'Гроприносин'),
('ОРВИ', 'Ибупрофен');

-- --------------------------------------------------------

--
-- Структура таблицы `patients`
--

CREATE TABLE IF NOT EXISTS `hospital`.`patients` (
  `FIO` varchar(255) NOT NULL,
  `STREET` varchar(50) NOT NULL,
  `HOME` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `patients`
--

INSERT INTO `patients` (`FIO`, `STREET`, `HOME`) VALUES
('Матюх Арсений Иванович', 'Ленина', 98),
('Млынчик Дмитрий Иванович', 'Ленина', 13),
('Тест Тест Тест', '1', 1),
('Тест2 т т', 'Ульяновская', 2),
('Шмаков Леонид Васильевич', 'Ленина', 99);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `adress_area`
--
ALTER TABLE `adress_area`
  ADD PRIMARY KEY (`STREET`,`AREA`),
  ADD KEY `AREA` (`AREA`);

--
-- Индексы таблицы `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`AREA`);

--
-- Индексы таблицы `description_disease`
--
ALTER TABLE `description_disease`
  ADD PRIMARY KEY (`DIAGNOSIS`,`SYMPTOMS`);

--
-- Индексы таблицы `diagnos`
--
ALTER TABLE `diagnos`
  ADD PRIMARY KEY (`DIAGNOSIS`);

--
-- Индексы таблицы `diagnosis_of_the_patient`
--
ALTER TABLE `diagnosis_of_the_patient`
  ADD PRIMARY KEY (`FIO`,`DIAGNOSIS`,`patients_ID`,`patients_FIO`),
  ADD KEY `fk_diagnosis_of_the_patient_patients1` (`patients_FIO`);

--
-- Индексы таблицы `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`DOCTOR_FIO`),
  ADD KEY `FIO_DOCTOR` (`AREA`);

--
-- Индексы таблицы `medicaments`
--
ALTER TABLE `medicaments`
  ADD PRIMARY KEY (`DIAGNOSIS`,`MEDICINE`);

--
-- Индексы таблицы `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`FIO`);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `adress_area`
--
ALTER TABLE `adress_area`
  ADD CONSTRAINT `AREA` FOREIGN KEY (`AREA`) REFERENCES `area` (`AREA`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Ограничения внешнего ключа таблицы `description_disease`
--
ALTER TABLE `description_disease`
  ADD CONSTRAINT `SYMPTOM` FOREIGN KEY (`DIAGNOSIS`) REFERENCES `diagnos` (`DIAGNOSIS`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Ограничения внешнего ключа таблицы `diagnosis_of_the_patient`
--
ALTER TABLE `diagnosis_of_the_patient`
  ADD CONSTRAINT `DIAGNOS` FOREIGN KEY (`FIO`) REFERENCES `diagnos` (`DIAGNOSIS`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_diagnosis_of_the_patient_patients1` FOREIGN KEY (`patients_FIO`) REFERENCES `patients` (`FIO`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Ограничения внешнего ключа таблицы `doctors`
--
ALTER TABLE `doctors`
  ADD CONSTRAINT `FIO_DOCTOR` FOREIGN KEY (`AREA`) REFERENCES `area` (`AREA`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Ограничения внешнего ключа таблицы `medicaments`
--
ALTER TABLE `medicaments`
  ADD CONSTRAINT `MEDICINE` FOREIGN KEY (`DIAGNOSIS`) REFERENCES `diagnos` (`DIAGNOSIS`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

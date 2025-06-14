CREATE TABLE `drivers`(
    `driverId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `driverRef` VARCHAR(255),
    `number` VARCHAR(255),
    `code` VARCHAR(255),
    `forename` VARCHAR(255),
    `surname` VARCHAR(255),
    `dob` TEXT,
    `nationality` VARCHAR(255)
);
CREATE TABLE `driver_standings`(
    `driverStandingsId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` INT UNSIGNED NOT NULL,
    `driverId` INT UNSIGNED NOT NULL,
    `points` INT,
    `position` INT,
    `positionText` TEXT,
    `wins` INT
);
CREATE TABLE `lap_times`(
    `raceId` INT UNSIGNED NOT NULL,
    `driverId` INT UNSIGNED NOT NULL,
    `lap` INT UNSIGNED NOT NULL,
    `position` INT,
    `time` TEXT,
    `milliseconds` INT,
    PRIMARY KEY(`raceId`,`driverId`,`lap`)
);
CREATE TABLE `pit_stops`(
    `raceId` INT UNSIGNED NOT NULL,
    `driverId` INT UNSIGNED NOT NULL,
    `stop` INT UNSIGNED NOT NULL,
    `lap` INT,
    `time` TEXT,
    `duration` DOUBLE,
    `milliseconds` INT,
    PRIMARY KEY(`raceId`,`driverId`,`stop`)
);
CREATE TABLE `qualifying`(
    `qualifyId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` INT UNSIGNED NOT NULL,
    `driverId` INT UNSIGNED NOT NULL,
    `constructorId` INT UNSIGNED NOT NULL,
    `number` INT,
    `position` INT,
    `q1` INT,
    `q2` INT,
    `q3` INT
);
CREATE TABLE `races`(
    `raceId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `year` INT,
    `round` INT,
    `circuitId` INT UNSIGNED NOT NULL,
    `name` TEXT,
    `date` TEXT,
    `time` TEXT
);
CREATE TABLE `results`(
    `resultId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` INT UNSIGNED NOT NULL,
    `driverId` INT UNSIGNED NOT NULL,
    `constructorId` INT UNSIGNED NOT NULL,
    `number` INT,
    `grid` INT,
    `position` TEXT,
    `points` INT,
    `laps` INT,
    `time` TEXT,
    `milliseconds` TEXT,
    `fastestLap` TEXT,
    `rank` TEXT
);
CREATE TABLE `constructors`(
    `constructorId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `constructorRef` TEXT,
    `name` TEXT,
    `nationality` TEXT
);
CREATE TABLE `constructor_results`(
    `constructorResultsId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` INT UNSIGNED NOT NULL,
    `constructorId` INT UNSIGNED NOT NULL,
    `points` INT
);
CREATE TABLE `constructor_standings`(
    `constructorStandingsId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` INT UNSIGNED NOT NULL,
    `constructorId` INT UNSIGNED NOT NULL,
    `points` INT,
    `position` INT,
    `wins` INT
);
CREATE TABLE `circuits`(
    `circuitId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `circuitRef` TEXT,
    `name` TEXT,
    `location` TEXT,
    `country` TEXT
);
ALTER TABLE
    `qualifying` ADD CONSTRAINT `qualifying_driverid_foreign` FOREIGN KEY(`driverId`) REFERENCES `drivers`(`driverId`);
ALTER TABLE
    `results` ADD CONSTRAINT `results_driverid_foreign` FOREIGN KEY(`driverId`) REFERENCES `drivers`(`driverId`);
ALTER TABLE
    `driver_standings` ADD CONSTRAINT `driver_standings_driverid_foreign` FOREIGN KEY(`driverId`) REFERENCES `drivers`(`driverId`);
ALTER TABLE
    `results` ADD CONSTRAINT `results_raceid_foreign` FOREIGN KEY(`raceId`) REFERENCES `races`(`raceId`);
ALTER TABLE
    `constructor_results` ADD CONSTRAINT `constructor_results_raceid_foreign` FOREIGN KEY(`raceId`) REFERENCES `races`(`raceId`);
ALTER TABLE
    `pit_stops` ADD CONSTRAINT `pit_stops_driverid_foreign` FOREIGN KEY(`driverId`) REFERENCES `drivers`(`driverId`);
ALTER TABLE
	`pit_stops` ADD CONSTRAINT `pit_stops_raceid_foregn` FOREIGN KEY(`raceId`) REFERENCES `races`(`raceId`);
ALTER TABLE 
	`lap_times` ADD CONSTRAINT `lap_times_driverid_foreign` FOREIGN KEY (driverId) REFERENCES drivers(driverId);
ALTER TABLE
	`lap_times` ADD CONSTRAINT `lap_times_raceid_foreign` FOREIGN KEY (raceId) REFERENCES races(raceId);
ALTER TABLE
    `races` ADD CONSTRAINT `races_circuitid_foreign` FOREIGN KEY(`circuitId`) REFERENCES `circuits`(`circuitId`);
ALTER TABLE
    `constructor_standings` ADD CONSTRAINT `constructor_standings_constructorid_foreign` FOREIGN KEY(`constructorId`) REFERENCES `constructors`(`constructorId`);
ALTER TABLE
    `constructor_standings` ADD CONSTRAINT `constructor_standings_raceid_foreign` FOREIGN KEY(`raceId`) REFERENCES `races`(`raceId`);
ALTER TABLE
    `driver_standings` ADD CONSTRAINT `driver_standings_raceid_foreign` FOREIGN KEY(`raceId`) REFERENCES `races`(`raceId`);
ALTER TABLE
    `constructor_results` ADD CONSTRAINT `constructor_results_constructorid_foreign` FOREIGN KEY(`constructorId`) REFERENCES `constructors`(`constructorId`);
ALTER TABLE
    `qualifying` ADD CONSTRAINT `qualifying_constructorid_foreign` FOREIGN KEY(`constructorId`) REFERENCES `constructors`(`constructorId`);
ALTER TABLE
    `results` ADD CONSTRAINT `results_constructorid_foreign` FOREIGN KEY(`constructorId`) REFERENCES `constructors`(`constructorId`);
ALTER TABLE
    `qualifying` ADD CONSTRAINT `qualifying_raceid_foreign` FOREIGN KEY(`raceId`) REFERENCES `races`(`raceId`);

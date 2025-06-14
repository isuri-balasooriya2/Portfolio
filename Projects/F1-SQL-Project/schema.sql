CREATE TABLE `drivers`(
    `driverId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `driverRef` VARCHAR(255) NOT NULL,
    `number` VARCHAR(255) NOT NULL,
    `code` VARCHAR(255) NOT NULL,
    `forename` VARCHAR(255) NOT NULL,
    `surname` VARCHAR(255) NOT NULL,
    `dob` DATE NOT NULL,
    `nationality` VARCHAR(255) NOT NULL
);
CREATE TABLE `driver_standings`(
    `driverStandingsId` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` BIGINT NOT NULL,
    `driverId` INT NOT NULL,
    `points` INT NOT NULL,
    `position` INT NOT NULL,
    `positionText` INT NULL,
    `wins` INT NOT NULL
);
CREATE TABLE `lap_times`(
    `raceId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `driverId` BIGINT NOT NULL,
    `lap` BIGINT NOT NULL,
    `position` BIGINT NOT NULL,
    `time` TIMESTAMP NOT NULL,
    `milliseconds` BIGINT NOT NULL,
    PRIMARY KEY(`driverId`)
);
CREATE TABLE `pit_stops`(
    `raceId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `driverId` BIGINT NOT NULL,
    `stop` BIGINT NOT NULL,
    `lap` BIGINT NOT NULL,
    `time` TIMESTAMP NOT NULL,
    `duration` DOUBLE NOT NULL,
    `milliseconds` BIGINT NOT NULL,
    PRIMARY KEY(`driverId`)
);
CREATE TABLE `qualifying`(
    `qualifyId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` BIGINT NOT NULL,
    `driverId` BIGINT NOT NULL,
    `constructorId` BIGINT NOT NULL,
    `number` BIGINT NOT NULL,
    `position` BIGINT NOT NULL,
    `q1` BIGINT NOT NULL,
    `q2` BIGINT NOT NULL,
    `q3` BIGINT NOT NULL
);
CREATE TABLE `races`(
    `raceId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `year` INT NOT NULL,
    `round` BIGINT NOT NULL,
    `circuitId` BIGINT NOT NULL,
    `name` BIGINT NOT NULL,
    `date` DATE NOT NULL,
    `time` TIMESTAMP NOT NULL
);
CREATE TABLE `results`(
    `resultId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` BIGINT NOT NULL,
    `driverId` BIGINT NOT NULL,
    `constructorId` BIGINT NOT NULL,
    `number` BIGINT NOT NULL,
    `grid` BIGINT NOT NULL,
    `position` TEXT NOT NULL,
    `points` BIGINT NOT NULL,
    `laps` BIGINT NOT NULL,
    `time` TEXT NOT NULL,
    `milliseconds` TEXT NOT NULL,
    `fastestLap` TEXT NOT NULL,
    `rank` TEXT NOT NULL
);
CREATE TABLE `constructors`(
    `constructorId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `constructorRef` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `nationality` TEXT NOT NULL
);
CREATE TABLE `constructor_results`(
    `constructorResultsId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` BIGINT NOT NULL,
    `constructorId` BIGINT NOT NULL,
    `points` BIGINT NOT NULL
);
CREATE TABLE `constructor_standings`(
    `constructorStandingsId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `raceId` BIGINT NOT NULL,
    `constructorId` BIGINT NOT NULL,
    `points` BIGINT NOT NULL,
    `position` BIGINT NOT NULL,
    `wins` BIGINT NOT NULL
);
CREATE TABLE `circuits`(
    `circuitId` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `circuitRef` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `location` TEXT NOT NULL,
    `country` TEXT NOT NULL
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
    `races` ADD CONSTRAINT `races_circuitid_foreign` FOREIGN KEY(`circuitId`) REFERENCES `circuits`(`circuitId`);
ALTER TABLE
    `drivers` ADD CONSTRAINT `drivers_driverid_foreign` FOREIGN KEY(`driverId`) REFERENCES `lap_times`(`driverId`);
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
ALTER TABLE
    `races` ADD CONSTRAINT `races_raceid_foreign` FOREIGN KEY(`raceId`) REFERENCES `lap_times`(`raceId`);
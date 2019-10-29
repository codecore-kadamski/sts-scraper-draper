DROP TABLE IF EXISTS `sports`;
CREATE TABLE IF NOT EXISTS `sports` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `sts_id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `url` VARCHAR(400) NOT NULL,
    UNIQUE (`name`, `sts_id`, `url`),
    UNIQUE KEY `sts_id_name_url` (`sts_id`,`name`,`url`),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;


DROP TABLE IF EXISTS `statistics`;
CREATE TABLE IF NOT EXISTS `statistics` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `sports_id` INT NOT NULL,
    `region_id` INT NOT NULL,
    `league_id` INT NOT NULL,
    `round` VARCHAR(100) NOT NULL,
    `date` VARCHAR(100) NOT NULL,
    `time` VARCHAR(100) NOT NULL,
    `match_id` VARCHAR(100) NOT NULL,
    `match` VARCHAR(100) NOT NULL,
    `half_time` VARCHAR(100) NOT NULL,
    `full_time` VARCHAR(100) NOT NULL,
    `finished` VARCHAR(100) NOT NULL,
    `ods_id` VARCHAR(100) NOT NULL,
    `url` VARCHAR(400) NOT NULL,
    UNIQUE (`name`, `sts_id`, `url`),
    UNIQUE KEY `sts_id_name_url` (`sts_id`,`name`,`url`),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;

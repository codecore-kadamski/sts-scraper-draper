CREATE TABLE IF NOT EXISTS `sports` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `sts_id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `url` VARCHAR(400) NOT NULL,
    UNIQUE (`name`, `sts_id`, `url`),
    UNIQUE KEY `sts_id_name_url` (`sts_id`,`name`,`url`),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;

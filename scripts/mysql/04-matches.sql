USE `stsparser`;
DROP TABLE IF EXISTS `matches`;
CREATE TABLE IF NOT EXISTS `matches` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `league_id` INT NOT NULL,
    `season` VARCHAR(100) DEFAULT NULL,
    `match_id` INT NOT NULL, #19094606
    `match_url` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL, #http://stats.betradar.com/s4/?clientid=66#2_1,3_257,22_1,5_66665,9_match,8_19094606,178_53064,7_5222
    `match_date` TIMESTAMP DEFAULT NULL,
    `match_time` TIMESTAMP DEFAULT NULL,
    `home_team` VARCHAR(100) DEFAULT NULL,
    `visitors_team` VARCHAR(100) DEFAULT NULL,
    `half_time` VARCHAR(10) DEFAULT NULL,
    `full_time` VARCHAR(10) DEFAULT NULL,
    `sys_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `sys_modified` TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;
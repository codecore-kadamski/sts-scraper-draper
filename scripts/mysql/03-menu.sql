USE `stsparser`;
DROP TABLE IF EXISTS `menu`;
CREATE TABLE IF NOT EXISTS `menu` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `sport` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
    `continent` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    `continent_url` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    `country` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    `country_url` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    `league` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    `league_url` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    `summary_url` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    `calendar_url` VARCHAR(400) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    `sys_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `sys_modified` TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    CONSTRAINT UC_summary UNIQUE (id,summary_url)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS outcomes
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          rand_number VARCHAR(150) NOT NULL,
                          win_lose VARCHAR(150) NOT NULL,
                          prize VARCHAR(150),
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `outcomes` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `outcomes` VALUES (1,'Test','TestOutcome','TESTPrize');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

CREATE TABLE IF NOT EXISTS users
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          first_name VARCHAR(30) NOT NULL,
                          last_name  VARCHAR(30) NOT NULL,
                          rand_number VARCHAR(150) NOT NULL,
                          win_lose VARCHAR(150) NOT NULL,
                          prize VARCHAR(150),
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Test','User','000','TestOutcome','');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

INSERT INTO genders (name)
VALUES ('male'), ('female');

INSERT INTO users (name, email, password, age, gender_id)
VALUES ('Boris', 'boris@test.com', 'password', 23, 1),
('Alina', 'alina@test.com', 'password', 32, 2),
('Maksim', 'maksim@test.com', 'password', 40, 1);

INSERT INTO contacts (name, email, phone, favorite, user_id)
VALUES ('Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
('Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
('Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
('Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
('Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, null);

SELECT id, name, email FROM contacts ORDER BY name;

SELECT id, name, email, age 
FROM users 
WHERE age BETWEEN 24 AND 39
ORDER BY name;

SELECT c.id, c.name, c.email 
FROM contacts AS c  
WHERE c.email LIKE '%co_%'
ORDER BY c.name;

-- Знайти кількість
SELECT COUNT(*)
FROM contacts c;

SELECT avg(age) as average_age
FROM users;

SELECT *
FROM contacts
WHERE user_id IN (SELECT id
					FROM users 
					WHERE age BETWEEN 24 AND 39);

SELECT *
FROM contacts c
INNER JOIN users u ON u.id = c.user_id;

UPDATE contacts SET user_id = 3  WHERE id = 5;

SELECT *
FROM contacts c
LEFT JOIN users u ON u.id = c.user_id;

ALTER TABLE users ADD telegram VARCHAR(50);
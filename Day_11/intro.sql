create table users(
	user_id Serial primary key,
	--serial for auto increment in integer, so we don't have to put number manually
	user_name varchar(20) not null,
	user_age int,
	user_ph_no varchar(10) unique,
	email varchar(20) unique
);

INSERT INTO users (user_name, user_age, user_ph_no, email)
VALUES 
('siva', 25, '1111111111', 'siva111@ai.com'),
('hari', 26, '2222222222', 'hari22@ai.com'),
('sivahari', 24, '3333333333', 'sivahari33@ai.com'),
('ram', 30, '4444444444', 'ram44@ai.com'),
('mara', 35, '5555555555', 'mara55@ai.com');

alter table users alter column user_ph_no type varchar(12);
-- to alter the constraint
ALTER TABLE users DROP CONSTRAINT user_ph_no;
ALTER TABLE users ADD UNIQUE (user_ph_no);
-- to check i work out this its give null value
update users set user_ph_no = null where user_name = 'ram'
select * from users
where user_age <=30

-- order by user_age asc;
order by user_name asc

show port;
-- it shows network port for PostgreSQL(we try to use PostgreSQL in vscode i need this network port to connect with it, to know that i use this code)
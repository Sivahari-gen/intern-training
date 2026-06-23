create table users(
	user_id Serial primary key,
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
select * from users
where user_age <=30

-- order by user_age asc;
order by user_name asc

show port;
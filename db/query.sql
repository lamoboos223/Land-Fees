mysql -u root -p

root

create database LandFees;

use LandFees;

CREATE TABLE NotifiedUsers (
    identity_number varchar(10) NOT NULL,
    instrument_number varchar(255) NOT NULL
);



INSERT INTO NotifiedUsers VALUES ("123412345", "123412345");
select * from NotifiedUsers;

drop table NotifiedUsers;

DELETE FROM NotifiedUsers WHERE identity_number=1234567890;

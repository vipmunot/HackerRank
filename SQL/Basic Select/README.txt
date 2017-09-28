Revising the Select Query I 

select * from CITY where COUNTRYCODE = 'USA' and POPULATION >100000

Revising the Select Query II

select name from CITY where COUNTRYCODE = 'USA' and POPULATION >120000

Select All

select * from city

Select By ID 

select * from city where ID = 1661

Japanese Cities' Attributes

select * from CITY where COUNTRYCODE = 'JPN'

Japanese Cities' Names 

select name from CITY where COUNTRYCODE = 'JPN'

Weather Observation Station 1

select city, state from station

Weather Observation Station 3

select distinct city from station where (id % 2) = 0;

Weather Observation Station 4

SELECT COUNT(City) - COUNT(DISTINCT City) FROM Station;

Weather Observation Station 5

SELECT MIN(CITY),LENGTH(CITY) FROM STATION GROUP BY LENGTH(CITY) ORDER BY LENGTH(CITY) limit 1; SELECT MIN(CITY),LENGTH(CITY) FROM STATION GROUP BY LENGTH(CITY) ORDER BY LENGTH(CITY) desc limit 1;

Weather Observation Station 6

select distinct city from station where city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%'
select distinct CITY from STATION where CITY RLIKE '^[AEIOU]'

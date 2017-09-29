### Revising the Select Query I 

select * from CITY where COUNTRYCODE = 'USA' and POPULATION >100000

### Revising the Select Query II

select name from CITY where COUNTRYCODE = 'USA' and POPULATION >120000

### Select All

select * from city

### Select By ID 

select * from city where ID = 1661

### Japanese Cities' Attributes

select * from CITY where COUNTRYCODE = 'JPN'

### Japanese Cities' Names 

select name from CITY where COUNTRYCODE = 'JPN'

### Weather Observation Station 1

select city, state from station

### Weather Observation Station 3

select distinct city from station where (id % 2) = 0;

### Weather Observation Station 4

SELECT COUNT(City) - COUNT(DISTINCT City) FROM Station;

### Weather Observation Station 5

SELECT MIN(CITY),LENGTH(CITY) FROM STATION GROUP BY LENGTH(CITY) ORDER BY LENGTH(CITY) limit 1; SELECT MIN(CITY),LENGTH(CITY) FROM STATION GROUP BY LENGTH(CITY) ORDER BY LENGTH(CITY) desc limit 1;

### Weather Observation Station 6

select distinct city from station where city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%'
<br>select distinct CITY from STATION where CITY RLIKE '^[AEIOU]'

### Weather Observation Station 7

select distinct city from station where city rlike '[aeiou]$'

### Weather Observation Station 8

select distinct city from station where city rlike '^[aeiou]' and city rlike '[aeiou]$'

### Weather Observation Station 9

select distinct city from station where city not in (select distinct city from station where city rlike '^[aeiou]')
<br>select distinct city from station where city rlike '^[^aeiou]'

### Weather Observation Station 10

select distinct city from station where city rlike '[^aeiou]$'

### Weather Observation Station 11

select distinct city from station where city rlike '[^aeiou]$' or city rlike '^[^aeiou]'

### Weather Observation Station 12

select distinct city from station where city rlike '[^aeiou]$' and city rlike '^[^aeiou]'

### Higher Than 75 Marks

select name from students where marks > 75 order by RIGHT(NAME, 3), id asc

### Employee Names

select name from employee order by name

### Employee Salaries

select name from employee where salary > 2000 and months < 10 order by employee_id
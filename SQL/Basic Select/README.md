### Revising the Select Query I 
```sql
select * from CITY where COUNTRYCODE = 'USA' and POPULATION >100000
```
### Revising the Select Query II
```sql
select name from CITY where COUNTRYCODE = 'USA' and POPULATION >120000
```
### Select All
```sql
select * from city
```
### Select By ID 
```sql
select * from city where ID = 1661
```
### Japanese Cities' Attributes
```sql
select * from CITY where COUNTRYCODE = 'JPN'
```
### Japanese Cities' Names 
```sql
select name from CITY where COUNTRYCODE = 'JPN'
```
### Weather Observation Station 1
```sql
select city, state from station
```
### Weather Observation Station 3
```sql
select distinct city from station where (id % 2) = 0;
```
### Weather Observation Station 4
```sql
SELECT COUNT(City) - COUNT(DISTINCT City) FROM Station;
```
### Weather Observation Station 5
```sql
SELECT MIN(CITY),LENGTH(CITY) FROM STATION GROUP BY LENGTH(CITY) ORDER BY LENGTH(CITY) limit 1; SELECT MIN(CITY),LENGTH(CITY) FROM STATION GROUP BY LENGTH(CITY) ORDER BY LENGTH(CITY) desc limit 1;
```
### Weather Observation Station 6
```sql
select distinct city from station where city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%'
```
```sql
select distinct CITY from STATION where CITY RLIKE '^[AEIOU]'
```
### Weather Observation Station 7
```sql
select distinct city from station where city rlike '[aeiou]$'
```
### Weather Observation Station 8
```sql
select distinct city from station where city rlike '^[aeiou]' and city rlike '[aeiou]$'
```
### Weather Observation Station 9
```sql
select distinct city from station where city not in (select distinct city from station where city rlike '^[aeiou]')
```
```sql
select distinct city from station where city rlike '^[^aeiou]'
```
### Weather Observation Station 10
```sql
select distinct city from station where city rlike '[^aeiou]$'
```
### Weather Observation Station 11
```sql
select distinct city from station where city rlike '[^aeiou]$' or city rlike '^[^aeiou]'
```
### Weather Observation Station 12
```sql
select distinct city from station where city rlike '[^aeiou]$' and city rlike '^[^aeiou]'
```
### Higher Than 75 Marks
```sql
select name from students where marks > 75 order by RIGHT(NAME, 3), id asc
```
### Employee Names
```sql
select name from employee order by name
```
### Employee Salaries
```sql
select name from employee where salary > 2000 and months < 10 order by employee_id
```
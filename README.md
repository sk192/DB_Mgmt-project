# Database Management System Implementation Project
README

## Members
- Divya Sravani Vukkusila
- Shweta Korulkar

### Description:-
We are developing a utility to data population for a Database Benchmark as recommended in “The Wisconsin Benchmark: Past, Present, and Future - David J. DeWitt, Computer Sciences Department, University of Wisconsin” . 

In a nutshell, we would be populating ONEKTUP, TENKTUP1  and  TENKTUP2 tables.  All of three tables with similar column structure and relations as below:-

``` text
CREATE TABLE TENKTUP1
( unique1 integer NOT NULL,			// random, 0 - (MAXTUPLES - 1)
  unique2 integer NOT NULL PRIMARY KEY,// sequential numbers
  two integer NOT NULL,			// unique1 mod 2
  four integer NOT NULL,			// unique1 mod 4
  ten integer NOT NULL,			// unique1 mod 10
  twenty integer NOT NULL,			// unique1 mod 20
  onePercent integer NOT NULL,		// unique1 mod 100
  tenPercent integer NOT NULL,		// unique1 mod 10
  twentyPercent integer NOT NULL,	// unique1 mod 5
  fiftyPercent integer NOT NULL,		// unique1 mod 2
  unique3 integer NOT NULL,			// unique1
  evenOnePercent integer NOT NULL,	// (onePercent * 2)
  oddOnePercent integer NOT NULL,	// (onePercent * 2) + 1
  stringu1 char(52) NOT NULL,		// convertIDToString(unique1)
  stringu2 char(52) NOT NULL,		// convertIDToString(unique2)
  string4 char(52) NOT NULL			// {A|H|O|V}*4 + x * 45
)
// convertIDToString(u: Integer) returns a string output is 
// based on the algorithm shared in the article.
```

### DB of choice:-
We chose to evaluate the script to populate on our local instance of PostGres Database. Due to our familiarity with PostGres local installation, interactions and diagnosis, we chose this option. With local Instance, we would have all the flexibility over tuning or controlling all the aspects of the DB compared to a cloud hosted or a remotely hosted PostGres. And Postgres provides better language support for Python and flexibility for user defined data types for any complex computation to be foreseen.


### Demonstration:-
We had populate 1000 rows for ONEKTUP table, 10000 rows for TENKTUP1, 10000 rows for TENKTUP2 and exported a sample of 50 rows for each table to csv files hosted at 
https://github.com/sk192/DB_Mgmt-project/blob/master/Data/ 

### Lessons learned:-


- On complex work-loads, PostgreSQL will be faster, but on simple primary key lookups MySQL with InnoDB will be faster.

### References:-
- The Wisconsin Benchmark: Past, Present, and Future - David J. DeWitt, Computer Sciences Department, University of Wisconsin
- Portland State University CS 587 course material
- www.python.org
- www.postgresql.org
- www.postgresqltutorial.com
- wiki.postgresql.org/wiki/Python


#!/usr/bin/python3

import psycopg2 

from psycopg2 import Error
import random
import sys, os, math
import traceback

def create_tables():
    conn = None

    try:
        conn = psycopg2.connect(user = "postgres",
                                password = "",
                                host = "localhost",
                                port = "5432",
                                database = "supplier")      # Connect to postgresql server
        cur = conn.cursor()
        commands = (

            """ CREATE table table1 (unique1 int UNIQUE, unique2 serial primary key, two int, four int,ten int,twenty int,onePercent int,
                    tenPercent int,fiftyPercent int,unique3 int UNIQUE , evenOnePercent int, oddOnePercent int, stringu1 varchar(60) Unique, stringu2 varchar(60) unique, string4 varchar(60))""",
            """ CREATE table table2 (unique1 int UNIQUE, unique2 serial primary key, two int, four int,ten int,twenty int,onePercent int,
                    tenPercent int,fiftyPercent int,unique3 int UNIQUE , evenOnePercent int, oddOnePercent int, stringu1 varchar(60) Unique, stringu2 varchar(60) unique,  string4 varchar(60)) """, 
            """ CREATE table table3 (unique1 int UNIQUE, unique2 serial primary key, two int, four int,ten int,twenty int,onePercent int,
                    tenPercent int,fiftyPercent int,unique3 int UNIQUE , evenOnePercent int, oddOnePercent int, stringu1 varchar(60) Unique, stringu2 varchar(60) unique, string4 varchar(60)) """
            )
        for command in commands:
            cur.execute(command)  
        cur.close()                          # Close communication with postgresql server 
        conn.commit()                        # commit the changes
    except Exception as e:
        traceback.print_exc()
    finally:
        if conn is not None:
            conn.close()

def generate_data_for_table1(n):
    
    conn = None
    try:
        conn = psycopg2.connect(user = "postgres",
                                password = "",
                                host = "localhost",
                                port = "5432",
                                database = "supplier")      # Connect to postgresql server
              
        cur2 = conn.cursor()
        unique_1_set = set()
        unique_3_set = set() 
        for i in range(n):
            unique1 = None  
            while True:
                unique1 = random.randint(0,n-1)
                if unique1 not in unique_1_set:
                    unique_1_set.add(unique1)
                    break
            unique2 = i
            two = unique1 % 2
            four = unique1 % 4
            ten = unique1 % 10
            twenty = unique1 % 20
            onePercent = unique1 % 100
            tenPercent = unique1 % 10
            fiftyPercent = unique1 % 2
            unique3 = None
            while True:
                unique3 = random.randint(0,n-1)
                if unique3 not in unique_3_set:
                    unique_3_set.add(unique3)
                    break
            evenOnePercent = (onePercent * 2)
            oddOnePercent = (onePercent * 2) + 1
            stringu1 = convertIDToString(unique1)
            stringu2 = convertIDToString(unique2)
            z = string4_generate(n)
            string4 = z[i]
            insert_data = """ INSERT INTO table1 (unique1, unique2,two,four,ten,twenty,onePercent,tenPercent,fiftyPercent,unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """      #---second step insert data
            data = (unique1, unique2, two,four,ten,twenty,onePercent,tenPercent,fiftyPercent,unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4)
            cur2.execute(insert_data, data)
        cur2.close()                          # Close communication with postgresql server 
        conn.commit()                        # commit the changes
    except Exception as e:
        traceback.print_exc()
    finally:
        if conn is not None:
            conn.close()


def generate_data_for_table2(m):

    conn = None
    try:
        conn = psycopg2.connect(user = "postgres",
                                    password = "",
                                    host = "localhost",
                                    port = "5432",
                                    database = "supplier")  
        cur1 = conn.cursor()
        unique_1_set = set()
        unique_3_set = set()
        for i in range(m):
            unique1 = None
            while True:
                unique1 = random.randint(0,m-1)
                if unique1 not in unique_1_set:
                    unique_1_set.add(unique1)
                    break
            unique2 = i
            two = unique1 % 2
            four = unique1 % 4
            ten = unique1 % 10
            twenty = unique1 % 20
            onePercent = unique1 % 100
            tenPercent = unique1 % 10
            fiftyPercent = unique1 % 2
            unique3 = None
            while True:
                unique3 = random.randint(0,m-1)
                if unique3 not in unique_3_set:
                    unique_3_set.add(unique3)
                    break
            evenOnePercent = (onePercent * 2)
            oddOnePercent = (onePercent * 2) + 1
            stringu1 = convertIDToString(unique1)
            stringu2 = convertIDToString(unique2)
            z = string4_generate(m)
            string4 = z[i]
            insert_data = """ INSERT INTO table2 (unique1, unique2,two,four,ten,twenty,onePercent,tenPercent,fiftyPercent,unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """     #---second step insert data
            data = (unique1, unique2, two,four,ten,twenty,onePercent,tenPercent,fiftyPercent,unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4)
            cur1.execute(insert_data, data)
        cur1.close()            # Close communication with postgresql server 
        conn.commit()           # commit the changes
    except Exception as e:
        traceback.print_exc()
    finally:
        if conn is not None:
            conn.close()
def generate_data_for_table3(o):

    conn = None
    try:
        conn = psycopg2.connect(user = "postgres",
                                    password = "",
                                    host = "localhost",
                                    port = "5432",
                                    database = "supplier")  
        cur3 = conn.cursor()
        unique_1_set = set()
        unique_3_set = set()
        l = 0
        for h in range(o):
            unique1 = None
            while True:
                unique1 = random.randint(0,o-1)
                if unique1 not in unique_1_set:
                    unique_1_set.add(unique1)
                    break
            unique2 = h
            two = unique1 % 2
            four = unique1 % 4
            ten = unique1 % 10
            twenty = unique1 % 20
            onePercent = unique1 % 100
            tenPercent = unique1 % 10
            fiftyPercent = unique1 % 2
            unique3 = None
            while True:
                unique3 = random.randint(0,o-1)
                if unique3 not in unique_3_set:
                    unique_3_set.add(unique3)
                    break
            evenOnePercent = (onePercent * 2)
            oddOnePercent = (onePercent * 2) + 1
            stringu1 = convertIDToString(unique1)
            stringu2 = convertIDToString(unique2)
            z = string4_generate(o)
            string4 = z[h]
            insert_data = """ INSERT INTO table3 (unique1, unique2,two,four,ten,twenty,onePercent,tenPercent,fiftyPercent,unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """     #---second step insert data
            data = (unique1, unique2, two,four,ten,twenty,onePercent,tenPercent,fiftyPercent,unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4)
            cur3.execute(insert_data, data)
        cur3.close()            # Close communication with postgresql server 
        conn.commit()           # commit the changes
    except Exception as e:
        traceback.print_exc()
    finally:
        if conn is not None:
            conn.close()
    
def convertIDToString(id):
    temp = [''] * 7
    result = [None] * 7
   
    for i in range(7):
        result[i] = 'A'
    i = 6
    while id > 0:
        rem = id % 26
        temp[i] = chr(ord('A') + rem) 
        id = id // 26
        i -= 1
        
    for j in range(i+1,7):
        result[j] = temp[j]
    for i in range(7, 53):
        result.append('x')
    q = ''.join(result)
    return q

def string4_generate(num):
    d = [] 
    n = num
    x = ['A', 'H', 'O', 'V']
    while num != 0:
        for j in x:
            if len(d) != n:
                d.append(j * 4 + 'x' * 45)
                num -= 1
            else:
                break
    return d

if __name__ == '__main__':

    create_tables()

    n = int(input("Enter number of rows for table 1: "))
    m = int(input("Enter number of rows for table 2: "))  
    o = int(input("Enter number of rows for table 3: "))
    generate_data_for_table1(n)
    generate_data_for_table2(m)
    generate_data_for_table3(o)
    



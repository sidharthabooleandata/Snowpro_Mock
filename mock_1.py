import streamlit as st

st.set_page_config(page_title="SnowPro Core Mock Exam", layout="centered")
st.title("🧠 Module 2: Snowflake Objects & SQL Essentials ")
st.markdown("Answer all 50 questions below. Submit at the end to view your score and the correct answers for incorrect ones.")

# List of questions with options and correct answer
questions = [
    {"question": "Q1. Which of the following SQL statements creates a new database in Snowflake?", "options": ["CREATE NEW DATABASE db1;", "CREATE DATABASE db1;", "MAKE DATABASE db1;", "INIT DATABASE db1;"], "answer": "CREATE DATABASE db1;"},
    {"question": "Q2. Which of the following table types does NOT retain data after session ends?", "options": ["Permanent", "Transient", "Temporary", "Materialized"], "answer": "Temporary"},
    {"question": "Q3. What is the default retention period for Time Travel on permanent tables?", "options": ["0 days", "1 day", "7 days", "30 days"], "answer": "7 days"},
    {"question": "Q4. Which command would you use to create a schema inside a database?", "options": ["CREATE NEW SCHEMA my_schema;", "MAKE SCHEMA my_schema;", "CREATE SCHEMA my_schema;", "INIT SCHEMA my_schema;"], "answer": "CREATE SCHEMA my_schema;"},
    {"question": "Q5. Which of these table types does NOT support Fail-safe?", "options": ["Temporary", "Permanent", "Transient", "None of the above"], "answer": "Temporary"},
    {"question": "Q6. What command is used to add data to an existing Snowflake table?", "options": ["ADD INTO", "INSERT INTO", "UPDATE TABLE", "MERGE INTO"], "answer": "INSERT INTO"},
    {"question": "Q7. Which keyword is used to remove all records from a table but keep its structure?", "options": ["DROP", "DELETE", "TRUNCATE", "CLEAR"], "answer": "TRUNCATE"},
    {"question": "Q8. How can you create a copy of a table's structure without data?", "options": ["CREATE TABLE clone FROM table1;", "CREATE TABLE table2 LIKE table1;", "DUPLICATE TABLE table1 TO table2;", "COPY STRUCTURE table1 INTO table2;"], "answer": "CREATE TABLE table2 LIKE table1;"},
    {"question": "Q9. What is the purpose of a MATERIALIZED VIEW in Snowflake?", "options": ["Stores only structure", "Precomputes and stores results", "Acts as a temp table", "Does not consume storage"], "answer": "Precomputes and stores results"},
    {"question": "Q10. Which view type always reflects real-time data from underlying tables?", "options": ["Static View", "Temp View", "Standard View", "Materialized View"], "answer": "Standard View"},
    {"question": "Q11. Which clause is used to filter results in SQL queries?", "options": ["GROUP BY", "WHERE", "ORDER BY", "SELECT"], "answer": "WHERE"},
    {"question": "Q12. Which of the following SQL statements creates a new sequence?", "options": ["CREATE SEQUENCE my_seq START 1;", "MAKE SEQUENCE my_seq;", "CREATE AUTO_INCREMENT my_seq;", "INIT SEQUENCE my_seq;"], "answer": "CREATE SEQUENCE my_seq START 1;"},
    {"question": "Q13. Which SQL command modifies data in an existing table?", "options": ["SELECT", "DELETE", "INSERT", "UPDATE"], "answer": "UPDATE"},
    {"question": "Q14. Which clause is used to join two tables?", "options": ["MATCH", "JOIN", "LINK", "CONNECT"], "answer": "JOIN"},
    {"question": "Q15. How do you create a temporary table in Snowflake?", "options": ["CREATE TEMPORARY TABLE my_table (...);", "CREATE SESSION TABLE my_table (...);", "CREATE TABLE TEMP my_table (...);", "CREATE TABLE TEMPORARILY my_table (...);"], "answer": "CREATE TEMPORARY TABLE my_table (...);"},
    {"question": "Q16. In Snowflake, what is the default table type if not specified?", "options": ["Temporary", "Permanent", "Transient", "External"], "answer": "Permanent"},
    {"question": "Q17. Which of the following is true about transient tables?", "options": ["Data is lost when session ends", "Data retained, no Fail-safe", "Always encrypted", "Stored in blob storage"], "answer": "Data retained, no Fail-safe"},
    {"question": "Q18. Which command retrieves all records from a table?", "options": ["SELECT * FROM table_name;", "FETCH ALL FROM table_name;", "VIEW table_name;", "SHOW ALL table_name;"], "answer": "SELECT * FROM table_name;"},
    {"question": "Q19. Which DML command removes specific records?", "options": ["DELETE", "TRUNCATE", "DROP", "REMOVE"], "answer": "DELETE"},
    {"question": "Q20. Which of the following is NOT a valid JOIN in Snowflake SQL?", "options": ["INNER JOIN", "OUTER JOIN", "SIDE JOIN", "LEFT JOIN"], "answer": "SIDE JOIN"},
    {"question": "Q21. Which Snowflake object is used to generate a unique sequence of numbers?", "options": ["Sequence", "View", "Schema", "Function"], "answer": "Sequence"},
    {"question": "Q22. What does the \"CREATE OR REPLACE TABLE\" statement do?", "options": ["Creates a backup", "Creates table if it doesn't exist", "Drops and recreates the table", "Creates a clone"], "answer": "Drops and recreates the table"},
    {"question": "Q23. What is the correct SQL syntax to update a record in Snowflake?", "options": ["MODIFY table_name ...", "UPDATE table_name SET col=value WHERE condition;", "CHANGE table_name SET ...", "ALTER VALUE table_name ..."], "answer": "UPDATE table_name SET col=value WHERE condition;"},
    {"question": "Q24. What does the command \"DROP TABLE my_table;\" do?", "options": ["Deletes only data", "Removes table and metadata", "Hides table", "Resets the table"], "answer": "Removes table and metadata"},
    {"question": "Q25. Which statement is used to combine rows from two tables including unmatched ones from both sides?", "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"], "answer": "FULL OUTER JOIN"},
    {"question": "Q26. What clause is used to sort SQL query results?", "options": ["ORDER BY", "SORT BY", "GROUP BY", "ARRANGE BY"], "answer": "ORDER BY"},
    {"question": "Q27. Which SQL command creates a user-defined function?", "options": ["CREATE FUNCTION", "NEW FUNCTION", "DEFINE FUNCTION", "INIT FUNCTION"], "answer": "CREATE FUNCTION"},
    {"question": "Q28. A primary key in Snowflake...", "options": ["Enforces uniqueness", "Automatically indexes", "Is mandatory", "Encrypts the column"], "answer": "Enforces uniqueness"},
    {"question": "Q29. In Snowflake, which statement returns metadata for a table?", "options": ["DESCRIBE TABLE my_table;", "INFO TABLE my_table;", "SHOW TABLE my_table;", "DETAIL TABLE my_table;"], "answer": "DESCRIBE TABLE my_table;"},
    {"question": "Q30. What does the following do: \"SELECT CURRENT_DATE;\"", "options": ["Returns Snowflake install date", "Returns today’s date", "Returns session expiry date", "Returns data load date"], "answer": "Returns today’s date"},
    {"question": "Q31. A transient table supports Time Travel up to how many days?", "options": ["0", "1", "7", "90"], "answer": "0"},
    {"question": "Q32. Which SQL command is used to define a column alias?", "options": ["DEFINE AS", "NAME AS", "AS", "RENAME"], "answer": "AS"},
    {"question": "Q33. What is a schema in Snowflake?", "options": ["A backup", "A view", "A namespace for objects", "An access control list"], "answer": "A namespace for objects"},
    {"question": "Q34. How do you retrieve distinct values from a column?", "options": ["SELECT UNIQUE column FROM table;", "SELECT DISTINCT column FROM table;", "SELECT column FROM table UNIQUE;", "SELECT ONLY column FROM table;"], "answer": "SELECT DISTINCT column FROM table;"},
    {"question": "Q35. How do you check existing databases in Snowflake?", "options": ["SHOW ALL DATABASES", "VIEW DATABASES", "SHOW DATABASES;", "SELECT * FROM DATABASES;"], "answer": "SHOW DATABASES;"},
    {"question": "Q36. Which clause is required for aggregation in SQL?", "options": ["GROUP BY", "FILTER BY", "JOIN BY", "AGGREGATE BY"], "answer": "GROUP BY"},
    {"question": "Q37. Which command will create a view in Snowflake?", "options": ["CREATE TABLE VIEW ...", "CREATE VIEW view_name AS SELECT ...", "CREATE VIRTUAL view_name", "CREATE DISPLAY view_name"], "answer": "CREATE VIEW view_name AS SELECT ..."},
    {"question": "Q38. Snowflake functions can be written in:", "options": ["JavaScript and SQL", "Python only", "Java only", "C++"], "answer": "JavaScript and SQL"},
    {"question": "Q39. A materialized view is best used when:", "options": ["You need real-time results", "You want to avoid storage cost", "You want to cache query results", "You want metadata only"], "answer": "You want to cache query results"},
    {"question": "Q40. Which of these is a valid Snowflake function?", "options": ["NEXTVAL(my_seq)", "NEXTVAL(my_table)", "INCREMENT(my_seq)", "GENERATE(my_seq)"], "answer": "NEXTVAL(my_seq)"},
    {"question": "Q41. What command gives the first 10 records from a query result?", "options": ["LIMIT 10", "FIRST 10", "FETCH 10", "RETURN 10"], "answer": "LIMIT 10"},
    {"question": "Q42. How would you rename a table in Snowflake?", "options": ["RENAME TO new_table", "ALTER TABLE old_table RENAME TO new_table;", "UPDATE TABLE old_table SET NAME new_table;", "MODIFY TABLE old_table TO new_table;"], "answer": "ALTER TABLE old_table RENAME TO new_table;"},
    {"question": "Q43. To change a column data type, which command is used?", "options": ["MODIFY", "CHANGE", "ALTER TABLE ... ALTER COLUMN", "UPDATE TYPE"], "answer": "ALTER TABLE ... ALTER COLUMN"},
    {"question": "Q44. What is the default behavior of CREATE OR REPLACE VIEW?", "options": ["Fails if view exists", "Drops existing and creates", "Creates if not exists", "Creates a temp view"], "answer": "Drops existing and creates"},
    {"question": "Q45. Which one is an aggregate function?", "options": ["COUNT", "SUBSTR", "GETDATE", "NEXTVAL"], "answer": "COUNT"},
    {"question": "Q46. Which Snowflake command grants object access?", "options": ["GRANT", "ALLOW", "PERMIT", "ENABLE"], "answer": "GRANT"},
    {"question": "Q47. How to list all tables in current schema?", "options": ["SHOW ALL TABLES", "SHOW TABLES;", "VIEW TABLES", "SELECT * FROM TABLES;"], "answer": "SHOW TABLES;"},
    {"question": "Q48. A view can be created from:", "options": ["Only one table", "Multiple tables", "Materialized Views only", "External files only"], "answer": "Multiple tables"},
    {"question": "Q49. Which clause is used to filter aggregated data?", "options": ["WHERE", "HAVING", "FILTER", "ORDER BY"], "answer": "HAVING"},
    {"question": "Q50. Which SQL statement is used to delete an existing database?", "options": ["REMOVE DATABASE", "DROP DATABASE", "DELETE DATABASE", "ERASE DATABASE"], "answer": "DROP DATABASE"}
]

if "submitted" not in st.session_state:
    st.session_state.submitted = False

user_answers = []

with st.form("exam_form"):
    for idx, q in enumerate(questions):
        user_answer = st.radio(q["question"], q["options"], key=f"q{idx}", index=None)
        user_answers.append(user_answer)
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state.submitted = True

if st.session_state.submitted:
    score = 0
    st.subheader("📊 Results")
    st.success(f"Your Score: {score} / {len(questions)}")

    for i, (q, user_answer) in enumerate(zip(questions, user_answers)):
        correct = q["answer"]
        if user_answer == correct:
            score += 1
        else:
            st.markdown(
                f"❌ **Question {i+1}: Incorrect**  \n"
                  
                
            )
  

import streamlit as st

st.set_page_config(page_title="SnowPro Core Mock Exam", layout="centered")
st.title("🧠 SnowPro Core Certification - Mock Exam")
st.markdown("Answer all 100 questions below. Submit at the end to view your score and correct answers.")

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

# Example questions list (use your full 50-question list)
questions = [
    {"question": "Q1. What happens when a warehouse is resized to a larger size in Snowflake?", "options": ["Running queries are terminated", "All running queries restart automatically", "Running queries benefit from increased resources", "A new warehouse is created"], "answer": "Running queries benefit from increased resources"},
    {"question": "Q2. Which system view helps analyze warehouse load and performance?", "options": ["QUERY_HISTORY", "WAREHOUSE_LOAD_HISTORY", "LOGIN_HISTORY", "SESSION_HISTORY"], "answer": "WAREHOUSE_LOAD_HISTORY"},
    {"question": "Q3. What is the effect of enabling auto-suspend in a virtual warehouse?", "options": ["It disables credit consumption", "It automatically resumes queries", "It suspends warehouse after inactivity", "It terminates all running queries immediately"], "answer": "It suspends warehouse after inactivity"},
    {"question": "Q4. Which parameter controls how long a warehouse waits before auto-suspending?", "options": ["MAX_CONCURRENCY_LEVEL", "AUTO_SUSPEND", "AUTO_RESUME", "QUEUE_TIMEOUT"], "answer": "AUTO_SUSPEND"},
    {"question": "Q5. What is the default behavior when a query is submitted to a suspended warehouse with auto-resume ON?", "options": ["The query fails", "The warehouse resumes and runs the query", "Query waits for manual resume", "Snowflake queues the query indefinitely"], "answer": "The warehouse resumes and runs the query"},
    {"question": "Q6. What is the key benefit of using multi-cluster warehouses in Snowflake?", "options": ["Faster billing", "Enhanced caching", "Scaling concurrency", "Improved semi-structured data parsing"], "answer": "Scaling concurrency"},
    {"question": "Q7. Which cache level stores query results for future reuse?", "options": ["Metadata cache", "Local cache", "Result cache", "Data cache"], "answer": "Result cache"},
    {"question": "Q8. When does the result cache become invalidated?", "options": ["If warehouse size is changed", "If the result is older than 1 hour", "If the underlying data changes", "If queries come from different users"], "answer": "If the underlying data changes"},
    {"question": "Q9. What happens when a warehouse reaches its MAX_CONCURRENCY_LEVEL?", "options": ["Queries fail", "Queries are queued", "Warehouse auto-scales", "Queries are terminated"], "answer": "Queries are queued"},
    {"question": "Q10. Which warehouse size provides the most compute power in Snowflake?", "options": ["X-Small", "Medium", "3X-Large", "Small"], "answer": "3X-Large"},
    {"question": "Q11. Which command helps reduce warehouse credits when not in use?", "options": ["ALTER WAREHOUSE SUSPEND", "DROP WAREHOUSE", "ALTER WAREHOUSE SET AUTO_RESUME = FALSE", "ALTER SESSION SET WAREHOUSE_IDLE = FALSE"], "answer": "ALTER WAREHOUSE SUSPEND"},
    {"question": "Q12. What kind of data can Snowflake natively parse using VARIANT data type?", "options": ["XML", "JSON", "Avro", "All of the above"], "answer": "All of the above"},
    {"question": "Q13. Which function is used to extract values from a VARIANT column?", "options": ["GET_JSON_OBJECT()", "TO_VARIANT()", "PARSE_JSON()", "GET_PATH()"], "answer": "GET_JSON_OBJECT()"},
    {"question": "Q14. What is the best format for storing semi-structured data in Snowflake?", "options": ["CSV", "VARIANT", "NUMBER", "TEXT"], "answer": "VARIANT"},
    {"question": "Q15. Which of the following is not considered semi-structured data?", "options": ["JSON", "Avro", "CSV", "Parquet"], "answer": "CSV"},
    {"question": "Q16. Which Snowflake data type can store image files?", "options": ["VARIANT", "TEXT", "STRING", "BINARY"], "answer": "BINARY"},
    {"question": "Q17. Which function converts a string to semi-structured JSON?", "options": ["TO_STRING()", "TO_VARIANT()", "PARSE_JSON()", "FLATTEN()"], "answer": "PARSE_JSON()"},
    {"question": "Q18. What is the function of FLATTEN in Snowflake?", "options": ["Convert XML to JSON", "Normalize CSV structure", "Flatten nested arrays in VARIANT", "Convert semi-structured to structured data"], "answer": "Flatten nested arrays in VARIANT"},
    {"question": "Q19. Which statement about VARIANT is correct?", "options": ["It can store only numeric values", "It's used only for structured data", "It stores semi-structured data like JSON or XML", "It automatically compresses text"], "answer": "It stores semi-structured data like JSON or XML"},
    {"question": "Q20. Which clause helps explode array objects into rows?", "options": ["JOIN", "SPLIT", "FLATTEN", "EXPAND"], "answer": "FLATTEN"},
    {"question": "Q21. Which data format is supported for loading unstructured files into Snowflake?", "options": ["ZIP", "BLOB", "FILE", "Any binary format"], "answer": "Any binary format"},
    {"question": "Q22. Which role has access to the MONITOR USAGE privilege?", "options": ["ACCOUNTADMIN", "SYSADMIN", "PUBLIC", "SECURITYADMIN"], "answer": "ACCOUNTADMIN"},
    {"question": "Q23. What does 'Warehouse Concurrency Scaling' help with?", "options": ["Query rewrite", "Auto resume", "Query queuing", "High parallel workload management"], "answer": "High parallel workload management"},
    {"question": "Q24. What determines whether a query can use result cache?", "options": ["Warehouse must be running", "Query must be identical", "Data must be unchanged", "All of the above"], "answer": "All of the above"},
    {"question": "Q25. Which caching layer sits closest to the storage layer?", "options": ["Result cache", "Local disk cache", "Metadata cache", "Remote cache"], "answer": "Local disk cache"},
    {"question": "Q26. What is the impact of auto-suspend = 0?", "options": ["The warehouse suspends immediately", "The warehouse never suspends", "It causes performance degradation", "It deletes warehouse"], "answer": "The warehouse suspends immediately"},
    {"question": "Q27. What happens to running queries when a warehouse is suspended?", "options": ["They fail immediately", "They continue until completion", "They pause", "They are queued"], "answer": "They continue until completion"},
    {"question": "Q28. Which Snowflake data type is best for flexible schemas?", "options": ["STRING", "VARIANT", "INTEGER", "OBJECT"], "answer": "VARIANT"},
    {"question": "Q29. Which is not a valid semi-structured format in Snowflake?", "options": ["Parquet", "JSON", "YAML", "Avro"], "answer": "YAML"},
    {"question": "Q30. How can you minimize warehouse cost with constant usage?", "options": ["Increase cache use", "Disable auto-suspend", "Schedule usage to off hours", "Set small size with auto-scale"], "answer": "Set small size with auto-scale"},
    {"question": "Q31. What is the key feature of semi-structured data?", "options": ["Fixed schema", "Row-column format", "Hierarchical and nested", "Requires transformation before storage"], "answer": "Hierarchical and nested"},
    {"question": "Q32. Which command is used to load semi-structured data in Snowflake?", "options": ["COPY INTO … FILE FORMAT = (TYPE = JSON)", "INSERT INTO … FORMAT=VARIANT", "PUT INTO … WITH FORMAT=AVRO", "COPY FROM JSON TO VARIANT"], "answer": "COPY INTO … FILE FORMAT = (TYPE = JSON)"},
    {"question": "Q33. Which system view provides warehouse credit usage?", "options": ["WAREHOUSE_LOAD_HISTORY", "WAREHOUSE_METERING_HISTORY", "QUERY_HISTORY", "CREDITS_HISTORY"], "answer": "WAREHOUSE_METERING_HISTORY"},
    {"question": "Q34. What is the effect of increasing the cluster count in a multi-cluster warehouse?", "options": ["Lower latency", "Higher storage", "Higher concurrency support", "More caching layers"], "answer": "Higher concurrency support"},
    {"question": "Q35. What is the best practice when using auto-scale multi-cluster warehouses?", "options": ["Set MIN_CLUSTER = MAX_CLUSTER", "Disable auto-suspend", "Use AUTO_RESUME = FALSE", "Always set to Medium size"], "answer": "Set MIN_CLUSTER = MAX_CLUSTER"},
    {"question": "Q36. When should you prefer VARIANT over OBJECT data type?", "options": ["When you need fixed keys", "When the structure changes frequently", "When only text is needed", "When you need relational joins"], "answer": "When the structure changes frequently"},
    {"question": "Q37. FLATTEN can be used with which clause?", "options": ["GROUP BY", "LATERAL", "UNION", "CREATE"], "answer": "LATERAL"},
    {"question": "Q38. How is semi-structured data stored internally in Snowflake?", "options": ["As plain text", "As compressed binary columnar", "As relational row-based", "As Parquet"], "answer": "As compressed binary columnar"},
    {"question": "Q39. What file formats are supported for external tables in Snowflake?", "options": ["Only CSV", "Only JSON", "JSON, Parquet, ORC, Avro", "Only structured formats"], "answer": "JSON, Parquet, ORC, Avro"},
    {"question": "Q40. Which privilege is needed to monitor warehouse usage?", "options": ["USAGE", "MONITOR", "VIEW", "SELECT"], "answer": "MONITOR"},
    {"question": "Q41. What happens when auto-scale is enabled and queries are queued?", "options": ["A new cluster spins up", "Queries fail", "Queries are rerouted", "Warehouse auto-resumes"], "answer": "A new cluster spins up"},
    {"question": "Q42. What Snowflake feature separates storage and compute?", "options": ["Virtual warehouse", "Snowpipe", "Time Travel", "Secure share"], "answer": "Virtual warehouse"},
    {"question": "Q43. What happens if multiple users query the same result set?", "options": ["Cached result is reused", "Separate warehouse is launched", "Cache is cleared", "The query is re-run each time"], "answer": "Cached result is reused"},
    {"question": "Q44. What does the OBJECT data type represent in Snowflake?", "options": ["JavaScript class", "Key-value pair structure", "Row from a table", "Only structured columns"], "answer": "Key-value pair structure"},
    {"question": "Q45. Which clause is necessary when accessing nested JSON in Snowflake?", "options": ["INFER", "LATERAL FLATTEN", "EXPAND JSON", "OUTER APPLY"], "answer": "LATERAL FLATTEN"},
    {"question": "Q46. In which case would result cache NOT be used?", "options": ["Data unchanged, same query", "Same user", "Underlying data changed", "Query executed within 24h"], "answer": "Underlying data changed"},
    {"question": "Q47. What Snowflake feature allows storing semi-structured and structured data together?", "options": ["Hybrid Table", "VARIANT", "FILE FORMAT", "COLUMN GROUP"], "answer": "VARIANT"},
    {"question": "Q48. How does Snowflake handle nested fields in JSON?", "options": ["Rejects them", "Flattens automatically", "Stores as VARIANT", "Transforms to structured format"], "answer": "Stores as VARIANT"},
    {"question": "Q49. What function is used to parse XML in Snowflake?", "options": ["TO_XML()", "PARSE_XML()", "GET_XML_OBJECT()", "READ_XML()"], "answer": "PARSE_XML()"},
    {"question": "Q50. Which feature helps reduce query latency when using shared data?", "options": ["External table", "Materialized View", "Secure View", "Result cache"], "answer": "Result cache"},
  {"question": "Q51. What is the default FILE FORMAT used by Snowflake when none is specified?", "options": ["CSV", "JSON", "Parquet", "None"], "answer": "None"},
  {"question": "Q52. Which Snowflake function extracts keys from a semi-structured VARIANT column?", "options": ["GET_PATH", "FLATTEN", "OBJECT_KEYS", "KEYS"], "answer": "OBJECT_KEYS"},
  {"question": "Q53. Which clause is used to specify how to handle bad records when loading data?", "options": ["BAD_RECORDS", "ERROR_ON_COLUMN", "ON_ERROR", "IGNORE_BAD_RECORDS"], "answer": "ON_ERROR"},
  {"question": "Q54. When using COPY INTO with JSON files, what file format option is crucial?", "options": ["FIELD_DELIMITER", "STRIP_NULL_VALUES", "COMPRESSION", "STRIP_OUTER_ARRAY"], "answer": "STRIP_OUTER_ARRAY"},
  {"question": "Q55. What Snowflake function allows you to transform semi-structured arrays into row sets?", "options": ["SPLIT", "FLATTEN", "EXPLODE", "CAST"], "answer": "FLATTEN"},
  {"question": "Q56. Which of the following data types can be used to load semi-structured data into Snowflake?", "options": ["TEXT", "VARCHAR", "VARIANT", "INT"], "answer": "VARIANT"},
  {"question": "Q57. Which command is used to define a custom FILE FORMAT?", "options": ["CREATE FILE_FORMAT", "DEFINE FILE_FORMAT", "REGISTER FILE_FORMAT", "MAKE FILE_FORMAT"], "answer": "CREATE FILE_FORMAT"},
  {"question": "Q58. What is the purpose of AUTO_DETECT in FILE FORMAT definition?", "options": ["To load data faster", "To apply compression automatically", "To infer schema from file", "To detect region"], "answer": "To infer schema from file"},
  {"question": "Q59. Which of the following is a common compression format supported by Snowflake?", "options": ["ZIP", "TAR", "GZIP", "RAR"], "answer": "GZIP"},
  {"question": "Q60. When FLATTEN is used, what pseudo-column gives the index of an element?", "options": ["INDEX", "SEQ", "POSITION", "LEVEL"], "answer": "INDEX"},
  {"question": "Q61. What determines if a virtual warehouse can handle more concurrent queries?", "options": ["Auto Suspend", "Auto Resume", "Size (e.g., X-Large)", "Clustered Index"], "answer": "Size (e.g., X-Large)"},
  {"question": "Q62. How many queries can a Small warehouse handle concurrently before queuing?", "options": ["8", "4", "16", "1"], "answer": "8"},
  {"question": "Q63. What Snowflake concept allows multiple compute clusters per warehouse?", "options": ["Auto Clustering", "Auto Scaling", "Multi-Cluster Warehouse", "Elastic Compute"], "answer": "Multi-Cluster Warehouse"},
  {"question": "Q64. Which view shows if a warehouse is experiencing queuing?", "options": ["QUERY_HISTORY", "WAREHOUSE_LOAD_HISTORY", "LOAD_BALANCER_STATS", "WAREHOUSE_EVENTS"], "answer": "WAREHOUSE_LOAD_HISTORY"},
  {"question": "Q65. What metric best helps determine if a warehouse needs resizing?", "options": ["Auto Resume duration", "Query latency", "Warehouse credit usage", "Warehouse queuing"], "answer": "Warehouse queuing"},
  {"question": "Q66. When scaling policy is set to ECONOMY, what happens?", "options": ["No autoscaling", "Fast scale up", "Fewer clusters spun up", "More credits consumed"], "answer": "Fewer clusters spun up"},
  {"question": "Q67. What happens when warehouse is suspended?", "options": ["Storage deleted", "Billing paused for compute", "Credits increase", "Permanent table is dropped"], "answer": "Billing paused for compute"},
  {"question": "Q68. Which command forces immediate scale-up in multi-cluster mode?", "options": ["ALTER WAREHOUSE SCALE UP", "RESUME FORCE", "MANUAL SCALE OUT", "It cannot be forced"], "answer": "It cannot be forced"},
  {"question": "Q69. Which column in WAREHOUSE_LOAD_HISTORY shows queries waiting?", "options": ["QUEUED_LOAD_PERCENT", "AVG_EXECUTION_TIME", "CREDITS_USED", "CONCURRENCY_LEVEL"], "answer": "QUEUED_LOAD_PERCENT"},
  {"question": "Q70. To reduce queuing in peak hours, you should:", "options": ["Reduce query complexity", "Enable multi-cluster warehouse", "Disable Auto Suspend", "Scale to Small size"], "answer": "Enable multi-cluster warehouse"},
  {"question": "Q71. Which SQL command enables you to create a zero-copy clone of a table?", "options": ["CREATE TABLE CLONE", "CLONE TABLE", "CREATE CLONE", "CREATE TABLE ... CLONE ..."], "answer": "CREATE TABLE ... CLONE ..."},
  {"question": "Q72. Time Travel in Snowflake allows data recovery for how long by default?", "options": ["7 days", "1 day", "90 days", "Indefinitely"], "answer": "1 day"},
  {"question": "Q73. Fail-safe provides additional data recovery for how long?", "options": ["1 day", "7 days", "14 days", "30 days"], "answer": "7 days"},
  {"question": "Q74. What table type in Snowflake does NOT support Time Travel?", "options": ["Permanent", "Transient", "Temporary", "External"], "answer": "Temporary"},
  {"question": "Q75. Which feature allows full schema rollback in Snowflake?", "options": ["Fail-safe", "Clone", "Time Travel", "UNDROP SCHEMA"], "answer": "Time Travel"},
  {"question": "Q76. Which DML operation is not recoverable after the Time Travel period?", "options": ["DELETE", "UPDATE", "MERGE", "TRUNCATE"], "answer": "TRUNCATE"},
  {"question": "Q77. Which command allows restoration of a dropped database?", "options": ["RESTORE DATABASE", "CREATE DATABASE CLONE", "UNDROP DATABASE", "ROLLBACK DATABASE"], "answer": "UNDROP DATABASE"},
  {"question": "Q78. What is the default retention period for Time Travel on transient tables?", "options": ["0 days", "1 day", "7 days", "3 days"], "answer": "0 days"},
  {"question": "Q79. What command is used to create a clone of a schema?", "options": ["CREATE SCHEMA CLONE", "CLONE SCHEMA", "CREATE SCHEMA ... CLONE", "DUPLICATE SCHEMA"], "answer": "CREATE SCHEMA ... CLONE"},
  {"question": "Q80. What is a requirement for Fail-safe to be available?", "options": ["Data must be in VARIANT", "Object must be permanent", "Table must be cloned", "Only admin can enable it"], "answer": "Object must be permanent"},
  {"question": "Q81. Which format allows nested data like arrays and structs in Snowflake?", "options": ["CSV", "JSON", "TXT", "XML"], "answer": "JSON"},
  {"question": "Q82. What Snowflake feature allows column-wise storage optimization?", "options": ["Time Travel", "Clustering", "Micro-partitioning", "FILE FORMAT"], "answer": "Micro-partitioning"},
  {"question": "Q83. How do you parse a VARIANT column as a number in SQL?", "options": ["PARSE_INT()", "TO_INT()", "CAST(... AS NUMBER)", "FLATTEN_TO_NUMBER()"], "answer": "CAST(... AS NUMBER)"},
  {"question": "Q84. What Snowflake object stores raw semi-structured JSON logs?", "options": ["STAGE", "VARIANT TABLE", "FLAT_TABLE", "EXTERNAL_TABLE"], "answer": "VARIANT TABLE"},
  {"question": "Q85. Which function extracts a value from a VARIANT by path?", "options": ["GET()", "EXTRACT()", "VARIANT_PATH()", ":", "GET_PATH()"], "answer": "GET()"},
  {"question": "Q86. What’s a benefit of columnar storage in Snowflake?", "options": ["Faster DDL", "Smaller row IDs", "Faster analytical queries", "Larger table size"], "answer": "Faster analytical queries"},
  {"question": "Q87. How does FLATTEN treat nested JSON arrays?", "options": ["Deletes them", "Converts to columns", "Explodes into rows", "Returns NULL"], "answer": "Explodes into rows"},
  {"question": "Q88. What is required to query JSON data in Snowflake?", "options": ["Set warehouse to JSON mode", "Enable JSON parsing", "Use VARIANT column type", "Use JSON_INDEX"], "answer": "Use VARIANT column type"},
  {"question": "Q89. Which command shows all file formats defined in a schema?", "options": ["LIST FILE FORMATS", "SHOW FILE FORMATS", "DESCRIBE FILE FORMAT", "GET FILE FORMAT"], "answer": "SHOW FILE FORMATS"},
  {"question": "Q90. Which clause in COPY INTO allows skipping headers?", "options": ["SKIP_HEADER", "IGNORE_HEADER", "HEADER=FALSE", "HEADER_ROWS"], "answer": "SKIP_HEADER"},
  {"question": "Q91. Which storage format is most compact for Snowflake?", "options": ["CSV", "PARQUET", "XML", "TXT"], "answer": "PARQUET"},
  {"question": "Q92. What object stores data for use across sessions?", "options": ["TEMP TABLE", "PERMANENT TABLE", "SESSION VARIABLE", "STAGE"], "answer": "STAGE"},
  {"question": "Q93. What is required before using COPY INTO to load data?", "options": ["Create a pipe", "Set up data masking", "Create a stage", "Define external table"], "answer": "Create a stage"},
  {"question": "Q94. What function converts a variant to a string?", "options": ["TO_STRING()", "CAST(... AS TEXT)", "TO_VARCHAR()", "ALL OF THESE"], "answer": "ALL OF THESE"},
  {"question": "Q95. Where is metadata stored in Snowflake?", "options": ["In the user's schema", "Separately by Snowflake", "In each table", "In CSV files"], "answer": "Separately by Snowflake"},
  {"question": "Q96. Which function allows casting to Boolean in SQL?", "options": ["TO_BOOL()", "CAST(... AS BOOLEAN)", "BOOL()", "BOOLEAN_CAST"], "answer": "CAST(... AS BOOLEAN)"},
  {"question": "Q97. What operation doesn’t consume compute credits?", "options": ["Running a SELECT", "Query from cache", "DDL change", "Data load"], "answer": "Query from cache"},
  {"question": "Q98. What command refreshes metadata for external tables?", "options": ["REFRESH EXTERNAL TABLE", "ALTER EXTERNAL TABLE REFRESH", "UPDATE EXTERNAL TABLE", "SYNC TABLE"], "answer": "ALTER EXTERNAL TABLE REFRESH"},
  {"question": "Q99. Which metadata view shows current warehouse sizes?", "options": ["WAREHOUSE_SIZE_VIEW", "WAREHOUSE_LOAD_HISTORY", "CURRENT_WAREHOUSES", "SHOW WAREHOUSES"], "answer": "SHOW WAREHOUSES"},
  {"question": "Q100. What allows querying historical data from a table?", "options": ["CLONE", "Time Travel", "Fail-safe", "PIPE"], "answer": "Time Travel"}
]
# Form to answer questions
# Form to submit answers
with st.form("mock_exam_form"):
    for i, q in enumerate(questions):
        st.markdown(q["question"])
        st.radio(
            label="",
            options=q["options"],
            key=f"q{i}"
        )
        st.markdown("---")
    
    submitted = st.form_submit_button("✅ Submit Exam")
    if submitted:
        st.session_state["submitted"] = True

# Result Display
if st.session_state["submitted"]:
    st.subheader("📊 Results")
    correct = 0
    total = len(questions)

    for i, q in enumerate(questions):
        selected_option = st.session_state.get(f"q{i}")
        if selected_option == q["answer"]:
            correct += 1

    st.markdown(f"## ✅ You scored: **{correct} / {total}**")
    st.markdown("---")

    # Detailed Feedback
    for i, q in enumerate(questions):
        selected_option = st.session_state.get(f"q{i}")
        correct_option = q["answer"]

        if selected_option == correct_option:
            st.success(f"Q{i+1}: Correct ✅")
        else:
            st.error(f"Q{i+1}: Incorrect ❌")
            st.info(f"Your answer: {selected_option}")
        st.info(f"✅ Correct answer: {correct_option}")
        st.markdown("---")

    st.balloons()
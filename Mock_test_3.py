import streamlit as st

st.set_page_config(page_title="SnowPro Core Mock Exam - COF-C02", layout="centered")
st.title("❄️ SnowPro Core Certification - Hard Mock Exam (50 Questions)")
st.markdown("Answer all questions below and submit to see your score and feedback.")

# Store submission state
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

questions = [
    {
        "question": "Q1. What happens to a zero-copy clone when the source object is dropped?",
        "options": ["Clone becomes invalid", "Clone retains full independent copy", "Clone continues to function with no changes", "Clone loses access to future Time Travel data"],
        "answer": "Clone continues to function with no changes"
    },
    {
        "question": "Q2. Which clause is required when loading semi-structured data like JSON into a VARIANT column?",
        "options": ["STRIP_NULL_VALUES", "FILE_FORMAT", "MATCH_BY_COLUMN_NAME", "SET_NULL_VALUES"],
        "answer": "FILE_FORMAT"
    },
    {
        "question": "Q3. In a multi-cluster warehouse, how does Snowflake handle high concurrency?",
        "options": ["Creates separate queues per user", "Scales up compute within a node", "Auto-provisions additional clusters", "Rejects new queries when limit is hit"],
        "answer": "Auto-provisions additional clusters"
    },
    {
        "question": "Q4. What is the impact of cloning a schema containing transient tables?",
        "options": [
            "Transient tables are not cloned",
            "All data is cloned but Time Travel is disabled",
            "Only metadata is cloned",
            "Cloned schema retains transient nature and data"
        ],
        "answer": "Cloned schema retains transient nature and data"
    },
    {
        "question": "Q5. A user needs to share data with external accounts using Secure Data Sharing. What is the minimum required object?",
        "options": ["External Stage", "Share", "Reader Account", "Secure View"],
        "answer": "Share"
    },
    {
        "question": "Q6. What Snowflake object allows access to historical versions of a table even after a DROP TABLE command?",
        "options": ["Fail-safe", "Time Travel", "Clone", "Streams"],
        "answer": "Time Travel"
    },
    {
        "question": "Q7. Which object type must be present for COPY INTO <table> to succeed?",
        "options": ["Temporary table", "Stage", "File format", "Pipe"],
        "answer": "Stage"
    },
    {
        "question": "Q8. Which clause can reduce data movement during transformations using CTAS?",
        "options": ["CLUSTER BY", "WITH NO DATA", "COPY GRANTS", "DATA_RETENTION_TIME_IN_DAYS"],
        "answer": "CLUSTER BY"
    },
    {
        "question": "Q9. How can you ensure minimal cost when running scheduled queries on large unstructured data files?",
        "options": ["Use VARIANT for all data types", "Use auto-suspend", "Set MAX_CLUSTER_COUNT = 10", "Use external table preview mode"],
        "answer": "Use auto-suspend"
    },
    {
        "question": "Q10. In Snowflake, which privilege is necessary to enable a user to create a new virtual warehouse?",
        "options": ["OWNERSHIP", "USAGE", "CREATE WAREHOUSE", "MODIFY"],
        "answer": "CREATE WAREHOUSE"
    },
    {
        "question": "Q11. Which file format does NOT support semi-structured data parsing natively in Snowflake?",
        "options": ["JSON", "Parquet", "CSV", "AVRO"],
        "answer": "CSV"
    },
    {
        "question": "Q12. How can you prevent a virtual warehouse from incurring charges when idle?",
        "options": ["Use auto-cluster", "Use auto-suspend", "Disable credits", "Use Snowpipe"],
        "answer": "Use auto-suspend"
    },
    {
        "question": "Q13. What is a key difference between a transient and temporary table?",
        "options": ["Temporary tables support cloning", "Transient tables retain Time Travel", "Temporary tables do not persist across sessions", "Transient tables are dropped at session end"],
        "answer": "Temporary tables do not persist across sessions"
    },
    {
        "question": "Q14. What happens when you execute CREATE OR REPLACE on a table that has a stream?",
        "options": ["Stream is invalidated", "Stream retains state", "Stream is reset", "Stream creates a clone"],
        "answer": "Stream is invalidated"
    },
    {
        "question": "Q15. How does Snowflake optimize concurrent queries on the same large table?",
        "options": ["Partitions data at runtime", "Executes all in parallel", "Scales cluster vertically", "Uses result cache and pruning"],
        "answer": "Uses result cache and pruning"
    },
    {
        "question": "Q16. Which stage type is used for external S3 data access in Snowflake?",
        "options": ["Internal Named Stage", "User Stage", "External Stage", "File Stage"],
        "answer": "External Stage"
    },
    {
        "question": "Q17. How long is fail-safe retention in Snowflake Enterprise Edition?",
        "options": ["1 day", "7 days", "14 days", "30 days"],
        "answer": "7 days"
    },
    {
        "question": "Q18. When does Fail-safe period begin?",
        "options": ["After warehouse suspension", "After Time Travel period ends", "Immediately on DROP", "On storage threshold breach"],
        "answer": "After Time Travel period ends"
    },
    {
        "question": "Q19. How is Snowpipe triggered automatically?",
        "options": ["Using a Cron schedule", "Using external function", "Using cloud storage event", "Using SnowSQL"],
        "answer": "Using cloud storage event"
    },
    {
        "question": "Q20. What file format should you use to maintain column types during structured data ingestion?",
        "options": ["CSV", "JSON", "Parquet", "XML"],
        "answer": "Parquet"
    },
    {
        "question": "Q21. What Snowflake object enables data versioning and undo operations?",
        "options": ["Clone", "Fail-safe", "Time Travel", "External Table"],
        "answer": "Time Travel"
    },
    {
        "question": "Q22. What clause allows sharing specific rows in a view across accounts securely?",
        "options": ["SECURE VIEW", "MASKING POLICY", "ROW ACCESS POLICY", "RESOURCE MONITOR"],
        "answer": "ROW ACCESS POLICY"
    },
    {
        "question": "Q23. Which of the following is NOT allowed inside a masking policy?",
        "options": ["CASE expression", "CURRENT_ROLE()", "CURRENT_USER()", "JOIN clause"],
        "answer": "JOIN clause"
    },
    {
        "question": "Q24. What is required before a Consumer account can access a Share?",
        "options": ["Reader account", "Database replica", "Imported share object", "Data pipe"],
        "answer": "Imported share object"
    },
    {
        "question": "Q25. Which DDL statement allows defining a table without loading data?",
        "options": ["CREATE TABLE CLONE", "CREATE TABLE LIKE", "CREATE TABLE AS SELECT", "CREATE OR REPLACE"],
        "answer": "CREATE TABLE LIKE"
    },
    {
        "question": "Q26. What ensures that a data file is loaded only once in COPY INTO?",
        "options": ["FILE_FORMAT check", "PATTERN parameter", "ON_ERROR clause", "Metadata tracking"],
        "answer": "Metadata tracking"
    },
    {
        "question": "Q27. Which keyword enables automatic scaling of virtual warehouses?",
        "options": ["MIN_CLUSTER_COUNT", "AUTO_CLUSTERING", "SCALING_POLICY", "MAX_CLUSTER_COUNT"],
        "answer": "MAX_CLUSTER_COUNT"
    },
    {
        "question": "Q28. What happens to the child objects when a schema is cloned?",
        "options": ["Only metadata copied", "All objects and data cloned", "Streams excluded", "Only permanent tables copied"],
        "answer": "All objects and data cloned"
    },
    {
        "question": "Q29. How do you ensure multi-tenant security when sharing data with multiple external accounts?",
        "options": ["Use UDFs", "Use separate databases", "Use secure views with policies", "Use fail-safe"],
        "answer": "Use secure views with policies"
    },
    {
        "question": "Q30. What determines whether a table supports Time Travel?",
        "options": ["Storage size", "Table type", "Clustering", "Role used for creation"],
        "answer": "Table type"
    },
    {
        "question": "Q31. Which command rewinds a table to a previous timestamp or statement ID?",
        "options": ["ALTER TABLE UNDROP", "CREATE TABLE CLONE", "FLASHBACK TABLE", "ALTER TABLE ... SET DATA_RETENTION_TIME_IN_DAYS"],
        "answer": "CREATE TABLE CLONE"
    },
    {
        "question": "Q32. What file formats support columnar compression natively?",
        "options": ["JSON", "AVRO", "Parquet", "XML"],
        "answer": "Parquet"
    },
    {
        "question": "Q33. Which Snowflake object is not eligible for cloning?",
        "options": ["Table", "Schema", "Database", "Pipe"],
        "answer": "Pipe"
    },
    {
        "question": "Q34. What DML operation is needed to incrementally apply changes to dimension tables?",
        "options": ["MERGE", "INSERT", "UPDATE", "DELETE"],
        "answer": "MERGE"
    },
    {
        "question": "Q35. How can you programmatically control cost limits on virtual warehouses?",
        "options": ["Virtual Roles", "Auto-resume", "Resource Monitors", "Warehouse quotas"],
        "answer": "Resource Monitors"
    },
    {
        "question": "Q36. Which is not a valid role hierarchy default in Snowflake?",
        "options": ["SYSADMIN > SECURITYADMIN", "SYSADMIN > PUBLIC", "ACCOUNTADMIN > SYSADMIN", "SECURITYADMIN > USERADMIN"],
        "answer": "SYSADMIN > SECURITYADMIN"
    },
    {
        "question": "Q37. What is a key benefit of columnar storage in Snowflake?",
        "options": ["Reduces network latency", "Improves row-level security", "Enables fast column pruning", "Requires less metadata"],
        "answer": "Enables fast column pruning"
    },
    {
        "question": "Q38. What clause prevents a role from inheriting privileges of another role?",
        "options": ["GRANT", "REVOKE", "SET DEFAULT ROLE", "None – inheritance always allowed"],
        "answer": "None – inheritance always allowed"
    },
    {
        "question": "Q39. How do Snowflake shares maintain security across accounts?",
        "options": ["Secure views only", "Only external stages are shared", "No data copied; metadata only", "Each share requires a user role"],
        "answer": "No data copied; metadata only"
    },
    {
        "question": "Q40. What is the role of a Reader Account in Snowflake?",
        "options": ["Allows creating new shares", "Allows non-Snowflake users to access shared data", "Allows granting privileges", "Used for cloning"],
        "answer": "Allows non-Snowflake users to access shared data"
    },
    {
        "question": "Q41. Which system-defined role has access to manage users and roles?",
        "options": ["SYSADMIN", "PUBLIC", "SECURITYADMIN", "USERADMIN"],
        "answer": "SECURITYADMIN"
    },
    {
        "question": "Q42. What ensures proper formatting and loading of semi-structured data?",
        "options": ["File naming conventions", "FILE_FORMAT parameter", "Partition key", "Pipe definition"],
        "answer": "FILE_FORMAT parameter"
    },
    {
        "question": "Q43. Which storage layer component in Snowflake handles metadata and statistics?",
        "options": ["Virtual Warehouse", "Query Cache", "Services Layer", "Metadata Store"],
        "answer": "Metadata Store"
    },
    {
        "question": "Q44. How can you ensure changes to roles are audited?",
        "options": ["Enable usage tracking", "Use event table", "Use Access History", "Use SNOWPIPE history"],
        "answer": "Use Access History"
    },
    {
        "question": "Q45. Which COPY option continues loading files even after an error?",
        "options": ["ON_ERROR='skip_file'", "IF EXISTS", "ABORT", "TRY_LOAD"],
        "answer": "ON_ERROR='skip_file'"
    },
    {
        "question": "Q46. Which Snowflake feature provides row-level security?",
        "options": ["Secure views", "Row access policies", "Object tagging", "Classification"],
        "answer": "Row access policies"
    },
    {
        "question": "Q47. What is a benefit of using clustering keys?",
        "options": ["Improve storage compression", "Optimize DDL speed", "Improve pruning on large datasets", "Control access policies"],
        "answer": "Improve pruning on large datasets"
    },
    {
        "question": "Q48. How many days of query history does the QUERY_HISTORY function retain by default?",
        "options": ["7", "14", "30", "1"],
        "answer": "14"
    },
    {
        "question": "Q49. How does Time Travel interact with permanent vs transient tables?",
        "options": ["Only permanent tables support Time Travel", "Transient supports full history", "All table types get 30 days by default", "It depends on fail-safe setting"],
        "answer": "Only permanent tables support Time Travel"
    },
    {
        "question": "Q50. Which object is required to load continuous data from S3 into Snowflake automatically?",
        "options": ["Pipe", "Task", "Sequence", "Role"],
        "answer": "Pipe"
    }
]



# Store user answers
with st.form("mock_exam_form"):
    for i, q in enumerate(questions):
        st.markdown(f"### Q{i+1}. {q['question'][4:]}")
        
        selected = st.radio(
            label="",
            options=q["options"],
            key=f"q{i}",
            index=None
        )

        # ✅ Show feedback only if submitted
        if st.session_state["submitted"]:
            correct_option = q["answer"]
            if selected == correct_option:
                st.success(f"✅ Your Answer: {selected} — Correct!")
            else:
                st.error(f"❌ Your Answer: {selected} — Incorrect")
                st.info(f"✅ Correct Answer: {correct_option}")

        st.markdown("---")

    submitted = st.form_submit_button("✅ Submit Exam")
    if submitted:
        st.session_state["submitted"] = True

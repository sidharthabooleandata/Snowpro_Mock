import streamlit as st

st.set_page_config(page_title="SnowPro Core Mock Exam", layout="centered")
st.title("🧠 SnowPro Core Certification - Mock Exam")
st.markdown("Answer all 100 questions below. Submit at the end to view your score and correct answers.")

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

# Example questions list (use your full 50-question list)
questions = [
    {"question": "Q1. True or False: Cloning a large table creates a full data copy.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q2. True or False: Time Travel allows querying historical data for up to 90 days even on Standard Edition.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q3. When you issue CREATE TABLE ... CLONE, which metadata is shared?", "options": ["Table data pages", "Object grants", "Table statistics", "File format metadata"], "answer": "Table data pages"},
    {"question": "Q4. The default Time Travel retention for a standard (non-transient) table is:", "options": ["1 day", "7 days", "0 days", "14 days"], "answer": "1 day"},
    {"question": "Q5. True or False: A transient table still has fail‑safe.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q6. What is fail‑safe used for?", "options": ["Immediate disaster recovery", "Regulatory data retention", "A 7‑day internal recovery buffer", "Table versioning beyond Time Travel"], "answer": "A 7‑day internal recovery buffer"},
    {"question": "Q7. Fast DML operations on large tables benefit most from:", "options": ["Clustering keys", "Materialized views", "Zero‑copy cloning", "Transient tables"], "answer": "Clustering keys"},
    {"question": "Q8. Which warehouse type supports multi-cluster scaling (SCALING_POLICY = 'STANDARD')?", "options": ["Regular always-on warehouses", "Multi-cluster warehouses", "Serverless warehouses", "Transient compute"], "answer": "Multi-cluster warehouses"},
    {"question": "Q9. Which operation can trigger micro-partition pruning?", "options": ["Filtering on clustered columns", "Large table scans", "Unstructured queries", "All SELECT queries"], "answer": "Filtering on clustered columns"},
    {"question": "Q10. True or False: Materialized views must be refreshed manually.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q11. How long does Time Travel last for transient tables?", "options": ["0 days", "1 day", "7 days", "It depends on edition."], "answer": "0 days"},
    {"question": "Q12. Executing ALTER WAREHOUSE ... RESUME uses credits for at least:", "options": ["The remainder of a minute", "The remainder of an hour", "5 minutes total", "A full auto‑suspend period"], "answer": "The remainder of a minute"},
    {"question": "Q13. True or False: SNOWFLAKE.ACCOUNT_USAGE.CLONE_HISTORY shows every clone operation in the account.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q14. You want high concurrency with unpredictable workloads. Use:", "options": ["Small warehouse", "Multi-cluster warehouse", "Serverless compute", "Auto-suspend settings"], "answer": "Multi-cluster warehouse"},
    {"question": "Q15. A large pipeline DELETE on a clustered table might benefit from:", "options": ["RECLUSTERING only", "Using transient staging", "Creating a materialized view", "VACUUM (as manual reclustering)"], "answer": "VACUUM (as manual reclustering)"},
    {"question": "Q16. True or False: Zero-copy clones share compute resources.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q17. Time Travel consumes storage credits as:", "options": ["Maximum data retention consumed", "Additional daily usage", "Flat monthly fee", "Only if data is queried historically"], "answer": "Additional daily usage"},
    {"question": "Q18. You can fail-safe retrieve data up to:", "options": ["14 days after Time Travel ends", "7 days", "1 year", "It depends on edition"], "answer": "14 days after Time Travel ends"},
    {"question": "Q19. True or False: User roles on clones are inherited from the source.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q20. To purge ingestion history older than 64 days, you must:", "options": ["Call DROP PIPE", "Use ACCOUNTADMIN TTL", "Wait; it's unpurgeable", "Use ALTER PIPE ... SET HISTORY_RETENTION_DAYS"], "answer": "Use ALTER PIPE ... SET HISTORY_RETENTION_DAYS"},
    {"question": "Q21. True or False: Snowpipe ingestion events can be replayed from an external stage.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q22. A multi-cluster warehouse is auto-scaled by what?", "options": ["Number of concurrent users", "Data size in tables", "Size of each query", "Number of schemas"], "answer": "Number of concurrent users"},
    {"question": "Q23. Which statement prevents automatic clustering maintenance?", "options": ["ALTER TABLE ... CLUSTER BY NONE", "ALTER WAREHOUSE ... SUSPEND_CLUSTERS=FALSE", "ALTER DATABASE ... AUTO_CLUSTERING=FALSE", "ALTER SCHEMA ... UNSET CLUSTERING"], "answer": "ALTER TABLE ... CLUSTER BY NONE"},
    {"question": "Q24. True or False: File size has no impact on load performance.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q25. Which object can time-travel only 0 days by default?", "options": ["Transient table", "Temporary table", "Permanent table", "Materialized view"], "answer": "Transient table"},
    {"question": "Q26. Streaming data via Snowpipe uses compute from:", "options": ["The target table’s warehouse", "A default Snowflake-managed warehouse", "The largest warehouse in the account", "The warehouse named SNOWPIPE_WH"], "answer": "A default Snowflake-managed warehouse"},
    {"question": "Q27. What parameter sets the maximum number of clusters?", "options": ["MIN_CLUSTER_COUNT", "MAX_CLUSTER_COUNT", "SCALING_POLICY", "AUTO_SCALE_MAX_CLUSTERS"], "answer": "MAX_CLUSTER_COUNT"},
    {"question": "Q28. True or False: Micro-partitions are recomputed on UPDATEs.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q29. Best practice for loading Parquet:", "options": ["Unzip first", "Use compressed copy", "Copy from internal stage", "Use Parquet COPY INTO"], "answer": "Use Parquet COPY INTO"},
    {"question": "Q30. Which cache stores compiled query plans?", "options": ["Result cache", "Warehouse cache", "Azure/Cloud storage cache", "Services layer cache"], "answer": "Services layer cache"},
    {"question": "Q31. How long are query results in result cache?", "options": ["24 hours", "12 hours", "Until warehouse suspends", "7 days"], "answer": "24 hours"},
    {"question": "Q32. True or False: Changing a warehouse size breaks result cache validity.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q33. To track column-level masking, you use:", "options": ["External masking policy", "Dynamic data masking policy", "Table level encryption", "Column encryption"], "answer": "Dynamic data masking policy"},
    {"question": "Q34. What’s required to share a table across accounts?", "options": ["CREATE SHARE then GRANT SELECT", "ALTER ACCOUNT SET SHARE MODE", "CREATE PROVIDER and GRANT", "ENABLE CROSS-ACCOUNT SHARING"], "answer": "CREATE SHARE then GRANT SELECT"},
    {"question": "Q35. True or False: Secure Data Sharing uses Zero-Copy sharing.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q36. How are cross-cloud database clones billed?", "options": ["Full storage cost", "Zero-copy clone storage", "Transfers + metadata charges", "Free between accounts"], "answer": "Transfers + metadata charges"},
    {"question": "Q37. A fail-safe duration for Standard Edition is:", "options": ["7 days", "0 days", "14 days", "1 day"], "answer": "7 days"},
    {"question": "Q38. Time Travel ends when:", "options": ["Retention period elapses", "You suspend the warehouse", "You clone the table", "Data is unloaded"], "answer": "Retention period elapses"},
    {"question": "Q39. True or False: Clones can be made across regions.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q40. A continuous data ingestion engine is:", "options": ["Stream", "Task", "Pipe", "Snowpipe"], "answer": "Snowpipe"},
    {"question": "Q41. Use AUTO_SUSPEND to:", "options": ["Pause warehouse when idle", "Save result cache", "Stop micro-partitioning", "Reset user sessions"], "answer": "Pause warehouse when idle"},
    {"question": "Q42. True or False: A multi-table clone creates separate micro-partitions.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q43. Which statement is accurate about cloning?", "options": ["Clones snapshot only metadata", "Uses twice the storage", "Requires a transient table", "Purges on Time Travel end"], "answer": "Clones snapshot only metadata"},
    {"question": "Q44. To resume a suspended warehouse via SQL:", "options": ["ALTER WAREHOUSE ... RESUME", "START WAREHOUSE", "RUN WAREHOUSE", "SET WAREHOUSE ... ON"], "answer": "ALTER WAREHOUSE ... RESUME"},
    {"question": "Q45. True or False: Deleting large volumes of data triggers micro-partition merge.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q46. Result cache returns results when:", "options": ["Same SQL executed", "Same warehouse", "Underlying data unchanged", "User is the same"], "answer": "Underlying data unchanged"},
    {"question": "Q47. Which metadata tracks eliminated micro-partitions?", "options": ["QUERY_HISTORY", "STORAGE_USAGE", "ACCESS_HISTORY", "QUERY_ACCELERATION_HISTORY"], "answer": "QUERY_ACCELERATION_HISTORY"},
    {"question": "Q48. True or False: Warehouses cannot auto-resume with multi-cluster scaling.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q49. A cloned table’s Time Travel retention is:", "options": ["Created by target table", "Inherited from source", "Always default", "0 days"], "answer": "Created by target table"},
    {"question": "Q50. Which cache is per-node during queries?", "options": ["Warehouse local disk cache", "Result cache", "Services layer cache", "Storage cache"], "answer": "Warehouse local disk cache"},
    {"question": "Q51. True or False: Variant cannot store STRUCT data.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q52. Use ALTER TABLE ... CLUSTER BY to:", "options": ["Define new clustering key", "Remove clustering", "Manually cluster table", "Export clustering"], "answer": "Define new clustering key"},
    {"question": "Q53. True or False: File headers are auto-detected in COPY INTO.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q54. To share external stages you need:", "options": ["Object-level grants", "Privileges on IAM role or bucket", "CROSS_ACCOUNT_SHARE enabled", "Stage DDL privileges"], "answer": "Privileges on IAM role or bucket"},
    {"question": "Q55. True or False: STAGE metadata persists on table clone.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q56. A task SQL runs with:", "options": ["The task’s warehouse", "Warehouse set in DDL", "Default warehouse", "ADMIN warehouse"], "answer": "Warehouse set in DDL"},
    {"question": "Q57. True or False: Schema auto-clustering can be globally disabled.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q58. Best warehouse size for short unpredictable bursts:", "options": ["Small, auto-suspend", "X-Small, auto-resume", "Multi-cluster small", "Large, manual suspend"], "answer": "Multi-cluster small"},
    {"question": "Q59. True or False: ALTER WAREHOUSE ... SET MIN*/MAX* changes cluster count.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q60. Warehouses can scale out only if:", "options": ["Multi-cluster created", "Enabled AUTO_SCALE", "Size ≥ Medium", "Created in Enterprise Edition"], "answer": "Multi-cluster created"},
    {"question": "Q61. Time Travel is disabled on:", "options": ["Transient tables", "External tables", "Views", "Clones"], "answer": "Transient tables"},
    {"question": "Q62. True or False: Drops with CASCADE skip Time Travel.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q63. MV maintenance is triggered by:", "options": ["Table changes", "Manual REFRESH MV", "Later query use", "All above"], "answer": "All above"},
    {"question": "Q64. A cluster is sized in credits based on:", "options": ["# of servers", "Micro-partition count", "Queries per second", "Table size"], "answer": "# of servers"},
    {"question": "Q65. True or False: Clones include access grants.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q66. Best practice before DML on large tables:", "options": ["Clone table", "Manual clustering", "Increase warehouse size", "Disable clustering"], "answer": "Increase warehouse size"},
    {"question": "Q67. True or False: They call unload to stage \"COPY INTO\" syntax.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q68. If underlying data changes, result cache is:", "options": ["Invalidated", "Unaffected", "Merged", "Logged"], "answer": "Invalidated"},
    {"question": "Q69. Zero-copy cross-region clone charges for:", "options": ["Egress and storage", "Double storage", "No extra cost", "Only compute"], "answer": "Egress and storage"},
    {"question": "Q70. True or False: Copy with validation mode loads no data.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q71. A view clone is:", "options": ["Logical only", "Light physical copy", "Full clone", "Invalid"], "answer": "Full clone"},
    {"question": "Q72. To retain MV data longer, raise:", "options": ["MARK_MV_RETENTION", "LONG_TIME_RETENTION", "CLUSTER_MAINTENANCE_RETENTION", "Extend_RETENTION"], "answer": "CLUSTER_MAINTENANCE_RETENTION"},
    {"question": "Q73. Result cache serves:", "options": ["Same user, same role, same warehouse", "All account users", "Across warehouses", "Across roles"], "answer": "Same user, same role, same warehouse"},
    {"question": "Q74. True or False: Streaming inserts bypass micro-partitioning.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q75. For small range pruning, use:", "options": ["Filter on clustering columns", "Multi-cluster warehouse", "Zero-copy clone", "Increase retention"], "answer": "Filter on clustering columns"},
    {"question": "Q76. Auto-suspend default is:", "options": ["10 minutes", "5 minutes", "1 minute", "15 minutes"], "answer": "10 minutes"},
    {"question": "Q77. True or False: Virtual warehouses are schema-level objects.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q78. Which privilege is needed for cloning?", "options": ["OWNERSHIP on source", "CREATE_TABLE only", "CLONE privilege", "CREATE DATABASE"], "answer": "OWNERSHIP on source"},
    {"question": "Q79. True or False: Materialized view uses warehouse at query time.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q80. To monitor warehouse auto-scale, check:", "options": ["WAREHOUSE_LOAD_HISTORY", "QUERY_HISTORY", "WAREHOUSE_METERING_HISTORY", "ACCOUNT_USAGE_CREDITS"], "answer": "WAREHOUSE_METERING_HISTORY"}
    {"question": "Q81. True or False: Cross-account share also replicates clones.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q82. External table Time Travel?", "options": ["Not supported", "1 day", "0 days", "Cloned ext tables inherit"], "answer": "Not supported"},
    {"question": "Q83. A COPY INTO to external stage uses:", "options": ["Warehouse compute", "Cloud services", "Stage overhead", "Storage only"], "answer": "Warehouse compute"},
    {"question": "Q84. To disable result cache:", "options": ["SESSION USE_CACHED_RESULT = FALSE", "ALTER ACCOUNT SET USE_CACHED_RESULT=FALSE", "ALTER SCHEMA ...", "Warehouse parameter"], "answer": "SESSION USE_CACHED_RESULT = FALSE"},
    {"question": "Q85. True or False: Streams track clones as DML.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q86. To override micro-partition recompute, run:", "options": ["ALTER TABLE ... RECLUSTER", "ALTER WAREHOUSE...", "CLONE TABLE...", "REFRESH CLUSTERING"], "answer": "ALTER TABLE ... RECLUSTER"},
    {"question": "Q87. Data unloading uses:", "options": ["COPY INTO @stage", "UNLOAD TO S3", "EXPORT TO azure", "STORE INTO"], "answer": "COPY INTO @stage"},
    {"question": "Q88. True or False: Multi-cluster warehouses cannot scale down automatically.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q89. Operating costs = compute +:", "options": ["Cloud services", "Storage only", "Monitoring", "Data sharing"], "answer": "Cloud services"},
    {"question": "Q90. True or False: Cloning a table resets statistics.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q91. To load via Web Interface, data can be loaded only into:", "options": ["Tables", "Named stages", "External tables", "File formats"], "answer": "Tables"},
    {"question": "Q92. True or False: Warehouse auto-resume counts towards credit usage.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q93. Snowpipe REST is triggered by:", "options": ["API call", "Named event notifications", "Manual execution", "STAGE polling"], "answer": "API call"},
    {"question": "Q94. True or False: Diluted clustering occurs when new data is written outside the clustering key range.", "options": ["True", "False"], "answer": "True"},
    {"question": "Q95. To speed up cold caches:", "options": ["PRELOAD function", "WARMUP cache via test queries", "Larger warehouse", "Multi-cluster scale-up"], "answer": "WARMUP cache via test queries"},
    {"question": "Q96. True or False: Using STREAM on clones works seamlessly.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q97. For data sharing, cross-cloud accounts must match:", "options": ["Edition", "Cloud platform", "Region", "Both B and C"], "answer": "Both B and C"},
    {"question": "Q98. True or False: Continuous data load (Snowpipe) uses transient warehouses.", "options": ["True", "False"], "answer": "False"},
    {"question": "Q99. A clone created of a clone still:", "options": ["Has no data copy", "Inherits time travel retention", "Nullifies fail-safe", "Creates full clone"], "answer": "Inherits time travel retention"},
    {"question": "Q100. True or False: Disabling auto clustering affects ongoing querying.", "options": ["True", "False"], "answer": "False"}
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
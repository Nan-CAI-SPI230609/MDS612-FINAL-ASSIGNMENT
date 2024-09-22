from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when, mean, datediff, to_date, year, month, expr, desc, avg, sum, lag
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder \
    .appName("HealthcareDataAnalysis") \
    .getOrCreate()

# Load the healthcare dataset
file_path = "/Users/cainan753/Downloads/healthcare_original_dataset.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Data cleaning and type conversion
df_cleaned = df.dropDuplicates().na.drop()
df_cleaned = df_cleaned.withColumn("Date of Admission", to_date(col("Date of Admission"), "yyyy/M/d"))
df_cleaned = df_cleaned.withColumn("Discharge Date", to_date(col("Discharge Date"), "yyyy/M/d"))
df_cleaned = df_cleaned.withColumn("Billing Amount", col("Billing Amount").cast("double"))
df_cleaned = df_cleaned.withColumn("Age", col("Age").cast("integer"))

# 1. Analyze average length of stay by medical condition
df_cleaned = df_cleaned.withColumn("LengthOfStay", datediff(col("Discharge Date"), col("Date of Admission")))
avg_stay = df_cleaned.groupBy("Medical Condition").agg(avg("LengthOfStay").alias("AvgStay")).orderBy(desc("AvgStay"))
print("1. Average Length of Stay by Medical Condition:")
avg_stay.show()

# 2. Analyze admission types distribution
admission_dist = df_cleaned.groupBy("Admission Type").count().orderBy(desc("count"))
print("2. Distribution of Admission Types:")
admission_dist.show()

# 3. Analyze age distribution and most common conditions by age group
df_cleaned = df_cleaned.withColumn("AgeGroup", expr(
    "CASE WHEN Age < 18 THEN 'Under 18' " +
    "WHEN Age BETWEEN 18 AND 30 THEN '18-30' " +
    "WHEN Age BETWEEN 31 AND 50 THEN '31-50' " +
    "WHEN Age BETWEEN 51 AND 70 THEN '51-70' " +
    "ELSE 'Over 70' END"
))
age_dist = df_cleaned.groupBy("AgeGroup").count().orderBy("AgeGroup")
print("3. Age Distribution:")
age_dist.show()

age_condition = df_cleaned.groupBy("AgeGroup", "Medical Condition").count().orderBy("AgeGroup", desc("count"))
print("Most Common Conditions by Age Group:")
age_condition.show()

# 4. Analyze seasonal trends in admissions
df_cleaned = df_cleaned.withColumn("AdmissionMonth", month("Date of Admission"))
monthly_admissions = df_cleaned.groupBy("AdmissionMonth").count().orderBy("AdmissionMonth")
print("4. Monthly Distribution of Admissions:")
monthly_admissions.show()

# 5. Analyze correlation between blood type and medical conditions
blood_condition = df_cleaned.groupBy("Blood Type", "Medical Condition").count().orderBy(desc("count"))
print("5. Correlation between Blood Type and Medical Conditions:")
blood_condition.show()

# 6. Analyze average billing amount by insurance provider
avg_billing = df_cleaned.groupBy("Insurance Provider").agg(avg("Billing Amount").alias("AvgBilling")).orderBy(desc("AvgBilling"))
print("6. Average Billing Amount by Insurance Provider:")
avg_billing.show()

# 7. Analyze most common medications prescribed for each medical condition
medication_condition = df_cleaned.groupBy("Medical Condition", "Medication").count().orderBy("Medical Condition", desc("count"))
print("7. Most Common Medications by Medical Condition:")
medication_condition.show()

# 8. Analyze readmission rates
readmission_window = Window.partitionBy("Name").orderBy("Date of Admission")
df_cleaned = df_cleaned.withColumn("PrevAdmission", lag("Date of Admission").over(readmission_window))
df_cleaned = df_cleaned.withColumn("DaysSinceLastAdmission", datediff(col("Date of Admission"), col("PrevAdmission")))
readmission_rate = df_cleaned.filter(col("DaysSinceLastAdmission").isNotNull() & (col("DaysSinceLastAdmission") <= 30)) \
    .groupBy("Medical Condition") \
    .agg(count("*").alias("Readmissions"), 
         (count("*") * 100 / df_cleaned.select("Medical Condition").distinct().count()).alias("ReadmissionRate")) \
    .orderBy(desc("ReadmissionRate"))
print("8. Readmission Rates by Medical Condition (within 30 days):")
readmission_rate.show()

# 9. Analyze treatment effectiveness
treatment_effectiveness = df_cleaned.groupBy("Medical Condition", "Medication").agg(
    avg("LengthOfStay").alias("AvgStay"),
    avg("Billing Amount").alias("AvgBilling")
).orderBy("Medical Condition", "AvgStay")
print("9. Treatment Effectiveness by Medical Condition:")
treatment_effectiveness.show()

# 10. Analyze patient demographics impact on health outcomes
demographics_impact = df_cleaned.groupBy("Gender", "AgeGroup", "Medical Condition").agg(
    avg("LengthOfStay").alias("AvgStay"),
    avg("Billing Amount").alias("AvgBilling")
).orderBy("Gender", "AgeGroup", desc("AvgStay"))
print("10. Impact of Patient Demographics on Health Outcomes:")
demographics_impact.show()

# Stop Spark session
spark.stop()
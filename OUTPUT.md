# Healthcare Data Analysis Results

## 1. Average Length of Stay by Medical Condition

| Medical Condition | AvgStay |
|-------------------|---------|
| Asthma            | 15.68   |
| Arthritis         | 15.50   |
| Cancer            | 15.50   |
| Obesity           | 15.45   |
| Hypertension      | 15.44   |
| Diabetes          | 15.43   |

## 2. Distribution of Admission Types

| Admission Type | Count |
|----------------|-------|
| Elective       | 18473 |
| Urgent         | 18391 |
| Emergency      | 18102 |

## 3. Age Distribution

| AgeGroup | Count |
|----------|-------|
| 18-30    | 10289 |
| 31-50    | 16167 |
| 51-70    | 16367 |
| Over 70  | 12027 |
| Under 18 |   116 |

### Most Common Conditions by Age Group

| AgeGroup | Medical Condition | Count |
|----------|-------------------|-------|
| 18-30    | Obesity           | 1747  |
| 18-30    | Cancer            | 1742  |
| 18-30    | Asthma            | 1709  |
| 18-30    | Hypertension      | 1700  |
| 18-30    | Arthritis         | 1697  |
| 18-30    | Diabetes          | 1694  |
| 31-50    | Arthritis         | 2755  |
| 31-50    | Diabetes          | 2743  |
| 31-50    | Obesity           | 2682  |
| 31-50    | Hypertension      | 2677  |
| 31-50    | Asthma            | 2670  |
| 31-50    | Cancer            | 2640  |
| 51-70    | Diabetes          | 2814  |
| 51-70    | Obesity           | 2760  |
| 51-70    | Cancer            | 2716  |
| 51-70    | Hypertension      | 2710  |
| 51-70    | Arthritis         | 2702  |
| 51-70    | Asthma            | 2665  |
| Over 70  | Hypertension      | 2053  |
| Over 70  | Arthritis         | 2043  |

## 4. Monthly Distribution of Admissions

| AdmissionMonth | Count |
|----------------|-------|
| 1              | 4655  |
| 2              | 4210  |
| 3              | 4622  |
| 4              | 4478  |
| 5              | 4555  |
| 6              | 4650  |
| 7              | 4765  |
| 8              | 4785  |
| 9              | 4508  |
| 10             | 4613  |
| 11             | 4508  |
| 12             | 4617  |

## 5. Correlation between Blood Type and Medical Conditions

| Blood Type | Medical Condition | Count |
|------------|-------------------|-------|
| AB+        | Hypertension      | 1204  |
| A+         | Diabetes          | 1201  |
| B+         | Arthritis         | 1191  |
| O+         | Arthritis         | 1186  |
| AB-        | Cancer            | 1186  |
| B+         | Cancer            | 1186  |
| A-         | Hypertension      | 1186  |
| B-         | Obesity           | 1182  |
| B+         | Diabetes          | 1180  |
| AB-        | Arthritis         | 1179  |

## 6. Average Billing Amount by Insurance Provider

| Insurance Provider | AvgBilling |
|--------------------|------------|
| Medicare           | 25,628.32  |
| Blue Cross         | 25,603.46  |
| Aetna              | 25,549.69  |
| Cigna              | 25,526.00  |
| UnitedHealthcare   | 25,414.51  |

## 7. Most Common Medications by Medical Condition

| Medical Condition | Medication  | Count |
|-------------------|-------------|-------|
| Arthritis         | Aspirin     | 1901  |
| Arthritis         | Paracetamol | 1858  |
| Arthritis         | Penicillin  | 1844  |
| Arthritis         | Lipitor     | 1810  |
| Arthritis         | Ibuprofen   | 1805  |
| Asthma            | Paracetamol | 1870  |
| Asthma            | Penicillin  | 1828  |
| Asthma            | Lipitor     | 1814  |
| Asthma            | Ibuprofen   | 1802  |
| Asthma            | Aspirin     | 1781  |

## 8. Readmission Rates by Medical Condition (within 30 days)

| Medical Condition | Readmissions | ReadmissionRate |
|-------------------|--------------|-----------------|
| Obesity           | 854          | 14,233.33       |
| Cancer            | 846          | 14,100.00       |
| Diabetes          | 832          | 13,866.67       |
| Hypertension      | 832          | 13,866.67       |
| Asthma            | 823          | 13,716.67       |
| Arthritis         | 779          | 12,983.33       |

## 9. Treatment Effectiveness by Medical Condition

| Medical Condition | Medication  | AvgStay | AvgBilling |
|-------------------|-------------|---------|------------|
| Arthritis         | Ibuprofen   | 15.26   | 25,660.25  |
| Arthritis         | Lipitor     | 15.44   | 25,242.05  |
| Arthritis         | Paracetamol | 15.45   | 25,245.44  |
| Arthritis         | Penicillin  | 15.60   | 25,700.28  |
| Arthritis         | Aspirin     | 15.75   | 25,705.12  |
| Asthma            | Paracetamol | 15.27   | 25,667.59  |
| Asthma            | Penicillin  | 15.48   | 25,511.29  |
| Asthma            | Aspirin     | 15.76   | 25,621.53  |
| Asthma            | Ibuprofen   | 15.87   | 26,240.45  |
| Asthma            | Lipitor     | 16.02   | 25,130.14  |

## 10. Impact of Patient Demographics on Health Outcomes

| Gender | AgeGroup | Medical Condition | AvgStay | AvgBilling |
|--------|----------|-------------------|---------|------------|
| Female | 18-30    | Asthma            | 15.84   | 25,735.40  |
| Female | 18-30    | Cancer            | 15.42   | 25,408.83  |
| Female | 18-30    | Arthritis         | 15.41   | 25,331.44  |
| Female | 18-30    | Hypertension      | 15.31   | 25,720.13  |
| Female | 18-30    | Obesity           | 15.30   | 26,139.05  |
| Female | 18-30    | Diabetes          | 15.11   | 25,989.24  |
| Female | 31-50    | Arthritis         | 15.73   | 24,983.18  |
| Female | 31-50    | Cancer            | 15.60   | 24,438.78  |
| Female | 31-50    | Asthma            | 15.50   | 25,527.61  |
| Female | 31-50    | Diabetes          | 15.42   | 25,000.20  |

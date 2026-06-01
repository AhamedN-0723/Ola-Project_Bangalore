# Ola Ride Booking Analytics Dashboard

## Overview

The Ola Ride Booking Analytics Dashboard is an end-to-end data analytics project designed to analyze ride booking patterns, customer behavior, driver performance, cancellations, revenue trends, and operational efficiency. The project leverages Python for data cleaning and preprocessing, SQLite for data storage and querying, Streamlit for interactive dashboard development, and Power BI for advanced business intelligence reporting.

The objective of this project is to transform raw ride-booking data into meaningful insights that help understand booking trends, customer satisfaction, cancellation patterns, payment preferences, and overall business performance.

---

## Tools & Technologies Used

- Python
- Pandas
- SQLite3
- Matplotlib
- Streamlit
- Power BI
- PyCharm

---

## Features

- Interactive dashboard for ride booking analysis.
- Plots displaying total bookings, revenue, cancellations, and successful rides.
- Vehicle-type-wise performance analysis.
- Customer and driver cancellation trend analysis.
- Revenue insights based on payment methods.
- Customer rating and driver rating analysis.
- Dynamic SQL-powered data retrieval and filtering.
- Power BI dashboard for advanced visual analytics and reporting.

---

## Project Structure

```text
Ola-Ride-Booking-Analytics/
│
├── data/
|   └── OLA_DataSet.xlsx
│
├── eda/
│   └── ola_read_clean.py
│
├── Querying/
│   └── ola_main.py
│
├── Streamlit/
│   └── app.py
│
├── visualization/
│   └── powerbi.pbix
│
└── README.md
```

---

## Key Insights Generated

- Total and successful ride bookings.
- Booking trends across different vehicle categories.
- Revenue distribution by payment method.
- Customer cancellation reasons analysis.
- Driver cancellation reasons analysis.
- Average customer and driver ratings.
- Ride distance and booking value trends.

---

## Dashboard Modules

### Streamlit Dashboard
- Booking Status Analysis
- Revenue Analysis
- Rating Analysis
- Cancellation Analysis

### Power BI Dashboard
- Executive Summary
- Revenue Dashboard
- Customer Insights
- Driver Performance Analysis
- Vehicle Type Analysis

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Install Dependencies

```bash
pip install pandas matplotlib streamlit
```

### 3. Run Data Processing Scripts

```bash
python ola_read_clean.py
```

### 4. Read cleaned data and create a db

```bash
python ola_main.py
```

### 5. Launch Streamlit Dashboard

```bash
streamlit run Streamlit app.py
```

---

## Future Enhancements

- Real-time ride booking analytics.
- Predictive cancellation analysis using Machine Learning.
- Driver performance forecasting.
- Automated report generation.
- Integration with cloud databases.

---

## Important Notes
Data Cleaning Workflow

The original dataset was provided in Excel (.xlsx) format. During the data cleaning process, the dataset was cleaned, standardized, and exported as:

ola_clean.csv

This cleaned CSV file serves as the single source for:

-SQLite database creation

-SQL querying and analysis

-Streamlit dashboard

-Power BI reporting

-Database Creation (Required Before Querying & Streamlit)

Before running any SQL queries or launching the Streamlit application, a SQLite database must be created using the cleaned dataset.

Run the following code after generating ola_clean.csv:

import pandas as pd
import sqlite3 as sq

df = pd.read_csv('ola_clean.csv')

conn = sq.connect('ola.db')
df.to_sql('ola_rides', conn, if_exists='replace', index=False)

This will create:

ola.db

with a table named:

ola_rides

The database is required for both:

-SQL-based analysis
-Streamlit dashboard functionality

## Handling of Null Values

Please note that the null values present in the original dataset were carefully analyzed and determined to be valid based on the business logic of the ride-booking process. Therefore, no records were removed due to missing values (except vehicle_images column).

For example:

Customer and driver ratings are naturally unavailable (null) when a ride is cancelled, since the trip was never completed and no rating can be provided.
Successful rides do not have cancellation reasons, as no cancellation occurred.
Certain cancellation-related fields may be unavailable depending on whether the ride was cancelled by the customer or the driver.
Therefore:

No rows containing null values were removed.
Missing values were preserved and replaced with "NA" (Not Applicable) wherever appropriate.
This approach ensures that business-critical information is retained and analytical accuracy is maintained.

Examples include:

Cancellation reasons for successful rides
Driver-related fields for customer-cancelled bookings
Customer-related fields for driver-cancelled bookings

These values are intentionally marked as "NA" because they are not applicable to those specific booking scenarios.

## Author

**Ahamed Nazeer**

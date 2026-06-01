#CREATING DATABASE AND QUERYING

import pandas as pd
import sqlite3 as sq


df = pd.read_csv('ola_clean.csv')

conn = sq.connect('ola.db')
df.to_sql('ola_rides', conn, if_exists='replace', index=False)
table = 'ola_rides'

#1. RETRIEVE ALL SUCCESSFUL BOOKINGS

query_success = f'''
SELECT *
FROM {table}
WHERE booking_status = 'Success';
'''
print('\n1. Total sucessful bookings:\n', pd.read_sql(query_success, conn))

#2. Average ride distance for each vehicle type

query_avg_distance = f'''
SELECT vehicle_type, ROUND(AVG(ride_distance),2) AS avg_distance
FROM {table}
GROUP BY vehicle_type
order by avg_distance desc;
'''

print('\n2. Average ride distance for each vehicle type:\n', pd.read_sql(query_avg_distance, conn))

#3. Total number of canceled rides by customers

query_cancelled_customer = f'''
SELECT
    booking_status, COUNT(booking_id) as total_rides
FROM
    {table}
WHERE
    booking_status = 'Canceled by Customer';
'''

print('\n3. Total number of canceled rides by customers:\n', pd.read_sql(query_cancelled_customer, conn))

#4. Top 5 customers who booked the highest number of rides
query_top_customers = f'''
SELECT
    customer_id, COUNT(booking_id) AS total_rides
FROM
    {table}
GROUP BY customer_id
ORDER BY total_rides DESC
LIMIT 5;
'''
print('\n4. Top 5 customers who booked the highest number of rides:\n', pd.read_sql(query_top_customers, conn))

#5. Number of rides cancelled by drivers due to personal and car-related issues

query_driver_issues = f'''
SELECT
    canceled_rides_by_driver, COUNT(booking_id) AS total_rides
FROM
    {table}
WHERE
    canceled_rides_by_driver = 'Personal & Car related issue'
'''
print('\n5. Number of rides cancelled by drivers due to personal and car-related issues:\n', pd.read_sql(query_driver_issues, conn))

#6. Maximum and minimum driver ratings for Prime Sedan bookings

query_driver_ratings = f'''
SELECT
    vehicle_type,
    MAX(driver_ratings) AS max_rating,
    MIN(driver_ratings) AS min_rating
FROM
    {table}
WHERE
    vehicle_type = 'Prime Sedan';
'''
print('\n6. Maximum and minimum driver ratings for Prime Sedan bookings:\n', pd.read_sql(query_driver_ratings, conn))

#7. All rides where payment was made using UPI

query_upi = f'''
SELECT
    *
FROM
    {table}
WHERE
    payment_method = 'UPI';
'''
print('\n7. All rides where payment was made using UPI:\n', pd.read_sql(query_upi, conn))

#8. Average customer rating per vehicle type

query_avg_rating = f'''
SELECT
    vehicle_type,
    ROUND(AVG(driver_ratings),2) AS avg_rating
FROM
    {table}
GROUP BY vehicle_type
ORDER BY avg_rating DESC;
'''
print('\n8. Average customer rating per vehicle type:\n', pd.read_sql(query_avg_rating, conn))

#9. Total booking value of rides completed successfully
query_total_revenue = f'''
SELECT
    booking_status, SUM(booking_value) AS total_revenue
FROM
    {table}
WHERE
    booking_status = 'Success';
'''
print('\n9. Total booking value of rides completed successfully:\n', pd.read_sql(query_total_revenue, conn))

#10. All incomplete rides along with the reason

query_incomplete = f'''
SELECT
    incomplete_rides_reason, COUNT(*) AS total_rides
FROM
    {table}
WHERE
    incomplete_rides = 'Yes'
GROUP BY incomplete_rides_reason;
'''
print('\n10. All incomplete rides along with the reason:\n', pd.read_sql(query_incomplete, conn))
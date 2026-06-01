import sqlite3 as sq
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

conn = sq.connect('ola.db')
st.title("\nOla Ride Insights - Bangalore\n")
table = 'ola_rides'

case_study = st.selectbox("Select Analysis".upper(),
                          ["SELECT ANY ANALYSIS TO CONTINUE",
                           "1. List of all successful bookings".upper(),
                           "2. Average ride distance for each vehicle type".upper(),
                           "3. Total number of canceled rides by customers".upper(),
                           "4. Top 5 customers who booked the highest number of rides".upper(),
                           "5. Number of rides cancelled by drivers due to personal and car-related issues".upper(),
                           "6. Maximum and minimum driver ratings for Prime Sedan bookings".upper(),
                           "7. All rides where payment was made using UPI".upper(),
                           "8. Average customer rating per vehicle type".upper(),
                           "9. Total booking value of rides completed successfully".upper(),
                           "10. All incomplete rides along with the reason".upper(),
                           "11. Payment Study".upper()])

if case_study == "SELECT ANY ANALYSIS TO CONTINUE":

 st.image(r"Ola-Fleet2.gif")
 st.markdown("<h4 style='text-align: right;'>by Ahamed N</h4>", unsafe_allow_html=True)


elif case_study == "1. List of all successful bookings".upper():
 query_success = f'''
    SELECT *
    FROM {table}
    WHERE booking_status = 'Success';
    '''
 df = pd.read_sql(query_success, conn)
 st.subheader("List of all successful bookings:".upper())
 st.dataframe(df)
 st.write("Helps track completed rides and measure platform reliability and demand trends.")



elif case_study == "2. Average ride distance for each vehicle type".upper():
 query_avg_distance = f'''
 SELECT vehicle_type, ROUND(AVG(ride_distance),2) AS avg_distance
 FROM {table}
 GROUP BY vehicle_type
 order by avg_distance desc;
 '''
 df= pd.read_sql(query_avg_distance, conn)
 st.subheader("Average ride distance for each vehicle type".upper())
 st.dataframe(df)
 st.write("Helps understand which vehicle types are used for short vs long trips and optimize fleet allocation.")
 fig, ax = plt.subplots()
 ax.bar(df["vehicle_type"], df["avg_distance"], width=0.5)
 plt.xticks(rotation=90)
 st.pyplot(fig)

elif case_study == "3. Total number of canceled rides by customers".upper():
 query_cancelled_customer = f'''
 SELECT
     booking_status, COUNT(booking_id) as total_rides
 FROM
     {table}
 WHERE
     booking_status = 'Canceled by Customer';
 '''
 df = pd.read_sql(query_cancelled_customer, conn)
 st.subheader("Total number of canceled rides by customers".upper())
 st.dataframe(df)
 st.write("Helps identify customer-side drop-offs and potential issues in pricing, UX, or availability.")


elif case_study == "4. Top 5 customers who booked the highest number of rides".upper():
 query_top_customers = f'''
 SELECT
     customer_id, COUNT(booking_id) AS total_rides
 FROM
     {table}
 GROUP BY customer_id
 ORDER BY total_rides DESC
 LIMIT 5;
 '''
 df = pd.read_sql(query_top_customers, conn)
 st.subheader("Top customers who booked the highest number of rides".upper())
 st.dataframe(df)
 st.write("Helps identify loyal/high-value customers for retention programs and rewards.")

elif case_study == "5. Number of rides cancelled by drivers due to personal and car-related issues".upper():
 query_driver_issues = f'''
 SELECT
     canceled_rides_by_driver, COUNT(booking_id) AS total_rides
 FROM
     {table}
 WHERE
     canceled_rides_by_driver = 'Personal & Car related issue'
 '''
 df= pd.read_sql(query_driver_issues, conn)
 st.subheader("Number of rides cancelled by drivers".upper())
 st.dataframe(df)
 st.write("Helps monitor driver reliability and highlight operational or maintenance problems.")



elif case_study == "6. Maximum and minimum driver ratings for Prime Sedan bookings".upper():
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
 df = pd.read_sql(query_driver_ratings, conn)
 st.subheader("Maximum and minimum driver ratings for Prime Sedan".upper())
 st.dataframe(df)
 st.write("Helps evaluate service quality extremes and identify top and low-performing drivers.")

elif case_study == "7. All rides where payment was made using UPI".upper():
 query_upi = f'''
 SELECT
     *
 FROM
     {table}
 WHERE
     payment_method = 'UPI';
 '''
 df = pd.read_sql(query_upi, conn)
 st.subheader("Rides by payment method".upper())
 st.dataframe(df)
 st.write("Helps analyze digital payment adoption and customer payment preferences.")


elif case_study == "8. Average customer rating per vehicle type".upper():
 query_avg_rating = f'''
 SELECT
     vehicle_type,
     ROUND(AVG(driver_ratings),2) AS avg_rating
 FROM
     {table}
 GROUP BY vehicle_type
 ORDER BY avg_rating DESC;
 '''
 df = pd.read_sql(query_avg_rating, conn)
 st.subheader("Average customer rating per vehicle type".upper())
 st.dataframe(df)
 st.write("Helps compare customer satisfaction across different vehicle categories.")
 fig, ax = plt.subplots()
 ax.bar(df["vehicle_type"], df["avg_rating"], width=0.5)
 plt.xticks(rotation=90)
 st.pyplot(fig)


elif case_study == "9. Total booking value of rides completed successfully".upper():
 query_total_revenue = f'''
 SELECT
     booking_status, SUM(booking_value) AS total_revenue_₹
 FROM
     {table}
 WHERE
     booking_status = 'Success';
 '''
 df = pd.read_sql(query_total_revenue, conn)
 st.subheader("Total booking value of rides completed successfully".upper())
 st.dataframe(df)
 st.write("Helps measure revenue generated from completed trips and overall business performance.")

elif case_study == "10. All incomplete rides along with the reason".upper():
 query_incomplete = f'''
 SELECT
     incomplete_rides_reason, COUNT(*) AS total_rides
 FROM
     {table}
 WHERE
     incomplete_rides = 'Yes'
 GROUP BY incomplete_rides_reason;
 '''
 df = pd.read_sql(query_incomplete, conn)
 st.subheader("Incomplete rides along with the reason".upper())
 st.dataframe(df)
 st.write("Helps detect operational gaps and reduce ride failures by fixing root causes.")
 fig, ax = plt.subplots()
 ax.bar(df["incomplete_rides_reason"], df["total_rides"], width=0.4)
 plt.xticks(rotation=90)
 st.pyplot(fig)

elif case_study == "11. Payment Study".upper():
 query_payment = f'''
  SELECT
      payment_method, COUNT(booking_id) AS total_rides
  FROM
      {table}
  WHERE booking_status = 'Success'
  GROUP BY payment_method
  ORDER BY total_rides DESC;
  '''
 df = pd.read_sql(query_payment, conn)
 st.subheader("Payment Study".upper())
 st.dataframe(df)
 st.write("Helps us understand the preferred payment methods by the customer.")
 fig, ax = plt.subplots()
 ax.bar(df["payment_method"], df["total_rides"], width=0.4)
 plt.xticks(rotation=90)
 st.pyplot(fig)
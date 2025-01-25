import sqlite3

# setting up the database
conn = sqlite3.connect("./weather.db")
cursor = conn.cursor()

# https://sqlite.org/datatype3.html
cursor.execute("""
    INSERT INTO cities (city, country, latitude, longitude)
    VALUES ('Playa de aro', 'Spain', 41.81762, 3.06747);
""")
# 4 data types: when you configure the databse you can be as specific as you want.


# https://sqlite.org/datatype3.html
cursor.execute("""
    INSERT INTO cities (city, country)
    VALUES ('Tallinn', 'Estonia');
""")
cursor.execute("""
    INSERT INTO cities (city, country, latitude, longitude)
    VALUES 
    ('Barcelona', 'Spain', 41.38506, 2.17340),
    ('Girona', 'Spain', 41.98181, 2.82493),
    ('Moscow', 'Russia', 55.75583, 37.61730),
    ('Madrid', 'Spain', 40.41678, -3.70379),
    ('Copenhagen', 'Denmark', 55.67610, 12.56834),
    ('Amsterdam', 'Netherlands', 52.36757, 4.90414),
    ('Paris', 'France', 48.85661, 2.35222),
    ('London', 'United Kingdom', 51.50735, -0.12776),
    ('Berlin', 'Germany', 52.52001, 13.40495),
    ('Rome', 'Italy', 41.90278, 12.49636),
    ('Milan', 'Italy', 45.46420, 9.18998),
    ('Saint Petersburg', 'Russia', 59.93428, 30.33510),
    ('Vienna', 'Austria', 48.20817, 16.37382),
    ('Bucharest', 'Romania', 44.42677, 26.10254),
    ('Athens', 'Greece', 37.98381, 23.72754),
    ('Prague', 'Czech Republic', 50.07554, 14.43780),
    ('Dublin', 'Ireland', 53.34980, -6.26031);
""")

# tell the database to confirm the changes made by the EXECUTE command
conn.commit()


# ALWAYS close the connection
conn.close()
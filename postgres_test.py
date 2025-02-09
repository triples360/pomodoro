# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 01:09:22 2025

@author: shubh
"""

import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="postgres", port=5432)

curr = conn.cursor()

curr.execute("""
 CREATE TABLE IF NOT EXISTS timer
 (id INT PRIMARY KEY,
 user_id INT,
 time_elapsed INT);
""")

curr.close()
conn.close()


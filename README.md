# Sensor Data Visualization

## Introduction

The purpose of this code is to take sensor data from given data source and visualize them in a local web dashboard. 

This code creates a local web page at http://localhost:8000/ and displays a dashboard containing sensor data from a PostgreSQL database. This Postgres database contains tables containing temperature, pH, dissolved oxygen, and pressure. We needed to query this data and use this data for display in a dashboard which we made using Plotly Dash. 

1. **Tech Stack:**
   - Python (provides libraries to easily query from database and interact with Plotly Dash) 
   - HTML (to help create frontend for local web page)
   - Plotly Dash (library to use dashboard and also creates web server at http://localhost:8000/_
   - PostgreSQL (to query data from Postgres database, which could be any other data source)
   - Docker (to be able to run this web dashboard on any machine quickly)
2. **How to run this code:**
   - Open the docker app, run docker compose up and on your browser go to http://localhost:8000/
3. **Challenges:**
   - A problem we ran into early on was the absence of `requirements.txt` for cleaner dependency installation in the Dockerfile. We           created a `requirements.txt` to address this
   - Another issue was having an outdated operating system for the Mac laptop so Docker would not run the container properly. To fix          this we had to update to the most recent version of the Mac Operating System
4. **Learnings:**
   - Overall, this project provided valuable experience with Docker, dealing with errors using external resources, interacting with           PostgreSQL databases in Python, and utilizing Dash and Plotly.

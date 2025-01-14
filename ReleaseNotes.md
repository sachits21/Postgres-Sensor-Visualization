# Explanation of Take-Home Project Steps

Hi! I wanted to explain the steps I took to finish this take-home project.

1. **Flask:**
   - After setting up my environment, I first used a very basic Flask server to see if the local server could run.

2. **Database Connection:**
   - I aimed to connect to PostgreSQL and extract the necessary data. For this, I chose the `psycopg2` library.

3. **Requirements.txt Creation:**
   - A problem I ran into early on was the absence of `requirements.txt` for cleaner dependency installation in the Dockerfile. I created a `requirements.txt` to address this.

4. **Plot Creation Without Docker:**
   - To visualize the data before integrating with Docker, I connected to the database on a local notebook and pulled the data. I used the `plotly` library for creating interactive plots, preferring it over something like `matplotlib`.

5. **Integration with Docker:**
   - After successfully creating the plots, I proceeded to complete the project within a Docker container.

6. **Choice of Dash Library:**
   - I decided to use the Dash library for this application since it integrates well with Plotly plots. As Dash is built on top of Flask, I didn't need to explicitly call Flask for anything.

7. **Dash Layout Design:**
   - I used a basic Dash layout featuring a 2x2 grid of the plots, which is implemented in my final server.

8. **Project Learnings:**
   - Overall, this project provided valuable experience with Docker, dealing with errors using external resources, interacting with PostgreSQL databases in Python, and utilizing Dash and Plotly.

9. **References:**
   - Here's a list of references I found helpful during the project:
     - [Dockerize Your Dash App](https://medium.com/@yahyasghiouri1998/dockerize-your-dash-app-f502275475fa)
     - [Full Stack Development with Docker Compose](https://medium.com/@datails/full-stack-development-with-docker-compose-c517ec826696)
     - [Docker Compose Networking](https://docs.docker.com/compose/networking/)
     - [Making Requests Between Containers](https://stackoverflow.com/questions/52010778/docker-compose-make-requests-between-containers)
     - [Dash for Beginners](https://towardsdatascience.com/dash-for-beginners-create-interactive-python-dashboards-338bfcb6ffa4)
     - [Plotly Dash with Flask](https://hackersandslackers.com/plotly-dash-with-flask/)
     - [YouTube Tutorial on Dash](https://www.youtube.com/watch?v=Ma8tS4p27JI&list=PLH6mU1kedUy8fCzkTTJlwsf2EnV_UvOV-)

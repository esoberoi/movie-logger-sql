# SQL Movie Logger (w/ Django)
(Very) basic movie logger site to test the ORM capabilities of Django with SQL databases.
Contains two dynamic models: Movie, MovieLog
**Languages**: Python, HTML
**Libraries**: Django, (implicit) SQL calls

## How it Works
- **TO RUN**: Navigate to project directory and run command "python manage.py runserver". Use given address + "/search" to avoid error with landing page
- Add movies to the Movie model (no hardcoding included, completely dynamic).
- Add logs to the MovieLog model. Title of movie must correspond to an existing movie in the Movie model (foreign key). Make sure to include a personal userID as well.
- Update your logs, sort by different criteria, and generate log reports with date ranges

## Features
- 3 indexes on commonly queried fields (Movie.year, MovieLog.user_id, MovieLog.date_watched)
- Built in Django SQL injection protection (query parameterization)
- Low level concurrency/transaction control with updating movie logs (atomicity transactions)
- Dynamic SQL additions, updating, and deletions

## Screenshots
![image](https://github.com/esoberoi/movie-logger-sql/assets/70533912/31735508-ef03-4704-89c7-683b275381d9)
![image](https://github.com/esoberoi/movie-logger-sql/assets/70533912/1ecad82e-9935-4e61-9db2-c63850f1a0ce)
![image](https://github.com/esoberoi/movie-logger-sql/assets/70533912/a1074397-7efe-4c02-97e0-b37aabf17367)
![image](https://github.com/esoberoi/movie-logger-sql/assets/70533912/484d77bd-b8cd-4cb1-954c-5b65b996ec93)
![image](https://github.com/esoberoi/movie-logger-sql/assets/70533912/1dcfb99c-911c-4ea2-a79f-1e9c50a12748)
![image](https://github.com/esoberoi/movie-logger-sql/assets/70533912/3295ea75-b435-42bb-952b-c36576f64d88)

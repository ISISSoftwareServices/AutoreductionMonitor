# Framework
## Description
* A small software service designed to regularly query a database (once per day).
* Generates statistics from data held within the target databse.
* Produces a single record (per instrument) to describe the changes in that target db each day.
* Pushes that record to its own database.
* Is accompanied by a script that will produce a report on the data in a human readable format.
  * Report can be customised for given instruments or given time period
* Is able to give feedback to the software team about missing runs from the database 

## Glossary
* Job = A single message through the system coralating to a reduction_run in the autoreduction database
* Run = The unique (per instrument) number assigned to a single peice of ISIS specific data

## Query defintiions
* for today:
  * for each instrument:
    * *EASY*
    * How many jobs took place      (jobs_total)
    * How many jobs succeeded       (jobs_passed)
    * How many jobs failed          (jobs_failed)
    * Runs started by service       (started_by_auto)
    * Runs started by devs          (started_by_devs)
    * Runs started by users         (started_by_users)
    * *MEDIUM*
    * Avg execution time for passed (avg_exe_time)
    * How many runs where processed (runs_total)
    * How many runs succeeded       (runs_passed)
    * How many runs failed          (runs_failed)
    * *HARD*
    * Runs that failed but now pass (resolved_runs)

## Main components
* Query Collection
  * python file - collection of strings relating to specific queries that can be formatted per instrument (or other param as required)
* Database Access to Autoreduction
  * python file - take this from autoreduction code base (database_client.py) 
* Database Access to Monitoring db
  * python file - might be same thing as above?
* Query handler
  * python file - execute query collection with replaced vars on autoreductio database
* Log handling
  * python file - handles all the logging to a single file
* Main
  * Python file - calls Query handler with current date (date range)
* Credentials
  * Python file - holds db credentials
  
## UML design


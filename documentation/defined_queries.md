# Defined Queries from Autoreduction DB

## A list of defined queries
### Runs and count of runs 
* get all runs which were created for the current date.
* get count of all runs which were created for the current date.
* get all runs which took place for current date per instrument
* get count of all runs which took place for current date per instrument
* get all runs which took place on current date per status
* get count of all runs which took place for current date per status
* get all runs which took place for current date per instrument per status
* get count of all runs which took place for current date per instrument per status.
* get count of all unique runs which took place for current date

### Resolved and count of resolved:
* get all runs which successfully resolved for current date
* get count of all runs which took place successfully for current date
* get all runs which took place successfully per instrument for current date
* get count of all runs which took place successfully per instrument for current date
* get all runs which did not successfully resolve for current date
* get count of all runs which did not successfully resolve for current date
* get count of all runs per instrument which did not successfully resolve for current date

### Run version count:
* get all runs which have more than one run version per instrument for current date
* get count of runs with multiple run versions per instrument for current date.
* get all runs which have more than one run version per instrument, per experiment for current date
* get count of runs with multiple run versions per instrument, per experiment for current date.

### Execution times:
* get time difference between started and finished per instrument  for current date.
* get time difference between started and finished per instrument, per experiment for current date.


## All of the above queries but over a date range:

### Averages:
* Average count of runs per day over a date range
* Average count of runs per day, per instrument over a date range
* Average count of runs per experiment. 
* Average count of runs per type of instrument/technique (will need to add types to python dict for this as not stored in db)
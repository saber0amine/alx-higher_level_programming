# Python - Object-relational mapping (ORM) Project

## Overview:

- Explored the implementation of object-relational mapping for database scripting in Python.
- Utilized MySQLdb and SQLAlchemy to perform various operations such as querying, creating, editing, and deleting tables in a MySQL database.

## Tests:

- [tests](./tests): Contains SQL and Python scripts for setting up test tables. Provided by ALX.

## Tasks:

### 0. Get all states
- [0-select_states.py](./0-select_states.py): Python script using MySQLdb to list all states in the `hbtn_0e_0_usa` database.
- Usage: `./0-select_states.py <mysql username> <mysql password> <database name>`.
- Results are ordered by ascending `states.id`.
- [Source Code](./0-select_states.py)

### 1. Filter states
- [1-filter_states.py](./1-filter_states.py): Python script using MySQLdb to list states with names starting with `N` in the `hbtn_0e_0_usa` database.
- Usage: `./1-filter_states.py <mysql username> <mysql password> <database name>`.
- Results are ordered by ascending `states.id`.
- [Source Code](./1-filter_states.py)

### 2. Filter states by user input
- [2-my_filter_states.py](./2-my_filter_states.py): Python script using MySQLdb to display states matching a given name in the `states` table of the `hbtn_0e_0_usa` database.
- Usage: `./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
- Results are ordered by ascending `states.id`.
- Uses string formatting to construct the SQL query.
- [Source Code](./2-my_filter_states.py)

### 3. SQL Injection...
- [3-my_safe_filter_states.py](./3-my_safe_filter_states.py): Python script using MySQLdb to display states matching a given name in the `states` table of the `hbtn_0e_0_usa` database.
- Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
- Results are ordered by ascending `states.id`.
- Protects against SQL injections.
- [Source Code](./3-my_safe_filter_states.py)

### 4. Cities by states
- [4-cities_by_state.py](./4-cities_by_state.py): Python script using MySQLdb to list all cities from the `hbtn_0e_4_usa` database.
- Usage: `./4-cities_by_state.py <mysql username> <mysql password> <database name>`.
- Results are ordered by ascending `cities.id`.
- [Source Code](./4-cities_by_state.py)

### 5. All cities by state
- [5-filter_cities.py](./5-filter_cities.py): Python script using MySQLdb to list all cities of a given state in the `hbtn_0e_4_usa` database.
- Usage: `./5-filter_cities.py <mysql username> <mysql password> <database name>`.
- Results are sorted by ascending `cities.id`.
- [Source Code](./5-filter_cities.py)

### 6. First state model
- [model_state.py](./model_state.py): Python module defining a class `State` that inherits from SQLAlchemy `Base` and links to the MySQL table `states`.
- [Source Code](./model_state.py)

### 7. All states via SQLAlchemy
- [7-model_state_fetch_all.py](./7-model_state_fetch_all.py): Python script using SQLAlchemy to list all `State` objects from the `hbtn_0e_6_usa` database.
- Usage: `./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>`.
- Results are sorted by ascending `states.id`.
- [Source Code](./7-model_state_fetch_all.py)

### 8. First state
- [8-model_state_fetch_first.py](./8-model_state_fetch_first.py): Python script using SQLAlchemy to print the first `State` object from the `hbtn_0e_6_usa` database, ordered by `states.id`.
- Usage: `./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>`.
- Prints `Nothing` if the `states` table is empty.
- [Source Code](./8-model_state_fetch_first.py)

### 9. Contains `a`
- [9-model_state_filter_a.py](./9-model_state_filter_a.py): Python script using SQLAlchemy to list all `State` objects that contain the letter `a` in the `hbtn_0e_6_usa` database.
- Usage: `./9-model_state_filter_a.py <mysql username> <mysql password> <database name>`.
- Results are ordered by ascending `states.id`.
- [Source Code](./9-model_state_filter_a.py)

### 10. Get a state
- [10-model_state_my_get.py](./10-model_state_my_get.py): Python script using SQLAlchemy to print the `id` of the `State` object with a name matching the argument in the `hbtn_0e_6_usa` database.
- Usage: `./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state searched name>`.
- Displays the `id` of the matched `State`.
- Prints `Not found` if no match is found.
- [Source Code](./10-model_state_my_get.py)

### 11. Add a new state
- [11-model_state_insert.py](./11-model_state_insert.py): Python script using SQLAlchemy to add the `State` object "Louisiana" to the `hbtn_0e_6_usa` database.
- Usage: `./11-model_state_insert.py <mysql username> <mysql password> <database name>`.
- Prints the `id` of the new `State` after creation.
- [Source Code](./11-model_state_insert.py)

### 12. Update a state
- [12-model_state_update_id_2.py](./12-model_state_update_id_2.py): Python script using SQLAlchemy to change the name of the `State` object with `id = 2` in the `hbtn_0e_6_usa` database to "New Mexico".
- Usage: `./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>`.
- [Source Code](./12-model_state_update_id_2.py)

### 13. Delete states
- [13-model_state_delete_a.py](./13-model_state_delete_a.py): Python script using SQLAlchemy to delete all `State` objects with a name containing the letter `a` from the `hbtn_0e_6_usa` database.
- Usage: `./13-model_state_delete_a.py <mysql username> <mysql password> <database name>`.
- [Source Code](./13-model_state_delete_a.py)

### 14. Cities in state
- [model_city.py](./model_city.py): Python module defining a class `City

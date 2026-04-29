# Security Database Project
This project is the result of completing a series of database security and management exercises provided by
Specialisterne.

It demonstrates PostgreSQL role management, controlled data access, and database initialization using the Northwind 
dataset.

## Exercise Goal
Implement a system that has the supports that following database users with the administrative privileges stated:

1. `Admin` - Full administrative access (`SUPERUSER`)
2. `Northwind Admin` - Full administrative access but limited to the Northwind database
3. `Data Inspector` - Read-only access to all tables
4. `Data Engineer` - Read and write access to all tables
5. `Analyst` - All privileges for the `reports` schema only
6. `Order Viewer` - Read-only access to a single table (`orders`) in the `reports` schema
7. `Report Viewer` - Read-only access to tables in the `reports` schema only 

> **Note:** Granting `SUPERUSER` privileges is not recommended in production environments. It is included here because it was part of the exercise requirements.


# See the Solution in Action
1. Create a PostgreSQL database instance.
2. Create a configuration file named `local_db_config.ini` in the `configs/` folder, based on `db_config_example.ini`.
3. Install the required dependencies from the `requirements.txt` file.
4. Run the `main.py` to initialize the the database create the roles and users with their respective privileges.

## Acknowledgements
[![img.png](docs/img.png)](https://dk.specialisterne.com/)

This project was developed while I was participating in the Specialisterne Academy as part of the Data Management track 
(February 2 to April 30, 2026).

Specialisterne is an organization that creates job opportunities for people with autism and similar challenges. Through 
training, support, and guidance for employers on workplace inclusion, it helps individuals strengthen their skills and 
find meaningful employment in the tech industry.

I am grateful for the structured learning environment, valuable feedback, and collaborative atmosphere that helped make 
this project possible.

## See Also
### Documentation
- [Project Challenges and Potential Future Work](docs/project_challenges.md)
Document detailing some of the notable technical challenges encountered during development, along with potential 
future improvements and extensions to the project.

### Specialisterne Academy Projects
- [Calculator](https://github.com/MikaelVM/Calculator) A simple calculator application built using Python, 
demonstrating basic programming concepts and CLI design.
- [Data Handling](https://github.com/MikaelVM/data-handling) A series of exercises focused on data manipulation and
analysis using Python.
- [Northwind Database](https://github.com/MikaelVM/northwind-foods) A project centered around the Northwind dataset, 
where i took the role of a data analyst to generate insights from the data.
- [Security Database](https://github.com/MikaelVM/security-db) A project focused on PostgreSQL role management and 
database security, demonstrating the implementation of various user roles with specific privileges.
- [Environment Database](https://github.com/MikaelVM/environment-data) A project focused on the ETL process of 
processing environment data from a public DMI API.
- [ETL Pipeline](https://github.com/MikaelVM/etl-pipeline) A full stack project utilizing the DMI weather data from the 
Environment Database project, with a focus on a more complete ETL pipeline, Docker-based initialization and 
a CLI for running the pipeline.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

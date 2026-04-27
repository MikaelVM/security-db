# Security Database Project
This project is the result of completing a series of database security and management exercises provided by
Specialisterne.

It demonstrates PostgreSQL role management, controlled data access, and database initialization using the Northwind 
dataset.

## Exercise Goal
Implement a system that has the supports that following database users with the administrative privileges stated:

1. `Admin` - Full administrative access (Superuser privileges)
2. `Northwind Admin` - Full administrative access but limited to the Northwind database
3. `Data Inspector` - Read-only access to all tables
4. `Data Engineer` - Read and write access to all tables
5. `Analyst` - All privileges for the `reports` schema only
6. `Order Viewer` - Read-only access to a single table (`orders`) in the `reports` schema
7. `Report Viewer` - Read-only access to tables in the `reports` schema only 

I would like to note, that i am aware that making a user with superuser privileges is not a good practice in production 
environments, but it was part of the exercise and thus included in the project.

# See the Solution in Action
1. Create a PostgreSQL database instance (e.g., using Docker or a local installation).
2. Create a new config named `local_db_config.ini` in the `config` folder, following the structure of `db_config_example.ini` and provide the necessary connection details for your PostgreSQL instance.
3. Install the required dependencies from the `requirements.txt` file.
4. Run the `main.py` script to execute the database initialization and user setup process.

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
### [Project Challenges and Potential Future Work](docs/project_challenges.md)
Document detailing some of the notable technical challenges encountered during development, along with potential 
future improvements and extensions to the project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

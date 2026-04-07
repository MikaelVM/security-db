# security-db
Project for the Data Management track in the Specialisterne Academy, focused on database security and management.

## Description

This project is a collection of Python scripts and SQL templates that demonstrate comprehensive database security and management practices. It focuses on:

- **Role-Based Access Control (RBAC)** - Creating and managing database roles with granular permissions
- **Database Initialization** - Automated setup of schemas, tables, and sample data
- **PostgreSQL Security** - Best practices for managing database users and privileges
- **Access Control Testing** - Verifying that roles can only access data they're authorized to view

The project uses the **Northwind database** as a realistic dataset for demonstrating security concepts in a business context.

## Getting Started

### Prerequisites
- Python 3.13 or higher
- PostgreSQL 18 or higher
- pip (Python package manager)

### Dependencies

**Core**

| Dependency        | Purpose                                |
|------------------|----------------------------------------|
| `psycopg[binary]`| PostgreSQL database adapter for Python |
| `pytest`         | Testing framework                      |
| `rich`           | Rich text and pretty printing          |

**Linting & Code Quality (flake8 ecosystem)**

| Dependency                   | Purpose                                |
|-----------------------------|----------------------------------------|
| `flake8`                    | Code quality and style checking        |
| `flake8-annotations`        | Enforces type annotations              |
| `flake8-bugbear`            | Detects common bugs in Python          |
| `flake8-docstrings`         | Enforces docstring conventions         |
| `flake8-docstrings-complete`| Validates complete docstrings          |
| `flake8_import_order`       | Checks import order consistency        |


### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd security-db
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database connection:**
   - Copy the example config file:
     ```bash
     cp configs/examples/db_config_example.ini configs/local_db_config.ini
     ```
   - Edit `configs/local_db_config.ini` with your PostgreSQL credentials:
     ```ini
     [DBCONFIG]
     host=localhost
     port=5432
     dbname=postgres
     user=postgres
     password=your_password
     ```

### Running the Project

The main entry point is `main.py`, which orchestrates database initialization and demonstrates role-based access control.

**Basic usage:**
```bash
python main.py
```

**What the script does:**

1. **Initializes the database** - Creates schemas, tables, and sample data from the Northwind dataset
2. **Creates security roles** - Sets up five database roles with different permission levels:
   - `northwind_admin` - Full administrative access
   - `data_inspector` - Read-only access to all tables
   - `data_engineer` - Ability to create and modify tables
   - `analyst` - Read-only access to reports
   - `report_viewer` - Limited read access to specific reports
3. **Demonstrates access control** - Tests that each role can only access data they're permitted to see
4. **Creates analysis tables** - Generates summary reports based on the sample data

### Configuration

The project requires a PostgreSQL database configuration file at `configs/local_db_config.ini`. 

**Configuration options:**
- `host` - PostgreSQL server hostname (default: localhost)
- `port` - PostgreSQL server port (default: 5432)
- `dbname` - Database name (default: postgres)
- `user` - Database user
- `password` - Database password

**⚠️ Security Note:** Never commit the config file with real credentials to version control. Use environment variables for production setups.

## Authors
- Mikael Vind Mikkelsen

## License
Not yet specified.

## Project Challenges
This section documents the key technical challenges encountered during development and the solutions discovered.

### Psycopg3 - String Composition for SQL Queries

**Challenge:** Safely composing SQL queries that include dynamic identifiers (e.g., usernames) while preventing SQL injection.

During development, I needed a flexible way to construct SQL queries with dynamic values. While standard parameter substitution works well for values, it cannot be used for SQL identifiers such as table or column names. To address this, Psycopg3 requires the use of the Identifier class from the psycopg.sql module when inserting identifiers into queries.

Although this approach improves security by preventing SQL injection, it proved to be cumbersome in practice. The syntax is relatively verbose, and the available documentation and community examples are limited, making it difficult to implement efficiently.

Due to time constraints and the added complexity, this feature was not implemented.
### PostgreSQL Role Management

**Challenge:** PostgreSQL's role and privilege system is complex and non-intuitive. The learning curve was steep, particularly with understanding:

- How to create and manage roles with proper hierarchies
- The difference between roles, users, and groups
- How privileges propagate (or don't propagate) through role memberships

**Key Insight - ALTER DEFAULT PRIVILEGES:**
Roles and permissions assigned to a user do not automatically grant permissions to other users when they create new tables. This was a critical discovery that required explicit privilege assignment for future objects:

Add a section under project challenges about string composition using the following as inspiration:
Psycopg3:
Proper string composition for SQL queries to avoid SQL injection:
I wanted an easy way to compose SQL queries with variables, but since i needed to pass a variable into an identifier (username), I had to use the Identifier class from psycopg3.sql module, as psycopg3 does not allow parameter substitution for identifiers. This is a security measure to prevent SQL injection attacks.
However, this approach was very cumbersome, lacked in depth documentation and examples from other users. As I ran out of time, O could not implment the feature.

## Acknowledgements
### [Specilisterne Academy](https://dk.specialisterne.com/)

This project was developed during my participation in the Specialisterne Academy’s three-month program (February 2 – 
April 30), as part of the Data Management track.

I am grateful for the structured learning environment, valuable feedback, and collaborative atmosphere that supported 
the development of this project.


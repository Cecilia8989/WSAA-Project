<h1 align="center">WSSA-project2024</h1>
<h2 align="center">Restful Api</h2>
<p align="center">
Cecilia Pastore 
</p>
<h3 align="center">Link of the built website:</h3>
<h3 align="center">https://cecilia891.pythonanywhere.com/</h3>
<h3 align="center">Please open it on Chrome</h3>

<details>
    <summary> Project assignement </summary>
           <p>

>Create a Web application in Flask that has a RESTful API, the application
should link to one or more database tables.
You should also create the web pages that can consume the API. I.e. performs
CRUD operations on the data.

</p>
</details>

## Table of Contents  
1. [Introduction](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#1-introduction)  
2. [Built with](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#2-built-with)
3. [How to Use It](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#3-how-to-use-it)  
    - 3.1 [Open the Website Hosted in PythonAnywhere](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#31-open-the-web-site-hosted-in-pythonanywhere)  
    - 3.2 [Run the Server on Your Local Network](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#32-run-the-server-on-your-local-network)  
        - 3.2.1 [Ensure Python is Installed, Along with the Following Libraries](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#321-ensure-that-python-is-installed-along-with-the-following-libraries)  
        - 3.2.2 [Set Up the Config File](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#322-set-up-the-config-file)  
        - 3.2.3 [Run the Server on Your Local Network](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#32-run-the-server-on-your-local-network)  
        - 3.2.4 [Accessing the Local API](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#325-accessing-the-local-api)
4. [Files Description](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#4-files-description)  
    - 4.1 [HTML/JavaScript/jQuery Templates](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#41-htmljavascriptjquery-templates)  
        - 4.1.1 [base.html](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#411-base-html)  
        - 4.1.2 [Home.html](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#412-homehtml)  
        - 4.1.3 [sign_up.html](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#413-sign_uphtml)  
        - 4.1.4 [login.html](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#414-loginhtml)  
        - 4.1.5 [update_DB.html](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#415-update_dbhtml)  
        - 4.1.6 [showDB.html](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#416-showdbhtml)  
        - 4.1.7 [create_employee.html](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#417-create_employeehtml)  
        - 4.1.8 [update_employee.html](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#418-update_employeehtml)  
    - 4.2 [Python Scripts](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#42-python-scripts)  
        - 4.2.1 [config_template.py](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#421-config_templatepy)  
        - 4.2.2 [create_sql_db.py](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#422-create_sql_dbpy)  
        - 4.2.3 [db_conn.py](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#423-db_connpy)
        - 4.2.4 [server.py](https://github.com/Cecilia8989/WSAA-Project/blob/main/README.md#424-serverpy)

[Source]()


## 1. Introduction 

This code builds a basic website where CRUD operations are performed on two tables within a SQL database. Users are allowed to sign in, log in, and log out. Unauthorized users can view the database but cannot create new entries or update/delete existing ones. Only logged-in users have permission to perform these actions. The website facilitates CRUD operations on two tables: one for registered users and one for the employees database. The employee database displays the name, surname, employee ID, and country for each entry. When registering on the website, usernames must be unique, and passwords must adhere to several security rules. Additionally, two users with the same employee ID cannot be created during a POST request.

The website is optimized for use on the Chrome browser.

## 2. Built with

This project leverages the following technologies:

- [HTML/CSS/JavaScript (1)](https://developer.mozilla.org/en-US/docs/Web): Used for the frontend development of the website.
- [Python (2)](https://www.python.org/): The backend of the website is developed using Python. The version that have been used is PYTHON 3.11.4
- [Flask (3)](https://flask.palletsprojects.com/): Flask, a lightweight WSGI web application framework, is utilized for building the web application.
- [jQuery (4)](https://jquery.com/): jQuery library is imported for simplifying AJAX calls and DOM manipulation.
- [Bootstrap (5)](https://getbootstrap.com/): Bootstrap framework is utilized for designing responsive and mobile-first websites.

## 3. How to use it

### 3.1 Open the Web site hosted in pythonanywhere

You can Open Website [cecilia891.pythonanywhere](https://cecilia891.pythonanywhere.com/) on a **Chrome browser** or run it on your local network.

<h4 align="center">OR</h4>

### 3.2 Run the server on your local network

Here are the steps to follow:

#### 3.2.1 Ensure that Python is installed, along with the following libraries:

- [Python (2)](https://www.python.org/): You can install Python from [here](https://www.python.org/ (2)) or [Anaconda (6)](https://www.anaconda.com/) package.
- [Flask (3)](https://pypi.org/project/Flask/): Flask is a lightweight WSGI web application framework for Python.
- [MySQL Connector (7)](https://pypi.org/project/mysql-connector-python/): MySQL Connector is a Python driver for connecting to MySQL databases.
- [Flask-Login (8)](https://pypi.org/project/Flask-Login/): Flask-Login provides user session management for Flask.

To install the libraries run the folloging command in the terminal:

    ```bash
    pip install Flask
    pip install Flask-Login
    pip install mysql-connector-python
    ```
#### 3.2.2 Set up the config file 

Navigate to the directory where the files are saved, 0pen the file `config_template.py` and add your Host, User, and Password for the SQL database. Finally, you can add a security key for the Flask application.

    ```python
    # File name: config_template.py

    class DBConfigSQL:
        HOST = "Enter the HOST of your MySQL"  # SQL database host
        USER = "Enter the USER of your MySQL"       # SQL database user
        PASSWORD = "Enter the PASSWORD of your MySQL"  # SQL database password

    class SecretKey:
        KEY = 'Enter a key for your Flask application'
    ```

Rename the `config_template.py` file to `config.py`. This will allow the server to recognize the config file with sensitive data to be imported.

#### 3.2.23 Create the mysql database named **employees_management**

On a command prompt, navigate to the repository where the scripts are located and run the script `create_sql_db.py` with the following command:

    ```bash
    python create_sql_db.py
    ```

The script will create a MySQL database called "employees_management" on your local machine using the connection defined in the config file previously modified.

#### 3.2.4 Run the Server.py

Navigate to a terminal where the repository is saved and run the `server.py` file with the following command:

    ```bash
    python server.py
    ```
#### 3.2.5 Accessing the Local API

open the indicated port on **Chrome browser** to navigate the API on your local network. This will start the server. By default, Flask applications run on port 5000. Then, open **Chrome** and navigate to http://127.0.0.1:5000/ to access the API.

```bash
Running on http://127.0.0.1:5000
```

## 4 Files Description

The project consists of several files belonging to two different categories:

- HTML/JavaScript/jQuery
- Python

Below is a description of each file involved.

### 4.1 HTML/JavaScript/jQuery Templates

#### 4.1.1 base html. 

This HTML file establishes the foundational structure and features for a Flask web application, encompassing navigation, message presentation, content arrangement, and styling, to be applied across all HTML files. The code has been take and adapted from the the tutorial [Tech With Tim (9)](https://www.youtube.com/watch?v=dam0GPOAvVI)

**Key Features:**

- **Meta Tags and Dependencies**: These are like instructions for the browser, ensuring everything looks right on different devices [(10)](https://stackoverflow.com/questions/1321878/how-to-prevent-favicon-ico-requests). It also includes links to some special style sheets [CSS (11)](https://www.w3schools.com/Css/) on [ Bootstrampt (5)](https://getbootstrap.com/) and a [fieldset style (12)](https://www.webteacher.ws/2009/12/10/style-fieldsets-like-a-pro/)to enhance the site's appearance.

- **Navigation Bar**: Positioned at the top of the page, the navigation bar facilitates user movement throughout the site, adjusting dynamically based on login status.

- **Flash Messages**: This section reserves space for dynamic messages generated by the application, providing feedback to users based on their interactions.

#### 4.1.2 Home.html

The "Home.html" file serves as the main page for presenting the structure of an API and is the landing page for users accessing the API.

**Key Features:**

- **Extending Base Template**: This file extends the "base.html" template, inheriting its navigation bar structure and styling [(9)](https://www.youtube.com/watch?v=dam0GPOAvVI).

- **Main Content**: The main content container showcases a welcoming message and a concise overview of the RESTful API's features. 

- **CSS Styling**: Custom CSS styles are applied to ensure proper formatting and layout of the content container, utilizing a [flexbox container (13)](https://www.w3schools.com/cssref/css3_pr_flex-direction.php) for improved alignment and responsiveness.

- **Action Selection**: Users are presented with action buttons within a form container. Two buttons are provided: one for displaying the "Employee-Database" and another for updating the database. Authentication is required for the latter action.

- **JavaScript Functions**: JavaScript functions are integrated to streamline navigation. Clicking on the buttons triggers functions that redirect users to specific pages: "show_employees" for displaying the employee database and "update_DB" for updating the database [(14)](https://stackoverflow.com/questions/52544089/how-to-create-two-html-buttons-side-by-side).

#### 4.1.3 sign_up.html

The "sign_up.html" file presents a sign-up form for users to register in the system. 

**Key Features:**

- **Extending Base Template**: This file extends the "base.html" template, inheriting its navigation bar structure and styling

- **Title of the Page**: The page title is set to "Sign up".

- **Main Content**: The main content container features a sign-up form where users can input their username, first name, last name, and password. The form is styled for clarity and usability [(9)](https://www.youtube.com/watch?v=dam0GPOAvVI).

- **CSS Styling**: Custom CSS styles are applied to position the content container and enhance the visual presentation of the form [(15)](https://www.w3schools.com/css/css_positioning.asp).

- **Submit and Go to Login Buttons**: Users can submit their sign-up information with the "Submit" button. Additionally, a "GoToLogin" button redirects users to the login page.

#### 4.1.4 login.html

The "login.html" file provides a login form for users to access the system [(9)](https://github.com/techwithtim/Flask-Web-App-Tutorial).

**Key Features:**

- **Main Content**: The main content container features a login form where users can input their username and password. The form is styled for clarity and usability.

- **Submit Button**: Users can submit their login credentials with the "Submit" button, which is aligned to the center of the form for easy access.

#### 4.1.5 update_DB.html

The "update_DB.html" file serves as a pivotal component within the Flask web application, providing users with a dynamic interface to interact with a database. It facilitates the display and execution of Create, Read, Update, and Delete (CRUD) operations seamlessly through Asynchronous JavaScript and XML (AJAX) requests.

**Key Features:**

- **Display and Interaction**: The page prominently showcases an "Employees Database," offering users a comprehensive view of the stored data. Through intuitive design and clear presentation, users can easily identify and interact with individual records.

- **Create New Employees**: Users are empowered to add new entries to the database with a dedicated "Create" button. Upon clicking, a form for inputting employee details is presented, ensuring a streamlined process for data entry.

- **Update Existing Employees**: For existing records, users can initiate updates directly from the displayed table. By selecting the "Update" option, pertinent employee information is retrieved, facilitating swift modification without navigating away from the page.

- **Delete Employees**: The ability to remove redundant or outdated entries is seamlessly integrated, offering users the option to delete records directly from the displayed table. Upon confirmation, the selected entry is promptly removed, ensuring data integrity and management efficiency.

- **AJAX Functionality**: Leveraging AJAX requests, all CRUD operations are performed asynchronously. This results in a fluid and responsive user experience, enhancing productivity and engagement [(16)](https://github.com/andrewbeattycourseware).

- **JavaScript Functionality**: Behind the scenes, a suite of JavaScript functions orchestrates the interaction between the user interface and backend server. These functions manage data retrieval, submission, and manipulation, ensuring smooth communication and error handling throughout the process [(17)](https://www.w3schools.com/jsref/jsref_encodeuricomponent.asp), [(18)](https://www.w3schools.com/jsref/prop_node_firstchild.asp).

#### 4.1.6 showDB.html

The "showDB.html" file plays a pivotal role within the Flask web application, providing users with a dynamic and interactive interface to view the contents of a database, facilitating efficient data exploration and analysis.

**Key Features:**

- **Database Display**: Presents database contents in a clear and concise tabular format, enabling users to analyze data attributes easily.

- **AJAX Operation**: Utilizes asynchronous data fetching for real-time updates and seamless interaction with the backend server [(16)](https://github.com/andrewbeattycourseware).

- **Navigation**: Offers intuitive navigation buttons for easy access to different sections of the application, ensuring a cohesive browsing experience.

- **JavaScript Functionality**: Employs JavaScript functions to manage AJAX operations and dynamically update table content, enhancing user experience and reliability.

#### 4.1.7 create_employee.html

The "create_employee.html" file serves as a pivotal component within the Flask web application, enabling users to create new employee records via a user-friendly form interface.

**Key Features:**

- **Employee Creation Form**: Presents a structured form interface for users to input details such as first name, last name, employee ID, and market. This intuitive form layout simplifies the data entry process, ensuring accurate and comprehensive employee records [(9)](https://www.youtube.com/watch?v=dam0GPOAvVI).

- **AJAX POST Operation**: Utilizes Asynchronous JavaScript and XML (AJAX) to perform seamless data submission to the backend server. Upon form submission, the entered employee data is sent asynchronously to the server, enhancing responsiveness and user experience.

- **Navigation**: Provides a convenient navigation button for users to return to the "Update DB" page effortlessly. This streamlined navigation feature ensures a cohesive browsing experience, allowing users to transition between different sections of the application seamlessly.

#### 4.1.8 update_employee.html

The "update_employee.html" file enable the user to update employee records efficiently and accurately through an intuitive form interface.

**Key Features:**

- **Employee Update Form**: The core feature of the file is the employee update form, which presents users with input fields for editing various attributes. This structured form layout simplifies the data modification process, ensuring that users can make changes quickly and accurately [(9)](https://www.youtube.com/watch?v=dam0GPOAvVI).

- **AJAX PUT Operation**: Leveraging Asynchronous JavaScript and XML (AJAX), the file performs updates to the backend server asynchronously. When users submit the update form, the modified employee data is sent to the server using the PUT method, enabling real-time updates without the need for page refreshes. 

- **Dynamic Form Population**: To streamline the update process, the form automatically populates with existing employee data retrieved from URL parameters. By presenting users with pre-filled fields, the file simplifies the update process and enhances usability [(19)](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/URLSearchParams), [(20)](https://builtin.com/articles/urlsearchparams).

- **Navigation**: The file includes a navigation button that allows users to return to the "Update DB" in any moment. 

- **JavaScript Functionality**: JavaScript functions embedded within the file orchestrate the form submission process and handle AJAX requests for updating employee records.

- **JavaScript Functionality**: Implements JavaScript functions to orchestrate the AJAX POST operation and handle form submission events. These functions facilitate efficient data transmission between the frontend interface and backend server, ensuring reliable creation of new employee records [(21)](https://www.w3schools.com/jsref/met_document_queryselector.asp).

### 4.2 Python Scripts

#### 4.2.1 config_template.py

The template contains the `DBConfigSQL` class, which provides a template to fill with configuration parameters for connecting to an SQL database. It includes essential details such as the host address, username, password, and security key required to establish a connection.

**Key Features:**

- **HOST:** Specifies the host address of the SQL database.
- **USER:** Specifies the username used to authenticate access to the SQL database.
- **PASSWORD:** Specifies the password used to authenticate access to the SQL database.
- **SECURITY_KEY:** Specifies the security key used inside the flask application [(22)](https://www.delftstack.com/howto/python-flask/flask-secret-key/).

**Usage:**

As explained in 'How to use it' section, the user needs to enter their personalized parameters and rename the file as `config.py` to be correctly imported in the main server script and `db_connection.py`.

#### 4.2.2 create_sql_db.py

The primary objective of "create_sql.py" is to establish a connection to a MySQL server, create the necessary database for the API and tables if they do not exist, and populate them with sample data. The script encapsulates functionalities to execute SQL queries, create and manage database entities, and ensure the integrity and consistency of the database structure.

**Nedded libraryes*:*

- **MySQL Connection**: The script utilizes the [MySQL Connector (7)](https://dev.mysql.com/doc/connector-python/en/) module to establish a connection to the MySQL server. It retrieves database configuration parameters from a configuration file that can be stored in a different location and secure database connectivity [(16)](https://github.com/andrewbeattycourseware).

**Key Features:**

- **Database and Table Creation**: If the specified database does not exist, the script creates it dynamically. Similarly, it creates the 'authentication_logins' and 'employees' tables if they are not present in the database, ensuring that the required database entities are available for data storage.

- **Data Population**: Upon table creation, the script populates the 'employees' and 'authentication_logins' tables with sample data. This data includes employee details such as first name, last name, employee ID, and market, as well as login credentials such as username and password. 

- **Data Reset**: Additionally, the script includes methods to reset the data in the 'employees' and 'authentication_logins' tables. This functionality empties the tables and inserts sample data, effectively restoring them to their original state.

The following functions are defined and used in the script:

- **execute_query()**: Executes a given SQL query on the database.
- **create_db()**: Creates the specified database if it does not exist.
- **create_authentication_logins_table()**: Creates the 'authentication_logins' table if it does not exist.
- **create_employees_table()**: Creates the 'employees' table if it does not exist.
- **empty_table()**: Empties the specified table by deleting all records.
- **reset_data_employees()**: Resets employee data by emptying the 'employees' table and inserting sample data.
- **reset_data_logins()**: Resets login data by emptying the 'authentication_logins' table and inserting sample data.

**Usage:**

To execute the script, simply run it as the main program. It will create the necessary database and tables, populate them with sample data, and display relevant status messages indicating the success of each operation.

#### 4.2.3 db_conn.py

The `db_conn.py` script defines a class `database_connection` that provides methods for interacting with a MySQL database. This script facilitates various operations for establishing a connection and executing SQL queries. It relies on the MySQL Connector/Python library and a configuration file called `config` for connection parameters.

**Nedded libraryes*:*

- **MySQL Connection**: Utilizes the [MySQL Connector/Python (7)](https://dev.mysql.com/doc/connector-python/en/) library to establish a connection to the MySQL server. Connection parameters such as host, user, password, and database name are fetched from a configuration file.

**Key Features:**

- **Database Interaction**: Provides methods for fetching all records from a table (`getAll()`), checking the uniqueness of usernames or employee IDs [(23)](https://stackoverflow.com/questions/54582898/flaskform-validation-code-checking-if-a-user-already-exists-or-not) (`check_unique_username()`, `check_unique_employee_id()`), creating new employee and logins records [(24)](https://www.w3schools.com/sql/sql_insert.asp) (`createNewEmployee()` - `create_new_login()`), updating employee records (`update_employee()`), and deleting employee records (`delete_employee()`).

- **Data Retrieval**: Includes methods to fetch user records by username (`get_user_by_username()`) or employee ID (`get_user_by_emp_id()`), and to find a record by its ID (`find_by_id()`).

**Defined Functions:**

- `getcursor()`: Establishes a database connection and returns a cursor for executing SQL queries.
- `closeAll()`: Closes both the connection and the cursor if they are open.
- `getAll(table, attkeys)`: Fetches all records from a specified table and returns them as a list of dictionaries. The table and attribute key definitions as variables outside the function grant flexibility to the method to be used on both the tables.
- `convertToDictionary(attkeys, resultLine)`: Converts database records to dictionaries using specified attribute keys.
- `check_unique_username(username)`: Checks if a username is unique in the 'authentication_logins' table.
- `check_unique_employee_id(employee_id)`: Checks if an employee ID is unique in the 'employees' table.
- `createNewEmployee(employee)`: Creates a new employee record in the 'employees' table.
- `create_new_login(user)`: Creates a new login record in the 'authentication_logins' table.
- `get_user_by_username(username)`: Fetches a user record by username in order to check the uniqueness of the attribute username.
- `get_user_by_emp_id(employee_id)`: Fetches a user record by employee ID to check the uniqueness of the attribute employee_id.
- `find_by_id(id)`: Fetches a record by its ID to use as a unique parameter on update operation.
- `update_employee(id, employee)`: Updates an employee record in the 'employees' table.
- `delete_employee(id)`: Deletes an employee record from the 'employees' table.

#### 4.2.4 server.py

The `server.py` script orchestrates a RESTful API tailored for managing user authentication and database interactions through CRUD operations. This Flask-based web service streamlines essential functionalities to ensure a seamless user experience and efficient data management. [Here (9)](https://www.youtube.com/watch?v=dam0GPOAvVI) and [here (25)](https://www.youtube.com/watch?v=71EU8gnZqZQ) the main references for this scrip.

**Nedded libraryes**

- [Flask (3)](https://pypi.org/project/Flask/): is a micro web framework for Python, designed to build web applications quickly and with minimal code. It provides the tools and libraries needed to create web servers and handle HTTP requests and responses.
- [Flask-Login (26)](https://pypi.org/project/Flask-Login/): Flask-Login is an extension for Flask that simplifies user session management and authentication in Flask applications. It provides decorators and utilities for managing user sessions, logging users in and out, and restricting access to certain parts of an application based on user authentication status. 

**Key Features:**

- **User Authentication:** handles user sign-up, login, and logout operations, ensuring secure access to the system. The API enforces strict password criteria and unique usernames for enhanced security.

- **Employee Management:** Facilitates CRUD operations for employee records, allowing users to create, read, update, and delete employee information. The API interacts with the database to maintain an organized and up-to-date employee database.

- **Database Interaction:** Interacts with two primary database tables, 'authentication_logins' and 'employees,' to execute various data retrieval and manipulation tasks. By leveraging Flask-Login and MySQL database connectivity, the script ensures efficient and reliable database interactions.

- **Flash Messages:** Utilizes Flash messages for providing feedback to users during authentication, CRUD operations, and other interactions. Flash messages are used to convey success messages, error messages, and other relevant information to users [(27)](https://stackoverflow.com/questions/63387031/how-to-clear-existing-flash-messages-in-flask), [(28)](https://nrodrig1.medium.com/remove-flash-message-from-flask-web-application-e5c82e639b2f), [(29)](https://pythongeeks.org/flask-flashing/#:~:text=By%20default%2C%20Flask%20does%20not%20automatically%20clear%20the,the%20flash.clear%20%28%29%20function%20from%20the%20flash%20module).

**Usage:**

To execute the script, simply run it as the main program. This will start the server, and it will be accessible through a **Chrome browser**. By default, Flask applications run on port 5000. Then, open Chrome and navigate to http://127.0.0.1:5000/ to access the API.


## Sources
<details>
    <summary> References </summary>
    <p>

* (1) [Web technology for developers](https://developer.mozilla.org/en-US/docs/Web)
* (2) [Python](https://www.python.org/)
* (3) [Flask](https://flask.palletsprojects.com/)
* (4) [jQuery](https://jquery.com/)
* (5) [Bootstrap](https://getbootstrap.com/)
* (6) [Anaconda](https://www.anaconda.com/)
* (7) [MySQL Connector](https://pypi.org/project/mysql-connector-python/)
* (8) [Flask-Login](https://pypi.org/project/Flask-Login/)
* (9) [Python Website Full Tutorial - Flask, Authentication, Databases & More](https://www.youtube.com/watch?v=dam0GPOAvVI)
* (10) [How to prevent favicon.ico requests?](https://stackoverflow.com/questions/1321878/how-to-prevent-favicon-ico-requests)
* (11) [CSS Tutorial](https://www.w3schools.com/Css/)
* (12) [Style Fieldsets like a Pro](https://www.webteacher.ws/2009/12/10/style-fieldsets-like-a-pro/)
* (13) [CSS flex-direction Property](https://www.w3schools.com/cssref/css3_pr_flex-direction.php)
* (14) [How to create two HTML buttons side by side](https://stackoverflow.com/questions/52544089/how-to-create-two-html-buttons-side-by-side)
* (15) [CSS Layout - The position Property](https://www.w3schools.com/css/css_positioning.asp)
* (16) [AndrewBeattyCourseware](https://github.com/andrewbeattycourseware)
* (17) [JavaScript encodeURIComponent()](https://www.w3schools.com/jsref/jsref_encodeuricomponent.asp)
* (18) [HTML DOM Element firstChild](https://www.w3schools.com/jsref/prop_node_firstchild.asp)
* (19) [URLSearchParams: URLSearchParams() constructor](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/URLSearchParams)
* (20) [How to Use URLSearchParams in JavaScript](https://builtin.com/articles/urlsearchparams)
* (21) [HTML DOM Document querySelector()](https://www.w3schools.com/jsref/met_document_queryselector.asp)
* (22) [Flask Secret Key](https://www.delftstack.com/howto/python-flask/flask-secret-key/#google_vignette)
* (23) [FlaskForm Validation Code: checking if a user already exists or not](https://stackoverflow.com/questions/54582898/flaskform-validation-code-checking-if-a-user-already-exists-or-not)
* (24) [SQL INSERT INTO Statement](https://www.w3schools.com/sql/sql_insert.asp)
* (25) [Python Flask Authentication Tutorial - Learn Flask Login](https://www.youtube.com/watch?v=71EU8gnZqZQ)
* (26) [Flask-Login 0.6.3](https://pypi.org/project/Flask-Login/)
* (27) [how to clear existing flash messages in Flask](https://stackoverflow.com/questions/63387031/how-to-clear-existing-flash-messages-in-flask)
* (28) [Remove Flash Message from Flask Web Application](https://nrodrig1.medium.com/remove-flash-message-from-flask-web-application-e5c82e639b2f)
* (29) [Python Flask Flashing](https://pythongeeks.org/flask-flashing/#:~:text=By%20default%2C%20Flask%20does%20not%20automatically%20clear%20the,the%20flash.clear%20%28%29%20function%20from%20the%20flash%20module)

</p>
</details>

<details>
    <summary> Other Resources </summary>
    <p>

* [CSS calc() Function](https://www.w3schools.com/cssref/func_calc.php)
* [RESTful Authentication with Flask](https://blog.miguelgrinberg.com/post/restful-authentication-with-flask)
* [6.9.5.16 MySQLCursor.lastrowid Property](https://dev.mysql.com/doc/connectors/en/connector-python-api-mysqlcursor-lastrowid.html)
* [5 Easy Ways to Insert Spaces in HTML](https://blog.hubspot.com/website/html-space)
* [Why transform:translate(-50%, -50%) to center element?](https://dev.to/urstrulyvishwak/why-transformtranslate-50-50-to-center-element-15m1)
* [Dillinger](https://dillinger.io/)
* [Awesome Readme Examples for Writing better Readmes ](https://dev.to/documatic/awesome-readme-examples-for-writing-better-readmes-3eh3)
* 
</p>
</details>


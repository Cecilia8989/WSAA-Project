<h1 align="center">WSSA-project2024</h1>
<h2 align="center">Restful Api</h2>
<p align="center">
Cecilia Pastore 
</p>
<h3 align="center">Link of the built website:</h3>
<h3 align="center">https://cecilia891.pythonanywhere.com/</h3>

<details>
    <summary> Project assignement </summary>
           <p>

>Create a Web application in Flask that has a RESTful API, the application
should link to one or more database tables.
You should also create the web pages that can consume the API. I.e. performs
CRUD operations on the data.

</p>
</details>

## 1. Introduction 

This code builds a basic website where CRUD operations are performed on two tables within a SQL database. Users are allowed to sign in, log in, and log out. Unauthorized users can view the database but cannot create new entries or update/delete existing ones. Only logged-in users have permission to perform these actions. The website facilitates CRUD operations on two tables: one for registered users and one for the employees database. The employee database displays the name, surname, employee ID, and country for each entry. When registering on the website, usernames must be unique, and passwords must adhere to several security rules. Additionally, two users with the same employee ID cannot be created during a POST request.

The website is optimized for use on the Chrome browser.

## 2. Built with

This project leverages the following technologies:

- [HTML/CSS/JavaScript](https://developer.mozilla.org/en-US/docs/Web): Used for the frontend development of the website.
- [Python](https://www.python.org/): The backend of the website is developed using Python. The version that have been used is PYTHON 3.11.4
- [Flask](https://flask.palletsprojects.com/): Flask, a lightweight WSGI web application framework, is utilized for building the web application.
- [jQuery](https://jquery.com/): jQuery library is imported for simplifying AJAX calls and DOM manipulation.
- [Bootstrap](https://getbootstrap.com/): Bootstrap framework is utilized for designing responsive and mobile-first websites.

## 3. How to use it

### 3.1 Open the Web site hosted in pythonanywhere

You can Open Website [cecilia891.pythonanywhere](https://cecilia891.pythonanywhere.com/) on a **Chrome browser** or run it on your local network.

<h4 align="center">OR</h4>

### 3.2 Run the server on your local network

Here are the steps to follow:

#### 3.2.1 Ensure that Python is installed, along with the following libraries:

- [Python](https://www.python.org/): You can install Python from [here](https://www.python.org/) or [Anaconda](https://www.anaconda.com/).
- [Flask](https://pypi.org/project/Flask/): Flask is a lightweight WSGI web application framework for Python.
- [MySQL Connector](https://pypi.org/project/mysql-connector-python/): MySQL Connector is a Python driver for connecting to MySQL databases.
- [Flask-Login](https://pypi.org/project/Flask-Login/): Flask-Login provides user session management for Flask.

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

open the indicated port on **Chrome browser** to navigate the API on your local network. Below is an example. In this case, the port is `http://127.0.0.1:5000`.

```bash
Running on http://127.0.0.1:5000
```

## 4 File Description

The project consists of several files belonging to two different categories:

- HTML/JavaScript/jQuery
- Python

Below is a description of each file involved.

### 4.1 HTML/JavaScript/jQuery Templates

#### 4.1.1 base html. 

This HTML file establishes the foundational structure and features for a Flask web application, encompassing navigation, message presentation, content arrangement, and styling, to be applied across all HTML files. The code has been take and adapted from the the tutorial [ Tech With Tim ()](https://www.youtube.com/watch?v=dam0GPOAvVI)

**Key Features:**

- **Meta Tags and Dependencies**: These are like instructions for the browser, ensuring everything looks right on different devices [()](https://stackoverflow.com/questions/1321878/how-to-prevent-favicon-ico-requests). It also includes links to some special style sheets [CSS ()](https://www.w3schools.com/Css/) on [ Bootstrampt ()](https://getbootstrap.com/) and a [fieldset style ()](https://www.webteacher.ws/2009/12/10/style-fieldsets-like-a-pro/)to enhance the site's appearance.

- **Navigation Bar**: Positioned at the top of the page, the navigation bar facilitates user movement throughout the site, adjusting dynamically based on login status.

- **Flash Messages**: This section reserves space for dynamic messages generated by the application, providing feedback to users based on their interactions.

#### 4.1.2 Home.html

The "Home.html" file serves as the main page for presenting the structure of an API and is the landing page for users accessing the API.

**Key Features:**

- **Extending Base Template**: This file extends the "base.html" template, inheriting its navigation bar structure and styling [(A)](https://www.youtube.com/watch?v=dam0GPOAvVI).

- **Main Content**: The main content container showcases a welcoming message and a concise overview of the RESTful API's features. 

- **CSS Styling**: Custom CSS styles are applied to ensure proper formatting and layout of the content container, utilizing a [flexbox container ()](https://www.w3schools.com/cssref/css3_pr_flex-direction.php) for improved alignment and responsiveness.

- **Action Selection**: Users are presented with action buttons within a form container. Two buttons are provided: one for displaying the "Employee-Database" and another for updating the database. Authentication is required for the latter action.

- **JavaScript Functions**: JavaScript functions are integrated to streamline navigation. Clicking on the buttons triggers functions that redirect users to specific pages: "show_employees" for displaying the employee database and "update_DB" for updating the database [()](https://stackoverflow.com/questions/52544089/how-to-create-two-html-buttons-side-by-side).

#### 4.1.3 sign_up.html

The "sign_up.html" file presents a sign-up form for users to register in the system. 

**Key Features:**

- **Extending Base Template**: This file extends the "base.html" template, inheriting its navigation bar structure and styling

- **Title of the Page**: The page title is set to "Sign up".

- **Main Content**: The main content container features a sign-up form where users can input their username, first name, last name, and password. The form is styled for clarity and usability [(A)](https://www.youtube.com/watch?v=dam0GPOAvVI).

- **CSS Styling**: Custom CSS styles are applied to position the content container and enhance the visual presentation of the form [()](https://www.w3schools.com/css/css_positioning.asp).

- **Submit and Go to Login Buttons**: Users can submit their sign-up information with the "Submit" button. Additionally, a "GoToLogin" button redirects users to the login page.

#### 4.1.4 login.html

The "login.html" file provides a login form for users to access the system [(A)](https://github.com/techwithtim/Flask-Web-App-Tutorial).

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

- **AJAX Functionality**: Leveraging AJAX requests, all CRUD operations are performed asynchronously. This results in a fluid and responsive user experience, enhancing productivity and engagement [()](https://github.com/andrewbeattycourseware).

- **JavaScript Functionality**: Behind the scenes, a suite of JavaScript functions orchestrates the interaction between the user interface and backend server. These functions manage data retrieval, submission, and manipulation, ensuring smooth communication and error handling throughout the process [()](https://www.w3schools.com/jsref/jsref_encodeuricomponent.asp), [()](https://www.w3schools.com/jsref/prop_node_firstchild.asp).

#### 4.1.6 showDB.html

The "showDB.html" file plays a pivotal role within the Flask web application, providing users with a dynamic and interactive interface to view the contents of a database, facilitating efficient data exploration and analysis.

**Key Features:**

- **Database Display**: Presents database contents in a clear and concise tabular format, enabling users to analyze data attributes easily.

- **AJAX Operation**: Utilizes asynchronous data fetching for real-time updates and seamless interaction with the backend server [(A)](https://github.com/andrewbeattycourseware).

- **Navigation**: Offers intuitive navigation buttons for easy access to different sections of the application, ensuring a cohesive browsing experience.

- **JavaScript Functionality**: Employs JavaScript functions to manage AJAX operations and dynamically update table content, enhancing user experience and reliability.

#### 4.1.7 create_employee

The "create_employee.html" file serves as a pivotal component within the Flask web application, enabling users to create new employee records via a user-friendly form interface.

**Key Features:**

- **Employee Creation Form**: Presents a structured form interface for users to input details such as first name, last name, employee ID, and market. This intuitive form layout simplifies the data entry process, ensuring accurate and comprehensive employee records [(A)](https://www.youtube.com/watch?v=dam0GPOAvVI),  [()](https://www.w3schools.com/css/css_positioning.asp).

- **AJAX POST Operation**: Utilizes Asynchronous JavaScript and XML (AJAX) to perform seamless data submission to the backend server. Upon form submission, the entered employee data is sent asynchronously to the server, enhancing responsiveness and user experience.

- **Navigation**: Provides a convenient navigation button for users to return to the "Update DB" page effortlessly. This streamlined navigation feature ensures a cohesive browsing experience, allowing users to transition between different sections of the application seamlessly.

- **JavaScript Functionality**: Implements JavaScript functions to orchestrate the AJAX POST operation and handle form submission events. These functions facilitate efficient data transmission between the frontend interface and backend server, ensuring reliable creation of new employee records [()](https://www.w3schools.com/jsref/met_document_queryselector.asp).



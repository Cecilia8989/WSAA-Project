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

Here the main feature of the file:

- **Meta Tags and Dependencies**: These are like instructions for the browser, ensuring everything looks right on different devices. It also includes links to some special style sheets [CSS ()](https://www.w3schools.com/Css/) on [ Bootstrampt ()](https://getbootstrap.com/) to enhance the site's appearance.

- **Navigation Bar**: Positioned at the top of the page, the navigation bar facilitates user movement throughout the site, adjusting dynamically based on login status.

- **Flash Messages**: This section reserves space for dynamic messages generated by the application, providing feedback to users based on their interactions.

#### 4.1.1 Home.html

The "Home.html" file serves as the main page for presenting the structure of an API and is the landing page for users accessing the API.

**Key Features:**

- **Extending Base Template**: This file extends the "base.html" template, inheriting its navigation bar structure and styling [(A)](https://www.youtube.com/watch?v=dam0GPOAvVI).

- **Main Content**: The main content container showcases a welcoming message and a concise overview of the RESTful API's features. 

- **CSS Styling**: Custom CSS styles are applied to ensure proper formatting and layout of the content container, utilizing a [flexbox container ()](https://www.w3schools.com/cssref/css3_pr_flex-direction.php) for improved alignment and responsiveness.

- **Action Selection**: Users are presented with action buttons within a form container. Two buttons are provided: one for displaying the "Employee-Database" and another for updating the database. Authentication is required for the latter action.

- **JavaScript Functions**: JavaScript functions are integrated to streamline navigation. Clicking on the buttons triggers functions that redirect users to specific pages: "show_employees" for displaying the employee database and "update_DB" for updating the database [()](https://stackoverflow.com/questions/52544089/how-to-create-two-html-buttons-side-by-side).

- **Main Content Container**:  Designed to accommodate content from other HTML templates extended by the base HTML, this container forms the central area for presenting site content.

- **JavaScript Files**: These are special files that add extra functionality to the website, like making dropdown menus work or creating pop-up.



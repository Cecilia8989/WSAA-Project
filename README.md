<h1 align="center">WSSA-project2024</h1>
 <h2 align="center">Restful Api</h2>

  <p align="center">
   Cecilia Pastore 

<details>
    <summary> Project assignement </summary>
           <p>

<h3 align="center"> Project Assignement</h2>
 
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

* [Python](https://www.python.org/) : 
* [Flask](https://flask.palletsprojects.com/)
* HTML/CSS/JavaScript
*  [![Python][python.com]][JQuery-url]
* [Bootstrap](https://getbootstrap.com/)
*  [![JQuery][JQuery.com]][JQuery-url]



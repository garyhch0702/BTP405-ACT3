# BTP405 - Act 3

## About
This repository contains the code for BTP405 Act 3, developed by Chenghao Hu.

## Project Description
The project is aimed at developing a RESTful API using Python's built-in HTTP server module, enabling clients to perform CRUD (Create, Read, Update, Delete) operations on data stored in a MySQL database. This API serves as the backend for a simple note-taking application.

## Technologies Used
- Programming Language: Python
- Database: MySQL
- Version Control: Git
- Containerization: Docker

## Installation and Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/garyhch0702/BTP405-ACT3.git
    ```

2. Navigate to the project directory:
    ```bash
    cd BTP405-ACT3
    ```

3. Install necessary dependencies:
    ```bash
    pip install mysql-connector-python
    ```

4. Build the Docker image:
    ```bash
    docker build -t my_api_image .
    ```

5. Run the Docker container:
    ```bash
    docker run --name GaryHu -p 8080:8080 my_api_image
    ```

6. Access the API endpoints at `http://localhost:8080`.

## API Endpoints
- `GET /notes`: Retrieve all notes
- `POST /notes`: Create a new note
- `PUT /notes/{note_id}`: Update an existing note
- `DELETE /notes/{note_id}`: Delete a note by ID





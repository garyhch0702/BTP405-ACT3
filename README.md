# BTP405 - Activity 3
**Student Name:** CHENGHAO HU

## Tools and Technologies
- **Programming Language:** Python
- **Database:** MySQL
- **Version Control:** Git
- **Containerization:** Docker
- **API Testing:** curl / Invoke-RestMethod (Windows)

## Config MySQL Docker
First, pull the MySQL Docker image and run the container:

```bash
docker pull mysql:latest
docker run --name=mysql1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password --restart on-failure -d mysql:latest
API Endpoints
GET Request
Python handler for GET requests:

python
Copy code
def do_GET(self):
    self._set_response()
    cursor.execute("SELECT note_id, title, content FROM NOTE")
    for (note_id, title, content) in cursor:
        self.wfile.write(f"{note_id}, {title}, {content}".encode('utf-8'))
Test command (Windows PowerShell):

powershell
Copy code
Invoke-RestMethod -Uri http://localhost:8080
Test command (curl):

bash
Copy code
curl http://127.0.0.1:8080
DELETE Request
Python handler for DELETE requests:

python
Copy code
def do_DELETE(self):
    self._set_response()
    cursor.execute("DELETE FROM NOTE")
    cnx.commit()
Test command (Windows PowerShell):

powershell
Copy code
Invoke-RestMethod -Uri http://localhost:8080 -Method DELETE
Test command (curl):

bash
Copy code
curl -X DELETE http://127.0.0.1:8080
PUT Request
Python handler for PUT requests:

python
Copy code
def do_PUT(self):
    self._set_response()
    cursor.execute("INSERT INTO NOTE (TITLE, CONTENT) values ('Python', 'Python is fun.')")
    cnx.commit()
Test command (Windows PowerShell):

powershell
Copy code
Invoke-RestMethod -Uri http://localhost:8080 -Method PUT
Test command (curl):

bash
Copy code
curl -X PUT http://127.0.0.1:8080
POST Request
Python handler for POST requests:

python
Copy code
def do_POST(self):
    self._set_response()
    cursor.execute("UPDATE NOTE SET CONTENT = 'Python is amazing!' WHERE TITLE = 'Python'")
    cnx.commit()
Test command (Windows PowerShell):

powershell
Copy code
Invoke-RestMethod -Uri http://localhost:8080 -Method POST
Test command (curl):

bash
Copy code
curl -X POST http://127.0.0.1:8080
Build and Run Docker Image
Build the Docker image:

bash
Copy code
docker build -t chenghaohu/notetaker:v1 .
Run the Docker container:

bash
Copy code
docker run -p 8080:8080 chenghaohu/notetaker:v1

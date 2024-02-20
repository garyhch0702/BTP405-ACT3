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
docker run --name=Gary Hu -p 3306:3306 -e MYSQL_ROOT_PASSWORD=657300 --restart on-failure -d mysql:latest

API Endpoints
GET Request
Python handler for GET requests:

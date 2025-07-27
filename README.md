# fastapi-backend-assignment
FastAPI-based backend with PostgreSQL for managing wheel specifications and bogie checksheet forms.
This project implements two APIs using FastAPI and PostgreSQL as per the assignment requirements.
The APIs handle Wheel Specifications and Bogie Checksheet forms.
Testing is done using Postman, and data persistence is ensured via PostgreSQL.

**Tech Stack**
Backend Framework: FastAPI (Python)

Database: PostgreSQL

ORM: SQLAlchemy

Validation: Pydantic

Testing: Postman

**Features**
API for creating and retrieving Wheel Specifications.

API for creating Bogie Checksheet entries.

PostgreSQL integration for data storage.

Swagger UI documentation at http://127.0.0.1:8000/docs.

**Setup Instructions**
1. Clone the Repository
git clone https://github.com/keertiG-1296/fastapi-backend-assignment.git
cd fastapi-backend-assignment

2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Database
Update your PostgreSQL connection string in database.py:
DATABASE_URL = "postgresql://username:password@localhost:5432/kpa_db"

5. Start the Server
uvicorn main:app --reload
API will run at:http://127.0.0.1:8000

**API Endpoints**
Method	Endpoint	Description
POST	/api/forms/wheel-specifications	Create a wheel specification
GET	/api/forms/wheel-specifications	Get all wheel specifications
POST	/api/forms/bogie-checksheet	Create a bogie checksheet


**Sample Requests**
1. POST /api/forms/wheel-specifications
{
  "formNumber": "WS123",
  "submittedBy": "John Doe",
  "submittedDate": "2025-07-27",
  "fields": {
    "additionalProp1": "value1",
    "additionalProp2": "value2",
    "additionalProp3": "value3"
  }
}


2. GET /api/forms/wheel-specifications
Returns a list of stored wheel specs.

3. POST /api/forms/bogie-checksheet
{
  "formNumber": "BC101",
  "inspectionBy": "Jane Smith",
  "inspectionDate": "2025-07-27",
  "bogieDetails": {
    "additionalProp1": "bogieDetail1",
    "additionalProp2": "bogieDetail2",
    "additionalProp3": "bogieDetail3"
  },
  "bogieChecksheet": {
    "additionalProp1": "check1",
    "additionalProp2": "check2",
    "additionalProp3": "check3"
  },
  "bmbcChecksheet": {
    "additionalProp1": "bmbc1",
    "additionalProp2": "bmbc2",
    "additionalProp3": "bmbc3"
  }
}

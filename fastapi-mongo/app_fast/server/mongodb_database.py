import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017/mongodb_database?authSource=admin"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.dsyh_mongo

employee_collection = database.get_collection("employee_collection")


def employee_helper(employee) -> dict:
    return {
        "emp_id": str(employee["_id"]),
        "full_name": employee["full_name"],
        "email_id": employee["email_id"],
        "role": employee["role"],
        "year_of_experience": employee["year_of_experience"],
        "salary": employee["salary"],
    }


# getting all the documents of employees
async def retrieve_employees():
    employees = []
    async for employee in employee_collection.find():
        employees.append(employee_helper(employee))
    return employees


# creating an employee entry in database
async def create_employee(employee_data: dict) -> dict:
    employee = await employee_collection.insert_one(employee_data)
    new_employee = await employee_collection.find_one({"_id": employee.inserted_id})
    return employee_helper(new_employee)


# reteriving employee details of given emp_id
async def retrieve_employee(id: str) -> dict:
    employee = await employee_collection.find_one({"_id": ObjectId(id)})
    if employee:
        return employee_helper(employee)


# updating employee entry with given emp_id
async def update_employee(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    employee = await employee_collection.find_one({"_id": ObjectId(id)})
    if employee:
        updated_employee = await employee_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_employee:
            return True
        return False


# for deleting employee entry in collection
async def delete_employee(id: str):
    employee = await employee_collection.find_one({"_id": ObjectId(id)})
    if employee:
        await employee_collection.delete_one({"_id": ObjectId(id)})
        return True


# for getting employeedetails in sorting way
async def sort_employee(key: str, order: int):
    employees = []
    employee_cursor = employee_collection.find().sort(key, order)
    async for employee in employee_cursor:
        employees.append(employee_helper(employee))
    return employees

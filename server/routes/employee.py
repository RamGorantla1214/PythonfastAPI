from app_fast.server.mongodb_database import (
    create_employee,
    delete_employee,
    retrieve_employee,
    retrieve_employees,
    update_employee,
    sort_employee
)
from app_fast.server.models.employee import (
    ErrorResponseModel,
    ResponseModel,
    EmployeeSchema,
    UpdateEmployeeModel,
)

router = APIRouter()

@router.post("/add_employee/", response_description="Employee data added into the database")
async def adding_employee_data(employee: EmployeeSchema = Body(...)):
    employee_add = jsonable_encoder(employee)
    new_employee = await create_employee(employee_add)
    return ResponseModel(new_employee, "Employee added successfully.")


@router.get("/", response_description="Employees data retrieved")
async def get_employees():
    employees_get = await retrieve_employees()
    if employees_get:
        return ResponseModel(employees_get, "employees data retrieved successfully")
    return ResponseModel(employees_get, "Empty list returned")


@router.get("/{id}", response_description="Employee data retrieved")
async def get_employee_data(id):
    employee = await retrieve_employee(id)
    if employee:
        return ResponseModel(employee, "Employee data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Employee doesn't exist.")


@router.put("/{id}")
async def update_employee_data(id: str, req: UpdateEmployeeModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_employee = await update_employee(id, req)
    if updated_employee:
        return ResponseModel(
            "Employee with ID: {} name update is successful".format(id),
            "Employee name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the Employee data.",
    )

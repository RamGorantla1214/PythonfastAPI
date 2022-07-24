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

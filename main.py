from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


app = FastAPI(
    title="Innovation Club Applications API",
    description="Week 1 Backend Task - FastAPI CRUD API using mock data",
    version="1.0.0"
)


# =========================
# SCHEMAS
# =========================

class ApplicationCreate(BaseModel):
    fullName: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    whatsappNumber: str = Field(..., min_length=10, max_length=15)

    university: str = Field(..., min_length=2)
    course: str = Field(..., min_length=2)
    level: str = Field(..., min_length=2)
    track: str = Field(..., min_length=2)

    motivation: str = Field(..., min_length=10)
    
    portfolioLink: Optional[str] = None
    resumeLink: Optional[str] = None

    joinInnovationClub: bool = False


class Application(ApplicationCreate):
    id: int
    status: str
    submittedAt: datetime


# =========================
# MOCK DATABASE
# =========================

applications = [
    {
        "id": 2,
        "fullName": "Ama Serwaa Owusu",
        "email": "amaserwaa@gmail.com",
        "phone": "0245567812",
        "whatsappNumber": "0245567812",
        "university": "University of Ghana",
        "course": "Computer Engineering",
        "level": "2nd Year",
        "track": "Embedded Systems",
        "motivation": "I want to gain hands-on experience in embedded systems and IoT development.",
        "portfolioLink": "https://github.com/amase",
        "resumeLink": "https://linkedin.com/in/amase",
        "joinInnovationClub": True,
        "status": "accepted",
        "submittedAt": "2026-05-04T10:12:45Z"
    },
    {
        "id": 3,
        "fullName": "Yaw Mensah",
        "email": "yawmensah@gmail.com",
        "phone": "0558876123",
        "whatsappNumber": "0558876123",
        "university": "KNUST",
        "course": "Electrical Engineering",
        "level": "4th Year",
        "track": "Radar & RF Systems",
        "motivation": "To improve my knowledge in RF systems, radar engineering, and wireless communications.",
        "portfolioLink": "https://github.com/yawmensah",
        "resumeLink": "https://linkedin.com/in/yawmensah",
        "joinInnovationClub": True,
        "status": "pending",
        "submittedAt": "2026-05-05T08:45:30Z"
    },
    {
        "id": 4,
        "fullName": "Priscilla Adjei",
        "email": "priscilla.adjei@gmail.com",
        "phone": "0203344556",
        "whatsappNumber": "0203344556",
        "university": "Ashesi University",
        "course": "Software Engineering",
        "level": "3rd Year",
        "track": "Backend Engineering",
        "motivation": "I want to strengthen my backend engineering skills using FastAPI and modern software architecture.",
        "portfolioLink": "https://github.com/priscillaadjei",
        "resumeLink": "https://linkedin.com/in/priscillaadjei",
        "joinInnovationClub": True,
        "status": "accepted",
        "submittedAt": "2026-05-06T14:18:22Z"
    },
    {
        "id": 5,
        "fullName": "Daniel Kofi Asante",
        "email": "danielasante@gmail.com",
        "phone": "0277788990",
        "whatsappNumber": "0277788990",
        "university": "UENR",
        "course": "Biomedical Engineering",
        "level": "2nd Year",
        "track": "Biomedical Systems",
        "motivation": "To explore biomedical monitoring systems and healthcare technology innovations.",
        "portfolioLink": "https://github.com/danielasante",
        "resumeLink": "https://linkedin.com/in/danielasante",
        "joinInnovationClub": False,
        "status": "rejected",
        "submittedAt": "2026-05-07T11:05:10Z"
    }
]


# =========================
# ROOT / HEALTH CHECK
# =========================

@app.get("/")
def root():
    return {
        "message": "Innovation Club Applications API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# =========================
# GET ALL APPLICATIONS
# =========================

@app.get("/applications", response_model=list[Application])
def get_applications():
    return applications


# =========================
# GET SINGLE APPLICATION
# =========================

@app.get("/applications/{application_id}", response_model=Application)
def get_application(
    application_id: int = Path(..., gt=0)
):
    for application in applications:
        if application["id"] == application_id:
            return application

    raise HTTPException(
        status_code=404,
        detail="Application not found"
    )


# =========================
# CREATE APPLICATION
# =========================

@app.post(
    "/applications",
    response_model=Application,
    status_code=201
)
def create_application(application: ApplicationCreate):

    # Check for duplicate email
    for existing in applications:
        if existing["email"].lower() == application.email.lower():
            raise HTTPException(
                status_code=400,
                detail="An application with this email already exists"
            )

    # Generate new ID
    new_id = max(
        [application["id"] for application in applications],
        default=0
    ) + 1

    new_application = {
        "id": new_id,
        **application.model_dump(),
        "status": "pending",
        "submittedAt": datetime.utcnow()
    }

    applications.append(new_application)

    return new_application


# =========================
# UPDATE APPLICATION
# =========================

@app.put(
    "/applications/{application_id}",
    response_model=Application
)
def update_application(
    application_id: int,
    application: ApplicationCreate
):

    for index, existing in enumerate(applications):

        if existing["id"] == application_id:

            updated_application = {
                "id": application_id,
                **application.model_dump(),
                "status": existing["status"],
                "submittedAt": existing["submittedAt"]
            }

            applications[index] = updated_application

            return updated_application

    raise HTTPException(
        status_code=404,
        detail="Application not found"
    )


# =========================
# DELETE APPLICATION
# =========================

@app.delete("/applications/{application_id}")
def delete_application(application_id: int):

    for index, application in enumerate(applications):

        if application["id"] == application_id:

            deleted_application = applications.pop(index)

            return {
                "message": "Application deleted successfully",
                "application": deleted_application
            }

    raise HTTPException(
        status_code=404,
        detail="Application not found"
    )
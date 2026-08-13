class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location="Remote",
        is_active=True
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.is_active = is_active

    def __str__(self):
        status = "Active" if self.is_active else "Closed"

        return (
            f"{self.job_id} | "
            f"{self.company} | "
            f"{self.role} | "
            f"{self.location} | "
            f"{status}"
        )


# Create JobDescription objects using keyword arguments
job1 = JobDescription(
    job_id=501,
    company="TechNova",
    role="Python Developer",
    location="Bengaluru",
    is_active=True
)

job2 = JobDescription(
    job_id=502,
    company="CodeWorks",
    role="Java Developer",
    location="Hyderabad",
    is_active=True
)

job3 = JobDescription(
    job_id=503,
    company="CloudScale",
    role="DevOps Engineer",
    location="Remote",
    is_active=False
)

# Display job details
print(job1)
print(job2)
print(job3)

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class JobLocation:
    address: str

@dataclass
class JobPosting:
    title: str
    locations: List[JobLocation]
    time_type: str
    posted_date: str
    job_id: str
    worker_type: str
    program_start_date: str
    program_duration: str
    description: str
    requirements: List[str]
    benefits: List[str]

def parse_nab_job_posting() -> JobPosting:
    # Create job locations
    locations = [
        JobLocation("15 Tran Bach Dang Thu Thiem Ward"),
        JobLocation("54A Nguyen Chi Thanh")
    ]
    
    # Create job posting
    job = JobPosting(
        title="NAB Early Careers - StarCamp by NAB's Tech Academy - Batch 16 (Group Security)",
        locations=locations,
        time_type="Full time",
        posted_date="Posted 14 Days Ago",
        job_id="JR108740",
        worker_type="Apprentice",
        program_start_date="Aug 2025",
        program_duration="3 months",
        description="""Security is one of the fastest growing segment in the IT Industry, covering a wide range of roles that work together to protect users from theft, damage, loss, and unauthorized access to their computers, network, and data.

NAB Vietnam is now opening a Security-focus StarCamp program for freshers in the IT industry.""",
        requirements=[
            "Analytical Problem Solvers",
            "Collaborative Team Players",
            "Outside the box Innovators",
            "Accountable deliverers",
            "Proactive and Eager Learners"
        ],
        benefits=[
            "Paid training allowance",
            "Developing soft skills and English skills",
            "International software development environment",
            "Work-life balance",
            "Professional growth opportunities",
            "Complete set of well-being offerings"
        ]
    )
    
    return job

def print_job_details(job: JobPosting):
    print(f"Title: {job.title}")
    print("\nLocations:")
    for location in job.locations:
        print(f"- {location.address}")
    print(f"\nTime Type: {job.time_type}")
    print(f"Posted: {job.posted_date}")
    print(f"Job ID: {job.job_id}")
    print(f"Worker Type: {job.worker_type}")
    print(f"\nProgram Details:")
    print(f"Start Date: {job.program_start_date}")
    print(f"Duration: {job.program_duration}")
    
    print("\nDescription:")
    print(job.description)
    
    print("\nRequirements:")
    for req in job.requirements:
        print(f"- {req}")
    
    print("\nBenefits:")
    for benefit in job.benefits:
        print(f"- {benefit}")

if __name__ == "__main__":
    job = parse_nab_job_posting()
    print_job_details(job) 
from dataclasses import dataclass
from typing import List, Dict
from job_parser import JobPosting, JobLocation

@dataclass
class Skill:
    name: str
    level: str = ""

@dataclass
class Experience:
    company: str
    position: str
    duration: str
    description: List[str]
    tech_stack: List[str]

@dataclass
class CV:
    name: str
    position: str
    contact: Dict[str, str]
    summary: str
    skills: List[Skill]
    experiences: List[Experience]
    education: List[str]

def create_cv() -> CV:
    return CV(
        name="CAO QUANG PHONG",
        position="BACKEND DEVELOPER",
        contact={
            "phone": "0822826817",
            "email": "caoquangphong310701@gmail.com",
            "address": "Ho Chi Minh City"
        },
        summary="Backend Developer with 2+ years of experience in building microservices with Java & Spring Boot. Proficient in Kafka, Docker, OAuth2/Keycloak, CI/CD; experienced in Agile teams and system optimization.",
        skills=[
            Skill("Java", "Advanced"),
            Skill("JavaScript", "Intermediate"),
            Skill("PHP", "Intermediate"),
            Skill("Spring Boot", "Advanced"),
            Skill("Spring Security", "Advanced"),
            Skill("Spring Cloud", "Intermediate"),
            Skill("Docker", "Intermediate"),
            Skill("Kafka", "Intermediate"),
            Skill("MySQL", "Advanced"),
            Skill("PostgreSQL", "Intermediate"),
            Skill("Oracle", "Intermediate"),
            Skill("Microservices", "Advanced"),
            Skill("CI/CD", "Intermediate"),
            Skill("Agile/Scrum", "Intermediate")
        ],
        experiences=[
            Experience(
                "Featured Projects",
                "E-commerce Microservices Platform",
                "2024",
                [
                    "Designed and built scalable microservices system",
                    "Developed 5 key services with clear responsibilities",
                    "Integrated Kafka for asynchronous communication",
                    "Implemented secure authentication with Keycloak",
                    "Enhanced observability with Zipkin and Spring Actuator"
                ],
                ["Java", "Spring Boot", "Kafka", "Spring Cloud", "Docker", "MySQL", "Keycloak", "Zipkin"]
            ),
            Experience(
                "Tuong Khanh Engineering Co., LTD",
                "Backend Developer",
                "04/2023 – 12/2023",
                [
                    "Designed and implemented 3 core microservices",
                    "Developed 5 RESTful APIs for platform integration",
                    "Automated data processing workflows",
                    "Implemented Excel import/export functionality",
                    "Optimized database interactions and queries"
                ],
                ["Java 17", "Spring Boot", "Spring Security", "Oracle", "JWT", "RESTful APIs", "Kafka"]
            ),
            Experience(
                "Cathay Life Viet Nam",
                "Java Developer",
                "01/2022 – 02/2023",
                [
                    "Designed and implemented 5+ SOAP APIs",
                    "Developed request approval system",
                    "Automated email notification workflows",
                    "Optimized complex SQL queries"
                ],
                ["Java", "Java MVC", "Spring Batch", "DB2", "SOAP API"]
            )
        ],
        education=[
            "Cao Thang Technical College | Software Technology | 09/2019 – 09/2022",
            "English: Basic (Level 2/6) and Intermediate (technical docs, team collaboration)"
        ]
    )

def analyze_fit(cv: CV, job: JobPosting) -> Dict[str, List[str]]:
    analysis = {
        "matching_skills": [],
        "relevant_experience": [],
        "potential_gaps": [],
        "recommendations": []
    }
    
    # Analyze security-related skills and experience
    security_keywords = ["security", "authentication", "authorization", "keycloak", "oauth2", "jwt"]
    
    # Check for security-related experience
    for exp in cv.experiences:
        for desc in exp.description:
            if any(keyword in desc.lower() for keyword in security_keywords):
                analysis["relevant_experience"].append(f"Security experience in {exp.company}: {desc}")
    
    # Check for required skills
    required_skills = ["java", "spring", "docker", "kafka", "microservices"]
    for skill in cv.skills:
        if any(req_skill in skill.name.lower() for req_skill in required_skills):
            analysis["matching_skills"].append(f"Strong {skill.name} skills")
    
    # Identify potential gaps
    if not any("security" in exp.description.lower() for exp in cv.experiences):
        analysis["potential_gaps"].append("Limited direct security implementation experience")
    
    # Add recommendations
    analysis["recommendations"].extend([
        "Highlight your microservices and distributed systems experience",
        "Emphasize your experience with authentication systems (Keycloak)",
        "Showcase your experience with system monitoring and observability",
        "Demonstrate your ability to work in agile environments"
    ])
    
    return analysis

def print_analysis(analysis: Dict[str, List[str]]):
    print("\n=== CV Analysis for NAB Security Position ===\n")
    
    print("Matching Skills:")
    for skill in analysis["matching_skills"]:
        print(f"✓ {skill}")
    
    print("\nRelevant Experience:")
    for exp in analysis["relevant_experience"]:
        print(f"✓ {exp}")
    
    print("\nPotential Gaps:")
    for gap in analysis["potential_gaps"]:
        print(f"! {gap}")
    
    print("\nRecommendations:")
    for rec in analysis["recommendations"]:
        print(f"→ {rec}")

if __name__ == "__main__":
    cv = create_cv()
    job = parse_nab_job_posting()
    analysis = analyze_fit(cv, job)
    print_analysis(analysis) 
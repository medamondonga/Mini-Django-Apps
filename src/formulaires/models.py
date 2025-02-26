from django.db import models

class Register(models.Model):
    PROFESSIONS = {
        "Data science": "Data Science",
        "IoT": "IoT",
        "CyberSecurity": "Cybersecurite",
        "DevOps": "DevOps",
        "Software Engineering": "Ingenierie Logicielle",
        "Artificial Intelligence": "Intelligence Artificielle",
        "Machine Learning": "Apprentissage Automatique",
        "Cloud Computing": "Informatique en Nuage",
        "Blockchain": "Blockchain",
        "Game Development": "Developpement de Jeux Video",
        "Mobile Development": "Developpement Mobile",
        "Web Development": "Developpement Web",
        "IT Support": "Support Informatique",
        "Network Administration": "Administration Reseau",
        "Database Administration": "Administration de Base de Donnees",
        "UI/UX Design": "Conception UI/UX",
        "System Architecture": "Architecture Systeme",
        "Robotics": "Robotique",
        "Embedded Systems": "Systemes Embarques",
        "Big Data": "Big Data",
        "Virtual Reality": "Realite Virtuelle"
    }

    PROMOTIONS = {
        "Licence 1": "L1",
        "Licence 2": "L2",
        "Licence 3": "L3",
        "Master 1": "M1",
        "Master 2": "M2"
    }

    email = models.EmailField()
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    date_of_birth = models.DateField()
    faculty = models.CharField(max_length=300, default="Sciences Informatiques")
    promotion = models.CharField(max_length=100, choices=PROMOTIONS)
    first_choice = models.CharField(max_length=300, choices=PROFESSIONS)
    second_choice = models.CharField(max_length=300, choices=PROFESSIONS)

    def __str__(self):
        return self.email


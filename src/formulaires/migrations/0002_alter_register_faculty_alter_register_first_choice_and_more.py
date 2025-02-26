# Generated by Django 5.1.4 on 2025-02-26 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("formulaires", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="register",
            name="faculty",
            field=models.CharField(default="Sciences Informatiques", max_length=300),
        ),
        migrations.AlterField(
            model_name="register",
            name="first_choice",
            field=models.CharField(
                choices=[
                    ("Data science", "Data Science"),
                    ("IoT", "IoT"),
                    ("CyberSecurity", "Cybersecurite"),
                    ("DevOps", "DevOps"),
                    ("Software Engineering", "Ingenierie Logicielle"),
                    ("Artificial Intelligence", "Intelligence Artificielle"),
                    ("Machine Learning", "Apprentissage Automatique"),
                    ("Cloud Computing", "Informatique en Nuage"),
                    ("Blockchain", "Blockchain"),
                    ("Game Development", "Developpement de Jeux Video"),
                    ("Mobile Development", "Developpement Mobile"),
                    ("Web Development", "Developpement Web"),
                    ("IT Support", "Support Informatique"),
                    ("Network Administration", "Administration Reseau"),
                    ("Database Administration", "Administration de Base de Donnees"),
                    ("UI/UX Design", "Conception UI/UX"),
                    ("System Architecture", "Architecture Systeme"),
                    ("Robotics", "Robotique"),
                    ("Embedded Systems", "Systemes Embarques"),
                    ("Big Data", "Big Data"),
                    ("Virtual Reality", "Realite Virtuelle"),
                ],
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="register",
            name="promotion",
            field=models.CharField(
                choices=[
                    ("Licence 1", "L1"),
                    ("Licence 2", "L2"),
                    ("Licence 3", "L3"),
                    ("Master 1", "M1"),
                    ("Master 2", "M2"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="register",
            name="second_choice",
            field=models.CharField(
                choices=[
                    ("Data science", "Data Science"),
                    ("IoT", "IoT"),
                    ("CyberSecurity", "Cybersecurite"),
                    ("DevOps", "DevOps"),
                    ("Software Engineering", "Ingenierie Logicielle"),
                    ("Artificial Intelligence", "Intelligence Artificielle"),
                    ("Machine Learning", "Apprentissage Automatique"),
                    ("Cloud Computing", "Informatique en Nuage"),
                    ("Blockchain", "Blockchain"),
                    ("Game Development", "Developpement de Jeux Video"),
                    ("Mobile Development", "Developpement Mobile"),
                    ("Web Development", "Developpement Web"),
                    ("IT Support", "Support Informatique"),
                    ("Network Administration", "Administration Reseau"),
                    ("Database Administration", "Administration de Base de Donnees"),
                    ("UI/UX Design", "Conception UI/UX"),
                    ("System Architecture", "Architecture Systeme"),
                    ("Robotics", "Robotique"),
                    ("Embedded Systems", "Systemes Embarques"),
                    ("Big Data", "Big Data"),
                    ("Virtual Reality", "Realite Virtuelle"),
                ],
                max_length=300,
            ),
        ),
    ]

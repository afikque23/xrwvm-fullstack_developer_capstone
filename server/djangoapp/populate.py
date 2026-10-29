from .models import CarMake, CarModel
from datetime import datetime


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese brand"},
        {"name": "Mercedes", "description": "Great cars. German brand"},
        {"name": "Audi", "description": "Great cars. German brand"},
        {"name": "Kia", "description": "Great cars. Korean brand"},
        {"name": "Toyota", "description": "Great cars. Japanese brand"},
        {"name": "Ford", "description": "American brand"},
        {"name": "Honda", "description": "Japanese brand"},
    ]

    car_make_instances = []
    for make in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=make["name"], description=make["description"])
        )

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "Qashqai", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "XTRAIL", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[0], "dealer_id": 2},
        {"name": "A-Class", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[1], "dealer_id": 2},
        {"name": "C-Class", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[1], "dealer_id": 3},
        {"name": "E-Class", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[1], "dealer_id": 3},
        {"name": "A4", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[2], "dealer_id": 4},
        {"name": "A5", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[2], "dealer_id": 4},
        {"name": "A6", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[2], "dealer_id": 5},
        {"name": "Telluride", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[3], "dealer_id": 5},
        {"name": "Carnival", "type": "VAN", "year": "2023-01-01", "car_make": car_make_instances[3], "dealer_id": 6},
        {"name": "Cerato", "type": "SEDAN", "year": "2023-01-01", "car_make": car_make_instances[3], "dealer_id": 6},
        {"name": "Corolla Cross", "type": "SUV", "year": "2023-01-01", "car_make": car_make_instances[4], "dealer_id": 7},
        {"name": "GR Yaris", "type": "COUPE", "year": "2023-01-01", "car_make": car_make_instances[4], "dealer_id": 7},
        {"name": "Mustang", "type": "COUPE", "year": "2023-01-01", "car_make": car_make_instances[5], "dealer_id": 8},
        {"name": "Civic", "type": "SEDAN", "year": "2023-01-01", "car_make": car_make_instances[6], "dealer_id": 8},
    ]

    for model in car_model_data:
        CarModel.objects.create(
            name=model["name"], type=model["type"],
            year=model["year"], car_make=model["car_make"],
            dealer_id=model["dealer_id"]
        )

from random import choice
import json


def main():
    jobs = get_jobs()
    water_jobs = [job for job in jobs if job["crystal"] == "water"]
    wind_jobs = [job for job in jobs if job["crystal"] == "wind"]
    fire_jobs = [job for job in jobs if job["crystal"] == "fire"]
    earth_jobs = [job for job in jobs if job["crystal"] == "earth"]

    print("job 1", choice(wind_jobs)["name"])
    print("job 2", choice(water_jobs)["name"])
    print("job 3", choice(fire_jobs)["name"])
    print("job 4", choice(earth_jobs)["name"])

def get_jobs() -> list[dict]:
    with open("jobs.json") as file:
        data = json.loads(file.read())
    return data


if __name__ == "__main__":
    main()
class Car:
    def __init__(self, dis, speed):
        self.dis = dis
        self.speed = speed


class Solution:
    def carFleet(
        self,
        target: int,
        position: List[int],
        speed: List[int]
    ) -> int:
        cars = []

        for dis, car_speed in zip(position, speed):
            cars.append(Car(dis, car_speed))

        # Closest car to the target first.
        cars.sort(reverse=True, key=lambda car: car.dis)

        fleets = 0
        start = 0

        while start < len(cars):
            finishing_cars = 0
            fleet_arrival_time = -1

            # Determine which active cars/fleets will finish
            # during the coming one-hour simulation step.
            for i in range(start, len(cars)):
                car = cars[i]

                solo_arrival_time = (
                    target - car.dis
                ) / car.speed

                # If this car would arrive later than every fleet
                # ahead, it cannot catch them and forms a new fleet.
                is_new_fleet = (
                    solo_arrival_time > fleet_arrival_time
                )

                if is_new_fleet:
                    fleet_arrival_time = solo_arrival_time

                # fleet_arrival_time is the car's actual arrival time:
                # either its own time or the time of the fleet it catches.
                if fleet_arrival_time <= 1:
                    finishing_cars += 1

                    if is_new_fleet:
                        fleets += 1
                else:
                    # Once one fleet takes more than one hour,
                    # every car behind it also takes more than one hour.
                    break

            start += finishing_cars

            if start == len(cars):
                break

            # Simulate one hour for cars that have not finished.
            for i in range(start, len(cars)):
                car = cars[i]
                car.dis += car.speed

                # Only compare with the active car directly ahead.
                if i > start and car.dis >= cars[i - 1].dis:
                    car.dis = cars[i - 1].dis
                    car.speed = cars[i - 1].speed

        return fleets
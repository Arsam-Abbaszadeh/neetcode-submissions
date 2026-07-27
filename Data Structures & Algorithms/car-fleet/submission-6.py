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
        fleets = 0
        cars = []

        for dis, car_speed in zip(position, speed):
            cars.append(Car(dis, car_speed))

        cars.sort(reverse=True, key=lambda x: x.dis)

        start = 0

        while start < len(cars):
            finish = []
            previous_positions = {}

            for i in range(start, len(cars)):
                car = cars[i]

                # Save this because car.dis and car.speed may be changed.
                previous_positions[i] = car.dis

                car.dis += car.speed

                # If the car ahead is not finishing this step,
                # this car cannot pass it or finish ahead of it.
                if (
                    i > start
                    and i - 1 not in finish
                    and car.dis >= cars[i - 1].dis
                ):
                    car.dis = cars[i - 1].dis
                    car.speed = cars[i - 1].speed

                if car.dis >= target:
                    finish.append(i)

            if finish:
                previous_finish_time = None

                for j in finish:
                    remaining = target - previous_positions[j]

                    finish_time = remaining / cars[j].speed

                    # First finishing car forms a fleet.
                    # A later car forms another fleet only if it
                    # reaches the target after the fleet ahead.
                    if (
                        previous_finish_time is None
                        or finish_time > previous_finish_time
                    ):
                        fleets += 1
                        previous_finish_time = finish_time

                start += len(finish)

        return fleets
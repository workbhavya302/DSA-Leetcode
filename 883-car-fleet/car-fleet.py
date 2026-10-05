class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        fleets = 0
        current_fleet_time = 0.0
        for pos, spd in cars:
            arrival_time = (target - pos) / spd
            if arrival_time > current_fleet_time:
                fleets += 1
                current_fleet_time = arrival_time
                
        return fleets

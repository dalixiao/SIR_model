import random
from vector import Vector
PERSON_MOVING_RANGE = 60
PERSON_MOVING_SPEED = 2
INITIAL_INFECTED_NUMBER = 7
TOO_CLOSE_RANGE = 6
RECOVER_COUNT_DOWN = 700
INFECTION_RATE = 0.3
class Population:
    def __init__(self,population_size,canvas_size):
        self.day = 0
        self.infected_num = INITIAL_INFECTED_NUMBER
        self.population_size = population_size
        self.people = []
        for i in range(population_size):
            self.people.append(Person(canvas_size,self))
        self.infected_arr = self.initialize_infected_arr(self.population_size)
        self.susceptible_arr = self.initialize_susceptible_arr(self.population_size,self.infected_arr)
        self.recovered_arr = set()

    def initialize_infected_arr(self,population_size):
        res = set(random.sample(range(population_size),INITIAL_INFECTED_NUMBER))
        print(res)
        for initial_infected_index in res:
            self.people[initial_infected_index].status = 'red'
        return res

    def initialize_susceptible_arr(self,population_size,infected_arr):
        susceptible_arr = set()
        for i in range(population_size):
            susceptible_arr.add(i)
        for element in infected_arr:
            susceptible_arr.remove(element)
        return susceptible_arr

    def people_move(self):
        self.day += 1
        for person in self.people:
            person.move(self)
        self.disease_spread()

    def disease_spread(self):
        for infected_index in self.infected_arr.copy():
            for susceptible_index in self.susceptible_arr.copy():
                if (self.people[infected_index].current_location - self.people[susceptible_index].current_location).length <= TOO_CLOSE_RANGE:
                    if random.uniform(0,1) < INFECTION_RATE:
                        self.people[susceptible_index].status = 'red'
                        self.infected_arr.add(susceptible_index)
                        self.susceptible_arr.remove(susceptible_index)
                        self.infected_num += 1


class Person:
    def __init__(self,canvas_size,Population):
        self.initial_x_position = random.uniform(0,1)*canvas_size
        self.initial_y_position = random.uniform(0,1)*canvas_size
        self.home_location = Vector(self.initial_x_position,self.initial_y_position)
        self.target_position  = self.home_location.copy()
        self.current_location = self.home_location.copy()
        self.moving_range = PERSON_MOVING_RANGE
        self.speed = PERSON_MOVING_SPEED
        self.status = 'yellow'
        self.count_down = RECOVER_COUNT_DOWN
    def next_target_position(self,moving_range):
        new_position = self.home_location + Vector( random.uniform(0,moving_range) , random.uniform(0,moving_range) )
        difference_vector = new_position-self.current_location
        unit_difference_vector = difference_vector.unify()
        self.step_vector = unit_difference_vector * self.speed
        return new_position

    def move(self,Population):
        if self.current_location == self.target_position:
            self.target_position = self.next_target_position(self.moving_range)
        if (self.target_position-self.current_location).length < self.step_vector.length:
            self.current_location = self.target_position
            self.target_position = self.next_target_position(self.moving_range)
        else:
            self.current_location += self.step_vector

        if self.status == 'red':
            if self.count_down > 0:
                self.count_down -= 1
            else:
                self.status = 'cyan'
                Population.infected_num -= 1

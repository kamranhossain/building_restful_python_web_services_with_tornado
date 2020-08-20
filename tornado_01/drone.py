from time import sleep


class HexacopterStatus:
    def __init__(self, motor_speed, turned_on):
        self.motor_speed = motor_speed
        self.turned_on = turned_on


class Hexacopter:
    MIN_SPEED = 0
    MAX_SPEED = 1000

    def __init__(self):
        self.motor_speed = self.__class__.MIN_SPEED
        self.turned_on = False

    def get_motor_speed(self):
        return self.motor_speed

    def set_motor_speed(self, motor_speed):
        if motor_speed < self.__class__.MIN_SPEED:
            raise ValueError(
                "The minimum speed is {0}".format(self.__class__.MIN_SPEED)
            )
        if motor_speed > self.__class__.MAX_SPEED:
            raise ValueError(
                "The maximum speed is {0}".format(self.__class__.MAX_SPEED)
            )
        self.motor_speed = motor_speed
        self.turned_on = self.motor_speed != 0
        sleep(2)
        return HexacopterStatus(self.get_motor_speed(), self.is_turned_on())

    def is_turned_on(self):
        return self.turned_on

    def get_hexacopter_status(self):
        sleep(3)
        return HexacopterStatus(self.get_motor_speed(), self.is_turned_on())


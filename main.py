def main():
    class Auto:
        def __init__(
                self,
                name="Lada",
                speed=0
        ):
            self.name = name
            self.speed = speed

        @property
        def speed(self):
            return self.__speed

        @speed.setter
        def speed(self, speed):
            try:
                if int(speed) < 0:
                    print(f"{speed} is invalid")
                else:
                    self.__speed = int(speed)
            except ValueError:
                print(f"{speed} is not a number")

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name):
            try:
                if len(str(name)) > 0:
                    self.__name = str(name)
                else:
                    print("The name must have  at least one character")
            except ValueError:
                print(f"{name} is not a string")

        def speed_up(self, acceleration):
            try:
                if int(acceleration) > 0:
                    self.speed = self.speed + int(acceleration)
                    print(f"Current speed is {self.speed}")
                else:
                    print(f"Invalid speed {acceleration}")
            except ValueError:
                print(f"{acceleration} is not a number")

        def speed_down(self, acceleration):
            try:
                if self.speed - acceleration < 0:
                    self.speed = 0
                else:
                    self.speed = self.speed - acceleration
                print(f"Current speed is {self.speed}")
            except TypeError:
                print(f"{acceleration} is not a number")

        def speed_current(self, acceleration):
            self.speed = acceleration
            print(f"Current speed is {self.speed}")

        def speed_action(self, acceleration):
            try:
                if self.speed < acceleration:
                    print(f"Increase speed on {acceleration - self.speed}")
                elif self.speed > acceleration:
                    print(f"Decrease speed on {self.speed - acceleration}")
            except TypeError:
                print(f"{acceleration} is not a number")


if __name__ == '__main__':
    main()

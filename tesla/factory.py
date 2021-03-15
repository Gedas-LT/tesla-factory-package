class Tesla:

    def __init__(self, model: str, color: str, autopilot: bool = False) -> None:
        self.__model = model
        self.__color = color
        self.__autopilot = autopilot
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__efficiency = 0.3

    @property
    def color(self) -> str:
        """
        Returns color of a car.

        Parameters
        ----------
        None

        Returns
        -------
            color : str
                Color of a car
        """
        
        return self.__color

    @property
    def seats_count(self) -> int:
        return self.__seats_count

    @seats_count.setter
    def seats_count(self, seats: int) -> None:
        """
        Set a new value to self.__seats_count.

        If value is equal or smaller than 1 the value stays the same.

        Parameters
        ----------
            seats : int
                Number of seats

        Returns
        -------
        None 
        """

        if seats > 1:
            self.__seats_count = seats

    def autopilot(self, obsticle: str) -> str:
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obsticle}"
        return "Autopilot is not available"

    def open_doors(self) -> str:
        if self.__is_locked:
            return "Car is locked!"
        return "Doors opens sideways"

    def unlock(self) -> None:
        if self.__is_locked:
            self.__is_locked = False

    def lock(self) -> None:
        """
        Lock the car if self.__is_locked equals to FALSE.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        if not self.__is_locked:
            self.__is_locked = True

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self) -> str:
        self.__battery_charge = 100
        return self.check_battery_level()

    def drive(self, travel_range: float) -> str:
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge -= battery_discharge_percent
            return self.check_battery_level()
        return self.check_battery_level()

    def welcome(self) -> str:
        raise NotImplementedError
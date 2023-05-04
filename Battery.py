class Battery:
    def __init__(self, max_capacity):
        self.__current_charge = 0
        self.current_available_energy = 0
        self.__max_capacity = max_capacity

    def get_charge_lvl(self):
        charge_lvl = self.__current_charge / self.__max_capacity * 100
        return charge_lvl

    def change_current_charge(self, value):
        if self.__current_charge + value > self.__max_capacity:
            print("naladowano do konca")
            self.__current_charge = self.__max_capacity
        else:
            self.__current_charge += value

        self.current_available_energy = 0.8 * self.__current_charge

        print(f"magazyn jest naladowany na {self.get_charge_lvl()}%")

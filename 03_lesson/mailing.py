from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f'Отправление {self.track} из {self.from_address.index}, {self.from_address.city}, '
                f'{self.from_address.street}, {self.from_address.house_number}-{self.from_address.flat_number} '
                f'в {self.to_address.index}, {self.to_address.city}, {self.to_address.street},'
                f'{self.to_address.house_number}-{self.to_address.flat_number}. Стоимость {self.cost} рублей.')


from address import Address
from mailing import Mailing

address1 = Address(111111, 'City1', 'Street1', 111, 11)
address2 = Address(222222, 'City2', 'Street2', 222, 22)

letter = Mailing(address1, address2, 125, 'DZ3112025')

print(letter)




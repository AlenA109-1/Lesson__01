from smartphone import Smartphone

t1 = Smartphone('Samsung', 'S1', '+79109101010')
t2 = Smartphone('Samsung', 'S2', '+79209202020')
t3 = Smartphone('Samsung', 'S3', '+79309303030')
t4 = Smartphone('Nokia', 'N1', '+79409404040')
t5 = Smartphone('Nokia', 'N2', '+79509505050')

catalog = [t1, t2, t3, t4, t5]

for smartphone in catalog:
    print(smartphone.type, '|',  smartphone.model, '|', smartphone.phoneNumber)

class Scheme:
    def __init__(self, id, name, rate, charge):
        self.scheme_id = id
        self.scheme_name = name
        self.outgoing_rate = rate
        self.message_charge = charge

    def display_scheme(self):
        print("Scheme id      : ", self.scheme_id)
        print("Scheme name    : ", self.scheme_name)
        print("Outgoing rate  : ", self.outgoing_rate)
        print("Message Charge : ", self.message_charge)


class Customer():
    def __init__(self, id, name, mobile):
        self.cust_id = id
        self.cust_name = name
        self.mobile_no = mobile

    def display_customer(self):
        print("Customer id : ", self.cust_id)
        print("Customer name : ", self.cust_name)
        print("Customer mobile : ", self.mobile_no)


obj1 = Scheme(1, "Shani", 15.4, 10000)
obj2 = Customer(2, "Bunny", 9874561230)
obj1.display_scheme()
print('**********************************')
obj2.display_customer()
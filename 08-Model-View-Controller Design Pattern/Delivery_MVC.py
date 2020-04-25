class Model:

    delivery_dict = {
        "less than 30kg" : {"price": 10000},
        "30-70kg"        : {"price": 15000},
        "70-100kg"       : {"price": 20000},
        "more than 100kg": {"price": 30000}
    }


class View:

    def show_delivery_list(self, delivery_dict):
        for key in delivery_dict:
            print(key)

    def show_price_list(self, delivery_dict):
        for key in delivery_dict:
            print(f"Delivery price for {key} is {Model.delivery_dict[key]['price']} (toamn)")


class Controller:

    def __init__(self):
        self.model = Model() 
        self.view = View()

    def get_delivery_list(self):
        self.delivery_list = self.model.delivery_dict.keys()
        return self.view.show_delivery_list(self.delivery_list)
    
    def get_price_list(self):
        self.delivery_list = self.model.delivery_dict.keys()
        return self.view.show_price_list(self.delivery_list)


# Client => User
controller = Controller()
print("[Delivery List]")
controller.get_delivery_list()
print("\n[Price List]")
controller.get_price_list()
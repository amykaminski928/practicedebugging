from customer import Customer
from soda_machine import SodaMachine
import user_interface

class Simulation:
    def __init__(self):
        super
        
        #SodaMachine.fill_inventory(self)
        #SodaMachine.fill_register()
    def run_simulation(self):
        """The central method called in main.py."""
        
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = True
        while will_proceed is True:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1:
                soda_machine.begin_transaction(customer)
            elif user_option == 2:
                customer.check_coins_in_wallet()
            elif user_option == 3:
                customer.check_backpack()
            else:
                will_proceed = False
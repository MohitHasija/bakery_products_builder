"""
This file implements the main function to run the entire Program.

"""

import logging
from bakery_handler import ProductsHandler, bakery_products


def main():
    """
    At first We initialise the Bakery Product Handler with all the Bakery Products
    """
    handler = ProductsHandler(bakery_products)
    logging.basicConfig(level=logging.INFO, filename="logfile.log", filemode='w')
    """
    Now we get the input from user and accordingly processes it.
    """
    result_text = []
    while True:
        handler_input = input("")
        try:
            number_of_products = int(handler_input.split(' ')[0])
            product_code = handler_input.split(' ')[1]
            result = handler.get_least_cost_of_product_packing( product_code, number_of_products)
            quantity_to_cost_mapping, second_tuple  = result #Unpack results
            total_cost, minimium_possible_combination = second_tuple
            text_to_add = handler_input + " $" + str(total_cost) + "\n"
            combination_cost_mapping = {}.fromkeys(list(set(minimium_possible_combination)))
            for entry in sorted(list(minimium_possible_combination), reverse=False):
                if not combination_cost_mapping[entry]:
                    combination_cost_mapping[entry] = 1
                else:
                    combination_cost_mapping[entry] += 1

            text_to_add += '\n'.join([str(value) + ' * ' + str(key) + ' ' + quantity_to_cost_mapping[str(key)]
                                      for key, value in combination_cost_mapping.items()])
            result_text.append(text_to_add)
            print("Process completed.")
        except Exception as e:
            logging.info(str(e))
            break
    print('\n'.join(result_text))

if __name__=='__main__':
    main()




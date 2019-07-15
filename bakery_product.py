"""
This file implements the Bakery Product class and methods
that are used to calcualte the right combination of parcels
for a given number

"""
import itertools
import logging


class BakeryPackQuantityAndCost(object):
    def __init__(self, pack_quantity, pack_cost):
        self.pack_quantity =  pack_quantity
        self.pack_cost = pack_cost


class BakeryProduct(object):
    def __init__(self, name, code, pack_quantity_and_cost_list):
        self.name = name
        self.code = code
        self.pack_quantity_and_cost_list = pack_quantity_and_cost_list

    def get_list_of_numbers_possible(self, numbers, packs):
        return [i for _ in range(packs) for i in numbers]

    def get_possible_combinations(self, source_list, sum_required):

        numbers = sorted(source_list, reverse=False)
        result_to_return = set()
        max_packs_possible = int(sum_required / numbers[0]) if not sum_required % numbers[0] else \
            int(sum_required / numbers[0]) + 1
        min_packs_possible = int(sum_required / numbers[-1]) if not sum_required % numbers[-1] else \
            int(sum_required / numbers[-1]) - 1
        found = False
        logging.info("The max packs possible are: {}".format(max_packs_possible))
        for i in range(min_packs_possible, max_packs_possible + 1):
            my_list = self.get_list_of_numbers_possible(numbers, i)
            for seq in itertools.combinations(my_list, i):
                    seq = tuple(sorted(list(seq)))
                    if sum(seq) == sum_required:
                        result_to_return.add(seq)
                        logging.info("The sequence possible is: {}".format(seq))
                        found = True
            if found:
                break
        logging.info("The possible combinations are: {}".format(result_to_return))
        return list(result_to_return)


    def get_minimium_sum_for_possible_combinations_of_packing(self, quantity_to_cost_mapping,
                                                              possible_combinations):
        minimium_combination = tuple()
        minimium_cost = 0
        possible_combinations = sorted(possible_combinations, reverse=False, key=len)
        minimium_number_of_packs = len(possible_combinations[0])
        for each_combination in possible_combinations:
            if len(each_combination) != minimium_number_of_packs:
                continue
            sum = 0.0
            for each_entry in each_combination:
                sum = sum + float(quantity_to_cost_mapping[str(each_entry)][1:])
            if not minimium_cost:
                minimium_cost = sum
                minimium_combination = each_combination
            elif minimium_cost < sum:
                minimium_cost = sum
                minimium_combination = each_combination
            else:
                continue

        return round(minimium_cost, 2), minimium_combination

    def get_minimium_cost_of_packing(self, number_of_packs_ordered):
        quantity_to_cost_mapping = {}
        number_of_packs_possible = []
        for entry in self.pack_quantity_and_cost_list:
            quantity_to_cost_mapping[entry.pack_quantity] = entry.pack_cost
            number_of_packs_possible.append(int(entry.pack_quantity))
        logging.info("The number of packs possible are: {}".format(number_of_packs_possible))
        possible_combinations = self.get_possible_combinations(source_list = number_of_packs_possible,
                                                               sum_required = number_of_packs_ordered)

        return quantity_to_cost_mapping, \
               self.get_minimium_sum_for_possible_combinations_of_packing(quantity_to_cost_mapping,
                                                                          possible_combinations)

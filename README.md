# bakery_products_builder

This package implements the Bakery Packing Algorithm to calculate the least possible packs
for a given customer input.

The Algorithm is as follows:
1. Initialise the handler with given Bakery Products and their cost and packaging specifications.

2. Take the User input for one product.

3. Find all possible combinations that can be possible for given number of product in an order with least number of packets.

4. For all the given possible combinations with least number of packets, calculate the cost effective  packets that can be created for a particular order to be completed.

5.Repeat the Step 2 for next user input.

6.Once the user hits enter, show the output for all the given user inputs.

Run instructions:

1. Copy the entire package in one directory.

2. Run main.py

3. Try enter the user input in format <number_of_products> <product_code> <enter key>

4. Keep on adding the user input for products with enter and finally hit enter to get result output on screen.

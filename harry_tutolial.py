# # # Interest Calculator
# # loan_amount = int(input("Type loan amount: "))
# # years = float(input("Type loan time: "))
# # rate = float(input("Type loan rate: "))
# #
# # interest = loan_amount * years * rate / 100
# # print("The interest is: " + str(interest))
# # print(f"The loan amount is: {loan_amount} and the interest is: {interest}")
# # # Creating BMI Calculator
# # weight = float(input('Enter weight in kgs: '))
# # height = float(input('Enter height in meters: '))
# #
# # bmi = weight / (height * height)
# # print('BMI is:', bmi)
#
# # # Initial list of products
# # products = ['phone', 'tablet', 'computer', 'laptop', 'journal']
# #
# # # Displaying the initial list of products
# # print(f"The current list of items is: {products}")
# #
# # # Removing products
# # remove_item = input("Enter the product to remove: ")
# # products.remove(remove_item)
# #
# # # Displaying the list after removing the product
# # print(f"The current list of items is: {products}")
# #
# # # Adding products
# # add_item = input("Enter the product to add: ")
# # products.append(add_item)
# #
# # # Displaying the list after adding the product
# # print(f"The current list of items is: {products}")
# # Initial list of products
# products = ['phone', 'tablet', 'computer', 'laptop', 'journal']
#
# # Displaying the initial list of products
# print(f"The current list of items is: {products}")
#
# # Adding products
# add_item = input("Enter the product to add: ")
#
# # Accepting the product after which you want to place the current product
# add_after = input(f"After which product do you want to place {add_item}? ")
# index = products.index(add_after)
# products.insert(index+1 , add_item)
#
# # Displaying the list after adding products
# print("The current list of items is:",products)
# products = ['phone', 'tablet', 'computer', 'laptop', 'journal']
# item = input("Enter product name:")
# print(item in products)
products = {'phone': 100,'tablet': 200,'computer': 300,'laptop': 400,'journal': 40}
product=input("Enter the product name:")
print(f"the price of {product} is {products[product]}")

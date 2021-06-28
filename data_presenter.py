# # import CupcakeInvoices.csv

# #Create a new file called data_presenter.py.
# # Open the CupcakeInvoices.csv.

data = open("CupcakeInvoices.csv")

# # Loop through all the data and print each row.
for cupcakes_type in data:
  print(cupcakes_type)

# # Loop through all the data and print the type of cupcakes purchased.

for cupcakes_type in data:
  x = cupcakes_type.split(',')
  print(x[2] )

# # Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
for earnings in data:
  x = earnings.split(',')

  total = int(x[3]) * float(x[4])
  print(total)


# # Loop through all the data, and print out the total for all invoices combined.
total1 = 0
for earnings in data:
  x = earnings.split(',')

  total = int(x[3]) * float(x[4])
  total1 = total1 + total

print(total1)
  


# # Close your open file.
data.close()

# # Challenge: Do some research and see if you can limit your floats to never exceed two characters after the decimal point.
total1 = str(round(total1, 2))

print(total1)


# PART 3¶
# Going Further
# Explore the graphing tools covered in today’s lecture. See if you can implement one of them to display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.


total1 = 0  
total2 = 0  
total3 = 0  
for cupcakes_type in data:
  
  x = cupcakes_type.split(',')
  
  if x[2] == "Vanilla":
   total = int(x[3]) * float(x[4])
   total1 = total1 + total
  elif x[2] == "Chocolate":
   total = int(x[3]) * float(x[4])
   total2 = total2 + total
  elif x[2] == "Strawberry":
   total = int(x[3]) * float(x[4])
   total3 = total3 + total
print(total1)
print(total2)
print(total3)

# for cupcakes_type in data:
  
  # x = cupcakes_type.split(',')


# for cupcakes_type in data:
  
  # x = cupcakes_type.split(',')
  # print(x[2] )
  
import plotly.graph_objects as go

labels = ['Chocolate','Vanilla','Strawberry']
values = [total1, total2, total3]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

data.close()
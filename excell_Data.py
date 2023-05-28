import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()

# Select the active worksheet
worksheet = workbook.active




# Add some data to the worksheet
worksheet['A1'] = 'ID'
worksheet['B1'] = 'Talim yonalish'
worksheet['C1'] = 'Talim tili'
worksheet['A2'] = 'John'
worksheet['B2'] = 25
# worksheet['A3'] = 'Jane'
# worksheet['B3'] = 30
#
# # Save the workbook
# workbook.save('example.xlsx')


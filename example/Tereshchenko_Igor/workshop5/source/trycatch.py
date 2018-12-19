import sys

input_file = 'data/orders.csv'
out_file = 'data/orders_out.csv'

try:
   with open(input_file, 'r') as f:
      file_content = f.read()
      print ("read file " + input_file)

   if not file_content:
      print ("no data in file " + input_file)
      file_content = "out data..."

   with open(out_file, 'w') as dest:
      dest.write(file_content)
      print ("wrote file " + out_file)
except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))

except: #handle other exceptions such as attribute errors
   print ("Unexpected error:", sys.exc_info()[0])

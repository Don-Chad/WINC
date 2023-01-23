# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

leek_order = 'leek 4'
leek_count = int(leek_order[5:])
sum_total = leek_count * leek_price
print(sum_total)


broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'
order_amount = float(broccoli_order[9:])
total_price = round(broccoli_price * order_amount, 2)
print(str(order_amount) + 'kg broccoli costs ' + str(total_price) + 'e')


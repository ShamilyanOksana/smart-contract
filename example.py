import Estate

import time
ws = Estate.Estate()

# Admin
# 0xAc771378BB6c2b8878fbF75F80880cbdDefd1B1e

# 0xa1FA391371acf51DFff14d5943E270BE14c1748A




# answer = ws.auth("0xac771378bb6c2b8878fbf75f80880cbddefd1b1e", '123456789')
# answer = ws.auth("0xa1fa391371acf51dfff14d5943e270be14c1748a", 'qwerty')
answer = ws.auth("0x370c6cFC1662a0d7B995B98B22652cb1DBE94795", 'qwerty')
# print(answer)

# ws.create_estate("0xa1fa391371acf51dfff14d5943e270be14c1748a", "Петровская, 12", 200, 150)
# ws.create_estate("0xac771378bb6c2b8878fbf75f80880cbddefd1b1e", "Малиновского, 102", 789, 250)
# ws.create_estate("0x370c6cFC1662a0d7B995B98B22652cb1DBE94795", "Чехова, 2", 123, 100)

# answer = ws.get_estates_number()
# print(answer)
# answer = ws.get_estates()
# print(answer)
# answer = ws.my_estates()
# print(answer)
# answer = ws.get_estate_by_id(4)
# print(answer)
# answer = ws.can_present()
# print(answer)
# ws.create_present(4, '0x370c6cFC1662a0d7B995B98B22652cb1DBE94795', 1)
# answer = ws.get_present_by_number(1)
# print(answer)
# answer = ws.get_present_by_number(1)
# print(answer)
# answer = ws.get_presents_number()
# print(answer)
# answer = ws.my_present()
# print(answer)
# answer = ws.confirm_present(0)
# answer = ws.cancel_present(4)
# print(answer)
# answer = ws.i_presented()
# print(answer)



# КУПЛЯ ПРОДАЖА

# answer = ws.can_sale()
# print(answer)
# answer = ws.get_sales_number()
# print(answer)
# ws.create_sale(3, 10, 86400)
# answer = ws.my_sales()
# print(answer)
ws.i_want_to_buy(1, 15)
# answer = ws.who_want_to_buy()
# print(answer)
# answer = ws.i_have_payed()
# print(answer)
# ws.cancel_sale(0)
# answer = ws.choose_to_buy()
# print(answer)
# answer = ws.get_estate_by_id(1)
# print(answer)
# answer = ws.get_sale_by_id(1)
# print(answer)


# ws.create_pledge(1, 10, 1)


import Estate

ws = Estate.Estate()

# auth - работает
answer = ws.auth("0xfeab30128bc6a3bb840a80a7931fe4ed58181fc9", "Drjfm1Px")

answer = ws.get_estate()

print(answer)

e_tot=0
o_tot=0
for x in range(1,101):
    if x%2 == 0: e_tot += x
    else: o_tot += x


print("1-100까지 짝수 합:{0}, 홀수 합:{1}".format(e_tot,o_tot))

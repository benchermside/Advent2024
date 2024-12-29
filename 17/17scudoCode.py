
desired = [2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0]
RB = 0
RC = 0
RA = []
found = []
while RA != 0:
    RB = RA%8
    RB = RB^0b011
    RC = RA//(2**RB)
    RB = RB^RC
    RB = RB ^ 0b011
    RA = RA //(0b011)
    found.append(RB%8)


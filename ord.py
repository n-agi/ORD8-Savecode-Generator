userid = "Khang"
savetime = 99
A=0
be = ["" for x in xrange(0, 5)]
Re = [0 for x in xrange(0, 5)]
n="IeuGS0fHZPQWN8g3tq1CJK2mxOyMD6LT49pa5kVjnXlwcibhERUoYAsrBzvd7F"
V = len(n)
N = 5
R = "ORD8"
E = ["" for x in xrange(0, 100)]
O = ["" for x in xrange(0, 100)]
B="~!@#$%^&*()_-+=\{\[\}]:;'<,>.?/"
D="abcdefghijklmnopqrstuvwxyz"
F="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
G=""
h=""
H=""
j=""
def rJ(Sj):
    global A, be, Re, n, V, N ,R, E, O, B, D, F ,G ,h, H, j
    wj = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    iJ = ""
    aJ = len(wj)
    nJ = len(Sj)
    cutLength = 0
    zj = 0
    uj = 0
    VJ = 0
    uj = 1
    while uj <= nJ:
        iJ = Sj[uj-1:uj]
        VJ = 1
        while VJ <= aJ:
            if(iJ == wj[VJ-1:VJ]):
                zj = zj+(VJ*uj)
            VJ = VJ + 1
        uj = uj+1
    return zj
def AJ():
    global A, be, Re, n, V, N ,R, E, O, B, D, F ,G ,h, H, j
    uj = 0
    NJ = N-1
    VJ = 1
    loopBE = len(R)
    #print loopBE
    uj = 1
    NJ = 64
    while uj <= NJ:
        O[uj] = n[uj-1:uj]
        E[uj] = ""
        uj = uj+1
    I = rJ(R)
    A = I
    E[1] = EJ(I)

def ModuloInteger(dividend, divisor):
    modulus = dividend - (dividend / divisor) * divisor
    if(modulus < 0):
        modulus = modulus + divisor
    return modulus
def EJ(Tj):
    global A, be, Re, n, V, N ,R, E, O, B, D, F ,G ,h, H, j
    #print Tj
    inputStr = str(Tj)
    zj = ""
    XJ = 0
    while Tj > 0:
        XJ = ModuloInteger(Tj, V)
        zj = n[XJ:XJ+1] + zj
        Tj = Tj / V
    return zj

for i in xrange(0, 5):
    be[i] = userid
for i in xrange(0, 5):
	for j in xrange(1, savetime+1):
		Re[i] += j
PI = 1
print "{0} savetime: {1}".format(userid, savetime)
AJ()

hJ=rJ(be[PI+1])
E[2]=EJ((hJ+Re[PI+1])*2)
E[3]=EJ((hJ+Re[PI+1]+ A))

print "Your save code: " + E[1] + "-" + E[2] + "-" + E[3]

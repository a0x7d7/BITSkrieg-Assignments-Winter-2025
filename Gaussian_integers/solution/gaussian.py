from sympy import factorint

#given values
N_real = 11054351449271364292225016851452143819751823155908557070133673254873159574935323176876508615548052488644128960752240531022390769334898261313297069016597670
N_imag = 2680612960154966008054997438584556149029321425722463373142140963489354451326574764044837508260358039483950861348071006278334896039849245876886158410280573

C_real = 3183173215846319694782552188901941004287847534987212181471715243976738858637329192715623528370953981955924702906982980548874269400263491690485606329441864
C_imag = -1904185067035626534182429829878423238989855853294933716063868180706657459357446871432753479485807730833884183329354487316528346312748248634190557446411811

e = 65537

N = (N_real, N_imag)
C = (C_real, C_imag)

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a, m):
    g, x, _ = egcd(a, m)
    return x % m

def gmul(a, b):
    return (
        a[0]*b[0] - a[1]*b[1],
        a[0]*b[1] + a[1]*b[0]
    )

def div_round(n, d):

    if n >= 0:
        return (n + d//2) // d
    else:
        return (n - d//2) // d

def gmod(a, m):
    norm = m[0]*m[0] + m[1]*m[1]

    real_num = a[0]*m[0] + a[1]*m[1]
    imag_num = a[1]*m[0] - a[0]*m[1]

    qr = div_round(real_num, norm)
    qi = div_round(imag_num, norm)

    return (
        a[0] - (qr*m[0] - qi*m[1]),
        a[1] - (qr*m[1] + qi*m[0])
    )


def gpow(base, exp, mod):
    result = (1, 0)
    while exp:
        if exp & 1:
            result = gmod(gmul(result, base), mod)
        base = gmod(gmul(base, base), mod)
        exp >>= 1
    return result

normN = N_real*N_real + N_imag*N_imag

factors = list(factorint(normN).keys())
p, q = factors[0], factors[1]

phi = (p - 1) * (q - 1)
d = modinv(e, phi)

M_real, M_imag = gpow(C, d, N)

print("Decrypted Gaussian integer:")
print(M_real, "+", M_imag, "i")

msg = M_real - N_real

print(int(msg).to_bytes((msg.bit_length()+7)//8, "big"))
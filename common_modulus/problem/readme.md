# Guide: RSA Common Modulus Attack


## Prerequisites

To understand this attack, you need familiarity with:

1. **RSA Basics:** $c \equiv m^e \pmod N$
2. **Greatest Common Divisor (GCD):** 
3. **Bézout's Identity:** If $\gcd(x, y) = 1$, there exist integers $a$ and $b$ such that $ax + by = 1$
4. **Modular Inverse:** Calculating $x^{-1} \pmod N$

## Theory

We possess two equations:

1. $c_1 \equiv m^{e_1} \pmod N$
2. $c_2 \equiv m^{e_2} \pmod N$

If the two exponents $e_1$ and $e_2$ are coprime (i.e., $\gcd(e_1, e_2) = 1$), the Extended Euclidean Algorithm guarantees that we can find two integers, $a$ and $b$, satisfying:

$$a \cdot e_1 + b \cdot e_2 = 1$$

Since we know $c_1$ and $c_2$ are just powers of $m$, we can raise them to the powers of $a$ and $b$ respectively and multiply them:

$$(c_1)^a \cdot (c_2)^b \equiv (m^{e_1})^a \cdot (m^{e_2})^b \pmod N$$

By exponent laws, this simplifies to:

$$m^{a \cdot e_1} \cdot m^{b \cdot e_2} \equiv m^{(a \cdot e_1 + b \cdot e_2)} \pmod N$$

Substituting our identity ($ae_1 + be_2 = 1$):

$$m^1 \equiv m \pmod N$$

**Conclusion:** We recover $m$ directly.

### Handling Negative Coefficients

If your coefficient $a$ is negative:

1. Calculate the modular inverse of the ciphertext: $\text{inv} = c_1^{-1} \pmod N$
2. Raise this inverse to the absolute value of $a$: $\text{inv}^{|a|} \pmod N$


## Resources

- **Wolfram MathWorld: Bézout's Identity** - Understanding the core math behind the linear combination
  - https://mathworld.wolfram.com/BezoutsIdentity.html

- **Wikipedia: Common Modulus Attack** - A high-level overview of why reusing $N$ is dangerous
  - https://en.wikipedia.org/wiki/Common_modulus_attack

- **GeeksForGeeks: Extended Euclidean Algorithm** - Useful for implementing the GCD function
  - https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

- **CryptoHack: RSA Challenges** - Excellent practice problems
  - https://cryptohack.org/challenges/rsa/

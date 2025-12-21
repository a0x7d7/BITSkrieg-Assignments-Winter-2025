# Guide: RSA over Gaussian Integers Attack


## Prerequisites

To understand this attack, you need familiarity with:

1. **RSA Basics:** $c \equiv m^e \pmod N$, $m \equiv c^d \pmod N$
2. **Gaussian Integers:** The ring $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$
3. **Gaussian Norm:** For $z = a + bi$, the norm is $N(z) = a^2 + b^2$
4. **Gaussian Primes:** Primes in $\mathbb{Z}[i]$ that cannot be factored further

## Theory

This challenge implements RSA over Gaussian integers instead of regular integers. The admin believes using complex numbers makes it "twice as secure" — it doesn't.

### Gaussian Integer Arithmetic

In $\mathbb{Z}[i]$, we have:

- **Multiplication:** $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$
- **Division with remainder:** Uses the norm to find quotient and remainder
- **Modular exponentiation:** Standard square-and-multiply, adapted for Gaussian integers

### The Vulnerability

The key insight is that the **norm is multiplicative**:

$$N(z_1 \cdot z_2) = N(z_1) \cdot N(z_2)$$

For the Gaussian modulus $N = p \cdot q$ (where $p, q$ are Gaussian primes):

$$\text{norm}(N) = \text{norm}(p) \cdot \text{norm}(q)$$

### The Attack

1. Compute the norm of $N$: $\text{norm}(N) = N_{\text{real}}^2 + N_{\text{imag}}^2$
2. Factor the norm (a regular integer) to get $\text{norm}(p)$ and $\text{norm}(q)$
3. Compute the Euler totient analog: $\phi(N) = (\text{norm}(p) - 1)(\text{norm}(q) - 1)$
4. Compute the private key: $d \equiv e^{-1} \pmod{\phi(N)}$
5. Decrypt using Gaussian modular exponentiation: $m \equiv c^d \pmod N$

### Why This Works

The structure of the multiplicative group of units in $\mathbb{Z}[i]/(N)$ has order related to the norms of the prime factors. When $N = pq$ with Gaussian primes $p$ and $q$, the totient function becomes:

$$\phi(N) = (\text{norm}(p) - 1)(\text{norm}(q) - 1)$$

This is directly analogous to standard RSA where $\phi(N) = (p-1)(q-1)$.


## Resources

- **Wikipedia: Gaussian Integer** - Overview of the ring $\mathbb{Z}[i]$
  - https://en.wikipedia.org/wiki/Gaussian_integer

- **Gaussian Primes Visualization** - Understanding prime factorization in $\mathbb{Z}[i]$
  - https://mathworld.wolfram.com/GaussianPrime.html

- **Algebraic Number Theory** - Theoretical foundation for generalized RSA
  - https://en.wikipedia.org/wiki/Algebraic_number_theory

- **CryptoHack: RSA Challenges** - Excellent practice problems
  - https://cryptohack.org/challenges/rsa/
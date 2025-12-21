# Guide: RSA Wiener's Attack


## Prerequisites

To understand this attack, you need familiarity with:

1. **RSA Basics:** $c \equiv m^e \pmod N$, $m \equiv c^d \pmod N$
2. **Continued Fractions:** Representing rationals as $a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cdots}}$
3. **Convergents:** Successive rational approximations from a continued fraction
4. **Euler's Totient:** $\phi(N) = (p-1)(q-1)$ for $N = pq$

## Theory

Wiener's attack exploits RSA when the private exponent $d$ is small relative to $N$. The vulnerability arises from using a very large public exponent $e$.

We know the RSA key equation:

$$e \cdot d \equiv 1 \pmod{\phi(N)}$$

This means there exists some integer $k$ such that:

$$e \cdot d = k \cdot \phi(N) + 1$$

Rearranging:

$$\frac{e}{\phi(N)} = \frac{k}{d} + \frac{1}{d \cdot \phi(N)}$$

Since $\phi(N) \approx N$ for large primes, we have:

$$\frac{e}{N} \approx \frac{k}{d}$$

**Key Insight:** If $d < \frac{1}{3}N^{1/4}$, then $\frac{k}{d}$ appears as a convergent in the continued fraction expansion of $\frac{e}{N}$.

### The Attack

1. Compute the continued fraction expansion of $\frac{e}{N}$
2. For each convergent $\frac{k}{d}$:
   - Compute $\phi(N) = \frac{e \cdot d - 1}{k}$
   - Check if $\phi(N)$ yields valid factors of $N$ by solving:
     - $p + q = N - \phi(N) + 1$
     - $p \cdot q = N$
   - If the discriminant $(p+q)^2 - 4pq$ is a perfect square, we found $d$
3. Decrypt: $m \equiv c^d \pmod N$

### Why Large $e$ is Dangerous

A large $e$ implies a small $d$ (since $e \cdot d \equiv 1 \pmod{\phi(N)}$). When $d$ is small enough, the continued fraction method efficiently recovers it, completely breaking the encryption.


## Resources

- **Wikipedia: Wiener's Attack** - Detailed explanation of the attack and its bounds
  - https://en.wikipedia.org/wiki/Wiener%27s_attack

- **Dan Boneh's Original Paper** - "Twenty Years of Attacks on the RSA Cryptosystem"
  - https://crypto.stanford.edu/~dabo/pubs/papers/RSA-survey.pdf

- **Continued Fractions Tutorial** - Understanding the mathematical foundation
  - https://mathworld.wolfram.com/ContinuedFraction.html

- **CryptoHack: RSA Challenges** - Excellent practice problems
  - https://cryptohack.org/challenges/rsa/
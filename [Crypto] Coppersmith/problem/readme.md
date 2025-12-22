# Guide: Coppersmith's Attack (Partial Prime Leak)


## Prerequisites

To understand this attack, you need familiarity with:

1. **RSA Basics:** $c \equiv m^e \pmod N$, $N = p \cdot q$
2. **Lattice Reduction:** LLL algorithm for finding short vectors
3. **Polynomial Roots:** Finding small roots of polynomials modulo composites
4. **Bit Masking:** Understanding partial information leakage

## Theory

Coppersmith's attack recovers small roots of polynomials modulo a composite $N$ (or its unknown factors). When partial bits of a prime factor $p$ are leaked, we can model the unknown portion as a small root.

### The Setup

Given:
- Public modulus $N = p \cdot q$
- Partial knowledge of $p$: the top $k$ bits are known
- Unknown: the remaining $(n - k)$ bits of $p$

We can write:

$$p = p_{\text{hint}} + x$$

Where:
- $p_{\text{hint}}$ is the known high bits (shifted appropriately)
- $x$ is the unknown low bits, bounded by $|x| < 2^{n-k}$

### Coppersmith's Theorem

For a monic polynomial $f(x)$ of degree $\delta$ with a root $x_0$ modulo some factor $b \geq N^\beta$:

$$\text{If } |x_0| < N^{\beta^2/\delta} \text{, then } x_0 \text{ can be found efficiently}$$

For our case with $f(x) = p_{\text{hint}} + x$ (degree 1) and $p \approx N^{0.5}$:

$$|x| < N^{0.25}$$

This means we can recover $p$ if roughly **half or more** of its bits are known.

### The Attack

1. Construct polynomial $f(x) = p_{\text{hint}} + x$ over $\mathbb{Z}_N$
2. Apply Coppersmith's method (lattice-based) to find small roots
3. Recover $x_0$, compute $p = p_{\text{hint}} + x_0$
4. Factor $N$ and decrypt: $q = N/p$, then standard RSA decryption


## Resources

- **Original Paper:** Don Coppersmith, "Finding a Small Root of a Univariate Modular Equation"
  - https://link.springer.com/chapter/10.1007/3-540-68339-9_14

- **Wikipedia: Coppersmith's Attack** - High-level overview
  - https://en.wikipedia.org/wiki/Coppersmith%27s_attack

- **SageMath small_roots Documentation** - Implementation details
  - https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_modn_dense_ntl.html

- **CryptoHack: RSA Challenges** - Excellent practice problems
  - https://cryptohack.org/challenges/rsa/
<br><br><br>
> **Note:** Coppersmith's method is computationally intensive due to lattice reduction. SageMath is strongly recommended as it provides optimized implementations. Pure Python alternatives exist but are significantly slower.

## SageMath Quick Reference

### Installation

```bash
# Ubuntu/Debian
sudo apt install sagemath

# Or use Docker
docker run -it sagemath/sagemath

# Or use online: https://sagecell.sagemath.org/
```

### Running Sage Scripts

```bash
# Run a .sage file
sage script.sage

# Interactive mode
sage
```

### Key SageMath Commands

```python
# Modular arithmetic ring
Zmod(N)                    # Ring of integers mod N
GF(p)                      # Finite field of prime order p

# Polynomial rings
PR.<x> = PolynomialRing(Zmod(N))   # Univariate over Z_N
PR.<x,y> = PolynomialRing(ZZ)      # Multivariate over integers

# Polynomial operations
f = x^2 + 3*x + 1
f.roots()                  # Find roots in the base ring
f.small_roots(X=bound)     # Coppersmith's method for small roots

# Number theory
factor(n)                  # Factor an integer
gcd(a, b)                  # Greatest common divisor
xgcd(a, b)                 # Extended GCD: returns (g, s, t) where as + bt = g
inverse_mod(a, m)          # Modular inverse
power_mod(a, e, m)         # Modular exponentiation
is_prime(n)                # Primality test

# Matrix/Lattice operations
M = matrix(ZZ, [[1,2],[3,4]])
M.LLL()                    # LLL lattice reduction

# Type conversions
ZZ(x)                      # Convert to integer
int(x)                     # Convert to Python int
```

### `small_roots()` Parameters

| Parameter | Description |
|-----------|-------------|
| `X` | Upper bound on the root: $\|x\| < X$ |
| `beta` | Factor size: $p \geq N^\beta$ (use ~0.4-0.5 for balanced primes) |
| `epsilon` | Precision parameter (default 1/8; smaller = slower but more thorough) |


---


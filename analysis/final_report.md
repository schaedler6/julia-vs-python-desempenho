
# 📊 Final Report – Julia vs Python Performance

## 📁 Project Path
`J:\SCHAEDLER\Senac Gabriel 2025\Desempenho Julia Vs Python`

## 🎯 Objective
Compare the performance between Julia and Python in computational tasks involving:
- Matrix multiplication
- Prime number generation
- Monte Carlo simulation for estimating π

---

## 🧪 Tests Summary

| Test                          | Julia Time (s) | Python Time (s) | Julia RAM (MB) | Python RAM (MB) |
|-------------------------------|----------------|------------------|----------------|-----------------|
| Matrix Multiplication         | 1.02           | 2.10             | 231.57         | 314.22          |
| Prime Number Generation       | 0.0038         | 0.05             | 0.74           | 9.45            |
| Monte Carlo Simulation (π)    | 0.0083         | 0.15             | 0.03           | 11.03           |

---

## 📈 Analysis

Julia consistently outperformed Python across all three tests. The differences were especially noticeable in memory efficiency and execution speed for simple iterative tasks such as the Monte Carlo simulation and prime number generation.

### Key Findings:
- Julia’s Just-In-Time (JIT) compilation and built-in support for efficient numerical operations provide a significant advantage.
- Python's higher-level abstraction and interpreter overhead result in slower performance for tight-loop computations.

---

## 🧠 AI Insights Summary

> **Prompt:** "Why is Julia faster in matrix operations?"  
> **IA:** Julia uses optimized native libraries (BLAS/LAPACK) with minimal overhead.

> **Prompt:** "In which cases is Julia preferable over Python?"  
> **IA:** When performance and memory usage are critical, especially in scientific and numerical computing.

---

## ✅ Conclusion

Julia is the ideal choice for performance-critical and memory-sensitive mathematical tasks. Python remains valuable for its ecosystem and ease of use, but in computational benchmarks, Julia proves to be more efficient and scalable.

---

*Prepared by Sid Schaedler – April 2025*

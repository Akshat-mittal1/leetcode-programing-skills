# 🔍 LeetCode 1822 – Sign of the Product of an Array

| Item            | Value                                                                 |
|-----------------|------------------------------------------------------------------------|
| **Solved on**   | 10‑JULY‑2025                                                           |
| **Category**    | Easy                                                                   |
| **Topic Tags**  | Array, Math                                                            |
| **Problem Link**| [Sign of the Product of an Array](https://leetcode.com/problems/sign-of-the-product-of-an-array/) |

---

## 📄 Problem Statement

You are given an integer array `nums`. Let `product` be the product of all values in the array.

- Return `1` if `product > 0`.
- Return `-1` if `product < 0`.
- Return `0` if `product == 0`.

---

## 🧠 Approach

- Check if the array contains a `0`. If yes, return `0` immediately.
- Count the number of negative elements.
  - If the count is even, the product sign is **positive** → return `1`.
  - If the count is odd, the product sign is **negative** → return `-1`.
- No need to actually compute the product (saves time and prevents overflow).

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n), where `n` is the number of elements in the array
- **Space Complexity:** O(1), using only a constant `count` variable

---

## ✅ Example

```python
Input: nums = [-1, -2, -3, -4, 3, 2, 1]
Output: 1

Input: nums = [1, 5, 0, 2, -3]
Output: 0
```

## 👨‍💻 Author 🔗 **[Akshat Mittal](https://github.com/akshat-mittal1)**

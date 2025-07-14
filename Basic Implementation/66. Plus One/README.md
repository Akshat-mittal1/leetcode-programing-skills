
# 🔍 LeetCode 66 – Plus One

| Item            | Value                                                                 |
|-----------------|-----------------------------------------------------------------------|
| **Solved on**   | 09‑JULY‑2025                                                          |
| **Category**    | Easy                                                                  |
| **Topic Tags**  | Array, Math                                                           |
| **Problem Link**| [Plus One](https://leetcode.com/problems/plus-one/)                   |

---

## 📄 Problem Statement

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the i-th digit of the integer.

The digits are ordered from most significant to least significant.  
Add one to the integer and return the resulting array of digits.

You must return the result as an array of digits.

---

## 🧠 Approach

- Combine all digits into a full number.
- Increment the number by 1.
- Convert it back into a list of digits using division logic.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## ✅ Example

```python
Input:  digits = [1, 2, 3]
Output: [1, 2, 4]

Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

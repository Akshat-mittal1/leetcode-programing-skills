# 🔍 LeetCode 459 – Repeated Substring Pattern

| Item            | Value                                                                          |
|-----------------|--------------------------------------------------------------------------------|
| **Solved on**   | 09‑JULY‑2025                                                                   |
| **Category**    | Easy                                                                           |
| **Topic Tags**  | String, String Matching                                                        |
| **Problem Link**| [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) |

---

## 📄 Problem Statement

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Return `True` if it can be done, otherwise return `False`.

---

## 🧠 Approach

- Try all possible substring lengths from `len(s)//2` to 1.
- For each, check if it divides the length of `s` evenly.
- If yes, construct the string by repeating that substring and compare it to `s`.
- Return `True` if any match occurs, else `False`.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n²) – checking repeated concatenation
- **Space Complexity:** O(n) – for the constructed string

---

## ✅ Example

```python
Input: s = "abab"
Output: True
# Explanation: It's "ab" repeated twice.

Input: s = "aba"
Output: False
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

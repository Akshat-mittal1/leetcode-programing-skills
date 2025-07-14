# 🔍 LeetCode 28 – Find the Index of the First Occurrence in a String

| Item            | Value                                                                                 |
|-----------------|----------------------------------------------------------------------------------------|
| **Solved on**   | 08‑JULY‑2025                                                                          |
| **Category**    | Easy                                                                                  |
| **Topic Tags**   | String, Implementation                                                                 |
| **Problem Link** | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |

---

## 📄 Problem Statement

Given two strings `haystack` and `needle`, return the index of the **first occurrence** of `needle` in `haystack`, or `-1`  
if `needle` is not part of `haystack`.

---

## 🧠 Approach

- Check if `needle` is within `haystack` using Python’s `in`.
- If present, return `haystack.index(needle)`.
- Otherwise, return `-1`.

---

## ⏱️ Time & Space Complexity

**Time Complexity:** O(n × m) — worst-case substring search  
**Space Complexity:** O(1)

---

## ✅ Example

```python
Input:
haystack = "hello", needle = "ll"
Output: 2

Input:
haystack = "leetcode", needle = "leeto"
Output: -1

```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

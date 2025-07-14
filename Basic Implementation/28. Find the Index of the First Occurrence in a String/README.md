# 🔍 LeetCode 28 – Find the Index of the First Occurrence in a String

- 📅 Solved on: 8-JULY-2025  
- 🗂️ Category: Easy  
- 🏷️ Topic Tags: String, Implementation  
- 🔗 [Leetcode Problem Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

---

## 📄 Problem Statement

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

---

## 🧠 Approach

- Use Python's built-in string functions.
- Check if `needle` is in `haystack` using `in`.
- If found, return the index using `haystack.index(needle)`.
- Else, return `-1`.

---

## ⏱️ Time & Space Complexity

| Type   | Complexity     |
|--------|----------------|
| 🕒 Time | O(n * m) worst |
| 💾 Space | O(1)          |

---

## ✅ Example

**Input:**

```python
haystack = "hello"
needle = "ll"
Output: 2

```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

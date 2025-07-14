# 🔍 LeetCode 242 – Valid Anagram

| Item            | Value                                                                 |
|-----------------|------------------------------------------------------------------------|
| **Solved on**   | 08‑JULY‑2025                                                           |
| **Category**    | Easy                                                                   |
| **Topic Tags**  | String, Sorting                                                        |
| **Problem Link**| [Valid Anagram](https://leetcode.com/problems/valid-anagram/)         |

---

## 📄 Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## 🧠 Approach

- If lengths are not equal, return `False`.
- Sort both strings and compare.
- If sorted versions are equal, return `True`; else, `False`.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n log n) – due to sorting  
- **Space Complexity:** O(n) – for storing sorted characters

---

## ✅ Example

```python
Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

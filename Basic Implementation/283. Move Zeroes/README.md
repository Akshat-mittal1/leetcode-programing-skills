# 🔍 LeetCode 283 – Move Zeroes

| Item            | Value                                                                 |
|-----------------|-----------------------------------------------------------------------|
| **Solved on**   | 08‑JULY‑2025                                                          |
| **Category**    | Easy                                                                  |
| **Topic Tags**  | Array, Two Pointers, In-Place Algorithm                               |
| **Problem Link**| [Move Zeroes](https://leetcode.com/problems/move-zeroes/)             |

---

## 📄 Problem Statement

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note: You must do this **in-place** without making a copy of the array.

---

## 🧠 Approach

- Use a `change` pointer to mark the next position to place non-zero.
- Traverse the list, and whenever a non-zero is found, swap it to the correct position.
- In-place modification, no extra space used.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## ✅ Example

```python
Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Input: nums = [0]
Output: [0]
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

# 🔍 LeetCode 1768 – Merge Strings Alternately

| Item            | Value                                                             |
|-----------------|-------------------------------------------------------------------|
| **Solved on**   | 10‑JULY‑2025                                                      |
| **Category**    | Easy                                                              |
| **Topic Tags**  | String, Two Pointers                                              |
| **Problem Link**| [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) |

---

## 📄 Problem Statement

You are given two strings `word1` and `word2`.  
Merge them by alternating characters starting with `word1`.  
If one string is longer, append the remaining characters at the end.

---

## 🧠 Approach

- Loop through the characters up to the minimum length.
- Alternate appending characters from both strings.
- After the loop, append any remaining characters from the longer string.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n) where n is the total length of both strings
- **Space Complexity:** O(n) for the result string

---

## ✅ Example

```python
Input: word1 = "ab", word2 = "pqrs"
Process:
- Merge 'a' + 'p' → "ap"
- Merge 'b' + 'q' → "apbq"
- Append remaining "rs" → "apbqrs"

Output: "apbqrs"

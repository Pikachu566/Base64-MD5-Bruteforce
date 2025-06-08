# 🔐 Password Encoder, Decoder & MD5 Brute Force Tool

This Python script provides functions to:
- Encode password to Base64 format and MD5 hash
- Decode Base64 back to original password
- Perform brute force attack on MD5 hash (security test)

---

## ⚙️ Main Functions

### 1. Encode Password
- Input: Regular password
- Output:
- Base64 encoded string
- MD5 hash from Base64 string

### 2. Decode Base64
- Input: Base64 string
- Output: Original password

### 3. Brute Force MD5
- Input: MD5 hash
- Output: Original password if guessed (max length: 8 characters, combination of letters and numbers)

---

## ▶️ How to Use

1. Run the script:
```bash
python script.py
```

2. Select menu:
- 1: Encode Password
- 2: Decode Base64
- 3: Brute Force MD5
- 4: Exit

---

## 📌 Important Note

- The brute force function is only suitable for testing and learning.
- MD5 is not suitable for real security purposes because it is easy to guess or break.
- Do not use this tool for illegal activities.

---

## 🧪 Example

### Encode:
```
Input: admin123
Output:
Base64: YWRtaW4xMjM=
MD5: c3d1a6d226fd8b7c5d60b6b3ef9ad14d
```

### Decode:
```
Input: YWRtaW4xMjM=
Output: admin123
```

---

## 📄 License

This code is provided for learning and experimental purposes only. Use outside the responsibility of the creator.

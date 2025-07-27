# 🍪 Cookie Hijack Analyzer

> Detect insecure cookie flags (`HttpOnly`, `Secure`) in websites using Python.  
> Built for ethical hackers, bug bounty hunters, and security learners.

---

## 📝 Overview

`Cookie Hijack Analyzer` is a lightweight and easy-to-use Python script that helps detect potential session security issues in web applications. It inspects cookies set by a web server and checks whether they are configured with the `HttpOnly` and `Secure` flags — both critical to prevent cookie theft and session hijacking.

---

## 🔍 What It Does

- Sends a request to the given URL.
- Captures cookies returned in the HTTP response.
- Checks if each cookie has:
  - ✅ `HttpOnly` flag (prevents JavaScript access to cookies)
  - ✅ `Secure` flag (ensures cookie is only sent over HTTPS)
- Flags any cookie that is missing these attributes.

---

## 🎯 Use Cases

- Penetration testing
- Bug bounty recon
- Security audits
- Web development QA
- Cybersecurity education

---

## 🛠️ Built With

- Python 3.x
- `requests` (for HTTP handling)

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure Python 3 is installed.

### 📦 Installation

```bash
git clone https://github.com/yourusername/cookie-hijack-analyzer.git
cd cookie-hijack-analyzer
pip install -r requirements.txt

## 🚀 Overview

This project is a **Flask-based demographic intelligence API** built for Insighta Labs.

It enables clients to query a dataset of **2026 user profiles** using:

- Advanced filtering
- Sorting
- Pagination
- Natural language search (rule-based parser)

The goal is to help marketing and analytics teams efficiently explore demographic data.

---

## ⚙️ Features

### 🔍 Profile Query API

Supports filtering, sorting, and pagination.

```http
GET /api/profiles

Example:

/api/profiles?gender=male&country_id=NG&min_age=25&sort_by=age&order=desc&page=1&limit=10
🧠 Natural Language Search API (Core Feature)
GET /api/profiles/search?q=young males from nigeria

Converts plain English queries into structured filters using a rule-based parser (no AI/LLMs used).

🧠 Natural Language Parsing Approach

The parser works in 4 stages:

1. Input Normalization
Converts query to lowercase
Tokenizes words for matching
2. Keyword → Filter Mapping
👤 Gender Mapping
Keyword	Filter
male / males	gender = male
female / females	gender = female
🎂 Age Mapping
Keyword	Filter
young	min_age = 16, max_age = 24
teenager	age_group = teenager
adult	age_group = adult
senior	age_group = senior
above X	min_age = X

Example:

"females above 30"
→ gender=female + min_age=30
🌍 Country Mapping
Country	Code
Nigeria	NG
Kenya	KE
Uganda	UG
Angola	AO
United States	US

Example:

"people from kenya"
→ country_id=KE
3. Rule Combination Logic

All detected filters are combined using AND logic:

gender + age_group + country + age constraints

Example:

"young male adults from nigeria"
→ gender=male
→ age_group=adult
→ country_id=NG
→ age range applied (young override)
4. Response Handling

Success:

{
  "status": "success",
  "page": 1,
  "limit": 10,
  "total": 2026,
  "data": []
}

Error:

{
  "status": "error",
  "message": "Unable to interpret query"
}
📄 Pagination

Default:

page = 1
limit = 10
max limit = 50

Formula:

offset = (page - 1) * limit
🔃 Sorting

Supported fields:

age
created_at
gender_probability

Order:

asc
desc

Example:

sort_by=age&order=desc
⚠️ Limitations

This system uses a rule-based parser only, meaning:

❌ No AI/NLP model

It does not understand natural language context or grammar.

❌ Limited vocabulary

Only predefined keywords are supported:

young, adult, teenager, senior
male, female
predefined country names
❌ No fuzzy matching

Misspellings are not handled:

"nigera" ❌ not recognized
❌ No context awareness

Each request is independent (no memory).

❌ No advanced logic

Does not support:

OR conditions
NOT filters
nested queries
❌ Simplified “young” logic

Always maps to:

16–24
🧱 Tech Stack
Python 3.10+
Flask
Flask-SQLAlchemy
SQLite
Flask-CORS
📦 Data Seeding

The database is seeded using a provided dataset of 2026 profiles.

Source: Google Drive JSON file
Safe re-seeding supported (no duplicates after reset)
📌 Summary

This project demonstrates:

REST API design
Advanced query filtering
Pagination & sorting
Rule-based natural language processing
Scalable backend architecture without AI dependency
```

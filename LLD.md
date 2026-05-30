# Low Level Design (LLD)

## Project Structure

app/
├── api/
│   └── routes.py
├── preprocessing/
│   └── feature_engineering.py
├── services/
│   └── similarity_service.py
├── vector_search/
│   └── faiss_index.py
└── main.py

---

## Module Responsibilities

### feature_engineering.py

Responsibilities:
- Handle missing values
- Create combined text features
- Generate TF-IDF vectors
- Scale numerical features
- Create final feature matrix

Input:
- Product dataset

Output:
- Feature vectors

---

### faiss_index.py

Responsibilities:
- Build FAISS index
- Store vector embeddings
- Perform nearest neighbor search

Input:
- Feature matrix

Output:
- Similar product indices

---

### similarity_service.py

Responsibilities:
- Business logic layer
- Find similar products
- Retrieve product metadata

Input:
- Product ID
- Number of similar products

Output:
- Similar product IDs

---

### routes.py

Responsibilities:
- REST API endpoints
- Request validation
- Error handling

Endpoint:
GET /find_similar_products

---

### main.py

Responsibilities:
- FastAPI application startup
- Route registration
- Health checks
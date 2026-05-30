# High Level Design (HLD)

## Architecture

Dataset (.ldjson)
    ↓
Data Preprocessing
    ↓
Feature Engineering
    ↓
TF-IDF Vectorization
    ↓
FAISS Vector Index
    ↓
Similarity Service
    ↓
FastAPI REST API
    ↓
Swagger UI / Client

## Components

### Data Layer
- Loads product dataset
- Cleans missing values
- Selects important attributes

### Feature Engineering Layer
- TF-IDF on text columns
- Numeric feature scaling
- Combined feature vectors

### Search Layer
- FAISS index
- Similarity retrieval
- Top-K nearest neighbors

### API Layer
- FastAPI
- REST endpoints
- JSON response

### Deployment Layer
- Docker container
- Uvicorn server
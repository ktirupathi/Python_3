# Python System Design for ML Interviews

## 1. Design a feature engineering pipeline
### Problem statement
Create a production-oriented design for: design a feature engineering pipeline.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 2. Design a model training pipeline
### Problem statement
Create a production-oriented design for: design a model training pipeline.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 3. Design a batch inference system
### Problem statement
Create a production-oriented design for: design a batch inference system.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 4. Design a streaming inference system
### Problem statement
Create a production-oriented design for: design a streaming inference system.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 5. Design a data preprocessing framework
### Problem statement
Create a production-oriented design for: design a data preprocessing framework.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 6. Design a model versioning system
### Problem statement
Create a production-oriented design for: design a model versioning system.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 7. Design a logging framework
### Problem statement
Create a production-oriented design for: design a logging framework.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 8. Design an ML experiment tracker
### Problem statement
Create a production-oriented design for: design an ml experiment tracker.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 9. Design a scalable ETL pipeline
### Problem statement
Create a production-oriented design for: design a scalable etl pipeline.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

## 10. Design a REST API for ML model
### Problem statement
Create a production-oriented design for: design a rest api for ml model.
### Architecture diagram explanation
Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.
### Components
- API Gateway
- Orchestrator
- Feature Store
- Model Registry
- Metadata/Logging
- Monitoring and Alerting
### Python-based pseudo implementation
```python
class Pipeline:
    def run(self, payload):
        features = self.transform(payload)
        model = self.load_model()
        preds = model.predict(features)
        self.log(preds)
        return preds
```
### Scalability considerations
Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.
### Trade-offs
Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.
### Interview tips
Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).

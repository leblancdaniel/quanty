# quanty
A little quantitative finance application.  Detect potential market over-reactions.  The goal is to identify companies with a higher probability of unjustified losses (eventually also unjustified gains) given systematic & idiosyncratic information

If you find this helpful, consider buying me a coffee! :) https://buymeacoffee.com/dleblanc


# TODO:
- pull sample polygon data and use it for testing locally
- pull market data from Polygon.io Flat files (https://polygon.io/dashboard) and store it
- process data in batches, streams, or both, and store pre-processed data somewhere
- configure and setup services (Database, Docker, Kubernetes, ECR, )
- Define and codify criteria for over-reactions.  Provide list of candidate stocks.
- Log predictions and evaluate them across different time horizons (daily, weekly, monthly).  Track other metrics (alpha, sharpe ratio, etc.)
- Pull financials, earnings reports & questions, and competitor analysis.  Infer on them using combination of foundational models and heuristics.
- Try intra-day once ready

## Data
- Daily stock data (polygon.io)
- Fetch company financials, qualitative info


## Pipeline
- ingest large dataset (polars, numpy)
- Dataset versioning (DVC)
- train & backtest (Pytorch, JAX)
- LLMs & Chain of Thought (Claude, LangChain, ReAct)?
- Feature engineering & feaature store (Feast, Sagemaker)
- Model experimentation & Storage (MLFlow)
- Model Evaluation, Reporting, Logging (MLFlow, Prometheus, Grafana)

## Infrastructure & DevOps
- GitHub actions
- Terraform (Infra as code)
- AWS for storage, containers (Docker, ECR)
- Kubernetes (AWS EKS)
- Batch processing (Spark)
- Stream processing (Kafka)
- Structured Data in PostgreS
- Timeseries data in TS DB
- Blob storage in S3
- Cache (Redis)
- Payments (Stripe, Venmo)
- Integrations (Charles Schwab?)

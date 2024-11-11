# quanty
a little quantitative finance application.  Detect potential market over-reactions.

If you find this helpful, any contribution would be encouraging :) https://buymeacoffee.com/dleblanc


# TODO:
- pull market data from Alpha Vantage and store it
- process data in batches or in streams (or both) and store pre-processed data
- configure and setup services (Docker, Kubernetes, ECR, )
- Define and codify criteria for over-reactions.  Provide list of candidate stocks.
- Log predictions and evaluate them across different time horizons (intraday, daily, weekly, monthly).  Track other metrics (alpha, sharpe ratio, etc.)
- Pull financials, earnings reports & questions, and competitor analysis.  Infer on them using combination of foundational models and heuristics.

## Non-functional Requirements
- low-latency: must be fast, constantly streaming (build tests and simulations)
- scalable: need to process an entire market data (maybe start with a certain sub-set first)
- Highly consistent: data must be accurate.  Downtime means no trades, but uptime with incorrect data means risk of losses

## Data
- Stock data streams (Alpha Vantage API)
- Fetch company financials, qualitative info
- ID companies with higher probability of unjustified losses or gains given systematic & idiosyncratic information

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

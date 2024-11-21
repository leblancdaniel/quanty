# quanty
A little quantitative finance application.  Detect potential market over-reactions.  The goal is to identify companies with a higher probability of unjustified losses (eventually also unjustified gains) given systematic & idiosyncratic information

If you find this interesting, consider buying me a coffee! :) https://buymeacoffee.com/dleblanc


## Setup
Install the necessary requirements (python 3.12+, terraform, atlas).  To get the gist, create a polygon.io account and enter your API key in the .env file.  
- `terraform setup.tf` will create a PostgreSQL database instance in AWS, along with a generated password.  You'll need to save the password in the `.env` file so you can continue.  It also stores the state of your infrastructure locally in `.tfstate`
- `Atlas` manages the schema of our database, and works a lot like `terraform`, but for database schemas.  `setup.sh` runs the Atlas script to inspect the schema
- `python import_eod.py` will spend some time inserting EOD data into the database

# TODO:
- setup postgres instance, write scripts to create and destroy it
- process daily prices in batches using fireduck, store data somewhere 
- pull market data from Polygon.io Flat files (https://polygon.io/dashboard) and store it
- configure and setup services (Database, Docker, Kubernetes, ECR, )
- Define and codify criteria for over-reactions.  Provide list of candidate stocks.
- Log predictions and evaluate them across different time horizons (daily, weekly, monthly).  Track other metrics (alpha, sharpe ratio, etc.)
- Pull financials, earnings reports & questions, and competitor analysis.  Infer on them using combination of foundational models and heuristics.
- Try intra-day once ready

## Data
- Daily stock data (polygon.io)
- Fetch company financials, qualitative info

## Pipeline
- ingest & process large dataset (fireduck, numpy)
- Dataset versioning (DVC)
- train & backtest (Pytorch, JAX)
- LLMs & Chain of Thought (Claude, LangChain, ReAct)?
- Feature engineering & feaature store (Feast, Sagemaker)
- Model experimentation & Storage (MLFlow)
- Model Evaluation, Reporting, Logging (MLFlow, Prometheus, Grafana)

## Infrastructure & DevOps
- GitHub actions
- Terraform (Infra as code)
- Atlas (Schema as Code)
- AWS for storage, containers (Docker, ECR)
- Kubernetes (AWS EKS)
- Batch processing (Spark)
- Stream processing (Kafka)
- Structured Data in PostgreS
- Blob storage in S3
- Cache (Redis)
- Payments (Stripe, Venmo)
- Integrations (Charles Schwab?)

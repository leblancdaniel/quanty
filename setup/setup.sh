terraform init
terraform plan
terraform apply
atlas schema inspect -u postgres://postgres:h39HizDPUecVTat3cc6Nke0eD37xVD1c@devdb.cxa224ygyyzi.us-east-2.rds.amazonaws.com:5432/ --format {{ sql . }} > schema.sql
atlas migrate diff stocks_daily --dir "file://migrations" --to "file://schema.sql" --dev-url "docker://postgres/16/" --format "{{ sql . }}"
atlas migrate push quanty --dev-url "docker://postgres/16/"
atlas migrate apply --env local

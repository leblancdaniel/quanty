locals {
    postgres_identifier     = "devdb"
    postgres_name           = "devDB"
    postgres_user_name      = "postgres"
    postgres_port           = 5432
}

provider "aws" {
    region                   = "us-east-2"
    profile                  = "default"
    shared_credentials_files = ["$HOME/.aws/credentials"]
}

data "aws_vpc" "default" {
    default = true 
}

resource "random_string" "devDB_password" {
    length  = 32
    upper   = true 
    numeric = true 
    special = false 
}

resource "aws_security_group" "devDB_security_group" {
    vpc_id      = "${data.aws_vpc.default.id}"
    name        = "devDB_security_group"
    description = "Allow all inbound for Postgres"

    ingress {
        from_port   = local.postgres_port 
        to_port     = local.postgres_port 
        protocol    = "tcp"
        description = "PostgreSQL"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_db_instance" "devdb" {
    identifier              = local.postgres_identifier 
    db_name                 = local.postgres_name 
    instance_class          = "db.t4g.micro"
    allocated_storage       = 20
    engine                  = "postgres"
    engine_version          = "16.3"
    skip_final_snapshot     = true 
    publicly_accessible     = true 
    vpc_security_group_ids  = [aws_security_group.devDB_security_group.id]
    username                = local.postgres_user_name 
    password                = random_string.devDB_password.result
    storage_type            = "gp2"
    parameter_group_name    = "default.postgres16"
}
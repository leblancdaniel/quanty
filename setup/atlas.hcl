# The "local" environment represents our local testings.
env "local" {
  url = "postgres://postgres:h39HizDPUecVTat3cc6Nke0eD37xVD1c@devdb.cxa224ygyyzi.us-east-2.rds.amazonaws.com:5432/"
  migration {
    dir = "atlas://quanty"
  }
}
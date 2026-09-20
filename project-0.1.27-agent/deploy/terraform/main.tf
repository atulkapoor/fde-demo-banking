# Chosen because this environment has to be destroyed cleanly, which is
# the one thing a convergence tool cannot do.
terraform {
  required_version = ">= 1.5"
}

variable "environment" {
  type        = string
  description = "Name of this environment. Used in every resource name"
}

# Resources go here. Keep them in one module per environment so that
# `terraform destroy` takes exactly one environment away.

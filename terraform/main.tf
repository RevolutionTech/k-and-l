terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}

module "simple-static-website" {
  source = "github.com/RevolutionTech/opstrich//terraform/modules/simple-static-website"

  github_repo = "k-and-l"
  domain_name = "katrinaand.lucasconnors.com"
  error_page  = "404.html"

  tags = {
    Tool = "terraform"
    Repo = "RevolutionTech/k-and-l"
    Env  = "prod"
  }
}

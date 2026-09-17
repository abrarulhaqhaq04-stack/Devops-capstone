variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro" # free-tier eligible
}

variable "key_name" {
  description = "Name of an existing EC2 key pair for SSH access"
  type        = string
}

variable "docker_image" {
  description = "Docker Hub image to pull and run, e.g. yourusername/todo-api:latest"
  type        = string
}

variable "app_port" {
  description = "Port the app listens on inside the container"
  type        = number
  default     = 8000
}

variable "allowed_ssh_cidr" {
  description = "CIDR block allowed to SSH into the instance (use your IP/32 for safety)"
  type        = string
  default     = "0.0.0.0/0"
}

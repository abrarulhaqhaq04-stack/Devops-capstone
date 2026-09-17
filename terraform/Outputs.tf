output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.todo_api.public_ip
}

output "app_url" {
  description = "URL to access the running app"
  value       = "http://${aws_instance.todo_api.public_ip}:${var.app_port}/docs"
}

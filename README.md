# AWS-Model-Deployment
AWS-Model-Deployment(Text_classification-sentiment_Analysis)-Project

![Image](https://github.com/user-attachments/assets/da728b97-7af4-469e-a2f2-1090295b6dde)

## Movie Sentiment Analysis - AWS EC2 Deployment

### Project Overview

This project is designed to analyze the sentiment of movie reviews, determining whether they are positive or negative. The model is hosted on an AWS EC2 instance, allowing users to send review text and receive sentiment predictions.

### Prerequisites

Before setting up the deployment, make sure you have the following:

An AWS account

An EC2 instance running Ubuntu (20.04 or later)

A working knowledge of basic Linux commands

An open security group allowing access to necessary ports (such as 5000 for the API)

### Setting Up the EC2 Instance

To get started, launch an EC2 instance using the AWS Management Console. Choose Ubuntu as the operating system and select an appropriate instance type based on your project requirements. Configure the security settings to allow SSH access for remote connection and open additional ports for accessing the application.

Once the instance is running, connect to it using an SSH client. Before proceeding, update the system packages to ensure a smooth setup process.

### Deploying the Application

Begin by transferring the project files to your EC2 instance. Once inside the instance, create an isolated environment to manage dependencies efficiently. Install all necessary libraries to support the application, ensuring compatibility with the deployed model.

If the application relies on a database, apply necessary migrations to prepare the database structure. Finally, launch the application to confirm it is running correctly.

### Keeping the Application Running

To prevent the application from stopping when the SSH session ends, consider running it in the background. There are multiple ways to achieve this, including process management tools that keep applications active even after disconnection.

### Configuring Access

Security settings play a crucial role in deployment. Adjust firewall rules to permit external access to the application while ensuring unauthorized users cannot exploit vulnerabilities. Validate the setup by accessing the deployed service through a web browser or an API client.

### Optimizing for Production

For a more robust deployment, consider integrating a process manager to handle multiple requests efficiently. Additionally, using a reverse proxy enhances security and performance by managing incoming connections before they reach the application.

### Troubleshooting

If issues arise during deployment, check for missing dependencies or misconfigured security rules. If the application is unreachable, verify firewall settings and ensure the correct ports are open. For missing packages, reinstalling dependencies often resolves common issues.

### Conclusion

With everything set up, your Movie Sentiment Analysis application is now live on AWS EC2! You can now analyze movie reviews in real time and integrate this capability into larger projects or services.

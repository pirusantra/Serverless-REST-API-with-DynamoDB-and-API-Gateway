# Serverless-REST-API-with-DynamoDB-and-API-Gateway

I built and deployed a Serverless REST API that performs CRUD (Create, Read, Update, Delete) operations for managing a simple to-do list application. The backend is fully serverless using API Gateway, Lambda, and DynamoDB, and the frontend is a static HTML website hosted on S3.

# Technologies Used

Amazon API Gateway – Exposes REST endpoints for CRUD operations.

AWS Lambda – Handles API logic for creating, reading, updating, and deleting tasks.

Amazon DynamoDB – Stores tasks as a NoSQL database.

AWS IAM – Secures Lambda and DynamoDB access with least-privilege roles.

Amazon CloudWatch – Monitors API calls and Lambda execution logs.

Amazon S3 – Hosts the static HTML frontend for the to-do list.

## ⚙️ Deployment Steps
### 1️⃣ DynamoDB Table
- I created a DynamoDB table named TodoTable with id as the primary key.
- Configured on-demand capacity mode for automatic scaling.

### 2️⃣ Lambda Function
- I wrote a Python Lambda function (lambda_function.py) to handle all CRUD operations:
  - POST → Create a new task.
  - GET → Retrieve all tasks or a task by ID.
  - PUT → Update an existing task.
  - DELETE → Remove a task.

### 3️⃣ API Gateway
- I created a REST API in API Gateway.
- Configured endpoints:
  - POST /todos → Create task
  - GET /todos → Retrieve tasks
  - PUT /todos → Update task
  - DELETE /todos → Delete task

- Enabled CORS for the S3 frontend.
- Integrated each method with the Lambda function using Lambda Proxy Integration.

### 4️⃣ IAM Role
- I created a Lambda execution role with permissions to:
  - Read and write items from TodoTable.
  - Write logs to CloudWatch.
  - Attached this role to the Lambda function.

### 5️⃣ Frontend Deployment on S3
- I created a simple HTML frontend (index.html) with forms to add, update, and delete tasks.
- Hosted the HTML file on an S3 bucket with static website hosting enabled.
- Users can submit tasks without JavaScript; forms send POST requests directly to the API Gateway.
- Frontend Features:
  - Add Task (ID, Title, Status)
  - Update Task (Change title or status)
  - Delete Task (By ID)


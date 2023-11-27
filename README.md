# Book recommendation API

## Project Overview
Based on the 7k records dataset, API provides book recommendation based on the existing title or any description. 


## Features
- Book recommendation based on existing title
- Book recommendation based on any description


## Endpoints

Example:

- `GET /recommend_by_description/`: Recommends books based on a given description.
  - Parameters:
    - `description`: A string containing the user's book description or theme.
    - `num_recommendations` (optional): Number of book recommendations to return.
   
- `GET /recommend_by_title/`: Recommends similar books based on a given title.
  - Parameters:
    - `title`: A string containing the provided book title
    - `num_recommendations` (optional): Number of book recommendations to return.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Application
1. **Clone the Repository**:
```
git clone https://github.com/kshuryhin/fastApiProject.git
```
3. **Navigate to the Project Directory**:
```
cd fastApiProject
```
5. **Start the Application with Docker Compose**:
```
docker-compose up -d
```
This command pulls the necessary Docker image, builds the service, and starts the FastAPI application.

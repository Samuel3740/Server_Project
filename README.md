<<<<<<< HEAD
# Server_Project1


# 🐳 Docker-Based Test Server Environment

Welcome! This project outlines a Docker environment built for simple and efficient server application testing.

---

## 🖥️ Server Specifications

| Category | Details |
| :--- | :--- |
| **CPU** | Intel N100 |
| **RAM** | 16GB |
| **Storage** | 512GB ROM |
| **OS** | Ubuntu Server 22.04 LTS |

---

## 🚀 Purpose

| The primary goal of this server is to **rapidly test various applications using Docker**. By leveraging a containerized setup, each application is isolated, minimizing dependency conflicts and providing a consistent testing environment. |
| :--- |

---

## 🏗️ Docker Composition

The server environment consists of four containers, each with a specific role:

| 🐘 PostgreSQL Container |
| :--- |
| **Role**: Relational Database Server <br/> **Description**: Stores and manages data for `Container 1`. It is a reliable and powerful open-source database. |

| 🧠 Neo4j Container |
| :--- |
| **Role**: Graph Database Server <br/> **Description**: Stores data for `Container 2` as nodes and edges, enabling easy analysis of complex relationships. |

| 📦 Application Container 1 |
| :--- |
| **Connects to**: PostgreSQL <br/> **Description**: An application designed to perform specific business logic by communicating with the PostgreSQL database. |

| 📦 Application Container 2 |
| :--- |
| **Connects to**: Neo4j <br/> **Description**: An application that processes relationship-based data by communicating with the Neo4j graph database. |

---

## 🚀 Setup & Usage

Follow the steps below to set up the environment and run the application.

```bash
# --- Step 1: Install Docker (if not already installed) ---
# Update server packages
sudo apt-get update && sudo apt-get upgrade -y

# Run the Docker installation script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
echo "Docker installation complete!"


# --- Step 2: Run the Application using Docker Compose ---
# Start all containers in the background
docker-compose up -d

# Check the running containers
docker ps

# View logs (e.g., for container1)
docker-compose logs -f [service_name_for_container_1]
=======
# Server_Project
Multi-project development setup on Ubuntu Server 22.04 LTS using Docker and various backend tools.
>>>>>>> ba844d090c9ad24a710507d17e23d01bd7a50f41

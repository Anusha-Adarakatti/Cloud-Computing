# Registration App Deployment Using Ansible

## 📦 Project Overview

This project automates the deployment of a full-stack registration web application using **Ansible**. It sets up:

- A **Node.js** backend (`app.js`)
- A **MongoDB** database
- An **NGINX** server to serve frontend files and act as a reverse proxy

Everything is deployed automatically using a single Ansible playbook.

---

## 📁 File Structure

```text
registration-app/
├── ansible/
│   ├── inventory
│   ├── playbook.yml
│   └── files/
│       ├── index.html
│       ├── style.css
│       └── app.js
├── README.md
```
## ⚙️ Prerequisites and Package Installation

### 1. Update and upgrade system packages
```text
sudo apt update && sudo apt upgrade -y
```
### 2. Install required packages
```text
sudo apt install -y curl gnupg
sudo apt install -y ansible nodejs npm nginx ufw
```
## 🍃 MongoDB Installation (Ubuntu 22.04/24.04 compatible)
### 1. Import MongoDB public key
```text
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
```
### 2. Add MongoDB repo (use jammy for 24.04)
```text
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
```
### 3. Reload package list
```text
sudo apt update
```
### 4. Install MongoDB
```text
sudo apt install -y mongodb-org
```
### 5. Start and enable MongoDB service
```text
sudo systemctl start mongod
sudo systemctl enable mongod
```
### 6. (Optional) Install mongosh if missing
```text
sudo apt install -y mongodb-mongosh
```
## 🔥 Start & Enable NGINX
```text
sudo systemctl start nginx
sudo systemctl enable nginx
```
## 🔐 Enable UFW Firewall and Allow Ports
```text
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw allow 3000/tcp     # Node.js
sudo ufw allow 27017/tcp    # MongoDB
sudo ufw enable
```
## Check status:
```text
sudo ufw status
```
## ▶️ Running the Ansible Playbook
### 1. Move to the ansible directory
```text
cd registration-app/ansible
```
### 2. Run the playbook
```text
ansible-playbook -i inventory playbook.yml --ask-become-pass
```
### This will:

#### Install missing packages

#### Copy frontend files

#### Deploy the backend app

#### Start all required services

## ✅ Validating the Deployment
### 1. Check all services
```text
sudo systemctl status mongod
sudo systemctl status nginx
ps aux | grep node
```
### 2. Test the frontend and backend
```text
curl http://localhost

curl -X POST http://localhost:3000/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Anusha","email":"anusha@example.com"}'
  ```
### 3. Check MongoDB entries
```text
mongosh

use registration
db.users.find().pretty()
```
## 🛑 Stopping the Services
### Stop MongoDB and NGINX

```text
sudo systemctl stop mongod
sudo systemctl stop nginx
```
### Kill Node.js manually (if pkill fails)
```text
ps aux | grep node
sudo kill <PID>
```
#### Or try:
```text
pkill node
```
## 🔁 Restarting the Services
### Start MongoDB and NGINX
```text
sudo systemctl start mongod
sudo systemctl start nginx
```
### Start Node.js manually
```text
node /path/to/app.js &
```
### Or simply rerun:

```text
ansible-playbook -i inventory playbook.yml --ask-become-pass
```
## 🧪 Troubleshooting
### Mongo not starting?
### Check logs:
```text
sudo journalctl -u mongod
```
### Node not killed?
### Use:

```text
ps aux | grep node
sudo kill <PID>
```
### NGINX errors?
### Check:

```text
sudo tail -f /var/log/nginx/error.log
```
### Playbook fails to gather facts?
### Use: --ask-become-pass

### Firewall issues?
### Run sudo ufw status to ensure ports are open.

## 📌 Notes
### Node.js should ideally run as a service or using PM2 for persistence.

### This project is for learning Ansible and basic app deployment. For production use, add process managers, log rotation, health checks, etc.

## 👩‍💻 Author
### Anusha Adarakatti
### Registration App Deployment with Ansible
### May 2025
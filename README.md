# HRMS Lite -- Frontend

HRMS Lite Frontend is a React-based web application built using Vite.\
It connects to a FastAPI backend to manage employees and track
attendance records.

------------------------------------------------------------------------

## 🚀 Tech Stack

-   React (Vite)
-   React Router DOM
-   Axios
-   Netlify (Deployment)

------------------------------------------------------------------------

## 📌 Prerequisites

Before running this project locally, make sure you have:

-   Node.js (v16 or higher recommended)
-   npm (comes with Node.js)

To verify installation:

node -v npm -v

------------------------------------------------------------------------

# 💻 Installation & Setup (Run Locally)

## 1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git cd
YOUR_REPO_NAME

------------------------------------------------------------------------

## 2️⃣ Install Dependencies

npm install

------------------------------------------------------------------------

## 3️⃣ Configure Backend API URL

Open:

src/services/api.js

If backend is running locally:

baseURL: "http://127.0.0.1:8000/api"

If using deployed backend:

baseURL: "https://fstbck-production.up.railway.app/api"

------------------------------------------------------------------------

## 4️⃣ Start Development Server

npm run dev

Open in browser:

http://localhost:5173/

------------------------------------------------------------------------

# 🏗 Production Build

npm run build

To preview production build:

npm run preview

------------------------------------------------------------------------

# 🌍 Deployment

For React Router support, add a file inside public folder named
`_redirects` with:

/\* /index.html 200

------------------------------------------------------------------------

# ✅ Features

-   View all employees\
-   Add new employee\
-   Delete employee\
-   Mark attendance\
-   View attendance records\
-   Integrated with FastAPI backend

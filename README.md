# Django E-commerce Website

A full-stack **e-commerce website** built using **Django**, **HTML**, and **CSS**, featuring dynamic product listings, responsive design, and a seamless shopping experience.

---

## 🌟 Features

- ✅ Dynamic product catalog with categories  
- ✅ Product detail pages with descriptions and images  
- ✅ Responsive design for mobile and desktop  
- ✅ Shopping cart functionality  
- ✅ User authentication (login/signup)  
- ✅ Checkout process (basic implementation)  
- ✅ Admin dashboard to manage products  

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS 
- **Backend:** Django (Python)  
- **Database:** MySQL 
- **Authentication:** Django built-in authentication system  

---

## 📂 Project Structure

ecommerce_project/
│
├── ecommerce_app/ # Django app for main functionality
│ ├── templates/ # HTML templates
│ ├── static/ # CSS, JS, images
│ ├── models.py # Database models
│ ├── views.py # Views & logic
│ └── urls.py # App routes
│
├── ecommerce_project/ # Project settings
│ └── settings.py
│
├── manage.py # Django management commands


---

## 🚀 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. **Create virtual environment and activate:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4.** Apply migrations:**
```bash
python manage.py migrate
```

5. **Run the development server:**
```bash
python manage.py runserver
```

🧑‍💻 Usage

Add items to the shopping cart
Sign up / log in as a user
Checkout items (basic checkout functionality)
Admin can log in to manage products

📌 Future Improvements

Payment gateway integration (Stripe, PayPal)
Order history & user profile
Advanced search & filtering
Responsive enhancements & animations
Review and rating system

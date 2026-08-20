## ✨ Features

### Authentication

* User registration
* Login / Logout
* Custom User model
* Role-based access
* Profile
* Avatar
* Preferred language
* Password management

### User Roles

Platformada 3 xil asosiy role mavjud:

* **Admin**
* **Teacher**
* **Student**

### Admin

Admin:

* Teacher yaratadi
* Userlarni boshqaradi
* Category yaratadi
* Course'larni moderatsiya qiladi
* Course'ni approve/reject qiladi
* Orderlarni ko‘radi
* Platformani boshqaradi

### Teacher

Teacher'ni faqat Admin yaratadi.

Teacher:

* Course yaratadi
* Category tanlaydi
* Course'ga lessons qo‘shadi
* Course ma'lumotlarini tahrirlaydi
* Course'ni approval uchun yuboradi
* O‘z kurslariga yozilgan studentlarni ko‘radi
* Student progressini ko‘radi

### Student

Student:

* Register qiladi
* Course'larni ko‘radi
* Search va filter qiladi
* Course sotib oladi
* Course'ga enrollment qilinadi
* Lessonlarni o‘qiydi
* Lessonlarni complete qiladi
* Progressni ko‘radi
* Like bosadi
* Comment yozadi
* Comment'ga reply beradi
* Course'ni bookmark qiladi
* Notification oladi
* Tilni o‘zgartiradi

---

# 🌍 Multilingual Support

StudyHub 3 ta tilni qo‘llab-quvvatlaydi:

* 🇺🇿 Uzbek
* 🇬🇧 English
* 🇷🇺 Russian

Loyihada ikki xil translation system mavjud.

### UI Translation

Django i18n orqali:

* Navbar
* Buttons
* Forms
* Messages
* Validation messages
* System text

tarjima qilinadi.

Ishlatiladi:

```text
gettext
gettext_lazy
{% translate %}
{% blocktranslate %}
```

### Database Content Translation

Course va Lesson kontenti alohida translation model orqali saqlanadi.

Masalan:

```text
Course
├── CourseTranslation (uz)
├── CourseTranslation (en)
└── CourseTranslation (ru)
```

---

# 🏗️ Architecture

```text
                    Browser
                       │
                       ▼
              Django Templates
                       │
                     HTMX
                       │
                       ▼
                    Django
                   /      \
                  /        \
                 ▼          ▼
          PostgreSQL       Redis
                             │
                             ▼
                           Celery
```

Application server:

```text
Django
```

Database:

```text
PostgreSQL
```

Cache / Celery broker:

```text
Redis
```

Background tasks:

```text
Celery
Celery Beat
```

Frontend interaction:

```text
HTMX
```

Containerization:

```text
Docker
Docker Compose
```

---

# 🛠️ Tech Stack

| Technology               | Purpose                    |
| ------------------------ | -------------------------- |
| Python                   | Programming language       |
| Django                   | Backend / Web framework    |
| PostgreSQL               | Database                   |
| HTMX                     | Dynamic server-rendered UI |
| Redis                    | Cache / Celery broker      |
| Celery                   | Background tasks           |
| Celery Beat              | Scheduled tasks            |
| Docker                   | Containerization           |
| Django Templates         | Frontend rendering         |
| Bootstrap / Tailwind     | UI                         |
| WhiteNoise               | Static files               |
| Django i18n              | Internationalization       |
| pytest / Django TestCase | Testing                    |
| Git                      | Version control            |
| GitHub                   | Collaboration / repository |

---

# 📦 Project Structure

```text
StudyHub/
│
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   │
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   │
│   ├── accounts/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   ├── courses/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   ├── orders/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   ├── learning/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   ├── interactions/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   └── notifications/
│       ├── migrations/
│       ├── models.py
│       ├── urls.py
│       ├── views.py
│       └── tests.py
│
├── templates/
│   ├── base.html
│   │
│   ├── accounts/
│   ├── courses/
│   ├── orders/
│   ├── learning/
│   ├── interactions/
│   ├── notifications/
│   │
│   └── components/
│       ├── navbar.html
│       ├── course_card.html
│       ├── pagination.html
│       ├── toast.html
│       └── loading.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── locale/
│   ├── uz/
│   │   └── LC_MESSAGES/
│   │       ├── django.po
│   │       └── django.mo
│   │
│   ├── ru/
│   │   └── LC_MESSAGES/
│   │
│   └── en/
│       └── LC_MESSAGES/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🗃️ Database Models

## User

```text
User
├── id
├── email
├── username
├── first_name
├── last_name
├── role
├── is_active
├── is_staff
└── date_joined
```

Roles:

```text
ADMIN
TEACHER
STUDENT
```

---

## Profile

```text
Profile
├── user
├── avatar
├── bio
├── preferred_language
└── created_at
```

Languages:

```text
uz
en
ru
```

---

## Category

```text
Category
├── id
├── name
├── slug
├── created_at
└── updated_at
```

Category'ni Admin boshqaradi.

---

## Course

```text
Course
├── id
├── teacher
├── category
├── slug
├── price
├── thumbnail
├── level
├── status
├── created_at
└── updated_at
```

Status:

```text
DRAFT
PENDING
PUBLISHED
REJECTED
ARCHIVED
```

Course workflow:

```text
Teacher creates course
        ↓
      DRAFT
        ↓
     PENDING
        ↓
   Admin Review
      ↙   ↘
 APPROVED  REJECTED
    ↓
 PUBLISHED
```

---

## CourseTranslation

```text
CourseTranslation
├── course
├── language
├── title
├── description
└── requirements
```

Constraint:

```text
Unique(course, language)
```

---

## Lesson

```text
Lesson
├── id
├── course
├── order
├── duration
├── video
├── is_free
├── created_at
└── updated_at
```

---

## LessonTranslation

```text
LessonTranslation
├── lesson
├── language
├── title
└── description
```

Constraint:

```text
Unique(lesson, language)
```

---

# 💳 Order

```text
Order
├── id
├── user
├── total_amount
├── status
├── payment_method
├── created_at
└── paid_at
```

Statuses:

```text
PENDING
PAID
CANCELLED
REFUNDED
```

---

# 🛒 OrderItem

```text
OrderItem
├── id
├── order
├── course
├── price
└── created_at
```

Course price OrderItem'da ham saqlanadi.

Bu tarixiy purchase price'ni saqlash uchun kerak.

---

# 🎯 Enrollment

```text
Enrollment
├── id
├── user
├── course
├── status
├── enrolled_at
└── completed_at
```

Statuses:

```text
ACTIVE
COMPLETED
CANCELLED
```

Constraint:

```text
Unique(user, course)
```

Enrollment faqat Order `PAID` bo‘lgandan keyin yaratiladi.

---

# 📊 LessonProgress

```text
LessonProgress
├── id
├── user
├── lesson
├── is_completed
├── completed_at
└── updated_at
```

Constraint:

```text
Unique(user, lesson)
```

Course progress:

```text
completed_lessons / total_lessons * 100
```

---

# ❤️ Like

```text
Like
├── id
├── user
├── course
└── created_at
```

Constraint:

```text
Unique(user, course)
```

---

# 💬 Comment

```text
Comment
├── id
├── user
├── course
├── parent
├── content
├── created_at
└── updated_at
```

`parent` self-referencing ForeignKey orqali comment reply qilish imkonini beradi.

---

# 🔖 Bookmark

```text
Bookmark
├── id
├── user
├── course
└── created_at
```

Constraint:

```text
Unique(user, course)
```

---

# 🔔 Notification

```text
Notification
├── id
├── recipient
├── sender
├── notification_type
├── course
├── comment
├── is_read
└── created_at
```

Notification types:

```text
COURSE_LIKED
COMMENT_ADDED
COMMENT_REPLIED
COURSE_APPROVED
COURSE_REJECTED
PAYMENT_SUCCESS
COURSE_COMPLETED
```

---

# ⚡ HTMX Features

HTMX quyidagi funksiyalarda ishlatiladi:

```text
Live search
Course filtering
Pagination
Like / Unlike
Bookmark / Unbookmark
Course enrollment
Comment creation
Comment reply
Comment deletion
Lesson completion
Progress update
Notification read
```

Example:

```text
Browser
   │
   │ HTMX POST
   ▼
Django View
   │
   ▼
Database
   │
   ▼
HTML Partial
   │
   ▼
HTMX updates DOM
```

Page reload qilinmaydi.

---

# 🔎 Search & Filtering

Course list quyidagilar bo‘yicha filter qilinadi:

* Search
* Category
* Level
* Price
* Language

Sorting:

```text
Newest
Oldest
Most popular
Price low → high
Price high → low
```

Search va filter HTMX orqali ishlaydi.

---

# 🔔 Notifications

Notificationlar real-time emas, lekin HTMX yordamida interaktiv boshqariladi.

Masalan:

```text
🔔 Notifications (3)
```

User notificationni ochadi:

```text
Unread → Read
```

va notification counter sahifani refresh qilmasdan yangilanadi.

---

# 🧠 Redis

Redis quyidagilar uchun ishlatiladi:

### Cache

```text
Popular courses
Categories
Frequently requested course data
```

### Celery Broker

```text
Django
   ↓
Celery
   ↓
Redis
   ↓
Worker
```

---

# ⏰ Celery

Background tasks:

* Enrollment email
* Payment confirmation
* Course approval notification
* Weekly learning summary
* Old notification cleanup

---

# 🕐 Celery Beat

Scheduled tasks:

```text
Every week
    ↓
Generate learning summary

Every day
    ↓
Cleanup old notifications
```

---

# 🐳 Docker

Services:

```text
web
db
redis
celery
celery-beat
```

Architecture:

```text
                 ┌─────────────┐
                 │   Browser   │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │    Django   │
                 │     web     │
                 └──────┬──────┘
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
       ┌─────────────┐     ┌─────────────┐
       │ PostgreSQL  │     │    Redis    │
       └─────────────┘     └──────┬──────┘
                                  │
                         ┌────────┴────────┐
                         ▼                 ▼
                    ┌─────────┐      ┌────────────┐
                    │ Celery  │      │Celery Beat │
                    └─────────┘      └────────────┘
```

---

# 🚀 Installation

## Requirements

Local development uchun:

* Git
* Docker
* Docker Compose

Python va PostgreSQL'ni host mashinaga alohida o‘rnatish shart emas.

---

# 📥 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/studyhub.git
```

Repository'ga o'ting:

```bash
cd studyhub
```

---

# 🔐 2. Environment Variables

`.env.example` faylidan `.env` yarating:

```bash
cp .env.example .env
```

`.env`:

```env
DEBUG=True

SECRET_KEY=change-me

POSTGRES_DB=studyhub
POSTGRES_USER=studyhub
POSTGRES_PASSWORD=studyhub_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_URL=redis://redis:6379/1

EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
```

> `.env` faylini hech qachon GitHub'ga commit qilmang.

---

# 🐳 3. Start Docker

Barcha containerlarni build qilish:

```bash
docker compose build
```

Ishga tushirish:

```bash
docker compose up
```

Background mode:

```bash
docker compose up -d
```

Logs:

```bash
docker compose logs -f
```

Faqat Django logs:

```bash
docker compose logs -f web
```

Celery logs:

```bash
docker compose logs -f celery
```

Redis logs:

```bash
docker compose logs -f redis
```

---

# 🗄️ 4. Run Migrations

```bash
docker compose exec web python manage.py migrate
```

---

# 👑 5. Create Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

Username, email va password kiriting.

Admin panel:

```text
http://localhost:8000/admin/
```

---

# 📦 6. Collect Static Files

Development:

```bash
docker compose exec web python manage.py collectstatic --noinput
```

WhiteNoise production static filesni servis qilishda yordam beradi.

---

# 🌍 7. Compile Translations

Translation fayllarini yaratish:

```bash
docker compose exec web python manage.py makemessages -l uz
docker compose exec web python manage.py makemessages -l ru
docker compose exec web python manage.py makemessages -l en
```

`.po` fayllarini tarjima qilgandan keyin:

```bash
docker compose exec web python manage.py compilemessages
```

> `*.po` fayllari GitHub'ga commit qilinadi. Generated `*.mo` fayllari repository policy'ga qarab ignore qilinishi mumkin.

---

# 🌐 8. Open Application

Brauzerda:

```text
http://localhost:8000/
```

Admin:

```text
http://localhost:8000/admin/
```

---

# 🧪 9. Run Tests

Django TestCase:

```bash
docker compose exec web python manage.py test
```

Agar pytest ishlatilsa:

```bash
docker compose exec web pytest
```

Coverage:

```bash
docker compose exec web coverage run -m pytest
docker compose exec web coverage report
```

---

# 🛠️ Useful Django Commands

Create migrations:

```bash
docker compose exec web python manage.py makemigrations
```

Apply migrations:

```bash
docker compose exec web python manage.py migrate
```

Open Django shell:

```bash
docker compose exec web python manage.py shell
```

Check project:

```bash
docker compose exec web python manage.py check
```

Create superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

Collect static:

```bash
docker compose exec web python manage.py collectstatic
```

---

# 🐘 PostgreSQL

PostgreSQL containeriga kirish:

```bash
docker compose exec db psql -U studyhub -d studyhub
```

Database'ni ko‘rish:

```sql
\dt
```

PostgreSQL'dan chiqish:

```sql
\q
```

---

# 🔴 Redis

Redis containeriga kirish:

```bash
docker compose exec redis redis-cli
```

Redis test:

```text
PING
```

Expected:

```text
PONG
```

---

# 🧵 Celery

Celery worker:

```bash
docker compose exec celery celery -A config worker -l INFO
```

Agar Celery alohida Docker service sifatida ishga tushayotgan bo‘lsa, bu commandni qo‘lda bajarish shart emas.

Celery Beat:

```bash
docker compose exec celery-beat celery -A config beat -l INFO
```

---

# 🧹 Stop Project

Containerlarni to‘xtatish:

```bash
docker compose down
```

Containerlar va volumes bilan to‘xtatish:

```bash
docker compose down -v
```

> `-v` PostgreSQL ma'lumotlarini ham o‘chirishi mumkin. Developmentda ehtiyotkorlik bilan ishlating.

---

# 🔄 Rebuild Project

Dependency yoki Docker configuration o‘zgarganda:

```bash
docker compose down
docker compose build --no-cache
docker compose up
```

---

# 🌱 Git Workflow

Project feature-based Git workflow'dan foydalanadi.

Main branches:

```text
main
develop
```

Feature branches:

```text
feature/authentication
feature/course-management
feature/lessons
feature/orders
feature/enrollment
feature/htmx
feature/notifications
feature/i18n
feature/redis-celery
feature/testing
```

Bug fixes:

```text
fix/course-permission
fix/enrollment
fix/notification-counter
```

Refactoring:

```text
refactor/course-queryset
refactor/notification-service
```

---

# 📝 Commit Convention

Commitlar ma'noli bo‘lishi kerak.

Examples:

```bash
git commit -m "feat: add custom user model"
git commit -m "feat: implement course translations"
git commit -m "feat: add teacher course management"
git commit -m "feat: implement course enrollment"
git commit -m "feat: add HTMX bookmark"
git commit -m "fix: prevent duplicate enrollment"
git commit -m "fix: restrict teacher course access"
git commit -m "refactor: optimize course queryset"
git commit -m "test: add enrollment tests"
git commit -m "docs: update README"
```

---

# 🔀 Feature Development Workflow

Yangi feature uchun:

```bash
git checkout develop
git pull origin develop
```

Branch yaratish:

```bash
git checkout -b feature/course-management
```

Development:

```bash
git add .
git commit -m "feat: implement course management"
```

Push:

```bash
git push -u origin feature/course-management
```

Keyin GitHub'da:

```text
feature/course-management
            ↓
         Pull Request
            ↓
          develop
```

Testlardan keyin:

```text
develop
   ↓
   main
```

---

# 🔐 Security

Secrets Git repository'ga joylanmaydi.

Ignore qilinadigan fayllar:

```text
.env
*.pem
*.key
secrets.json
```

Repository'da faqat:

```text
.env.example
```

bo‘ladi.

`.env.example` real password yoki secretlarni o‘z ichiga olmaydi.

---

# 🧪 Testing Strategy

Critical business logic test qilinadi.

### Authentication

* User registration
* Login
* Logout
* Permissions

### Teacher

* Teacher course yaratishi
* Faqat o‘z course'ini edit qilishi
* Course approval workflow

### Student

* Course sotib olish
* Duplicate enrollment
* Purchased course access
* Lesson progress

### Interactions

* Like
* Unlike
* Comment
* Reply
* Bookmark

### Notifications

* Notification creation
* Read/unread
* Permission

### Multilingual

* UI translations
* Course translations
* Lesson translations

---

# 📈 Future Improvements

Kelajakda quyidagilar qo‘shilishi mumkin:

* Real payment integration
* Stripe
* Click
* Payme
* Course certificates
* Video streaming
* Instructor dashboard
* Student dashboard
* Course ratings
* Wishlist
* Coupons
* Advanced analytics
* Elasticsearch
* S3-compatible storage
* Nginx
* Gunicorn
* CI/CD
* GitHub Actions
* Production deployment
* Monitoring
* Error tracking

---

# 🎯 Project Goals

StudyHub quyidagi bilimlarni amaliy tarzda mustahkamlash uchun yaratilmoqda:

* Django architecture
* Custom User
* Django ORM
* PostgreSQL
* Database relationships
* Transactions
* Permissions
* Authentication
* Django Templates
* HTMX
* Multilingual applications
* Redis
* Celery
* Celery Beat
* Docker
* Testing
* Git
* GitHub
* Feature branches
* Pull Requests
* Code review
* Production configuration

---

# 🏆 Learning Objectives

Project yakunida developer quyidagilarni mustaqil bajara olishi kerak:

```text
Create a Django project
        ↓
Design database models
        ↓
Implement authentication
        ↓
Implement role-based permissions
        ↓
Build multilingual content
        ↓
Build dynamic HTMX interfaces
        ↓
Implement course purchasing
        ↓
Implement enrollment
        ↓
Track learning progress
        ↓
Implement notifications
        ↓
Use Redis
        ↓
Run background tasks with Celery
        ↓
Containerize with Docker
        ↓
Write tests
        ↓
Work with Git/GitHub
        ↓
Deploy the application
```

---

# 👨‍💻 Development Principles

StudyHub development follows these principles:

* Keep business logic maintainable
* Use meaningful model relationships
* Avoid unnecessary JavaScript
* Prefer HTMX for simple dynamic interactions
* Use reusable Django template components
* Optimize database queries
* Prevent N+1 queries
* Validate permissions at the backend
* Use transactions for critical operations
* Write tests for important business logic
* Keep secrets outside Git
* Use meaningful commits
* Work with feature branches
* Review code through Pull Requests
* Keep documentation updated

---

# 📄 License

This project is created for educational and portfolio purposes.

---

# 👨‍💻 Author

**Ilhomjon**

Python Backend Developer

GitHub:

`https://github.com/ilhomjondevuz`

---

## 🚀 Quick Start

Agar projectni faqat tez ishga tushirmoqchi bo‘lsangiz:

```bash
git clone https://github.com/YOUR_USERNAME/studyhub.git

cd studyhub

cp .env.example .env

docker compose up --build -d

docker compose exec web python manage.py migrate

docker compose exec web python manage.py createsuperuser

docker compose exec web python manage.py collectstatic --noinput
```

Keyin:

```text
http://localhost:8000/
```

Admin:

```text
http://localhost:8000/admin/
```

---

## 📌 Development Status

```text
🚧 Project Status: In Development
```

Current development milestones:

```text
[ ] Project setup
[ ] Docker
[ ] PostgreSQL
[ ] Custom User
[ ] Authentication
[ ] Teacher management
[ ] Categories
[ ] Courses
[ ] Course translations
[ ] Lessons
[ ] Lesson translations
[ ] Orders
[ ] Enrollment
[ ] Lesson progress
[ ] HTMX interactions
[ ] Comments
[ ] Likes
[ ] Bookmarks
[ ] Notifications
[ ] Redis
[ ] Celery
[ ] Celery Beat
[ ] Testing
[ ] UI improvements
[ ] Production configuration
[ ] Deployment
```

---

### Muhim eslatma

README'dagi `YOUR_USERNAME`ni o‘z GitHub username'ing bilan almashtirasan:

```bash
git clone https://github.com/ilhomjondevuz/studyhub.git
```

Agar repository nomini `StudyHub` qilib katta harf bilan ochsang ham, README'dagi URL'ni GitHub bergan **aniq clone URL** bilan almashtirganing ma'qul.

**Yana bir muhim narsa:** README'da hozir ko‘rsatilgan `config/settings/base.py`, `development.py`, `production.py` kabi struktura — agar sen hali settings'ni alohida fayllarga ajratmagan bo‘lsang, uni majburan yaratish shart emas. Avval projectni ishlaydigan qilib qurib, keyin settings'ni production-style ajratishing mumkin.
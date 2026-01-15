# WASET

## Software Requirements Specification (SRS)

**Project Name:** WASET  
**Course:** CSAI 203 – Introduction to Software Engineering  
**Institution:** Zewail City of Science, Technology and Innovation  
**Date:** November 2025

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements of **WASET**, a web-based marketplace platform. The system aims to connect producers (such as farmers and workshop owners) with importers and general users. WASET supports two primary selling mechanisms: **direct-price sales** and **auction-based sales**.  

This document serves as a reference for the design, implementation, and testing phases of the project.

---

### 1.2 Scope
WASET is a web-based marketplace that supports three main user roles:
- **Producer (Seller)**
- **Importer (Buyer)**
- **General User**

The platform provides features for user authentication, product listing, auction management, bidding, and product browsing.

**Out of scope:**
- Real payment processing (payment is simulated)
- Shipping and logistics management

---

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Description |
|-----|------------|
| SRS | Software Requirements Specification |
| FR  | Functional Requirement |
| NFR | Non-Functional Requirement |
| AJAX | Asynchronous JavaScript and XML |
| GUI | Graphical User Interface |
| DB | Database (MySQL) |

---

### 1.4 References
- IEEE 830-1998 – Recommended Practice for Software Requirements Specifications
- CSAI 203 Course Project Document, Fall 2025
- Flask Documentation
- SQLAlchemy Documentation

---

### 1.5 Overview
Section 2 presents an overall description of WASET, including its users and operating environment. Section 3 specifies the functional and non-functional requirements, use cases, and conceptual data model.

---

## 2. Overall Description

### 2.1 Product Perspective
WASET is a new, standalone web application designed as a digital marketplace. It provides a centralized platform for producers to sell products and for importers and users to browse, bid, and purchase items.

---

### 2.2 Product Functions
The main functions of WASET include:
- User registration, login, and profile management
- Product listing through direct sale or auction
- Auction lifecycle management
- Bidding and real-time auction updates
- Browsing and filtering of products
- Transaction status tracking

---

### 2.3 User Classes and Characteristics

- **Producer (Seller):** Creates and manages product listings and auctions. *(High importance)*
- **Importer (Buyer):** Searches products, places bids, and completes purchases. *(High importance)*
- **General User:** Browses products with limited interaction. *(Medium importance)*

> Note: Producer and Importer are logical roles derived from the User entity.

---

### 2.4 Operating Environment
- **Backend:** Python with Flask framework
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript (Jinja2 templates)
- **Client:** Modern web browsers
- **Hosting:** Standard commercial hosting environment

---

### 2.5 Design and Implementation Constraints
- Flask-based backend is mandatory
- MVC architectural pattern must be followed
- MySQL must be used as the database
- GitHub must be used for version control

---

### 2.6 User Documentation
The system will include:
- FAQ section
- Inline help text
- A concise user manual covering registration, listing, and bidding

---

### 2.7 Assumptions and Dependencies
**Assumptions:**
- Users have stable internet access
- Users possess basic computer literacy

**Dependencies:**
- MySQL database availability
- JavaScript/AJAX for dynamic auction updates

---

## 3. Specific Requirements

### 3.1 Functional Requirements

| ID | Requirement Description | User Class |
|----|-------------------------|-----------|
| FR1 | The system shall allow users to register and log in, selecting their role (Producer or Importer). | All |
| FR2 | The system shall allow Producers to create product listings using a multi-step form. | Producer |
| FR3 | The system shall allow Producers to choose between auction-based or direct-price sales. | Producer |
| FR4 | The system shall allow Importers to place bids on active auctions if the bid is higher than the current price. | Importer |
| FR5 | The system shall update auction price and remaining time dynamically using AJAX. | Importer |
| FR6 | The system shall allow users to browse and filter listings by category and sale type. | All |
| FR7 | The system shall automatically close auctions when their end time is reached. | System |
| FR8 | The system shall simulate payment by allowing the winner to mark an auction as paid. | Importer |
| FR9 | The system shall provide a dashboard for Producers to manage listings and auctions. | Producer |
| FR10 | The system shall allow users to securely log out. | All |

---

### 3.2 Non-Functional Requirements

| ID | Type | Requirement | Test Plan |
|----|------|-------------|-----------|
| NFR1 | Performance | Auction status updates must respond within 2 seconds under normal load. | Simulate 50 concurrent users accessing auction status API. |
| NFR2 | Security | User passwords must be securely hashed (e.g., bcrypt) before storage. | Inspect database to ensure no plaintext passwords exist. |

---

### 3.3 Use Case Descriptions

#### UC1 – Register Account
- **Actors:** All users  
- **Precondition:** None  
- **Postcondition:** User account created with hashed password  
- **Flow:** User submits registration form → System validates input → Password is hashed → Data stored

#### UC2 – Create Listing
- **Actors:** Producer  
- **Precondition:** Producer is logged in  
- **Postcondition:** New product or auction listing created  
- **Flow:** Producer completes multi-step form → System validates → Data saved

#### UC3 – Place Bid
- **Actors:** Importer  
- **Precondition:** Auction is active, importer logged in  
- **Postcondition:** Bid recorded and current price updated  
- **Flow:** Importer submits bid → System validates amount and time → Bid saved → UI updated

#### UC4 – Finalize Auction
- **Actors:** System  
- **Precondition:** Auction end time reached  
- **Postcondition:** Auction closed and winner determined  
- **Flow:** System checks expiration → Determines highest bid → Updates auction status

#### UC5 – Simulate Payment
- **Actors:** Importer  
- **Precondition:** Importer is auction winner  
- **Postcondition:** Auction marked as paid  
- **Flow:** Importer clicks "Mark as Paid" → System verifies → Status updated

---

### 3.4 Conceptual Data Model

#### Core Classes

| Class | Description | Key Attributes |
|------|------------|----------------|
| User | Represents all system users | id, username, email, password_hash, role |
| Auction | Represents auction listings | id, title, description, start_price, current_price, end_time, status, winner_id |
| Bid | Represents bids on auctions | id, auction_id, user_id, amount, timestamp |
| Product | Represents direct-sale products | id, title, description, price, producer_id |

---

## 4. Status
This document represents **Version 1.0** of the WASET SRS and will evolve as the system is developed.


DROP DATABASE IF EXISTS waset;
CREATE DATABASE waset;
USE waset;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('User', 'Producer') NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    shipping_company VARCHAR(100),
    industry_type VARCHAR(100),
    rating DECIMAL(2, 1) DEFAULT 0.0,
    profile_image TEXT, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE listings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    listing_type ENUM('Direct', 'Auction') DEFAULT 'Direct',
    image_url TEXT,
    producer_id INT,
    status ENUM('Active', 'Sold', 'Expired') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producer_id) REFERENCES users(id) ON DELETE CASCADE
);
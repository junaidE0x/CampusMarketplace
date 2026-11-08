
CREATE DATABASE IF NOT EXISTS campus_marketplace;

USE campus_marketplace;

CREATE TABLE IF NOT EXISTS listings (
    listing_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    registration_number VARCHAR(30) NOT NULL,
    item_name VARCHAR(150) NOT NULL,
    category ENUM(
        'Books',
        'Electronics',
        'Stationery',
        'Hostel Essentials',
        'Clothing',
        'Sports',
        'Other'
    ) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (price >= 0)
);

-- View all marketplace listings
SELECT * FROM listings;

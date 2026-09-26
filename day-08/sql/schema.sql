CREATE DATABASE IF NOT EXISTS facility_management; USE facility_management;
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL,email VARCHAR(150) UNIQUE NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE departments (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL UNIQUE);
CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY,department_id INT NOT NULL,name VARCHAR(120) NOT NULL,email VARCHAR(150) UNIQUE NOT NULL,salary DECIMAL(12,2) NOT NULL,FOREIGN KEY(department_id) REFERENCES departments(id));
CREATE TABLE facilities (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(150) NOT NULL,location VARCHAR(150) NOT NULL,cleanliness_score DECIMAL(4,2),water_availability BOOLEAN DEFAULT TRUE,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE inspections (id INT AUTO_INCREMENT PRIMARY KEY,facility_id INT NOT NULL,inspection_date DATE NOT NULL,cleanliness_score DECIMAL(4,2),odor_score DECIMAL(4,2),waste_level DECIMAL(4,2),status ENUM('Good','Needs Attention','Poor') NOT NULL,remarks TEXT,FOREIGN KEY(facility_id) REFERENCES facilities(id) ON DELETE CASCADE);
CREATE TABLE complaints (id INT AUTO_INCREMENT PRIMARY KEY,facility_id INT NOT NULL,description TEXT NOT NULL,status ENUM('Open','In Progress','Resolved') DEFAULT 'Open',created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY(facility_id) REFERENCES facilities(id) ON DELETE CASCADE);
CREATE INDEX idx_inspections_facility_date ON inspections(facility_id,inspection_date); CREATE INDEX idx_complaints_facility ON complaints(facility_id);

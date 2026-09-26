CREATE TABLE facilities(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(150) NOT NULL,location VARCHAR(150) NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE inspections(id INT AUTO_INCREMENT PRIMARY KEY,facility_id INT NOT NULL,inspection_date DATE NOT NULL,cleanliness_score DECIMAL(4,2),odor_score DECIMAL(4,2),waste_level DECIMAL(4,2),footfall INT, hours_since_cleaning DECIMAL(8,2),FOREIGN KEY(facility_id) REFERENCES facilities(id));
CREATE TABLE complaints(id INT AUTO_INCREMENT PRIMARY KEY,facility_id INT NOT NULL,description TEXT NOT NULL,status VARCHAR(30) DEFAULT 'Open',created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY(facility_id) REFERENCES facilities(id));
CREATE INDEX idx_inspection_facility_date ON inspections(facility_id,inspection_date);

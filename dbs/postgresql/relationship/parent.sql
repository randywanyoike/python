CREATE TABLE IF NOT EXISTS parent(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS parent_address(
    id BIGSERIAL PRIMARY KEY,
    county_name VARCHAR(250),
    town VARCHAR(250),
    longitude REAL,
    latitude REAL,
    house_no VARCHAR(250)
);

INSERT INTO parent 
(name,email)
 VALUES
('Kimberly Sada','kimberly@gmail.com'),
('John Doe','john@gmail.com'),
('Randy Wanyoike','randy@gmail.com'),
('Tonnie Kabithi','tonnie@gmail.com'),
('Martin Mbatia','martin@gmail.com');


INSERT INTO parent_address
(county_name,town,longitude,latitude,house_no)
VALUES
('Nairobi','Westlands',36.8219,-1.2921,'123'),
('Mombasa','Nyali',39.6572,-4.0435,'456'),
('Kisumu','Milimani',34.7617,-0.0917,'789'),
('Nakuru','London Estate',35.9203,-0.3031,'101'),
('Eldoret','Elgon View',35.2694,0.5149,'202');

--DROP TABLE IF EXISTS student;
CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    dob DATE,
    phone INTEGER NOT NULL UNIQUE,
    marks REAL CHECK(marks>-1 AND marks<101),
    pocket_money INTEGER,
    school_fee_balance INTEGER,
    is_married BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
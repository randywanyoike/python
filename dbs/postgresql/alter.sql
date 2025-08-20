--ALTER TABLE student
--ADD
--school_fee_balance INTEGER;

ALTER TABLE student 
ALTER COLUMN school_fee_balance SET TO NOT NULL;
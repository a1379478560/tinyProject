-- -------------------
-- Insert Investors data
-- -------------------

INSERT INTO INVESTORS VALUES (1, 'Jean-Paul Sartre', '123-45-6789', '100 Main St., New York, NY');
INSERT INTO INVESTORS VALUES (2, 'Franz Kafka', '111-11-1111', '100 Main St., New York, NY');
INSERT INTO INVESTORS VALUES (3, 'Albert Camus', '222-222-2222', '100 Main St., New York, NY');
INSERT INTO INVESTORS VALUES (4, 'Fyodor Dostoevsky', '333-33-3333', null);

-- This record will fail because it inserts a duplicate primary key (Investor ID)
INSERT INTO INVESTORS VALUES (4, 'Leo Chestov', '444-44-4444', null);
-- This record will fail beacuse it inserts a duplicate unique key (SSN)
INSERT INTO INVESTORS VALUES (5, 'Soren Kierkegaard', '111-11-1111', 'Some address');


-- -------------------
-- Insert Stocks data
-- -------------------

INSERT INTO STOCKS VALUES ('AAPL', 'Apple Inc,', 'Common stock');
INSERT INTO STOCKS VALUES ('MSFT', 'Microsoft', null);
INSERT INTO STOCKS VALUES ('GOOGL', 'Alphabet Inc', 'Class A');

-- This record will fail because it inserts a duplicate primary key (Ticker)
INSERT INTO STOCKS VALUES ('AAPL', 'A different Apple Company', null);


-- ----------------------
-- Insert Portfolio data
-- -------------------

INSERT INTO PORTFOLIO VALUES (1,'AAPL');
INSERT INTO PORTFOLIO VALUES (1,'MSFT');
INSERT INTO PORTFOLIO VALUES (3,'GOOGL');
INSERT INTO PORTFOLIO VALUES (4,'MSFT');
INSERT INTO PORTFOLIO VALUES (4,'AAPL');

-- This record will fail because it references a non-existing investor
INSERT INTO PORTFOLIO VALUES (5, 'AAPL');
-- This record will fail because it references a non-existing stock
INSERT INTO PORTFOLIO VALUES (2, 'IBM');

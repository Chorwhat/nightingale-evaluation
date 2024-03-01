INSERT OR REPLACE INTO cities 
(LatD, LatM, LatS, NS, LonD, LonM, LonS, EW, City, State) 
SELECT ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
--- this where clause checks if there isnt a duplicate entry
WHERE NOT EXISTS (
    SELECT 1 FROM cities
    WHERE 
        LatD = ? AND 
        LatM = ? AND 
        LatS = ? AND 
        NS = ? AND 
        LonD = ? AND 
        LonM = ? AND 
        LonS = ? AND 
        EW = ? AND 
        City = ? AND 
        State = ?
);

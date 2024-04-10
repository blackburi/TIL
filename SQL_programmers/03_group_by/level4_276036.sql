WITH pcd AS (
            SELECT code
            FROM skillcodes
            WHERE name = 'Python'
            ),
    ccd AS (
            SELECT code
            FROM skillcodes
            WHERE name = 'C#'
            ),
    fcd AS (
            SELECT SUM(code) AS code
            FROM skillcodes
            WHERE category = 'Front End'
            )

SELECT CASE 
        WHEN skill_code & (SELECT code FROM pcd) 
            AND skill_code & (SELECT code FROM fcd) THEN 'A'
        WHEN skill_code & (SELECT code FROM ccd) THEN 'B'
        WHEN skill_code & (SELECT code FROM fcd) THEN 'C'
    END AS grade, id, email
FROM developers
HAVING grade IS NOT NULL
ORDER BY grade, id
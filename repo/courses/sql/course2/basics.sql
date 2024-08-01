SELECT 
      --table.column
FROM 
      --table

LIMIT --5 the number of rows that will be displayed  ; the semicolon shows where the function finishes   



--- order of operators

/*  

SELECT column1, column2, ...: Specifies the columns to retrieve.
FROM table_name: Indicates the table from which to retrieve the data.
WHERE condition: Filters the rows based on a specified condition.
GROUP BY column: Groups rows that have the same values in specified columns into summary rows.
HAVING condition: Filters groups based on a specified condition.
ORDER BY column1 [ASC|DESC]: Sorts the result set in ascending or descending order based on one or more columns.
LIMIT number: Limits the number of rows returned.


*/


SELECT 
      --table.column
FROM 
      --table
WHERE 
     condition (av_salary Between 20000 and 30000 )

order BY
      av_salary


/*
Question Prompt:
Get job details for BOTH 'Data Analyst' or 'Business Analyst' positions:

For 'Data Analyst,' I want jobs only > $100K
For 'Business Analyst,' I only want jobs > $70K
Only include jobs located in EITHER:

'Boston, MA'
'Anywhere' (i.e., Remote jobs)*/

SELECT 
    job_title_short, 
    job_location, 
    salary_year_avg
FROM 
    job_postings_fact
WHERE 
    (
        (job_title_short = 'Data Analyst' AND salary_year_avg > 100000) 
        OR 
        (job_title_short = 'Business Analyst' AND salary_year_avg > 70000)
    )
    AND
    (
        job_location = 'Boston, MA' 
        OR 
        job_location = 'Anywhere'
    );

-- Look for non-senior data analyst or business analyst roles.

--            • Only get job titles that include either 'Data' or 'Business'

--            • Also include those with 'Analyst' in any part of the title

--            • Don't include any job titles with 'Senior' followed by any character

-- get the job tilte, location and average yearly salary


SELECT
    job_title AS job,
    job_location AS location,
    salary_year_avg AS salary
FROM 
    job_postings_fact AS job_p
WHERE 
    (
        (job_title LIKE '%Data%' OR job_title LIKE '%Business%')
        AND
        job_title LIKE '%Analyst%'
        AND
        job_title NOT LIKE 'Senior%'
    );

--- 


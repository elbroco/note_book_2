
--Inner Joins, full/left/right/ outer joins


select *
from tutorialsql.dbo.EmployeeDemographics
inner join tutorialsql.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID



select *
from tutorialsql.dbo.EmployeeDemographics
full outer join tutorialsql.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID


select *
from tutorialsql.dbo.EmployeeDemographics
left outer join tutorialsql.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID



select *
from tutorialsql.dbo.EmployeeDemographics
Right Outer Join tutorialsql.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID


select EmployeeDemographics.EmployeeID, FirstName, LastName, JobTitle,Salary
from tutorialsql.dbo.EmployeeDemographics
inner Join tutorialsql.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID


select EmployeeDemographics.EmployeeID, FirstName, LastName,Salary
from tutorialsql.dbo.EmployeeDemographics
inner Join tutorialsql.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
where FirstName <> 'michael' 
order by Salary desc


select JobTitle, AVG(Salary)
from tutorialsql.dbo.EmployeeDemographics
inner Join tutorialsql.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
where JobTitle = 'Salesman' 
group by JobTitle


--- union, union all

INSERT INTO EmployeeDemographics (EmployeeID, FirstName, LastName, Age, Gender)
VALUES
(1010, 'Darryl', 'Philbin', '36', 'Male'),
(1011, 'Roy', 'Anderson', '34', 'Male'),
(1012, 'Meredith', 'Palmer', '45', 'Female');


select *
from tutorialsql.dbo.EmployeeDemographics
union
select*
from tutorialsql.dbo.WareHouseEmployeeDemographics

select *
from tutorialsql.dbo.EmployeeDemographics
union all
select*
from tutorialsql.dbo.WareHouseEmployeeDemographics
order by EmployeeID


--- case statement



select FirstName, LastName, Age,
case
	when Age > 30 then 'old'
	else 'young'
end
from tutorialsql.dbo.EmployeeDemographics
where Age is not null
order by Age


SELECT FirstName, LastName, Age,
    CASE
        WHEN Age > 30 THEN 'old'
        WHEN Age BETWEEN 28 AND 30 THEN 'young'
        ELSE 'baby'
    END 
FROM tutorialsql.dbo.EmployeeDemographics
WHERE Age IS NOT NULL
ORDER BY Age;


SELECT FirstName, LastName, Age,
    CASE
	    WHEN Age = 50 THEN 'STANLEY'
        WHEN Age > 30 THEN 'old'
        ELSE 'baby'
    END AS age_group
FROM tutorialsql.dbo.EmployeeDemographics
WHERE Age IS NOT NULL
ORDER BY Age;


SELECT FirstName, LastName, JobTitle, Salary,
CASE
	when JobTitle = 'Salesman' then Salary + (Salary * .10)
	when JobTitle = 'Accountant' then Salary + (Salary * .05)
	when JobTitle = 'HR' then Salary + (Salary * .0005)
	else Salary + (salary * .001)
end as Salary_after_raise
FROM tutorialsql.dbo.EmployeeDemographics
join tutorialsql.dbo.EmployeeSalary
	ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID


--having clause

Select JobTitle, COUNT(JobTitle)
from tutorialsql.dbo.EmployeeDemographics
join tutorialsql.dbo.EmployeeSalary
	on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
group by JobTitle
having count(JobTitle) > 0

Select JobTitle, AVG(Salary)
from tutorialsql.dbo.EmployeeDemographics
join tutorialsql.dbo.EmployeeSalary
	on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
group by JobTitle
having avg(Salary) > 45000
ORDER BY AVG(Salary)


--updating/deleting data

INSERT INTO EmployeeDemographics ( FirstName, LastName, Age, Gender)
VALUES
( 'julio', 'Palmer', '30', 'male');


update tutorialsql.dbo.EmployeeDemographics
set EmployeeID = 1010
where FirstName = 'julio' and LastName = 'Palmer'


INSERT INTO EmployeeDemographics ( FirstName, LastName)
VALUES
( 'cuco', 'baloi');

update tutorialsql.dbo.EmployeeDemographics
set EmployeeID = 1010, Age = 44, Gender = 'male'
where FirstName = 'cuco' and LastName = 'baloi'


delete
FROM tutorialsql.dbo.EmployeeDemographics
where EmployeeID = 1010 and Age = 44


-- aliasing

select FirstName as fname
from tutorialsql.dbo.EmployeeDemographics

select FirstName + ' ' + LastName AS FullName
from tutorialsql.dbo.EmployeeDemographics


select Demo.EmployeeID, sal.Salary
from tutorialsql.dbo.EmployeeDemographics as Demo
join tutorialsql.dbo.EmployeeSalary as sal
	on Demo.EmployeeID = sal.EmployeeID


-- partition by

SELECT
    dem.FirstName,
    dem.LastName,
    dem.Gender,
    sal.Salary,
    COUNT(*) OVER(PARTITION BY dem.Gender) AS TotalGender
FROM
    tutorialsql..EmployeeDemographics dem
JOIN
    tutorialsql..EmployeeSalary sal ON dem.EmployeeID = sal.EmployeeID;

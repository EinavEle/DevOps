## Intro
Check out this NYC site:  [https://opendata.cityofnewyork.us]()



There is a lot of data that you can get in a JSON format file and use it for your programs.

But to save you some trouble, we have prepared the [json file](https://github.com/Elevationacademy/data-for-python-lessons/blob/master/nyc_jobs.json) for you: `nyc_jobs.json`.





We are going to work with the data in this file.

So start by loading the data, so that you can use it for later.

Also take a minute to investigate the structure of the data, as we are going to explore this data more deeply.



### About Using Sets

You can solve the following exercises without using sets, and you know what, it might even be more efficient.

But by using sets we get better readability and the code is easier to maintain.

In this amount of data, the difference in efficiency is not critical, and our code should still run in less than a second.

## Search in Description
Normally we would not want all the jobs, but the ones we are interested in.



Let's start with a warm up task:

Find jobs by searching for a word in the job description:



For example:

if we print the number of jobs that contains "experience" in their description we will get 165
```python
print(len(find_jobs_by_word("experience"))) # 165
```
Note: in this exercise you **don't need** to use sets.

<details>
<summary>Solution</summary>
<div> 

```python
def find_jobs_by_word(word):
    return [job for job in jobs if word in job.get("job_description")]
    
print(len(find_jobs_by_word("experience"))) # 165
```
</div>
</details>


## Junior Jobs in Brooklin
Find out which agencies offers at least 1 Entry-Level job and at least 1 job that is located in Broadway.



The answer should be:
```python
{
    'DEPT OF ENVIRONMENT PROTECTION',
    'NYC POLICE PENSION FUND',
    'MAYORS OFFICE OF CONTRACT SVCS',
    'DEPARTMENT OF CITY PLANNING',
    'EQUAL EMPLOY PRACTICES COMM'
}
```
<details>
<summary>Solution</summary>
<div> 

```python
# which agencies offers Entry-Level jobs and jobs that are located in Broadway (not neccesarily the same job)
# this does not mean that an agency needs to have a job in entry level and in Broadway
entry_level_jobs = set([job["agency"] for job in jobs if job["career_level"] == "Entry-Level"])
not_in_brooklin = set([job["agency"] for job in jobs if "Broadway" in job["work_location"]])

result = (entry_level_jobs & not_in_brooklin)
print("broadway", result)
```
</div>
</details>

## Max Hourly Salary
Find out what is the max salary for jobs that are hourly but not Entry-Level.

Use the `salary_range_to` key.


The answer is:
```
88.7549
```
<details>
<summary>Solution</summary>
<div> 

```python
import json

jobs = None

with open("nyc_jobs.json") as file:
    jobs = json.load(file)


Entry-Level
hourly = set([job["salary_range_to"] for job in jobs if job["salary_frequency"] == "Hourly"])
entry_level = set([job["salary_range_to"] for job in jobs if job["career_level"] != "Entry-Level"])
res = hourly & entry_level
print("max", max(res))
```
</div>
</details>


## Salaries in Range
Find out what are the agencies that offers jobs with salaries in the range of 17 to 21.



Your answer should be: 
```python
{'DEPARTMENT OF CITY PLANNING', 'DEPT OF ENVIRONMENT PROTECTION'}
```
<details>
<summary>Solution</summary>
<div> 

```python
def is_in_range(job, from_, to):
    is_above_min = float(job.get("salary_range_from")) >= from_
    is_below_max = float(job.get("salary_range_to")) <= to
    return is_above_min and is_below_max

salary_min = 17
salary_max = 18
agencies_in_range = [job["agency"] for job in jobs if is_in_range(job, salary_min, salary_max)]
print("in range", (set(agencies_in_range)))
```
</div>
</details>


## Extension Exercise

Here you have a good opportunity to compare with an implementation that does not uses sets.

Write another solution without using sets and compare your 2 answers by means of readability and maintainability.
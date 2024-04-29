"""
Sets

You are working on a recruitment platform, which should match the available jobs and the candidates based on their skills.
The skills required for the job, and the candidate's skills are stored in sets.
Complete the program to output the matched skill.
You can use the intersect operator to get the values present in both sets.
"""
skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(list(skills & job_skills)[0])

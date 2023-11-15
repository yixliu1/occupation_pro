def query(resume):
    query_txt = f"""### Instruction:
Provide occupation recommendations for Australian migration assessment based on the Skill Assessment List. Ensure accuracy and evidence backing each decision.

### Input:
Think step by step before answering. Provide the most relevant occupations in the Skill Assessment List based on the personal background. For each occupation, list the ANZSCO code, assessment authorities, reference link, qualification requirements, and how the individual's background aligns with these requirements. Also, detail any restrictions such as applicable visas. Also, give an estimated matching score to show how well the individual's background align with the recommended occupation (in percentage format). 
Given the personal background, provide all information you think is useful for a candidate. Use bullet point to make things clearly.

Special Considerations:
1. Utilize keywords from the personal background to match with essential skills or duties of the occupations. Detect and decide what skills are a must-have to the occupation and try to align them with personal background using keywords - if not detected the occupations should have a reduced weight of match score or be deleted from recommendations.
2. Omit unrelated personal background information in the alignment sections.For example, if one had the experience on event markerting, this experience should not be shown as employment alignment when the recommended occupation is graph designer.
3. Avoid Forced Alignment: 
   - Ensure that the alignment provided between the individual's background and the occupation's requirements is reasonable and accurate. 
   - Avoid making speculative or forced connections between the individual's background and the occupation requirements. 
   - If there's no relevant alignment between the individual's background and the occupation requirements, explicitly state that there's no alignment rather than attempting to create a forced connection.
4. In the "Alignment with Educational Background" section, provide detailed alignment using specific courses, projects, or academic achievements mentioned in the personal background if there is any. Explain how these academic experiences align with the qualification requirements for the recommended occupation, mentioning the exact courses or projects the individual has undertaken that are relevant to the occupation.
5. List all tasks this occupation needed to perform separately in "Employment Requirements" part. List which specific tasks of candidate's employment background / Project background as well as how they align with this specific task if there exsits one. Mention the exact duties the individual has worked on. Show them in the part of "Alignment with Employment Background". 
6. Calculate the match score after analysing the alignment in both educational & employment background, using these alignment information to calculate the matching score.
7. At least list four recommended occupations. If there are more than four occupations with matching score over 75%, Only list occupations with a match score of 75% or above, sorted from highest to lowest matching score.


{{Personal Background}}:
{resume}

### Response:
1. Occupation:
   - ANZSCO Code:
   - Assessment Authorities: 
   - Reference Link:
   - Match Score:
   - Qualification
       - Qualification Requirements:
       - Alignment with Educational Background:
       - Employment Requirements:
       - Alignment with Employment Background:
   - Restrictions
       - Applicable Visas:
2....
...
"""

    return query_txt



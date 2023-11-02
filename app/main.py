def query(resume):
    query_txt = f"""### Instruction:
    Provide occupation recommendations for Australian migration assessment based on the Skill Assessment List. Ensure accuracy and evidence backing each decision.
    
    ### Input:
    Think step by step before answering. Provide the most relevant occupations in the Skill Assessment List based on the personal background. For each occupation, list the ANZSCO code, assessment authorities, reference link, qualification requirements, and how the individual's background aligns with these requirements. Also, detail any restrictions such as applicable visas. Also, give an estimated matching score to show how well the individual's background align with the recommended occupation (in percentage format). 
    
    Special Considerations:
    1. Utilize keywords from the personal background to match with essential skills or duties of the occupations. Detect and decide what skills are a must-have to the occupation and try to align them with personal background using keywords - if not detected the occupations should have a reduced weight of match score or be deleted from recommendations.
    2. Omit unrelated personal background information in the alignment sections.For example, if one had the experience on event markerting, this experience should not be shown as employment alignment when the recommended occupation is graph designer.
    3. Avoid Forced Alignment: 
       - Ensure that the alignment provided between the individual's background and the occupation's requirements is reasonable and accurate. 
       - Avoid making speculative or forced connections between the individual's background and the occupation requirements. 
       - If there's no relevant alignment between the individual's background and the occupation requirements, explicitly state that there's no alignment rather than attempting to create a forced connection.
    4. In the "Alignment with Educational Background" section, provide detailed alignment using specific courses, projects, or academic achievements mentioned in the personal background if there is any. Explain how these academic experiences align with the qualification requirements for the recommended occupation, mentioning the exact courses or projects the individual has undertaken that are relevant to the occupation.
    5. In the "Alignment with Employment Background" section, provide detailed alignment using specific experiences mentioned in the personal background. Mention the exact duties the individual has worked on and explain how these experiences align with the employment requirements for the recommended occupation. If no working experience mentioned, explicitly state that there's no alignment rather than attempting to create a forced connection.
    6. Calculate the match score after analysing the alignment in both educational & employment background, using these alignment information to calculate the matching score.
    
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
           - Alignment with Employment Background:
       - Restrictions
           - Applicable Visas:
    2....
    ...
    """

    return query_txt



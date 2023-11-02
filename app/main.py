resume = """PERSONAL PROFILE 
Final year commerce student majoring in marketing and business analytics at the University of Sydney 
seeking a position in marketing to utilise my marketing and analytical skills. 
EDUCATION 
The University of Sydney  
Feb 2021 – Dec 2023 
Bachelor of Commerce, Majoring in Marketing and Business Analytics 
o WAM: 81.5% (Distinction, top 10%), Vice Chancellor’s Global Mobility Scholarship 
o Enrolled as Dalyell Scholar, Job Smart Gold badge earner and member of BGS honour society 
o Relevant courses: Predictive Analytics, Statistical Modelling, Operations Management, Advertising, 
Marketing Insights. 
University of Michigan                 
Jan 2023 – May 2023 
Exchange student, Bachelor of Business Administration 
o GPA: 4.0/4.0 
o Relevant courses: Digital Marketing, International Marketing, Marketing Analytics 
Fujian Medical University  
Sep 2019 – Jan 2021 
Clinical Medicine (Combined Bachelor-Master’s Degree Program, 8 years) 
o GPA: 3.73/4.0 (Top 6%) 
o The First Prize Scholarship (3%), Individual Scholarship, Third prize of 2020 "FLTRP·ETIC Cup" 
English Public Speaking Contest 
RELEVANT EXPERIENCE 
Marketing Intern | USYD Job Smart                                                                    
Nov 2022 – Feb 2023 
o Actively participated in the Job Smart program, earned the gold badge and internship rewards due to 
top performance. 
o Collaborated with 2 team members to provide business review of client SBIS’s operating and 
marketing strategy. Created consumer profile and provided suggestions on strategic marketing 
plan as well as business lead generator. 
o Conducted exhaustive competitive analysis of client Space Tank’s social media channels a 
visualized analysis of 300+ recent posts and content review.  
o Developed social media marketing strategy, curated relevant content with 8 samples and designed 
the social media calendar for client Space Tank’s LinkedIn marketing. 
Student Business Consultant | Infosys                                                                                       
Apr 2022 
o Worked in a team of 6 student consultants to conduct exhaustive research on Australian MBA 
schools, searched for venues to boost Infosys’s event marketing and completed a 5000-word 
industry report.  
Account Exceutive Intern | Ogilvy Shanghai  
Nov 2021 – Jan 2022 
o Collaborated with 6 crew members and communicated with client Jim Beam, writing monthly 
social media reports and competitors’ activation individually. 
o Operated Jim Beam’s social media account, wrote 8 WeChat articles which earned 8000+ 
average impressions and 3000+ new followers, 26 posts on Weibo with 200+ average 
engagements. 
o Engaged in 3 pitches regarding Estee Lauder and SUNTORY in a team of 14, accurately 
provided industry-specific information and conducted competitive analysis.
OTHER EXPERIENCE 
Design & Marketing Subcomm | USYD Business Analytics Association           
Aug 2022 - present 
o Collaborating with 3 team members to assist in event marketing, designing Instagram posts and 
accessories with Adobe Photoshop and Canva. 
o Partnering with the University of Sydney’s Business Analytics Discipline in promoting the 
university major and forging meaningful relationships with other organisations that share similar 
workstreams, helping the faculty develop social media strategy and design a branding story. 
Receptionist | Healthpac Medical Centre                                                            
Jun 2022 – Dec 2022 
o Answered phone in both Mandarin and English, greeted, registered and made appointments for 
100+ patients daily in a busy medical centre, excellent in communication and multitasking. 
o Responsible for housekeeping and banking reconciliation, issuing invoices to private patients 
and billing to Medicare with 100% accuracy. 
o Assisted 10+ general practices and specialist in admin, managed scanning, emailing and faxing 
of documents and communicated with different insurance companies and medical institutions. 
Team Leader | L’Oréal Brandstorm 2022                                                                            
Mar 2022 
o Lead a team of 3, dominated the daily meeting and labour division with high efficiency within 
team. Designed personalized beauty products shopping experience and consumer journey for 
L’Oréal and won a top 50 place in the competition. 
o Individually designed the marketing mix for product and modelled it with Unreal Engine, self
directed and edited a 3-minute promotion video with Adobe Premier Pro. 
Associate Director | FJMU Student Union, Department of Art                         
Sep 2019 – Jun 2021 
o Eminent student cadre (Top 5%) 
o Lead a team of 23 and organized 8 galas with 3000+ audiences, fully involved from process 
designing, staff arrangement, sponsorship negotiating, venue decoration to stage lighting. 
o Worked as the marketing & design director, lead a team of 6 to design posters, videos and 
promote events. 
Research Assistant | Neurobiology Lab at FJMU                                                
Nov 2019 – Jan 2021 
o Conducted experiments on anesthesiology, neurobiology and pharmacology, responsible for 
the monitoring and visualization of raw data. 
o Engaged in academic writing, contributed to Regulation of wakefulness by GABAergic DRN-VTA 
pathway as co-author. 
SKILLS & INTERESTS 
Computer Skills: Microsoft Office,  Power BI,  Photoshop,  Canva,  Premiere Pro,  Python,  SPSS,  
Google Analytics, SQL,  LaTeX  
Language: Mandarin (native), English (bilingual) 
Interests: 16-year piano player, heavy user of social media, cooking 
REFEREE (available upon request): Gwen Ng (Practice Manager at Healthpac Hurstville)"""


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
    7. At least list three recommended occupations. If there are more than three occupations with matching score over 75%, Only list occupations with a match score of 75% or above, sorted from highest to lowest matching score.
    8. Give a notice at the end of respoonse. The notices should be something like: "Only work experience with payment evidence (such as taxation record / payslip record) can be served as emplyment evidence. Please check cautionsly whether your employment experience is eligible for assessment."
    
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



import os
from bs4 import BeautifulSoup, Tag
import re


directory = r'C:\Users\yixliu1\Desktop\SEMS(1)\SEMS\RSMS ROL'


############################## Extract information from source ###########################
def extract_visa_subclasses(soup):
    h2_visa_subclasses = soup.find('h2', string=lambda text: 'visa subclasses' in text.lower())
    if not h2_visa_subclasses:
        return []

    # Find all subsequent siblings until the next <h2> tag
    visa_subclasses_list = []
    for sibling in h2_visa_subclasses.next_siblings:
        if isinstance(sibling, Tag):
            if sibling.name == 'h2':
                break  # Stop if another <h2> tag is found
            if sibling.name == 'li':
                visa_subclasses_list.append(sibling.text)

    return visa_subclasses_list


# Function to check the format of the file content
def check_format(file_content):
    soup = BeautifulSoup(file_content, 'html.parser')

    # Check for Occupation Name, ANZSCO Code, and Assessment Authorities
    occupation = soup.find('h1', text=lambda t: t and 'Occupation Name:' in t)
    anzscocode = soup.find('h1', text=lambda t: t and 'ANZSCO Code:' in t)
    authorities = soup.find('h1', text=lambda t: t and 'Assessment Authorities:' in t)
    reference_link = soup.find('h1', text=lambda t: t and 'Reference link:' in t)

    occupation = occupation.get_text().split(': ')[1] if occupation else None
    anzscocode = anzscocode.get_text().split(': ')[1] if anzscocode else None
    authorities = authorities.get_text().split(': ')[1] if authorities else None
    reference_link = reference_link.get_text().split(': ')[1] if reference_link else None

    visa_subclasses_list = extract_visa_subclasses(soup)

    return occupation, anzscocode, authorities, reference_link, visa_subclasses_list


################################# Deal with result #################################
# Function to replace the occupation name and reference link
def replace_values(chunk, occupation_name, reference_link, assessment_name):
    chunk = re.sub(r'([Oo]ccupation:\s*).+', r'\1' + occupation_name, chunk, flags=re.MULTILINE)
    chunk = re.sub(r'([Rr]eference [Ll]ink:\s*).+', r'\1' + reference_link, chunk, flags=re.MULTILINE)
    chunk = re.sub(r'([Aa]ssessment [Aa]uthorities:\s*).+', r'\1' + assessment_name, chunk, flags=re.MULTILINE)

    return chunk


def replace_visa(chunk, visa_list):
    visa_text = '\n'
    for i in visa_list:
        visa_text += f'\t-{i}\n'
    chunk = re.sub(r'([Aa]pplicable [Vv]isa.+:\s*).+', r'\1' + visa_text, chunk, flags=re.MULTILINE)

    return chunk


def read_content(directory, filename):
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    return content


def process_result(chunks):
    j = 1
    try:
        processed_chunks = []
        for i in chunks:
            if 'occupation' not in i.lower():
                j += 1
                processed_chunks.append(i)
            else:
                break

        anz_codes = []
        for i in range(j, len(chunks), 2):  # Iterate over the occupation headers and their corresponding chunks
            chunk = f'{chunks[i - 1]}{chunks[i]}'
            anz_code_match = re.search(r'ANZSCO Code:\s*(\d+)', chunk, flags=re.IGNORECASE)
            if anz_code_match:
                anz_code = anz_code_match.group(1).replace(' ', '')
                if anz_code not in anz_codes:
                    anz_codes.append(anz_code)
                else:
                    continue

                try:
                    doc = read_content(directory, f'{anz_code}.txt')
                    occupation, anzscocode, authorities, reference_link, visa_subclasses_list = check_format(doc)
                    chunk = replace_values(chunk, occupation, reference_link, authorities)
                    processed_chunk = replace_visa(chunk, visa_subclasses_list)
                except:
                    print('############################################')
                    print(f'no find file with {anz_code}')
                    processed_chunk = chunk

                processed_chunks.extend([processed_chunk])
            else:
                processed_chunks.extend([chunk])
    except:
        print('Except Error')
        processed_chunks = chunks

    processed_text = ''.join(processed_chunks)
    return processed_text

# This Code Will Take Inputs for Concept Titles and Descriptions and Output Formatted HTML for All Available Inputs - Combined Into One Output


# Below is the expected format for TITLE and DESCRIPTION notes for the following procedures to ingest
# The list element format is ['TITLE', 'DESCRIPTION']

notes_list = [['Python', 'Python is a Programming Language'],['For Loop', 'For Loops allow you to iterate over lists'],['Lists', 'Lists are sequences of data']]


# Below is the HTML structure used in my course notes web pages

#<div class="lessonContentBox">
#    <div class="content_article">
#        <div class="lessonTitle">
#            <h2>(Concept Title)</h2>
#        </div>
#        <p>
#            (Concept Description)
#        </p>
#    </div>
#</div>


# The parse_title_and_description procedure takes in a list that contains the TITLE and DESCRIPTION, and parses the data, and then outputs it into separate values

def parse_title_and_description(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_formatted_HTML(concept_title, concept_description)

	
# The generate_formatted_HTML procedure takes the parsed TITLE and DESCRIPTION inputs, and outputs the structured HTML

def generate_formatted_HTML(concept_title, concept_description):
    html_part_1 = '''
<div class="lessonContentBox">
    <div class="content_article">
        <div class="lessonTitle">
            <h2>''' + concept_title
    html_part_2 = '''</h2>
        </div>
        <p>
            '''+ concept_description
    html_part_3 = '''
        </p>
    </div>
</div>
'''
    
    full_html = html_part_1 + html_part_2 + html_part_3
    return full_html

	
# The assemble_parsed_for_generate_HTML procedure loops through the input list (lists within a list) and outputs the final formatted HTML

def assemble_parsed_for_generate_HTML(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = parse_title_and_description(concept)
        HTML = HTML + concept_HTML
    return HTML

	
# The print used below outputs the final HTML that can be used in a web page	
	
print assemble_parsed_for_generate_HTML(notes_list)
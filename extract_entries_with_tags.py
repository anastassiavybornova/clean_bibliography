"""
Script extracts the entries with a specific tag from an original bib file and saves the cleaned entries in another bib file.

Author: Antoine Allard (antoineallard.info)
"""

from clean_bibliography import bibliography


source_bib_filename='../zotero/DynamicaLab.bib'
bib = bibliography(source_bib_filename)

tags_to_keep = ['network_geometry']
target_bib_filename = 'references.bib'
keep_keywords = True
bib.extract_entries_with_given_keyword(tags_to_keep, target_bib_filename, keep_keywords)

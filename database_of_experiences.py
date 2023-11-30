import pandas as pd

# Creating a database for the experiences, teaching/outreach, and awards from the provided resume content.

# Research Experience
research_experience = [
    {"Position": "Research Assistant", "Duration": "October 2021 – Present", "Institution": "University of California Irvine (UCI)", "Details": "Working under Jose M. Ranz; NIH UCI Minority Science Program funded."},
    {"Position": "Research Assistant", "Duration": "June 2021 – Nov 2021", "Institution": "University of California Irvine (UCI)", "Details": "Directed by Luis Mota-Bravo; NIH and UCI Minority Science Program funded."},
    {"Position": "Research Assistant", "Duration": "May – Aug 2020", "Institution": "University of Southern California (USC)", "Details": "Funded by the Diversity Inclusion Access (DIA) Jumpstart Graduate School Program."},
    {"Position": "Research Assistant", "Duration": "June – Aug 2019", "Institution": "University of Colorado Boulder (CU Boulder)", "Details": "Funded by the Summer Multicultural Access to Research Training (SMART) Program."},
    {"Position": "Research Assistant", "Duration": "June – Dec 2018", "Institution": "University of California Irvine (UCI)", "Details": "Funded by NIH and UCI Minority Science Program Bridges to Baccalaureate."}
]

# Teaching/Outreach
teaching_outreach = [
    {"Role": "Tutor", "Duration": "2020-2021", "Institution": "Fullerton College", "Subject": "Calculus II and Statistics"},
    {"Role": "Tutor", "Duration": "2019-2020", "Institution": "Fullerton College", "Subject": "Philosophy"},
    {"Role": "Teacher’s Assistant", "Duration": "Jan 2019", "Institution": "Anaheim High School", "Details": "Taught the Amgen Biotech Lab."},
    {"Role": "Teacher’s Assistant", "Duration": "Jan 2019", "Institution": "Fullerton College", "Details": "Assisted in 'Intro to Biotechnology' course."},
    {"Role": "Volunteer", "Duration": "May 2018", "Institution": "Fullerton College", "Details": "Crime Scene Investigation Camp."},
    {"Role": "Volunteer", "Duration": "June 2016", "Institution": "Open Houses and College Nights", "Details": "Helped in biotechnology program events."}
]

# Awards
awards = [
    {"Award": "UCI IMSD and MARC Scholar", "Year": "2021-Present"},
    {"Award": "UROP Award", "Year": "2022"},
    {"Award": "USC DIA Graduate School Summer Intern", "Year": "2020"},
    {"Award": "Dartmouth Scholar", "Year": "2020"},
    {"Award": "Scholarship by Boeing Company", "Year": "2019"},
    {"Award": "Scholarship by Avid Bioservices Inc.", "Year": "2019"},
    {"Award": "ABRCMS Poster Award", "Year": "2018"},
    {"Award": "Dean’s Honor List", "Year": "2017-20"},
    {"Award": "North Orange County ROP Biomedical Scholarship", "Year": "2016"}
]

# Convert to DataFrames
df_research_experience = pd.DataFrame(research_experience)
df_teaching_outreach = pd.DataFrame(teaching_outreach)
df_awards = pd.DataFrame(awards)

df_research_experience, df_teaching_outreach, df_awards


# Import Libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page Title
image = Image.open('DNA.png')
st.image(image, use_column_width=True)
st.write("""
# DNA Nucleotide Count
Counts Nucleotide Composition of DNA!
""")

# Input Text Box
st.header('Enter DNA Sequence')

sequence_input = ">DNA\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=220)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Skips the Sequence Name (First Line)
# Concatenates List to String without any Whitespace.
sequence = ''.join(sequence)

# DNA Nucleotide Count
st.header('DNA Nucleotide Count')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = DNA_nucleotide_count(sequence)

# Display DataFrame
st.subheader('DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')

df = df.rename({0: 'Count'}, axis='columns')  # Rename Column Name
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'Nucleotide'})  # Rename Column Name
st.write(df)

# Display Bar Chart using Altair
st.subheader('Bar chart')
bar = alt.Chart(df).mark_bar().encode(x='Nucleotide', y='Count')
bar = bar.properties(width=alt.Step(80))  # Bar Width

st.write(bar)

import streamlit as st
import pandas as pd
from huffman import huffman_output, Huffman_Parser

st.title("Demonstracja algorytmu Huffmana")
st.header("Wiktor Flis IMST 1.1/2")

"""
Testowe teskty

1. She sells sea-shells on the sea-shore.
The shells she sells are sea-shells, I’m sure.
For if she sells sea-shells on the sea-shore
Then I’m sure she sells sea-shore shells.

2. Wiktor Flis teleinformatyka
"""

input_string = st.text_input(label="Tekst wejsciowy")

col1, col2 = st.beta_columns(2)

out_dict, freq, root_node = None, None, None

if input_string:
    out_dict, freq, root_node = huffman_output(input_string)

with col1:
    st.subheader("Zakodowany tekst:")

    if out_dict:
        out_str = """ """
        for c in input_string:
            out_str += f"""{out_dict[c]}"""
        out_str += """ """

        st.markdown(
            f"<p style='word-break: break-all;'>{out_str}</p>", unsafe_allow_html=True
        )

    else:
        with st.empty():
            st.write("Tutaj zobaczysz zakodowany tekst")
            st.table()

with col2:
    st.subheader("Liczba wystapien znakow:")
    if freq:
        df = pd.DataFrame(freq)
        st.dataframe(df, height=450)

st.subheader("Drzewo Huffmana:")
st.text("Kazdy z lisci drzewa jest podpisany '<tworzace_litery>=kod'")
if root_node:
    parser = Huffman_Parser()
    parser.huffman_tree_parse(root_node)
    graph = parser.huffman_tree_graph(root_node)
    st.graphviz_chart(graph)
import streamlit as st 

st.title("Gestion de classe")

st.markdown("""
### GESTION DE CLASSE

Point de services (ou un campus qui fait partie d'un plus grand établissement d'enseignement) offrant des services d'instruction ou d'éducation à un groupe d'élèves. Une école peut avoir une seule unité administrative avec plusieurs points de services (ou groupe d'écoles à plusieurs branches ou écoles satellites ou campus). Une unité administrative réfère à toute école ou groupe d'écoles dirigé par un seul directeur ou une administration unique. Un point de services réfère à n'importe quel emplacement où un service est fourni aux élèves ou étudiants, qu’il s’agisse d’une seule entité ou partie d'une plus grande unité administrative



""")

st.header(":blue[calcule de notes]")

devoir1 =st.number_input("devoir 1")

devoir2 =st.number_input("devoir 2")
moyennedevoir=(devoir1+devoir2)/2

if st.button("moyenne devoir"):
    st.write(moyennedevoir)


notescompos = st.number_input("composition")

if st.button("moyenne semestre"):
    moyensemestre=(notescompos+moyennedevoir)/2
    moyfoiscoeff=moyensemestre*5
    st.write(moyensemestre)
    st.write("Moy x Coeff")
    st.write(moyfoiscoeff)
    


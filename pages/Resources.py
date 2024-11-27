import base64
import pandas as pd
import streamlit as st

st.title("Resources")

st.link_button("CFAI Institute Link", "https://study.cfainstitute.org/app/cfa-program-level-ii-for-may-2025")
st.link_button("CFA Account Link", "https://www.cfainstitute.org/account")
st.link_button("DB Link", "https://docs.google.com/spreadsheets/d/11EUKLaoZQYvCi4ghibrDgTU14oaV6HBd7YYC0Pf9imc/edit?gid=0#gid=0")

subjects = pd.read_csv('Subjects.csv')

st.dataframe(subjects, hide_index = True)


selected_option = None

option_map = {
    0: "CFAI",
    1: "Kaplan Schweser",
}
selection = st.pills(
    "Select Resource",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
)

if selection != None:
    selected_option = option_map[selection]

if selected_option != None and selected_option == 'CFAI':
    option = st.selectbox(
        f"Select a {option_map[selection]} book to open.",
        ('Ethics', 'Quantitative Methods', 'Economics', 'Fixed Income', 'Financial Statement Analysis', 'Equity Valuation', 'Corporate Issuers', 
         'Alternative Investments', 'Portfolio Management', 'Derivatives'),
        index=None
    )

    if option != None:
        st.write("Opening ", option)
    
    if option != None:
    
        with open(f"{option}.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        
        # Embed PDF in Streamlit
        pdf_viewer = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
        st.markdown(pdf_viewer, unsafe_allow_html=True)

elif selected_option != None and selected_option == 'Kaplan Schweser':
    option = st.selectbox(
        f"Select a {option_map[selection]} book to open.",
        ('1. Quant + Econ', '2. FSA + Corporate Issuers', '3. Equity Valuation', '4. FI, Derivatives and AI', '5. PM And Ethics', 'Quick Sheet'),
        index=None
    )

    if option != None:
        st.write("Opening ", option)
    
    if option != None:
    
        with open(f"{option}.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        
        # Embed PDF in Streamlit
        pdf_viewer = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
        st.markdown(pdf_viewer, unsafe_allow_html=True)

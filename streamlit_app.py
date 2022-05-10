def streamlit_app():
    import streamlit as st

    st.title("Streamlit Tutorial")
    st.text("This is a Streamlit tutorial")
    st.image("https://www.streamlit.io/static/media/logo.png", width=200)

    with st.form("my_form"):
        type_transaction = st.text_input("Entrer le type de transaction")
        montant = st.number_input("Entrer le montant")
        name_origine = st.text_input("Entrer le nom de l'origine")
        name_destination = st.text_input("Entrer le nom de la destination")
        old_balance = st.number_input("Entrer le solde")

        submitted = st.form_submit_button("Envoyer")
        if submitted:
            new_balance = old_balance - montant
            detect_fraud = (type_transaction == "TRANSFER" or type_transaction == "CASH_OUT") \
                           and (new_balance == 0 and name_origine.startswith("C") and name_destination.startswith("C"))
            if detect_fraud is True:
                st.write("Fraude detectée")
                return
            st.success("Transaction réussie")


if __name__ == "__main__":
    streamlit_app()

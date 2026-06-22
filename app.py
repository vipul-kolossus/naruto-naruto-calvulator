import streamlit as st

st.set_page_config(page_title="Calvulator", layout="centered")

st.title("Calvulator")

if "expression" not in st.session_state:
    st.session_state.expression = ""

display = st.text_input("", value=st.session_state.expression, key="display", disabled=True)

buttons = [
    ["C", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "⌫", "="],
]

for row in buttons:
    cols = st.columns(4)
    for i, label in enumerate(row):
        with cols[i]:
            if st.button(label, use_container_width=True):
                expr = st.session_state.expression
                if label == "C":
                    st.session_state.expression = ""
                elif label == "⌫":
                    st.session_state.expression = expr[:-1]
                elif label == "=":
                    try:
                        result = expr.replace("÷", "/").replace("×", "*").replace("−", "-")
                        st.session_state.expression = str(eval(result))
                    except Exception:
                        st.session_state.expression = "Error"
                elif label == "+/-":
                    try:
                        val = float(expr)
                        st.session_state.expression = str(-val)
                    except Exception:
                        pass
                elif label == "%":
                    try:
                        val = float(expr)
                        st.session_state.expression = str(val / 100)
                    except Exception:
                        pass
                else:
                    st.session_state.expression += label
                st.rerun()

st.markdown("""
<style>
div.stButton > button {
    height: 60px;
    font-size: 20px;
    border-radius: 10px;
    background-color: #f0f0f0;
    color: #222;
    border: 1px solid #ccc;
}
div.stButton > button:hover {
    background-color: #ddd;
}
</style>
""", unsafe_allow_html=True)

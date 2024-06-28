import streamlit as st 
import pandas as pd 
from st_aggrid import AgGrid

# Load data
house = pd.read_csv('house_clean.csv')

# Fungsi utama untuk Streamlit app
def main():
    st.title('Halaman Streamlit David')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown ')
    st.write('Some Phytagorean Equation : ')
    st.latex('c^2 = a^2 + b^2')

    st.dataframe(house)
    
    st.write('Metrics')
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

    st.write('Menampilkan Dataframe dengan St AgGrid')
    AgGrid(house.head(100))
    st.table([x for x in range(1, 5)])

    # Button dan Checkbox
    click_me_btn = st.button('Click Me')
    if click_me_btn:
        st.write('Button Clicked!')

    check_btn = st.checkbox('Klik Jika Setuju')
    if check_btn:
        st.write('Anda Setuju')
        radio_button = st.radio('Choose below', [x for x in range(1, 3)])
        st.write('Anda Memilih', radio_button)

    # Slider
    age_slider = st.slider('Berapa Usia Anda', 0, 100)
    st.write('Usia Anda', age_slider)

    # Input (Typing)
    num_input = st.number_input('Input Berapapun')
    st.write(f'Kuadrat dari {num_input} adalah {num_input**2}')

    # Sidebar
    st.sidebar.header('Sidebar Menu')
    sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
    sidebar_radio_button = st.sidebar.radio('Pilih Menu', options=['A', 'B', 'C'])
    st.sidebar.write(f'You selected {sidebar_radio_button} from the sidebar.')

    # Columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    # Expander
    with st.expander("Klik Untuk Detail"):
        st.write('Anda Telah Membuka Detail')

    # Form di Sidebar
    with st.sidebar.form("Data Diri"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        
        # Tombol submit
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Slider:", slider_val, "Checkbox:", checkbox_val)

    st.write("Outside the form")

    # Tabs
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    tab1.write("this is tab 1")
    tab2.write("this is tab 2")

    with tab1:
        st.radio("Select one:", [1, 2])

if __name__ == '__main__':
    main()

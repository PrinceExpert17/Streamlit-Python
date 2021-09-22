import pandas as pd
import numpy as np
import streamlit as st
import neattext.functions as nfx

def main():
    st.title('Simple File Downloader App')
    menu = ['Home', 'DF', 'About']
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == 'Home':
        #st.subheader('Home Page')
        raw_text = st.text_area('Enter a text here:')
        if st.button('Clean Text'):
            # Layout
            col1, col2 = st.columns(2)
            with col1:
                st.info('Original Text')
                st.write(raw_text)
                
            with col2:
                st.success('Proceed Text')
                results = nfx.clean_text(raw_text)
                st.write(results)
                # Download Button
                st.download_button(label='Download File', data=results, file_name='myresults.csv')
                
    elif choice == 'DF':
        st.subheader('Create a Random Generated Dataframe')
        random = st.sidebar.number_input('Random Number', min_value=10, max_value=500, value=10)
        
        # Create dataframe
        df = pd.DataFrame(np.random.randint(0, int(random), size=(100,4)), columns=list('ABCD'))
        st.dataframe(df)
        
        # Download button
        st.download_button(label='Download CSV', data=df.to_csv(), mime='text/csv')
            
    else:
        pass
            
    
if __name__ == '__main__':
    main()
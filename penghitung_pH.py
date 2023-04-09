import streamlit as st
import numpy as np
st.title('Ini adalah web aplikasi penghitung pH :red[titrasi Asam Kuat oleh Basa Kuat]')

M_titrat = st.number_input('Masukkan Molaritas titrat', step = 0.0001, format = "%.4f")
V_titrat = st.number_input('Masukkan Volume titrat')
M_titran = st.number_input('Masukkan Molaritas Titran', step = 0.0001, format = "%.4f")
V_titran = st.number_input('Masukkan Volume Titran')


mmol_titrat = M_titrat * V_titrat
mmol_titran = M_titran * V_titran
V_total = V_titrat + V_titran

sisa_mmol = abs(mmol_titran - mmol_titrat)
H_OH = sisa_mmol/V_total
np.seterr(divide='ignore')

pH = round(-(np.log10(H_OH)),2) 
if st.button('Tampilkan nilai pH') :
    if mmol_titran > mmol_titrat :
        st.write('nilai pH adalah : ',14 - pH)
    elif mmol_titran == mmol_titrat : 
        st.write('nilai pH adalah : ',  7)
    else :
        st.write('nilai pH adalah : ', pH)
else :
    st.write('Tekan tombol untuk memunculkan nilai')
  

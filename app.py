# app.py
import streamlit as st
import random
import time

st.set_page_config(layout="centered", page_title="Sürpriz Kutu!")

def create_surprise_box_web():
    st.title("🎁 Sürpriz Kutunuz Geliyor... 🎁")
    st.write("Biraz heyecanlı mısınız? Hadi kutuyu açalım!")

    if st.button("Kutuyu Aç!"):
        with st.spinner('Kutu açılıyor...'):
            time.sleep(2) # 2 saniye bekletme simülasyonu

        messages = [
            "Seni çok seviyorum! ❤️",
            "Sen benim için çok değerlisin!",
            "Gülüşünle dünyamı aydınlatıyorsun! ✨",
            "Her zaman yanındayım!",
            "Hayatımda olduğun için çok şanslıyım!",
            "Seninle olmak harika!",
            "Sana kocaman bir sarılma! 🤗",
            "Seni düşünmek bile beni mutlu ediyor!",
            "Senin gibi birine sahip olmak bir mucize!",
            "İyi ki varsın! 😊"
        ]

        chosen_message = random.choice(messages)

        st.success("🎉 Kutunun İçinden Çıkan 🎉")
        st.markdown(f"## **>>> {chosen_message} <<<**")
        st.write("Umarım bu küçük sürpriz seni gülümsetmiştir! 😊")
        st.write("Teşekkür ederim! ❤️")

# Uygulamayı çalıştır
create_surprise_box_web()
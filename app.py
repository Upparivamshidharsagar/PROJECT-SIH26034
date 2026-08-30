import streamlit as st
import time

st.title("📦 Packaged Commodity Compliance Checker")

st.write("Upload a product image to check its compliance.")

uploaded_image = st.file_uploader(
    "📷 Upload Product Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded Product Image",
        use_container_width=True
    )

    st.success("Image uploaded successfully!")

    if st.button("🔍 Check Compliance"):

        with st.spinner("🔍 Analyzing product..."):
            time.sleep(1)

        st.success("Analysis completed!")

        st.subheader("📋 Compliance Results")

        st.write("**Product Name:**")
        st.write("**MRP:**")
        st.write("**Net Quantity:**")
        st.write("**Manufacturer:**")

        st.divider()

        st.write("**Compliance Status:**")
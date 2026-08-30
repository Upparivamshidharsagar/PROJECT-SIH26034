import streamlit as st
import time

st.title("📦 Packaged Commodity Compliance Checker")

st.write("Upload a product image to check its compliance.")

uploaded_image = st.file_uploader(
    "📷 Upload Product Image",
    type=["jpg", "jpeg", "png"],
    help="Upload a clear image of the product label."
)

if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded Product Image",
        width="stretch"
    )

    st.success("Image uploaded successfully!")

    if st.button("🗑️ Remove Image"):
        st.rerun()

    if st.button("🔍 Check Compliance"):

     with st.spinner("🔍 Analyzing product..."):

        st.info("Sending image for analysis...")

    st.success("Image sent for analysis.")
st.subheader("📋 Compliance Results")

col1, col2 = st.columns(2)

with col1:
    st.write("**Product Name**")
    st.info("Waiting for result...")

    st.write("**MRP**")
    st.info("Waiting for result...")

with col2:
    st.write("**Net Quantity**")
    st.info("Waiting for result...")

    st.write("**Manufacturer**")
    st.info("Waiting for result...")

st.divider()

st.write("### Compliance Status")

st.warning("Waiting for compliance analysis...")
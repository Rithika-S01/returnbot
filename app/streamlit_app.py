import streamlit as st
import sys
sys.path.append(".")
from rag.chain import get_chain

st.set_page_config(page_title="ReturnBot", page_icon="🛒")
st.title("🛒 ReturnBot")
st.caption("Ask anything about return & refund policies across platforms")
st.markdown("---")

query = st.text_input("💬 Your Question:", placeholder="Can I return a used product on Flipkart?")

if st.button("🔍 Ask ReturnBot") and query:
    with st.spinner("Searching through policies..."):
        retriever, llm = get_chain()

        # Get relevant docs
        docs = retriever.invoke(query)

        # Build context from docs
        context = "\n\n".join([doc.page_content for doc in docs])

        # Build prompt manually
        prompt = f"""You are a helpful assistant that answers questions about e-commerce return policies.
Use the following policy information to answer the question.
Always mention which platform the information is from.

Policy Information:
{context}

Question: {query}

Answer:"""

        # Get answer from LLM
        answer = llm.invoke(prompt)

    st.markdown("### ✅ Answer")
    st.success(answer)

    st.markdown("### 📄 Sources Used")
    for doc in docs:
        with st.expander(f"📌 Source: {doc.metadata['source'].upper()}"):
            st.write(doc.page_content)
            
            
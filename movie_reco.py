import streamlit as st
import joblib

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

X = joblib.load(r"D:\ai_agentic\ai_conda\vectors.pkl")
model = joblib.load(r"D:\ai_agentic\ai_conda\model.pkl")
df = joblib.load(r"D:\ai_agentic\ai_conda\dataframe.pkl")

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: #0b0b0f;
    color: white;
}

/* Header */

.hero {
    padding: 45px 35px;
    border-radius: 20px;
    margin-bottom: 30px;

    background:
        linear-gradient(
            90deg,
            rgba(0,0,0,0.95),
            rgba(30,10,20,0.75),
            rgba(0,0,0,0.45)
        ),
        url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1600");

    background-size: cover;
    background-position: center;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #dddddd;
}

/* Recommendation cards */

.movie-card {
    background: #17171d;
    border-radius: 15px;
    padding: 20px;
    margin-top: 15px;
    border: 1px solid #292933;
    transition: 0.3s;
}

.movie-card:hover {
    border: 1px solid #e50914;
    transform: translateY(-3px);
}

.movie-number {
    font-size: 30px;
    font-weight: 800;
    color: #e50914;
}

.movie-name {
    font-size: 19px;
    font-weight: 600;
    color: white;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: #111116;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Buttons */

.stButton > button {
    width: 100%;
    background: #e50914;
    color: white;
    border: none;
    border-radius: 10px;
    height: 48px;
    font-weight: 600;
    font-size: 16px;
}

.stButton > button:hover {
    background: #b20710;
}

/* Select box */

div[data-baseweb="select"] > div {
    background-color: #17171d;
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;">
            <div style="font-size:55px;">🎬</div>
            <h2>Movie AI</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("📖 About")

    st.write(
        "This Movie Recommendation System uses "
        "Machine Learning to find movies similar "
        "to the movie you select."
    )

    st.divider()

    st.subheader("⚙️ How it works")

    st.write("""
    1. 🎬 Select a movie
    2. 🤖 AI analyzes movie features
    3. 🔎 Finds similar movies
    4. ⭐ Shows recommendations
    """)

    st.divider()

    st.subheader("🛠️ Tech Stack")

    st.write("""
    🐍 **Python**  
    🎈 **Streamlit**  
    🤖 **Machine Learning**  
    🧠 **NLP (Natural Language Processing)**  
    📊 **Scikit-learn**  
    📦 **Joblib**  
    🐼 **Pandas**
    """)

# ---------------------------------------------------
# HERO
# ---------------------------------------------------

st.title("🎬 Movie Recommendation System")
st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# MOVIE SELECTION
# ---------------------------------------------------

sam = st.selectbox(
    "Select a movie to get recommendations:",
    df.name.values  
)
# ---------------------------------------------------
# RECOMMENDATION
# ---------------------------------------------------

if st.button("🔍 Get Recommendations"):
    index = df[df.name == sam].index[0]
    z,y = model.kneighbors(X[index].toarray())
    for i in y:
        c = (df.name[i]).values
    x=1
    for i in range (4):
        st.write(x ,c[i+1])
        x += 1



# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(" 🎬 Movie Recommendation System Built by me(Ankit)")

import streamlit as st
from datetime import date

# =====================================================
# UGANDA GOVERNANCE GUIDE
# Version 2.0
# =====================================================

st.set_page_config(
    page_title="Uganda Governance Guide",
    page_icon="UG",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# DESIGN SYSTEM
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --forest: #102F2A;
    --green: #176B50;
    --green-light: #E8F2EC;
    --gold: #D5AA54;
    --ivory: #F7F5EF;
    --white: #FFFFFF;
    --text: #243B35;
    --muted: #75847C;
    --border: #E6E2D7;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: var(--ivory);
    color: var(--text);
}

[data-testid="stSidebar"] {
    background: var(--forest);
    border-right: 1px solid #284A40;
}

[data-testid="stSidebar"] * {
    color: #F7F5EF !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #D5E2DA !important;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif;
    color: var(--forest);
    font-weight: 800;
}

.hero {
    background: linear-gradient(120deg, #102F2A 0%, #176B50 100%);
    border-left: 5px solid var(--gold);
    padding: 38px;
    border-radius: 17px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(16,47,42,.12);
}

.hero h1 {
    color: white;
    font-size: 36px;
    margin-bottom: 10px;
}

.hero p {
    color: #E2EEE8;
    font-size: 16px;
}

.metric {
    background: white;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 22px;
    min-height: 120px;
    box-shadow: 0 4px 14px rgba(16,47,42,.04);
}

.metric h2 {
    color: var(--green);
    margin: 0;
    font-size: 29px;
}

.metric p {
    color: var(--muted);
    margin-top: 8px;
}

.panel {
    background: white;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 12px;
}

.panel h3 {
    color: var(--green);
}

.stButton > button {
    background: var(--green);
    color: white !important;
    border: 1px solid var(--green);
    border-radius: 9px;
    font-weight: 600;
}

.stButton > button:hover {
    background: var(--forest);
    border-color: var(--gold);
    color: white !important;
}

.stLinkButton > a {
    background: var(--green);
    color: white !important;
    border: 1px solid var(--green);
    border-radius: 9px;
}

[data-testid="stMetricValue"] {
    color: var(--green);
}

[data-testid="stExpander"] {
    background: white;
    border: 1px solid var(--border);
    border-radius: 10px;
}

[data-testid="stTextInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"] {
    border-radius: 9px;
}

a {
    color: var(--green) !important;
}

hr {
    border-color: var(--border);
}

.footer {
    text-align: center;
    padding: 20px;
    color: var(--muted);
    font-size: 12px;
}

.gold-line {
    height: 3px;
    background: var(--gold);
    border-radius: 5px;
    margin: 15px 0;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# OFFICIAL SOURCES
# =====================================================

SOURCES = {
    "State House": "https://statehouse.go.ug/",
    "Parliament": "https://www.parliament.go.ug/",
    "Judiciary": "https://www.judiciary.go.ug/",
    "Legal Information Institute": "https://ulii.org/",
    "Electoral Commission": "https://www.ec.or.ug/",
    "Local Government": "https://molg.go.ug/",
    "UBOS": "https://www.ubos.org/",
    "Office of the Prime Minister": "https://opm.go.ug/",
    "Inspectorate of Government": "https://www.igg.go.ug/",
    "Auditor General": "https://www.oag.go.ug/",
    "Public Service Commission": "https://psc.go.ug/",
    "PPDA": "https://www.ppda.go.ug/",
}


# =====================================================
# INSTITUTION DIRECTORY
# =====================================================

INSTITUTIONS = [
    {
        "name": "Office of the President",
        "category": "Executive",
        "description": "National executive leadership and constitutional responsibilities.",
        "website": "State House"
    },
    {
        "name": "Cabinet",
        "category": "Executive",
        "description": "Supports executive policy direction and government administration.",
        "website": "State House"
    },
    {
        "name": "Office of the Prime Minister",
        "category": "Executive",
        "description": "Coordinates government business and national programmes.",
        "website": "Office of the Prime Minister"
    },
    {
        "name": "Parliament of Uganda",
        "category": "Legislature",
        "description": "Makes laws, represents citizens and oversees government.",
        "website": "Parliament"
    },
    {
        "name": "Supreme Court",
        "category": "Judiciary",
        "description": "The highest court in Uganda.",
        "website": "Judiciary"
    },
    {
        "name": "Court of Appeal",
        "category": "Judiciary",
        "description": "Hears appeals and constitutional matters within its jurisdiction.",
        "website": "Judiciary"
    },
    {
        "name": "High Court",
        "category": "Judiciary",
        "description": "Exercises original and appellate jurisdiction under the law.",
        "website": "Judiciary"
    },
    {
        "name": "Electoral Commission",
        "category": "Elections",
        "description": "Organises and conducts elections and referenda.",
        "website": "Electoral Commission"
    },
    {
        "name": "Inspectorate of Government",
        "category": "Accountability",
        "description": "Investigates corruption and abuse of authority within its mandate.",
        "website": "Inspectorate of Government"
    },
    {
        "name": "Office of the Auditor General",
        "category": "Accountability",
        "description": "Audits public accounts and examines public resource management.",
        "website": "Auditor General"
    },
    {
        "name": "Public Service Commission",
        "category": "Public Service",
        "description": "Performs public service appointment and related functions.",
        "website": "Public Service Commission"
    },
    {
        "name": "Public Procurement and Disposal of Public Assets Authority",
        "category": "Procurement",
        "description": "Regulates public procurement and disposal of public assets.",
        "website": "PPDA"
    }
]


# =====================================================
# ADMINISTRATIVE STRUCTURE
# =====================================================

LEVELS = [
    ("National", "Central Government"),
    ("District", "District Local Government"),
    ("City", "City Local Government"),
    ("Municipality", "Municipal Council"),
    ("Town Council", "Town Council"),
    ("Sub-county", "Sub-county Administration"),
    ("Division", "Urban Division"),
    ("Parish", "Parish or Ward"),
    ("Village", "Village or Cell")
]


# =====================================================
# CONSTITUTIONAL TOPICS
# =====================================================

CONSTITUTION = [
    (
        "Sovereignty of the people",
        "The people are the source of public authority."
    ),
    (
        "Constitutional supremacy",
        "The Constitution is the supreme law of Uganda."
    ),
    (
        "Separation of powers",
        "Government authority is distributed among the Executive, Legislature and Judiciary."
    ),
    (
        "Human rights",
        "The Constitution protects fundamental rights and freedoms."
    ),
    (
        "Decentralisation",
        "The Constitution provides for decentralised local government."
    ),
    (
        "Public accountability",
        "Public institutions and officers are subject to legal accountability."
    )
]


# =====================================================
# SIDEBAR NAVIGATION
# =====================================================

with st.sidebar:

    st.markdown(
        "<h1 style='color:#D5AA54;'>UGANDA</h1>",
        unsafe_allow_html=True
    )

    st.markdown("### GOVERNANCE GUIDE")
    st.caption("PUBLIC INFORMATION PORTAL")

    st.markdown("<div class='gold-line'></div>",
                unsafe_allow_html=True)

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Government Structure",
            "Institutions Directory",
            "Ministries",
            "Local Government",
            "District Registry",
            "Constitution & Law",
            "Elections",
            "Accountability",
            "Official Resources",
            "About"
        ]
    )

    st.markdown("<div class='gold-line'></div>",
                unsafe_allow_html=True)

    st.caption("Independent civic information portal")
    st.caption("Uganda | Version 2.0")


# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Uganda Governance Guide</h1>
        <p>
        Understand Uganda's government, public institutions,
        administrative structures and constitutional framework.
        </p>
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)

    metrics = [
        (a, "3", "Branches of Government"),
        (b, "9", "Administrative Levels"),
        (c, "Public", "Information Directory")
    ]

    for col, value, label in metrics:
        with col:
            st.markdown(f"""
            <div class="metric">
                <h2>{value}</h2>
                <p>{label}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("## Government at a glance")

    columns = st.columns(3)

    branches = [
        (
            "Executive",
            "Implements laws, directs government policy and administers public services."
        ),
        (
            "Legislature",
            "Makes laws, represents citizens and scrutinises government."
        ),
        (
            "Judiciary",
            "Interprets laws and resolves disputes."
        )
    ]

    for col, (title, description) in zip(columns, branches):
        with col:
            st.markdown(f"""
            <div class="panel">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("## Explore the guide")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="panel">
            <h3>Public Institutions</h3>
            <p>Explore government institutions and their responsibilities.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="panel">
            <h3>Administrative Registry</h3>
            <p>Explore Uganda's administrative levels and local government.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "Always verify current government information "
        "through the relevant official institution."
    )


# =====================================================
# GOVERNMENT STRUCTURE
# =====================================================

elif page == "Government Structure":

    st.title("Government Structure")
    st.caption("The three principal branches of government.")

    sections = {
        "Executive": [
            "President",
            "Vice President",
            "Prime Minister",
            "Cabinet",
            "Government ministries"
        ],
        "Legislature": [
            "Parliament",
            "Members of Parliament",
            "Parliamentary committees",
            "Legislative processes"
        ],
        "Judiciary": [
            "Supreme Court",
            "Court of Appeal",
            "High Court",
            "Subordinate courts"
        ]
    }

    for name, items in sections.items():

        with st.expander(name, expanded=True):

            for item in items:
                st.write(f"- {item}")


# =====================================================
# INSTITUTIONS DIRECTORY
# =====================================================

elif page == "Institutions Directory":

    st.title("Institutions Directory")
    st.caption("Search public institutions and their responsibilities.")

    query = st.text_input("Search institutions")

    categories = ["All"] + sorted(
        set(item["category"] for item in INSTITUTIONS)
    )

    category = st.selectbox(
        "Institution category",
        categories
    )

    results = [
        item for item in INSTITUTIONS
        if query.lower() in (
            item["name"] + item["description"] + item["category"]
        ).lower()
        and (
            category == "All"
            or item["category"] == category
        )
    ]

    st.caption(f"{len(results)} institutions found")

    for item in results:

        with st.container(border=True):

            st.subheader(item["name"])
            st.caption(item["category"])

            st.write(item["description"])

            st.link_button(
                "Visit official website",
                SOURCES[item["website"]]
            )


# =====================================================
# MINISTRIES
# =====================================================

elif page == "Ministries":

    st.title("Government Ministries")

    st.write("""
    This section is intended to provide a directory of
    Uganda's government ministries, ministers and portfolios.
    """)

    st.info(
        "Current ministry names, portfolios and office holders "
        "must be verified against official government records "
        "before being added to the directory."
    )

    st.link_button(
        "State House Uganda",
        SOURCES["State House"]
    )

    st.link_button(
        "Office of the Prime Minister",
        SOURCES["Office of the Prime Minister"]
    )


# =====================================================
# LOCAL GOVERNMENT
# =====================================================

elif page == "Local Government":

    st.title("Local Government")
    st.caption("Uganda's decentralised administrative framework.")

    for level, description in LEVELS:

        with st.expander(level):

            st.write(description)

    st.markdown("## Local government responsibilities")

    st.markdown("""
    - Local planning and budgeting
    - Delivery of public services
    - Community participation
    - Local infrastructure
    - Public health administration
    - Implementation of national policies
    """)

    st.link_button(
        "Ministry of Local Government",
        SOURCES["Local Government"]
    )


# =====================================================
# DISTRICT REGISTRY
# =====================================================

elif page == "District Registry":

    st.title("Uganda Administrative Registry")

    st.write("""
    Central directory for Uganda's districts, cities,
    municipalities, town councils and lower administrative units.
    """)

    search = st.text_input("Search administrative units")

    admin_type = st.selectbox(
        "Administrative category",
        [
            "All",
            "District",
            "City",
            "Municipality",
            "Town Council"
        ]
    )

    st.info(
        "The registry is awaiting a verified official dataset. "
        "No unverified district counts or administrative boundaries "
        "are published."
    )

    st.write("Search term:", search if search else "None")
    st.write("Selected category:", admin_type)

    st.link_button(
        "Uganda Bureau of Statistics",
        SOURCES["UBOS"]
    )

    st.link_button(
        "Ministry of Local Government",
        SOURCES["Local Government"]
    )


# =====================================================
# CONSTITUTION AND LAW
# =====================================================

elif page == "Constitution & Law":

    st.title("Constitution & Law")

    for title, description in CONSTITUTION:

        with st.expander(title):

            st.write(description)

    st.link_button(
        "Uganda Legal Information Institute",
        SOURCES["Legal Information Institute"]
    )

    st.warning(
        "This is an educational reference, not legal advice."
    )


# =====================================================
# ELECTIONS
# =====================================================

elif page == "Elections":

    st.title("Elections & Representation")

    st.markdown("""
    ### Electoral Commission

    - Electoral administration
    - Voter registration
    - Electoral programmes
    - Election results
    - Electoral laws

    ### Parliamentary representation

    - Members of Parliament
    - Constituencies
    - Parliamentary committees
    - Legislative representation
    """)

    st.link_button(
        "Electoral Commission",
        SOURCES["Electoral Commission"]
    )

    st.link_button(
        "Parliament of Uganda",
        SOURCES["Parliament"]
    )


# =====================================================
# ACCOUNTABILITY
# =====================================================

elif page == "Accountability":

    st.title("Accountability & Oversight")

    institutions = [
        (
            "Inspectorate of Government",
            "Investigates corruption and maladministration.",
            "Inspectorate of Government"
        ),
        (
            "Auditor General",
            "Audits public accounts and expenditure.",
            "Auditor General"
        ),
        (
            "Parliament",
            "Exercises legislative and oversight functions.",
            "Parliament"
        ),
        (
            "Public Procurement Authority",
            "Oversees public procurement.",
            "PPDA"
        )
    ]

    for name, description, source in institutions:

        with st.container(border=True):

            st.subheader(name)
            st.write(description)

            st.link_button(
                "Official website",
                SOURCES[source]
            )


# =====================================================
# OFFICIAL RESOURCES
# =====================================================

elif page == "Official Resources":

    st.title("Official Government Resources")

    search = st.text_input("Search government websites")

    filtered = {
        name: url
        for name, url in SOURCES.items()
        if search.lower() in name.lower()
    }

    for name, url in filtered.items():

        with st.container(border=True):

            st.subheader(name)

            st.link_button(
                "Open official website",
                url
            )


# =====================================================
# ABOUT
# =====================================================

elif page == "About":

    st.title("About Uganda Governance Guide")

    st.markdown("""
    Uganda Governance Guide is an independent public-information
    platform designed to improve access to information about
    Uganda's governance system.

    ### Objectives

    - Explain government structures.
    - Organise public institution information.
    - Provide administrative registry resources.
    - Improve access to official government websites.
    - Support civic and constitutional education.

    ### Editorial principles

    - Prioritise official government sources.
    - Verify changing information.
    - Avoid publishing unverified figures.
    - Clearly identify information that needs confirmation.
    - Keep legal information linked to authoritative sources.
    """)

    st.write("Application version: 2.0")
    st.write("Date:", date.today())


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div class="footer">
    UGANDA GOVERNANCE GUIDE<br>
    Independent Public Information Portal<br>
    Verify current information through official institutions.
</div>
""", unsafe_allow_html=True)

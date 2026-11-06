
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Uganda Governance Guide",
    page_icon="UG",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f4f7f6;
}

[data-testid="stSidebar"] {
    background: #102b35;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif;
}

.hero {
    background: linear-gradient(120deg, #102b35, #176b50);
    padding: 38px;
    border-radius: 16px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 35px;
}

.hero p {
    color: #dceee6;
}

.metric {
    background: white;
    border: 1px solid #e1e9e5;
    border-radius: 13px;
    padding: 20px;
}

.metric h2 {
    color: #176b50;
}

.panel {
    background: white;
    padding: 20px;
    border-radius: 13px;
    border: 1px solid #e1e9e5;
    margin-bottom: 12px;
}

a {
    color: #176b50 !important;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ---------------- DATA ----------------

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
        "description": "Coordinates government business and relevant national programmes.",
        "website": "Office of the Prime Minister"
    },
    {
        "name": "Parliament of Uganda",
        "category": "Legislature",
        "description": "Makes laws, represents citizens and provides government oversight.",
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
        "name": "PPDA",
        "category": "Procurement",
        "description": "Regulates public procurement and disposal of public assets.",
        "website": "PPDA"
    },
]

LEVELS = [
    ("National", "Central Government"),
    ("District", "District Local Government"),
    ("City", "City Local Government"),
    ("Municipality", "Municipal Council"),
    ("Town Council", "Town Council"),
    ("Sub-county", "Sub-county Administration"),
    ("Division", "Urban Division"),
    ("Parish", "Parish or Ward"),
    ("Village", "Village or Cell"),
]

CONSTITUTION = [
    ("Sovereignty", "The people are the source of public authority."),
    ("Constitutional supremacy", "The Constitution is the supreme law of Uganda."),
    ("Separation of powers", "Government powers are distributed among the three branches."),
    ("Human rights", "The Constitution protects fundamental rights and freedoms."),
    ("Decentralisation", "The Constitution provides for decentralised local government."),
    ("Accountability", "Public institutions and officers are subject to legal accountability."),
]


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("# UGANDA")
    st.markdown("### GOVERNANCE GUIDE")
    st.caption("Public information portal")

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

    st.divider()
    st.caption("Independent educational reference")


# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Uganda Governance Guide</h1>
        <p>
        Explore Uganda's government, public institutions,
        administrative structures and constitutional framework.
        </p>
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)

    for col, heading, value in [
        (a, "Government branches", "3"),
        (b, "Information directory", "Public"),
        (c, "Administrative levels", "9")
    ]:
        with col:
            st.markdown(
                f"""
                <div class="metric">
                    <h2>{value}</h2>
                    <p>{heading}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.subheader("The three branches")

    cols = st.columns(3)

    branches = [
        ("Executive", "Implements laws and directs government policy."),
        ("Legislature", "Makes laws and represents citizens."),
        ("Judiciary", "Interprets laws and resolves disputes.")
    ]

    for col, (name, description) in zip(cols, branches):
        with col:
            st.markdown(
                f"""
                <div class="panel">
                    <h3>{name}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.info(
        "This portal is an independent educational guide. "
        "Verify changing information through official sources."
    )


# ---------------- GOVERNMENT STRUCTURE ----------------

elif page == "Government Structure":

    st.title("Government Structure")

    st.write("Uganda's national government operates through three principal branches.")

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


# ---------------- INSTITUTIONS ----------------

elif page == "Institutions Directory":

    st.title("Government Institutions")

    query = st.text_input("Search institutions")

    category = st.selectbox(
        "Institution category",
        ["All"] + sorted(set(x["category"] for x in INSTITUTIONS))
    )

    results = [
        x for x in INSTITUTIONS
        if query.lower() in (
            x["name"] + x["description"] + x["category"]
        ).lower()
        and (category == "All" or x["category"] == category)
    ]

    st.caption(f"{len(results)} institutions found")

    for item in results:
        with st.container(border=True):
            st.subheader(item["name"])
            st.caption(item["category"])
            st.write(item["description"])
            st.link_button(
                "Official website",
                SOURCES[item["website"]]
            )


# ---------------- MINISTRIES ----------------

elif page == "Ministries":

    st.title("Government Ministries")

    st.write(
        "Use official government sources to verify the current "
        "ministries, ministerial portfolios and institutional responsibilities."
    )

    st.link_button(
        "Visit State House",
        SOURCES["State House"]
    )

    st.link_button(
        "Visit Office of the Prime Minister",
        SOURCES["Office of the Prime Minister"]
    )

    st.warning(
        "The ministry directory and current office holders require "
        "verification against current official government records."
    )


# ---------------- LOCAL GOVERNMENT ----------------

elif page == "Local Government":

    st.title("Local Government Structure")

    st.write(
        "Explore the general decentralised administrative structure."
    )

    for level, description in LEVELS:
        with st.expander(level):
            st.write(description)

    st.link_button(
        "Ministry of Local Government",
        SOURCES["Local Government"]
    )

    st.link_button(
        "Uganda Bureau of Statistics",
        SOURCES["UBOS"]
    )


# ---------------- DISTRICT REGISTRY ----------------

elif page == "District Registry":

    st.title("Uganda Administrative Registry")

    st.write(
        "A dedicated registry for districts, cities, municipalities "
        "and lower administrative units."
    )

    st.info(
        "The registry is prepared for expansion. "
        "Official administrative records must be imported and verified "
        "before publishing district counts or boundary information."
    )

    registry_search = st.text_input(
        "Search administrative unit"
    )

    registry_type = st.selectbox(
        "Administrative type",
        ["All", "District", "City", "Municipality", "Town Council"]
    )

    st.caption(
        "No unverified administrative entries are displayed."
    )

    st.link_button(
        "Official statistics",
        SOURCES["UBOS"]
    )

    st.link_button(
        "Local Government records",
        SOURCES["Local Government"]
    )


# ---------------- CONSTITUTION ----------------

elif page == "Constitution & Law":

    st.title("Constitution & Law")

    for title, description in CONSTITUTION:
        with st.expander(title):
            st.write(description)

    st.link_button(
        "Read Ugandan laws and legal materials",
        SOURCES["Legal Information Institute"]
    )

    st.warning(
        "Educational information only. Consult current legislation "
        "and qualified legal professionals for legal decisions."
    )


# ---------------- ELECTIONS ----------------

elif page == "Elections":

    st.title("Elections & Representation")

    st.markdown("""
    ### Electoral Commission
    - Electoral administration
    - Voter registration
    - Election programmes
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


# ---------------- ACCOUNTABILITY ----------------

elif page == "Accountability":

    st.title("Accountability Institutions")

    institutions = [
        ("Inspectorate of Government", "Investigates corruption and maladministration."),
        ("Auditor General", "Audits public expenditure and accounts."),
        ("Parliament", "Exercises legislative and oversight responsibilities."),
        ("PPDA", "Oversees public procurement.")
    ]

    for name, description in institutions:
        with st.container(border=True):
            st.subheader(name)
            st.write(description)

    st.link_button(
        "Inspectorate of Government",
        SOURCES["Inspectorate of Government"]
    )

    st.link_button(
        "Office of the Auditor General",
        SOURCES["Auditor General"]
    )


# ---------------- RESOURCES ----------------

elif page == "Official Resources":

    st.title("Official Government Resources")

    search = st.text_input("Search official websites")

    for name, url in SOURCES.items():
        if search.lower() in name.lower():
            with st.container(border=True):
                st.write(f"**{name}**")
                st.link_button("Open website", url)


# ---------------- ABOUT ----------------

elif page == "About":

    st.title("About Uganda Governance Guide")

    st.write("""
    Uganda Governance Guide is an independent public-information
    platform designed to make government structures and public
    institutions easier to understand.

    Its objectives include:

    - Improving access to public information.
    - Explaining government structures.
    - Organising administrative information.
    - Connecting citizens to official resources.
    - Supporting civic and constitutional education.
    """)

    st.write(f"Application date: {date.today()}")

    st.caption("Version 1.0")


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "UGANDA GOVERNANCE GUIDE | Independent educational resource | "
    "Verify current information through official institutions."
)

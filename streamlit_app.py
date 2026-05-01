from pathlib import Path

import streamlit as st


ROOT = Path(__file__).parent
HERO_IMAGE = ROOT / "assets" / "civic-assistant-hero.png"

TOPICS = {
    "Register to Vote": "How does voter registration usually work?",
    "Election Timeline": "How do election timelines usually work?",
    "Voting Options": "What are common voting options?",
    "Ballot Prep": "How should I prepare before marking a ballot?",
    "Election Day": "What should I expect on election day?",
    "After Voting": "What happens after people vote?",
}

PREP_STEPS = [
    ("Check eligibility", "Confirm age, residency, citizenship, and any local requirements."),
    ("Register or update", "Make sure your name, address, and party preference rules are current."),
    ("Choose how to vote", "Review in-person, early, mail, or absentee options available locally."),
    ("Review the ballot", "Read candidate and measure information from official sources."),
    ("Make a voting plan", "Know deadlines, ID rules, polling hours, and transportation."),
]

TIMELINE = [
    ("1. Registration Window", "Voters register, update addresses, or confirm status before the local deadline."),
    ("2. Ballot Information", "Election offices publish candidate lists, ballot measures, sample ballots, and voter guides."),
    ("3. Early or Mail Voting", "Some places open early voting sites or send mail ballots before election day."),
    ("4. Election Day", "Polling places open for in-person voting, check-in, ballot marking, and ballot casting."),
    ("5. Counting and Certification", "Officials verify, count, audit where required, report results, and certify the final outcome."),
]

ANSWERS = [
    {
        "keywords": ["register", "registration", "update", "eligibility", "eligible"],
        "title": "Voter registration",
        "points": [
            "Check whether you meet your location's eligibility rules.",
            "Register online, by mail, or in person if your election office offers those methods.",
            "Update your registration when your name, address, or party preference changes.",
            "Look up the official registration deadline for your state, county, or election authority.",
        ],
    },
    {
        "keywords": ["timeline", "deadline", "date", "calendar", "schedule"],
        "title": "Election timelines",
        "points": [
            "Timelines usually start with registration and ballot information deadlines.",
            "Early voting or mail ballot windows may open before election day.",
            "Election day has fixed polling hours set by local law.",
            "Results may be unofficial at first, then finalized through canvassing and certification.",
        ],
    },
    {
        "keywords": ["option", "early", "mail", "absentee", "in person", "polling"],
        "title": "Voting options",
        "points": [
            "Common options include election-day in-person voting, early in-person voting, mail voting, or absentee voting.",
            "Availability depends on local rules, deadlines, and eligibility requirements.",
            "If voting by mail, check request, return, signature, and postmark rules carefully.",
            "If voting in person, confirm your polling place before leaving.",
        ],
    },
    {
        "keywords": ["ballot", "candidate", "measure", "prepare", "research"],
        "title": "Ballot preparation",
        "points": [
            "Find a sample ballot from an official election website when available.",
            "Read neutral voter guides, candidate statements, and measure explanations.",
            "Note contests where you need more information before voting.",
            "Bring any allowed notes or sample ballot according to your local rules.",
        ],
    },
    {
        "keywords": ["day", "expect", "id", "place", "poll"],
        "title": "Election day",
        "points": [
            "Confirm your polling location and hours before you go.",
            "Bring any identification or documents required in your area.",
            "Check in with poll workers, receive or access your ballot, mark choices, and cast it.",
            "Ask a poll worker for help if a machine, ballot, or check-in issue comes up.",
        ],
    },
    {
        "keywords": ["after", "count", "results", "certify", "certification", "audit"],
        "title": "After voting",
        "points": [
            "Election-night results are often unofficial and can change as valid ballots are counted.",
            "Officials may verify signatures, process provisional ballots, and conduct required checks.",
            "Certification is the formal step that makes final results official.",
            "Use official election office channels for final results and recount information.",
        ],
    },
]

FALLBACK = {
    "title": "A simple way to think about it",
    "points": [
        "Start by identifying your location and the election you care about.",
        "Check registration, voting options, ballot information, and deadlines from official sources.",
        "Make a plan for when, where, and how you will vote.",
        "For exact dates and rules, use your state or local election office website.",
    ],
}


def find_answer(question: str) -> dict:
    normalized = question.lower()
    for answer in ANSWERS:
        if any(keyword in normalized for keyword in answer["keywords"]):
            return answer
    return FALLBACK


def add_assistant_answer(question: str) -> None:
    answer = find_answer(question)
    st.session_state.messages.append({"role": "user", "content": question})
    st.session_state.messages.append({"role": "assistant", "content": answer})


def render_answer(answer: dict) -> None:
    st.markdown(f"**{answer['title']}**")
    for point in answer["points"]:
        st.markdown(f"- {point}")


st.set_page_config(
    page_title="Election Guide Assistant",
    page_icon="EG",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container { padding-top: 1.5rem; }
    div[data-testid="stSidebar"] { background: #f7faf9; }
    .hero-title { font-size: clamp(2.4rem, 5vw, 4.6rem); line-height: 1; font-weight: 800; margin: 0; }
    .eyebrow { color: #b97914; font-weight: 800; text-transform: uppercase; font-size: .8rem; margin-bottom: .35rem; }
    .muted { color: #607174; font-size: 1.05rem; line-height: 1.6; }
    .timeline-card { border: 1px solid #dbe6e4; border-radius: 8px; padding: 1rem; min-height: 150px; background: #fbfdfd; }
    .timeline-card strong { color: #17324d; }
    </style>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": {
                "title": "Hi, I can help you understand the election process.",
                "points": [
                    "Ask about registration, timelines, voting options, ballot prep, election day, or results.",
                    "Rules vary by location, so I will keep explanations general and point you toward official local sources for exact deadlines.",
                ],
            },
        }
    ]

with st.sidebar:
    st.subheader("Ask About")
    for label, question in TOPICS.items():
        if st.button(label, use_container_width=True):
            add_assistant_answer(question)

    st.divider()
    st.subheader("Prep Tracker")
    for title, detail in PREP_STEPS:
        st.checkbox(title, help=detail)

left, right = st.columns([1.15, 0.85], vertical_alignment="center")
with left:
    if HERO_IMAGE.exists():
        st.image(str(HERO_IMAGE), use_container_width=True)
with right:
    st.markdown('<div class="eyebrow">Challenge 2</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Election Guide Assistant</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="muted">A friendly, step-by-step assistant for understanding voter registration, timelines, polling options, ballot preparation, and what happens after voting.</p>',
        unsafe_allow_html=True,
    )

st.divider()

st.subheader("Interactive Helper")
quick_cols = st.columns(3)
quick_questions = [
    "What are the main steps to vote?",
    "How do election timelines usually work?",
    "What should I check before election day?",
]
for column, question in zip(quick_cols, quick_questions):
    if column.button(question, use_container_width=True):
        add_assistant_answer(question)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            render_answer(message["content"])
        else:
            st.write(message["content"])

prompt = st.chat_input("Ask about registration, ballots, polling places, results...")
if prompt:
    add_assistant_answer(prompt)
    st.rerun()

st.divider()
st.subheader("Typical Election Journey")
timeline_cols = st.columns(len(TIMELINE))
for column, (title, body) in zip(timeline_cols, TIMELINE):
    column.markdown(
        f"""
        <div class="timeline-card">
            <strong>{title}</strong>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

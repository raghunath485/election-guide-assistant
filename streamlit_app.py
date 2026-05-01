from datetime import date
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
    "Provisional Ballots": "What is a provisional ballot?",
    "Accessibility": "What accessibility support can voters ask about?",
}

PREP_STEPS = [
    ("Check eligibility", "Confirm age, residency, citizenship, and any local requirements."),
    ("Register or update", "Make sure your name, address, and party preference rules are current."),
    ("Choose how to vote", "Review in-person, early, mail, or absentee options available locally."),
    ("Review the ballot", "Read candidate and measure information from official sources."),
    ("Make a voting plan", "Know deadlines, ID rules, polling hours, and transportation."),
    ("Track or confirm", "Use official tools to confirm registration, ballot status, or final results."),
]

TIMELINE = [
    ("1. Registration Window", "Voters register, update addresses, or confirm status before the local deadline."),
    ("2. Ballot Information", "Election offices publish candidate lists, ballot measures, sample ballots, and voter guides."),
    ("3. Early or Mail Voting", "Some places open early voting sites or send mail ballots before election day."),
    ("4. Election Day", "Polling places open for in-person voting, check-in, ballot marking, and ballot casting."),
    ("5. Counting and Certification", "Officials verify, count, audit where required, report results, and certify the final outcome."),
]

GLOSSARY = {
    "Absentee ballot": "A ballot used when a voter cannot or chooses not to vote at a polling place, depending on local rules.",
    "Canvass": "The official review and confirmation of vote totals after ballots are counted.",
    "Certification": "The formal act that makes election results official.",
    "Early voting": "An in-person voting period before election day, available in some places.",
    "Poll worker": "A trained election worker who helps voters check in, receive ballots, and use voting equipment.",
    "Provisional ballot": "A ballot used when eligibility or registration needs review before it can be counted.",
    "Sample ballot": "A preview ballot that helps voters research contests before voting.",
}

QUIZ = [
    {
        "question": "Which source should you use for exact deadlines?",
        "options": ["Official election office", "A social media post", "A campaign flyer"],
        "answer": "Official election office",
        "why": "Deadlines and rules vary by location, so official election offices are the reliable source.",
    },
    {
        "question": "What should you do if your name is not found at the polling place?",
        "options": ["Ask a poll worker for next steps", "Leave without asking", "Use someone else's ballot"],
        "answer": "Ask a poll worker for next steps",
        "why": "Poll workers can explain available local options, including whether a provisional ballot is appropriate.",
    },
    {
        "question": "Are election-night results always final?",
        "options": ["No, they may be unofficial", "Yes, always", "Only if posted on television"],
        "answer": "No, they may be unofficial",
        "why": "Valid ballots may still need processing, review, canvassing, or certification.",
    },
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
        "next": "Confirm your registration status before planning how to vote.",
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
        "next": "Write down the deadlines that apply to your location and voting method.",
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
        "next": "Choose the method that fits your schedule and confirm the local rules for it.",
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
        "next": "Make a short list of contests or measures you still need to research.",
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
        "next": "Decide when you will go and what you need to bring.",
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
        "next": "Use official result pages and wait for certification before treating results as final.",
    },
    {
        "keywords": ["provisional", "challenge", "not listed", "missing name"],
        "title": "Provisional ballots",
        "points": [
            "A provisional ballot may be offered when registration or eligibility cannot be confirmed immediately.",
            "Election officials review the issue after election day using local procedures.",
            "Voters may receive instructions for checking whether the ballot was counted.",
            "The exact process depends on local law, so ask poll workers for written instructions when possible.",
        ],
        "next": "If this happens, keep any receipt or tracking instructions you receive.",
    },
    {
        "keywords": ["accessibility", "disabled", "language", "help", "assistance"],
        "title": "Voter assistance and accessibility",
        "points": [
            "Many election offices provide accessible voting equipment, curbside options, language assistance, or help from poll workers.",
            "Available support varies by location and election type.",
            "You can ask your election office what assistance is available before voting.",
            "At the polling place, ask a poll worker for help if you need accommodations or instructions.",
        ],
        "next": "Contact the election office early if you need a specific accommodation.",
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
    "next": "Try asking about registration, voting options, ballot prep, election day, or results.",
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
    st.info(answer["next"])


def plan_items(profile: dict) -> list[str]:
    method = profile["method"]
    items = [
        f"Confirm registration for {profile['location'] or 'your election jurisdiction'}.",
        f"Find the official page for the {profile['election_type'].lower()} election.",
        "Save the registration, ballot request, return, and polling-place deadlines that apply to you.",
        "Review a sample ballot and mark any contests that need research.",
    ]

    if method == "Vote by mail or absentee":
        items.extend(
            [
                "Check whether you must request a ballot or whether one is sent automatically.",
                "Review signature, witness, envelope, postmark, and drop-off rules.",
                "Track your ballot if your election office offers tracking.",
            ]
        )
    elif method == "Vote early in person":
        items.extend(
            [
                "Find early voting locations, dates, and hours.",
                "Check whether any location can serve you or whether one is assigned.",
            ]
        )
    else:
        items.extend(
            [
                "Confirm your assigned polling place before election day.",
                "Check polling hours, ID rules, and transportation.",
            ]
        )

    if profile["needs_accessibility"]:
        items.append("Contact the election office early about accessibility, language, or assistance needs.")
    if profile["new_voter"]:
        items.append("Read the check-in and ballot-casting steps before voting for the first time.")
    return items


def export_plan(profile: dict, items: list[str]) -> str:
    lines = [
        "# Election Guide Action Plan",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Location: {profile['location'] or 'Not specified'}",
        f"Election type: {profile['election_type']}",
        f"Preferred voting method: {profile['method']}",
        "",
        "Important: verify all deadlines and requirements with your official election office.",
        "",
        "## Checklist",
    ]
    lines.extend(f"- [ ] {item}" for item in items)
    return "\n".join(lines)


def readiness_score(values: dict) -> int:
    completed = sum(1 for value in values.values() if value)
    return round((completed / len(values)) * 100)


st.set_page_config(
    page_title="Election Guide Assistant",
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
    .timeline-card { border: 1px solid #dbe6e4; border-radius: 8px; padding: 1rem; min-height: 165px; background: #fbfdfd; }
    .timeline-card strong { color: #17324d; }
    .metric-card { border: 1px solid #dbe6e4; border-radius: 8px; padding: 1rem; background: #ffffff; }
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
                    "Rules vary by location, so I keep explanations general and point you toward official local sources for exact deadlines.",
                ],
                "next": "Use the Plan Builder tab when you want a personalized checklist.",
            },
        }
    ]

with st.sidebar:
    st.subheader("Ask About")
    for label, question in TOPICS.items():
        if st.button(label, use_container_width=True):
            add_assistant_answer(question)

    st.divider()
    st.subheader("Readiness Tracker")
    readiness_values = {}
    for title, detail in PREP_STEPS:
        readiness_values[title] = st.checkbox(title, help=detail)
    score = readiness_score(readiness_values)
    st.progress(score / 100)
    st.caption(f"{score}% ready based on checked steps")

left, right = st.columns([1.15, 0.85])
with left:
    if HERO_IMAGE.exists():
        st.image(str(HERO_IMAGE), use_container_width=True)
with right:
    st.markdown('<div class="eyebrow">Challenge 2</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Election Guide Assistant</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="muted">An interactive civic assistant that explains election processes, builds a voting plan, teaches key terms, and helps users prepare without relying on partisan or outdated information.</p>',
        unsafe_allow_html=True,
    )
    metric_cols = st.columns(3)
    metric_cols[0].metric("Topics", len(TOPICS))
    metric_cols[1].metric("Plan steps", len(PREP_STEPS))
    metric_cols[2].metric("Quiz items", len(QUIZ))

st.divider()

guide_tab, plan_tab, timeline_tab, quiz_tab, glossary_tab = st.tabs(
    ["Assistant", "Plan Builder", "Timeline", "Quiz", "Glossary"]
)

with guide_tab:
    st.subheader("Interactive Helper")
    quick_cols = st.columns(4)
    quick_questions = [
        "What are the main steps to vote?",
        "How do election timelines usually work?",
        "What should I check before election day?",
        "What is a provisional ballot?",
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

with plan_tab:
    st.subheader("Personalized Voting Plan")
    st.caption("This creates a practical checklist. It does not replace official local election information.")

    profile_cols = st.columns(2)
    with profile_cols[0]:
        location = st.text_input("State, county, or city", placeholder="Example: Travis County, Texas")
        election_type = st.selectbox(
            "Election type",
            ["General", "Primary", "Local", "Special", "School board", "Not sure"],
        )
        method = st.radio(
            "Preferred voting method",
            ["Vote on election day", "Vote early in person", "Vote by mail or absentee"],
            horizontal=False,
        )
    with profile_cols[1]:
        target_date = st.date_input("Election day or target date", value=date.today())
        new_voter = st.toggle("I am a first-time voter")
        needs_accessibility = st.toggle("I may need accessibility, language, or other assistance")
        has_sample_ballot = st.toggle("I already found my sample ballot")

    profile = {
        "location": location,
        "election_type": election_type,
        "method": method,
        "target_date": target_date,
        "new_voter": new_voter,
        "needs_accessibility": needs_accessibility,
        "has_sample_ballot": has_sample_ballot,
    }
    items = plan_items(profile)
    if has_sample_ballot:
        items.append("Use your sample ballot to research each contest before voting.")
    else:
        items.append("Find your sample ballot or voter guide from an official election source.")

    st.markdown("#### Recommended next actions")
    for index, item in enumerate(items, start=1):
        st.checkbox(item, key=f"plan_item_{index}")

    days_until = (target_date - date.today()).days
    if days_until > 0:
        st.success(f"{days_until} day(s) until your selected date. Use official sources for real deadlines.")
    elif days_until == 0:
        st.warning("Your selected date is today. Confirm polling hours and requirements before leaving.")
    else:
        st.info("Your selected date is in the past. Use this as a learning or review plan.")

    st.download_button(
        "Download action plan",
        data=export_plan(profile, items),
        file_name="election-guide-action-plan.md",
        mime="text/markdown",
        use_container_width=True,
    )

with timeline_tab:
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

    st.markdown("#### What to verify locally")
    verify_cols = st.columns(3)
    verify_cols[0].info("Registration deadlines and eligibility rules")
    verify_cols[1].info("Voting method availability and ballot return rules")
    verify_cols[2].info("Polling places, hours, ID rules, and final result certification")

with quiz_tab:
    st.subheader("Election Process Quiz")
    st.caption("A short check for understanding. Answers are educational, not legal advice.")
    quiz_score = 0
    for index, item in enumerate(QUIZ, start=1):
        selected = st.radio(
            item["question"],
            item["options"],
            key=f"quiz_{index}",
            index=None,
        )
        if selected:
            if selected == item["answer"]:
                st.success(f"Correct. {item['why']}")
                quiz_score += 1
            else:
                st.error(f"Not quite. {item['why']}")
    st.metric("Quiz score", f"{quiz_score}/{len(QUIZ)}")

with glossary_tab:
    st.subheader("Election Terms Glossary")
    search = st.text_input("Filter glossary", placeholder="Search terms like provisional, canvass, certification...")
    filtered_terms = {
        term: meaning
        for term, meaning in GLOSSARY.items()
        if search.lower() in term.lower() or search.lower() in meaning.lower()
    }
    for term, meaning in filtered_terms.items():
        with st.expander(term, expanded=not search):
            st.write(meaning)

    st.divider()
    st.subheader("Official Source Reminder")
    st.write(
        "For exact requirements, users should check their official state or local election office. "
        "This assistant explains the process and helps organize questions to verify."
    )

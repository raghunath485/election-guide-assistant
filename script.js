const topics = [
  {
    label: "Register to Vote",
    question: "How does voter registration usually work?"
  },
  {
    label: "Election Timeline",
    question: "How do election timelines usually work?"
  },
  {
    label: "Voting Options",
    question: "What are common voting options?"
  },
  {
    label: "Ballot Prep",
    question: "How should I prepare before marking a ballot?"
  },
  {
    label: "Election Day",
    question: "What should I expect on election day?"
  },
  {
    label: "After Voting",
    question: "What happens after people vote?"
  }
];

const prepSteps = [
  {
    title: "Check eligibility",
    detail: "Confirm age, residency, citizenship, and any local requirements."
  },
  {
    title: "Register or update",
    detail: "Make sure your name, address, and party preference rules are current."
  },
  {
    title: "Choose how to vote",
    detail: "Review in-person, early, mail, or absentee options available locally."
  },
  {
    title: "Review the ballot",
    detail: "Read candidate and measure information from official sources."
  },
  {
    title: "Make a voting plan",
    detail: "Know deadlines, ID rules, polling hours, and transportation."
  }
];

const timeline = [
  {
    title: "1. Registration Window",
    body: "Voters register, update addresses, or confirm status before the local deadline."
  },
  {
    title: "2. Ballot Information",
    body: "Election offices publish candidate lists, ballot measures, sample ballots, and voter guides."
  },
  {
    title: "3. Early or Mail Voting",
    body: "Some places open early voting sites or send mail ballots before election day."
  },
  {
    title: "4. Election Day",
    body: "Polling places open for in-person voting, check-in, ballot marking, and ballot casting."
  },
  {
    title: "5. Counting and Certification",
    body: "Officials verify, count, audit where required, report results, and certify the final outcome."
  }
];

const answers = [
  {
    keywords: ["register", "registration", "update", "eligibility", "eligible"],
    title: "Voter registration",
    points: [
      "Check whether you meet your location's eligibility rules.",
      "Register online, by mail, or in person if your election office offers those methods.",
      "Update your registration when your name, address, or party preference changes.",
      "Look up the official registration deadline for your state, county, or election authority."
    ]
  },
  {
    keywords: ["timeline", "deadline", "date", "calendar", "schedule"],
    title: "Election timelines",
    points: [
      "Timelines usually start with registration and ballot information deadlines.",
      "Early voting or mail ballot windows may open before election day.",
      "Election day has fixed polling hours set by local law.",
      "Results may be unofficial at first, then finalized through canvassing and certification."
    ]
  },
  {
    keywords: ["option", "early", "mail", "absentee", "in person", "polling"],
    title: "Voting options",
    points: [
      "Common options include election-day in-person voting, early in-person voting, mail voting, or absentee voting.",
      "Availability depends on local rules, deadlines, and eligibility requirements.",
      "If voting by mail, check request, return, signature, and postmark rules carefully.",
      "If voting in person, confirm your polling place before leaving."
    ]
  },
  {
    keywords: ["ballot", "candidate", "measure", "prepare", "research"],
    title: "Ballot preparation",
    points: [
      "Find a sample ballot from an official election website when available.",
      "Read neutral voter guides, candidate statements, and measure explanations.",
      "Note contests where you need more information before voting.",
      "Bring any allowed notes or sample ballot according to your local rules."
    ]
  },
  {
    keywords: ["day", "expect", "id", "place", "poll"],
    title: "Election day",
    points: [
      "Confirm your polling location and hours before you go.",
      "Bring any identification or documents required in your area.",
      "Check in with poll workers, receive or access your ballot, mark choices, and cast it.",
      "Ask a poll worker for help if a machine, ballot, or check-in issue comes up."
    ]
  },
  {
    keywords: ["after", "count", "results", "certify", "certification", "audit"],
    title: "After voting",
    points: [
      "Election-night results are often unofficial and can change as valid ballots are counted.",
      "Officials may verify signatures, process provisional ballots, and conduct required checks.",
      "Certification is the formal step that makes final results official.",
      "Use official election office channels for final results and recount information."
    ]
  }
];

const fallbackAnswer = {
  title: "A simple way to think about it",
  points: [
    "Start by identifying your location and the election you care about.",
    "Check registration, voting options, ballot information, and deadlines from official sources.",
    "Make a plan for when, where, and how you will vote.",
    "For exact dates and rules, use your state or local election office website."
  ]
};

const chatLog = document.querySelector("#chatLog");
const chatForm = document.querySelector("#chatForm");
const questionInput = document.querySelector("#questionInput");
const topicList = document.querySelector("#topicList");
const stepList = document.querySelector("#stepList");
const timelineGrid = document.querySelector("#timelineGrid");
const resetChat = document.querySelector("#resetChat");

function renderTopics() {
  topicList.innerHTML = topics
    .map((topic) => `<button class="topic-button" type="button" data-question="${topic.question}">${topic.label}</button>`)
    .join("");
}

function renderSteps() {
  stepList.innerHTML = prepSteps
    .map((step, index) => `
      <label class="step-item">
        <input type="checkbox" aria-label="${step.title}" data-step="${index}">
        <span>
          <strong>${step.title}</strong>
          <span>${step.detail}</span>
        </span>
      </label>
    `)
    .join("");
}

function renderTimeline() {
  timelineGrid.innerHTML = timeline
    .map((item) => `
      <article class="timeline-card">
        <strong>${item.title}</strong>
        <p>${item.body}</p>
      </article>
    `)
    .join("");
}

function addMessage(role, html) {
  const message = document.createElement("article");
  message.className = `message ${role}`;
  message.innerHTML = html;
  chatLog.append(message);
  chatLog.scrollTop = chatLog.scrollHeight;
}

function addTextMessage(role, text) {
  const message = document.createElement("article");
  message.className = `message ${role}`;
  message.textContent = text;
  chatLog.append(message);
  chatLog.scrollTop = chatLog.scrollHeight;
}

function answerFor(question) {
  const normalized = question.toLowerCase();
  return answers.find((answer) => answer.keywords.some((keyword) => normalized.includes(keyword))) || fallbackAnswer;
}

function formatAnswer(answer) {
  const items = answer.points.map((point) => `<li>${point}</li>`).join("");
  return `<strong>${answer.title}</strong><ul>${items}</ul>`;
}

function ask(question) {
  const trimmed = question.trim();
  if (!trimmed) return;

  addTextMessage("user", trimmed);
  addMessage("assistant", formatAnswer(answerFor(trimmed)));
}

function resetConversation() {
  chatLog.innerHTML = "";
  addMessage(
    "assistant",
    "<strong>Hi, I can help you understand the election process.</strong><ul><li>Ask about registration, timelines, voting options, ballot prep, election day, or results.</li><li>Rules vary by location, so I will keep explanations general and remind you where official deadlines matter.</li></ul>"
  );
  questionInput.focus();
}

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();
  ask(questionInput.value);
  questionInput.value = "";
});

document.addEventListener("click", (event) => {
  const button = event.target.closest("[data-question]");
  if (!button) return;
  ask(button.dataset.question);
});

resetChat.addEventListener("click", resetConversation);

renderTopics();
renderSteps();
renderTimeline();
resetConversation();

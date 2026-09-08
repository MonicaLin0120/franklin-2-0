import streamlit as st

st.set_page_config(
    page_title="Franklin 2.0",
    page_icon="📜",
    layout="wide"
)
st.markdown("""
<style>
div[data-testid="stExpander"] summary * {
    font-size: 22px !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

virtues = {
    "Temperance": "Control how much you consume and avoid excess.",
    "Silence": "Speak when there is a useful reason to speak instead of talking unnecessarily.",
    "Order": "Keep your belongings and time organized.",
    "Resolution": "Decide what you need to do and follow through with it.",
    "Frugality": "Spend money carefully and do not waste resources.",
    "Industry": "Use your time productively and avoid wasting it.",
    "Sincerity": "Be honest and do not deceive others in ways that cause harm.",
    "Justice": "Do not harm others, and do not ignore responsibilities you have toward them.",
    "Moderation": "Avoid extreme reactions, especially when someone has wronged you.",
    "Cleanliness": "Keep yourself, your clothing, and your surroundings clean.",
    "Tranquillity": "Do not become overly upset about small problems or things you cannot control.",
    "Chastity": "Franklin believed sexual behavior should be controlled and should not harm yourself or another person.",
    "Humility": "Franklin connects humility with following the examples of Jesus and Socrates rather than being overly proud of yourself."
}

scenarios = [
    {
        "title": "Just One More Video",
        "emoji": "📱",
        "virtues": "Temperance • Order • Resolution • Industry",

        "situation":
        """
        A student has an important test tomorrow. They planned to stop studying
        at 11:00 p.m. and go to sleep, but during a short break, they start
        watching TikTok. At 1:30 a.m., they are still scrolling.

        They know they should stop, but watching videos helps them relax when
        they are stressed.
        """,

        "connection":
        """
        **Order** means giving each responsibility its proper time.

        **Resolution** means doing what you have decided you ought to do.

        **Industry** means not wasting time on unnecessary actions.

        Franklin also believed that knowing what is right is not enough.
        People need to develop habits that help them actually do it.

        The student already knows they should stop scrolling. The problem is
        turning that knowledge into a habit.
        """,

        "franklin":
        """
        Franklin would probably tell the student to put the phone away and
        follow the schedule they created.

        He would also encourage the student to examine the mistake afterward
        and keep working on the same weakness until a better habit develops.
        """,

        "modern":
        """
        ### Partly Agree

        Having self-control and a schedule is useful, but relying only on
        willpower may not work with modern technology.

        We would also use tools such as:

        - App limits
        - Do Not Disturb
        - Keeping the phone away from the study area
        - Scheduling some time for entertainment
        """,

        "complication":
        """
        **If social media genuinely helps someone relax after a stressful day,
        when does healthy relaxation become a failure of self-discipline?**
        """
    },

    {
        "title": "The Secret",
        "emoji": "🤫",
        "virtues": "Silence • Sincerity • Justice",

        "situation":
        """
        A friend privately tells you why they recently ended a relationship
        and asks you not to tell anyone.

        Later, people at school begin spreading a false story that makes your
        friend look terrible.

        You could correct the rumor, but doing so might reveal information your
        friend trusted you to keep private.
        """,

        "connection":
        """
        **Silence** means speaking only when your words may benefit yourself
        or others.

        **Sincerity** means avoiding harmful deceit.

        **Justice** means not harming someone through your actions or through
        failing to do something that is your duty.

        This creates a conflict between Franklin's virtues. Silence suggests
        protecting the friend's private information, while Sincerity and
        Justice might suggest correcting a harmful lie.
        """,

        "franklin":
        """
        Franklin would probably tell the person not to participate in gossip
        or spread private information.

        However, they could correct the false rumor without revealing
        unnecessary details.
        """,

        "modern":
        """
        ### Partly Agree

        We would first talk to the friend and ask how they want the situation
        handled.

        If the rumor is seriously hurting them, we could say that the story
        is false without explaining the private details.
        """,

        "complication":
        """
        **When does protecting someone's secret become less important than
        protecting their reputation?**
        """
    },

    {
        "title": "Who Gets the Credit?",
        "emoji": "🏆",
        "virtues": "Moderation • Tranquillity • Humility",

        "situation":
        """
        You do most of a group project, but during the presentation your
        teacher praises another student for an idea that was actually yours.

        After class, the teacher asks whether everyone contributed equally.
        """,

        "connection":
        """
        **Moderation** means avoiding extreme reactions when someone has
        wronged you.

        **Tranquillity** means not becoming overly disturbed by small problems
        or conflicts.

        **Humility** encourages a person not to become controlled by pride.

        However, being humble does not necessarily mean allowing another
        person to take credit for your work.
        """,

        "franklin":
        """
        Franklin would probably tell the student to remain calm and avoid
        angrily attacking the teammate.

        The student should explain their contribution honestly without
        exaggerating it or trying to embarrass anyone.
        """,

        "modern":
        """
        ### Agree

        We would explain our contribution honestly, but focus on correcting
        the misunderstanding rather than attacking the teammate.

        A person can stand up for their work without becoming aggressive or
        obsessed with receiving praise.
        """,

        "complication":
        """
        **How can you practice humility while still making sure other people
        do not receive credit for your work?**
        """
    },

    {
        "title": "AI Wrote It for Me",
        "emoji": "🤖",
        "virtues": "Industry • Sincerity • Resolution",

        "situation":
        """
        A student has an essay due tomorrow morning but has barely started it.

        An AI tool can generate a strong essay in seconds.

        The student could change some of the wording, submit it, and probably
        never get caught.
        """,

        "connection":
        """
        **Industry** means using time for useful purposes and cutting off
        unnecessary actions.

        **Sincerity** means avoiding harmful deceit.

        **Resolution** means following through on what you know you ought to do.

        The problem is not simply whether AI is good or bad. The real question
        is whether using AI to replace your own work violates Franklin's ideas
        about honesty, effort, and responsibility.
        """,

        "franklin":
        """
        Franklin would probably tell the student to complete the work
        honestly, even if the final essay is not as good.

        He would probably also see the student's procrastination as a failure
        of Industry and Resolution.
        """,

        "modern":
        """
        ### Partly Agree

        Submitting an AI-generated essay as your own would be dishonest.

        However, completely refusing to use AI may not make sense today.

        If the teacher allows it, AI could help:

        - Brainstorm ideas
        - Organize an outline
        - Give feedback
        - Help improve clarity

        The student should still do the actual thinking and writing.
        """,

        "complication":
        """
        **If AI helps someone develop ideas and they understand everything
        they eventually submit, at what point does assistance become cheating?**
        """
    },

    {
        "title": "The Perfect Room",
        "emoji": "🧹",
        "virtues": "Cleanliness • Moderation • Tranquillity",

        "situation":
        """
        You share a room with someone who leaves clothes on the floor,
        food containers on their desk, and belongings everywhere.

        You value a clean environment, so you repeatedly ask them to clean.

        Eventually, you become so obsessed with keeping everything perfect
        that you are arguing almost every day.

        The room is becoming cleaner, but your relationship is becoming worse.
        """,

        "connection":
        """
        **Cleanliness** means keeping yourself, your clothes, and your living
        space clean.

        **Moderation** means avoiding extremes, even when you believe your
        frustration is reasonable.

        **Tranquillity** means not becoming overly disturbed by small or
        unavoidable problems.

        Franklin himself struggled with trying to follow some virtues perfectly,
        especially Order.
        """,

        "franklin":
        """
        Franklin would probably encourage reasonable cleanliness while also
        recognizing that demanding perfection can become excessive.

        The roommates should create reasonable standards instead of arguing
        over every small mess.
        """,

        "modern":
        """
        ### Partly Agree

        Real hygiene problems should be addressed, especially old food or
        serious mess.

        However, a few clothes on the floor are probably not worth constantly
        damaging the relationship.

        The roommates should agree on basic standards and compromise on
        smaller differences.
        """,

        "complication":
        """
        **If pursuing one virtue too aggressively causes you to violate another
        virtue, is it still virtuous behavior?**
        """
    },

    {
        "title": "The Group Chat",
        "emoji": "💬",
        "virtues": "Tranquillity • Silence • Moderation • Humility",

        "situation":
        """
        Someone insults you publicly in a group chat.

        Several people have already seen and reacted to the message.

        You are angry and have written a response that would embarrass the
        other person even more.
        """,

        "connection":
        """
        **Tranquillity** means not becoming disturbed by small problems or
        common and unavoidable events.

        **Moderation** means avoiding extreme reactions and not resenting
        injuries as much as you think they deserve.

        **Silence** encourages people to avoid speech that does not benefit
        themselves or others.
        """,

        "franklin":
        """
        Franklin would probably tell the person not to send the angry response
        immediately.

        They should calm down and avoid turning the conflict into something
        bigger simply to defend their pride.
        """,

        "modern":
        """
        ### Mostly Agree

        Responding while angry can make the situation worse.

        However, we do not think someone should always stay silent.

        If the behavior continues, the person could:

        - Calmly set a boundary
        - Speak privately to the other person
        - Ask for help if the situation becomes bullying
        """,

        "complication":
        """
        **When does staying calm show maturity, and when does staying silent
        allow someone to continue treating you badly?**
        """
    }
]

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "scenario" not in st.session_state:
    st.session_state.scenario = 0

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("📜 Franklin 2.0")

if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.page = "Home"

if st.sidebar.button("📖 13 Virtues", use_container_width=True):
    st.session_state.page = "Virtues"

if st.sidebar.button("✅ Virtue Tracker", use_container_width=True):
    st.session_state.page = "Tracker"

st.sidebar.divider()

st.sidebar.caption(
    "UNDERSTAND → APPLY → QUESTION → EVALUATE"
)

# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

if st.session_state.page == "Home":

    st.title("📜 Franklin 2.0")
    st.subheader("Modern Virtue Survival Kit")

    st.write(
        """
        Benjamin Franklin believed people could improve themselves by
        identifying weaknesses, practicing better habits, and examining their
        behavior.

        **Can Franklin's eighteenth-century virtues still work in modern life?**
        """
    )

    st.divider()

    st.header("Choose a Modern-Life Challenge")

    col1, col2, col3 = st.columns(3)

    columns = [col1, col2, col3]

    for i, scenario in enumerate(scenarios):

        with columns[i % 3]:

            st.markdown(
                f"### {scenario['emoji']} Challenge {i + 1}"
            )

            st.write(
                f"**{scenario['title']}**"
            )

            if st.button(
                "Open Challenge",
                key=f"challenge_{i}",
                use_container_width=True
            ):
                st.session_state.scenario = i
                st.session_state.page = "Scenario"
                st.rerun()

# ---------------------------------------------------------
# SCENARIO
# ---------------------------------------------------------

elif st.session_state.page == "Scenario":

    scenario = scenarios[st.session_state.scenario]
    number = st.session_state.scenario + 1

    st.caption(f"MODERN LIFE CHALLENGE {number}")

    st.title(
        f"{scenario['emoji']} {scenario['title']}"
    )

    st.info(
        f"**Franklin's Virtues:** {scenario['virtues']}"
    )

    st.header("1. The Situation")

    st.markdown(
    f"""
    <style>
    .big-situation {{
        font-size: 24px;
        line-height: 1.7;
    }}
    </style>

    <div class="big-situation">
    {scenario["situation"].strip().replace(chr(10), "<br>")}
    </div>
    """,
    unsafe_allow_html=True
)

    st.divider()

    st.header(
        "What would Franklin tell this person to do?"
    )

    st.write(
        "Think about your answer before opening the sections below."
    )

    with st.expander(
    "📖 2. Connection to Franklin"
    ):
        st.markdown(
            f"""
            <div style="font-size: 24px; line-height: 1.7;">
            {scenario["connection"].strip().replace(chr(10), "<br>")}
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.expander(
        "🤔 3. Franklin's Solution"
    ):
        st.markdown(
            f"""
            <div style="font-size: 24px; line-height: 1.7;">
            {scenario["franklin"].strip().replace(chr(10), "<br>")}
            </div>
         """,
            unsafe_allow_html=True
        )

    with st.expander(
        "💡 4. Our Modern Solution"
    ):
        st.markdown(
            f"""
            <div style="font-size: 24px; line-height: 1.7;">
            {scenario["modern"].strip().replace(chr(10), "<br>")}
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.expander(
        "❓ 5. The Complication"
    ):
        st.markdown(
            f"""
            <div style="font-size: 24px; line-height: 1.7;">
            {scenario["complication"].strip().replace(chr(10), "<br>")}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    left, middle, right = st.columns(3)

    with left:
        if st.session_state.scenario > 0:
            if st.button(
                "← Previous",
                use_container_width=True
            ):
                st.session_state.scenario -= 1
                st.rerun()

    with middle:
        if st.button(
            "🏠 Back to Challenges",
            use_container_width=True
        ):
            st.session_state.page = "Home"
            st.rerun()

    with right:
        if st.session_state.scenario < len(scenarios) - 1:
            if st.button(
                "Next →",
                use_container_width=True
            ):
                st.session_state.scenario += 1
                st.rerun()

# ---------------------------------------------------------
# VIRTUES
# ---------------------------------------------------------

elif st.session_state.page == "Virtues":

    st.title("📖 Franklin's Thirteen Virtues")

    st.write(
        """
        Franklin created thirteen virtues that he believed could help him
        become a better person.
        """
    )

    st.divider()

    for number, (name, meaning) in enumerate(
        virtues.items(),
        start=1
    ):

        with st.expander(
            f"{number}. {name}"
        ):
            st.write(
                meaning
            )

# ---------------------------------------------------------
# TRACKER
# ---------------------------------------------------------

elif st.session_state.page == "Tracker":

    st.title("✅ Franklin's Virtue Tracker")

    st.write(
        """
        Franklin kept track of his mistakes and focused on improving one
        virtue at a time.

        This is a modern version of his idea.
        """
    )

    st.divider()

    selected = st.selectbox(
        "Choose today's virtue:",
        list(virtues.keys())
    )

    st.info(
        virtues[selected]
    )

    st.subheader(
        f"Did you practice {selected} successfully today?"
    )

    yes, no = st.columns(2)

    with yes:

        if st.button(
            "✅ Yes",
            use_container_width=True
        ):

            st.success(
                f"Nice work practicing {selected}. "
                "Keep strengthening the habit."
            )

    with no:

        if st.button(
            "❌ Not Yet",
            use_container_width=True
        ):

            st.warning(
                f"You struggled with {selected} today. "
                "Franklin's method was about noticing mistakes "
                "and trying again."
            )

    st.divider()

    st.markdown(
        """
        ### Franklin's Main Idea

        The goal is not necessarily to become perfect.

        The goal is to **notice your habits, examine your behavior,
        and deliberately try to improve.**
        """
    )
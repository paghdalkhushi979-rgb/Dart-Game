import streamlit as st
import random
import math

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Dart Name Picker",
    page_icon="🎯",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "names" not in st.session_state:
    st.session_state.names = [
        "Khushi",
        "Trusha",
        "Manasvi",
        "Yashvi",
        "Kajal",
        "Pritam",
        "Krish",
        "Paresh",
        "Deepak",
        "Meet"
    ]

if "winner" not in st.session_state:
    st.session_state.winner = None

if "dart_number" not in st.session_state:
    st.session_state.dart_number = None

if "history" not in st.session_state:
    st.session_state.history = []

if "no_repeat" not in st.session_state:
    st.session_state.no_repeat = False


# =========================================================
# PREMIUM MIDNIGHT NAVY BACKGROUND
# ONLY UI / BACKGROUND IS CHANGED
# =========================================================

st.html("""
<style>

.stApp {

    background:
        radial-gradient(
            circle at 50% 42%,
            rgba(35, 60, 82, 0.16),
            transparent 28%
        ),
        radial-gradient(
            circle at 5% 20%,
            rgba(20, 38, 55, 0.20),
            transparent 30%
        ),
        radial-gradient(
            circle at 95% 20%,
            rgba(25, 45, 62, 0.16),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #05080D 0%,
            #08111A 50%,
            #05080D 100%
        );

    color: #F2F5F7;
}


/* =====================================================
   MAIN AREA
   ===================================================== */

.block-container {

    max-width: 1250px;

    padding-top: 25px;

    padding-bottom: 45px;
}


/* =====================================================
   HEADER
   ===================================================== */

.arena-title {

    text-align: center;

    font-size: clamp(40px, 5vw, 58px);

    font-weight: 900;

    letter-spacing: 1px;

    margin-bottom: 5px;
}


.arena-title .white {

    color: #F5F7F8;
}


.arena-title .accent {

    color: #8DA5B8;
}


.arena-subtitle {

    text-align: center;

    color: #9AAAB8;

    font-size: 16px;

    margin-bottom: 12px;
}


.arena-line {

    width: 180px;

    height: 1px;

    margin: 10px auto 13px auto;

    background:
        linear-gradient(
            90deg,
            transparent,
            #40586C,
            transparent
        );
}


/* =====================================================
   STAT CARDS
   ===================================================== */

.stat-card {

    background:
        rgba(10, 18, 27, 0.86);

    border:
        1px solid rgba(80, 105, 125, 0.28);

    border-radius: 17px;

    padding: 15px 10px;

    text-align: center;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.32);
}


.stat-number {

    font-size: 29px;

    font-weight: 900;

    color: #F4F6F7;
}


.stat-label {

    font-size: 13px;

    color: #95A4B1;
}


/* =====================================================
   PANEL TITLE
   ===================================================== */

.panel-title {

    font-size: 19px;

    font-weight: 850;

    color: #E8EDF1;

    margin-bottom: 12px;
}


/* =====================================================
   PARTICIPANT ITEM
   ===================================================== */

.participant-item {

    background:
        rgba(12, 23, 34, 0.78);

    border:
        1px solid rgba(72, 96, 116, 0.25);

    border-radius: 10px;

    padding: 8px 11px;

    margin: 5px 0;

    color: #D7E0E6;
}


/* =====================================================
   DART ARENA
   ===================================================== */

.arena {

    position: relative;

    min-height: 610px;

    padding-top: 5px;
}


.arena-glow {

    position: absolute;

    width: 520px;

    height: 520px;

    left: 50%;

    top: 47%;

    transform:
        translate(-50%, -50%);

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(35, 62, 83, 0.15),
            rgba(20, 40, 56, 0.06) 45%,
            transparent 72%
        );

    pointer-events: none;
}


/* =====================================================
   SUBTLE BACKGROUND TARGETS
   ===================================================== */

.side-target {

    position: absolute;

    width: 125px;

    height: 125px;

    border-radius: 50%;

    border:
        10px solid rgba(65, 91, 111, 0.08);

    box-shadow:
        0 0 0 8px rgba(5, 10, 16, 0.65),
        0 0 0 16px rgba(65, 91, 111, 0.04);

    opacity: 0.75;
}


.side-target.left {

    left: -55px;

    top: 105px;
}


.side-target.right {

    right: -55px;

    top: 105px;
}


/* =====================================================
   DARTBOARD
   ===================================================== */

.dartboard {

    width: min(430px, 72vw);

    height: min(430px, 72vw);

    margin: 28px auto 25px auto;

    border-radius: 50%;

    position: relative;

    background:
        repeating-conic-gradient(
            from 0deg,
            #16191C 0deg 9deg,
            #E5E0D5 9deg 18deg
        );

    border:
        12px solid #0B1015;

    box-shadow:

        0 0 0 3px #2A3B49,

        0 0 35px rgba(50, 72, 90, 0.18),

        0 25px 60px rgba(0,0,0,0.72);
}


/* =====================================================
   CENTER OF BOARD
   ===================================================== */

.dartboard::before {

    content: "";

    position: absolute;

    inset: 0;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,

            #C82030 0px,

            #C82030 23px,

            #111416 24px,

            #111416 39px,

            transparent 40px
        );
}


/* =====================================================
   BOARD RINGS
   ===================================================== */

.dartboard::after {

    content: "";

    position: absolute;

    inset: 12%;

    border-radius: 50%;

    border:
        7px solid #C82030;

    box-shadow:

        inset 0 0 0 7px #111416,

        inset 0 0 0 14px #25855A;
}


/* =====================================================
   BOARD LINES
   ===================================================== */

.board-line {

    position: absolute;

    width: 2px;

    height: 100%;

    left: 50%;

    top: 0;

    background:
        rgba(0,0,0,0.35);

    transform-origin: center;

    z-index: 3;
}


/* =====================================================
   NAMES ON BOARD
   ===================================================== */

.name {

    position: absolute;

    background:
        rgba(8, 14, 21, 0.96);

    color: #F0F4F6;

    border:
        1px solid rgba(115, 137, 153, 0.35);

    padding: 6px 9px;

    border-radius: 13px;

    font-weight: 800;

    font-size: 12px;

    box-shadow:
        0 5px 14px rgba(0,0,0,0.52);

    transform:
        translate(-50%, -50%);

    white-space: nowrap;

    z-index: 5;
}


/* =====================================================
   DART
   ===================================================== */

.dart {

    position: absolute;

    font-size: 46px;

    transform:
        translate(-50%, -50%)
        rotate(-25deg);

    z-index: 10;

    filter:
        drop-shadow(
            0 5px 8px rgba(0,0,0,0.8)
        );
}


/* =====================================================
   WINNER BOX
   ===================================================== */

.winner-box {

    margin: 15px auto 18px auto;

    max-width: 520px;

    padding: 17px 20px;

    text-align: center;

    border-radius: 18px;

    background:
        rgba(13, 25, 37, 0.92);

    border:
        1px solid rgba(92, 120, 140, 0.42);

    box-shadow:
        0 12px 35px rgba(0,0,0,0.38);
}


.winner-label {

    color: #9EB4C5;

    font-size: 14px;

    font-weight: 800;
}


.winner-name {

    color: #F4F7F8;

    font-size: 35px;

    font-weight: 900;

    margin-top: 3px;
}


/* =====================================================
   HISTORY
   ===================================================== */

.history-item {

    padding: 9px 11px;

    margin: 5px 0;

    border-radius: 10px;

    background:
        rgba(14, 27, 40, 0.72);

    border:
        1px solid rgba(72, 96, 116, 0.20);

    color: #D6E0E6;
}


/* =====================================================
   STREAMLIT BUTTONS
   ===================================================== */

div.stButton > button {

    background:
        #0C1723;

    color:
        #EAF0F3;

    border:
        1px solid #334C60;

    border-radius:
        10px;

    font-weight:
        700;

    min-height:
        43px;

    transition:
        all 0.2s ease;
}


div.stButton > button:hover {

    background:
        #122335;

    border-color:
        #5B7488;

    color:
        #FFFFFF;
}


/* =====================================================
   TEXT INPUT
   ===================================================== */

div[data-baseweb="input"] {

    background:
        #0C1723;

    border-radius:
        10px;
}


div[data-baseweb="input"] input {

    color:
        #EAF0F3;
}


/* =====================================================
   EXPANDERS
   ===================================================== */

div[data-testid="stExpander"] {

    background:
        rgba(8, 16, 25, 0.82);

    border:
        1px solid rgba(65, 91, 111, 0.30);

    border-radius:
        12px;

    margin-bottom:
        10px;
}


/* =====================================================
   FOOTER
   ===================================================== */

.tip {

    text-align: center;

    color: #687B8A;

    font-size: 13px;

    margin-top: 25px;
}

</style>
""")


# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="arena-title">

    <span class="white">
        🎯 Dart
    </span>

    <span class="accent">
        Name Picker
    </span>

</div>

<div class="arena-line"></div>

<div class="arena-subtitle">

    Throw the dart and let the game choose your participant!

</div>
""")


# =========================================================
# STATISTICS
# =========================================================

s1, s2, s3 = st.columns(3)


with s1:

    st.html(f"""
    <div class="stat-card">

        <div class="stat-number">
            {len(st.session_state.names)}
        </div>

        <div class="stat-label">
            👥 Participants
        </div>

    </div>
    """)


with s2:

    st.html(f"""
    <div class="stat-card">

        <div class="stat-number">
            {len(st.session_state.history)}
        </div>

        <div class="stat-label">
            🎯 Total Throws
        </div>

    </div>
    """)


with s3:

    st.html(f"""
    <div class="stat-card">

        <div class="stat-number">
            {len(set(st.session_state.history))}
        </div>

        <div class="stat-label">
            🏆 Winners
        </div>

    </div>
    """)


st.write("")


# =========================================================
# MAIN LAYOUT
# =========================================================

left, center, right = st.columns(
    [1.05, 1.7, 1.05],
    gap="large"
)


# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.html("""
    <div class="panel-title">
        👤 Add Participant
    </div>
    """)


    new_name = st.text_input(
        "Name",
        placeholder="e.g. Rahul",
        label_visibility="collapsed"
    )


    add = st.button(
        "➕ Add Participant",
        use_container_width=True
    )


    if add:

        clean_name = new_name.strip()


        if clean_name == "":

            st.warning(
                "Please enter a name."
            )


        elif clean_name.lower() in [
            n.lower()
            for n in st.session_state.names
        ]:

            st.warning(
                "Name already exists."
            )


        else:

            st.session_state.names.append(
                clean_name
            )

            st.rerun()


    st.html("""
    <div class="panel-title"
         style="margin-top:20px;">

        👥 Participants

    </div>
    """)


    for i, name in enumerate(
        st.session_state.names
    ):

        c1, c2 = st.columns(
            [5, 1]
        )


        with c1:

            st.html(
                f"""
                <div class="participant-item">

                    {i + 1}. {name}

                </div>
                """
            )


        with c2:

            remove = st.button(
                "🗑️",
                key=f"remove_{i}"
            )


            if remove:

                st.session_state.names.pop(i)


                if (
                    st.session_state.winner
                    == name
                ):

                    st.session_state.winner = None

                    st.session_state.dart_number = None


                st.rerun()


# =========================================================
# CENTER DARTBOARD
# =========================================================

with center:

    st.html("""
    <div class="arena">

        <div class="arena-glow"></div>

        <div class="side-target left"></div>

        <div class="side-target right"></div>

    </div>
    """)


    names = st.session_state.names


    if names:

        total = len(names)

        positions = []

        radius = 43


        for i in range(total):

            angle = (
                (360 / total) * i
            ) - 90


            left_pos = (
                50
                +
                radius
                *
                math.cos(
                    math.radians(angle)
                )
            )


            top_pos = (
                50
                +
                radius
                *
                math.sin(
                    math.radians(angle)
                )
            )


            positions.append(
                (
                    left_pos,
                    top_pos
                )
            )


        board_html = """
        <div class="dartboard">
        """


        line_step = max(
            1,
            int(360 / total)
        )


        for angle in range(
            0,
            360,
            line_step
        ):

            board_html += f"""
            <div
                class="board-line"
                style="
                    transform:
                    translateX(-50%)
                    rotate({angle}deg);
                "
            >
            </div>
            """


        for i, name in enumerate(names):

            left_pos, top_pos = (
                positions[i]
            )


            board_html += f"""
            <div
                class="name"
                style="
                    left:{left_pos}%;
                    top:{top_pos}%;
                "
            >

                {i + 1}. {name}

            </div>
            """


        # =================================================
        # DART ON SELECTED NAME
        # =================================================

        if (
            st.session_state.dart_number
            is not None
        ):

            left_pos, top_pos = (
                positions[
                    st.session_state.dart_number
                ]
            )


            board_html += f"""
            <div
                class="dart"
                style="
                    left:{left_pos}%;
                    top:{top_pos}%;
                "
            >

                🎯

            </div>
            """


        board_html += """
        </div>
        """


        st.html(board_html)


    # =====================================================
    # THROW DART
    # =====================================================

    throw = st.button(
        "🎯  THROW DART",
        use_container_width=True
    )


    if throw:

        available = list(
            range(len(names))
        )


        # ================================================
        # NO REPEAT OPTION
        # ================================================

        if st.session_state.no_repeat:

            available = [

                i

                for i, name in enumerate(names)

                if name
                not in st.session_state.history

            ]


            if not available:

                st.warning(
                    "Everyone has been selected. "
                    "Reset the game to play again."
                )

                st.stop()


        # ================================================
        # SELECT RANDOM PARTICIPANT
        # ================================================

        selected_index = random.choice(
            available
        )


        selected_name = names[
            selected_index
        ]


        st.session_state.dart_number = (
            selected_index
        )


        st.session_state.winner = (
            selected_name
        )


        st.session_state.history.append(
            selected_name
        )


        st.rerun()


    # =====================================================
    # WINNER
    # =====================================================

    if st.session_state.winner:

        # IMPORTANT:
        # BALLOON EFFECT RESTORED

        st.balloons()


        st.html(
            f"""
            <div class="winner-box">

                <div class="winner-label">

                    🏆 SELECTED PARTICIPANT

                </div>

                <div class="winner-name">

                    {st.session_state.winner}

                </div>

            </div>
            """
        )


    else:

        st.info(
            "Click THROW DART to select a participant."
        )


    # =====================================================
    # RESET GAME
    # =====================================================

    reset = st.button(
        "🔄 RESET GAME",
        use_container_width=True
    )


    if reset:

        st.session_state.winner = None

        st.session_state.dart_number = None

        st.session_state.history = []

        st.rerun()


# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    if st.session_state.winner:

        st.html("""
        <div class="panel-title">

            🏆 Winner

        </div>
        """)


        st.html(
            f"""
            <div class="winner-box">

                <div class="winner-name">

                    {st.session_state.winner}

                </div>

            </div>
            """
        )


    # =====================================================
    # WINNER HISTORY
    # =====================================================

    with st.expander(
        "📜 Winner History"
    ):

        if st.session_state.history:

            for i, winner in enumerate(
                st.session_state.history,
                1
            ):

                st.html(
                    f"""
                    <div class="history-item">

                        🎯 Round {i}
                        &nbsp;→&nbsp;
                        <b>{winner}</b>

                    </div>
                    """
                )

        else:

            st.write(
                "No winner selected yet."
            )


    # =====================================================
    # GAME SETTINGS
    # =====================================================

    with st.expander(
        "⚙️ Game Settings"
    ):

        st.session_state.no_repeat = (
            st.checkbox(
                "Don't select the same person again",

                value=
                st.session_state.no_repeat
            )
        )


        st.caption(
            "When enabled, every participant gets "
            "one chance before anyone is selected again."
        )


    # =====================================================
    # MANAGE PARTICIPANTS
    # =====================================================

    with st.expander(
        "👥 Manage Participants"
    ):

        st.write(
            f"Total participants: "
            f"**{len(st.session_state.names)}**"
        )


        st.write(
            "Use the 🗑️ buttons on the left "
            "to remove participants."
        )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="tip">

    🎯 Add participants
    •
    Throw the dart
    •
    Let the game decide

</div>
""")


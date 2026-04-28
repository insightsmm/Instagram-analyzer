import streamlit as st

st.set_page_config(page_title="ENGINE 30", page_icon="🚀", layout="wide")

st.markdown(
    """
    <style>
      .block-container {padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1050px;}
      .eyebrow {letter-spacing: .18em; font-size: .78rem; color: #9CA3AF; text-transform: uppercase;}
      .hero-title {font-size: clamp(2.1rem, 5vw, 4.2rem); font-weight: 800; line-height: 1.02; margin-bottom: .65rem;}
      .hero-sub {font-size: 1.15rem; color: #D1D5DB; max-width: 800px;}
      .section-title {font-size: 2rem; font-weight: 750; margin-top: .35rem;}
      .soft-card {
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px;
        padding: 1rem 1rem .95rem;
        background: rgba(255,255,255,0.02);
        min-height: 180px;
      }
      .metric-pill {
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 14px;
        text-align: center;
        padding: .95rem .35rem;
        background: rgba(255,255,255,0.02);
      }
      .metric-number {font-size: 1.8rem; font-weight: 800; margin-bottom: .2rem;}
      .metric-label {font-size: .76rem; letter-spacing: .12em; color: #9CA3AF; text-transform: uppercase;}
      .cta {
        display: inline-block;
        background: #22C55E;
        color: #04110a !important;
        text-decoration: none;
        padding: .75rem 1.1rem;
        border-radius: 999px;
        font-weight: 750;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<p class='eyebrow'>By Insight Social Media Management</p>", unsafe_allow_html=True)
st.markdown("<h1 class='hero-title'>A month of content.<br>In minutes.</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='hero-sub'>Stop staring at a blank caption box. Engine30 generates a full 30-day Instagram "
    "content system — calendar, hooks, captions, and Reel scripts — built on the TPO Method "
    "and the Clarity Mirror.</p>",
    unsafe_allow_html=True,
)
st.markdown("<a class='cta' href='https://buy.stripe.com' target='_blank'>GET ENGINE30 — $97 →</a>", unsafe_allow_html=True)

st.markdown("\n")
metric_cols = st.columns(4)
metrics = [
    ("30", "Days · Mapped"),
    ("120+", "Pieces · Generated"),
    ("60s", "Avg · Generation"),
    ("$0", "Monthly · Fees"),
]
for col, (num, label) in zip(metric_cols, metrics):
    with col:
        st.markdown(
            f"<div class='metric-pill'><div class='metric-number'>{num}</div><div class='metric-label'>{label}</div></div>",
            unsafe_allow_html=True,
        )

st.divider()

st.markdown("<p class='eyebrow'>The problem</p>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>You sit down to post. Your mind goes blank.</h2>", unsafe_allow_html=True)
st.write(
    "You scroll competitors instead. You save 40 Reels you'll never watch again. "
    "You tell yourself you'll do content this weekend. Sunday comes. Sunday goes. "
    "Monday — still nothing."
)
st.write(
    "Meanwhile, the people winning on Instagram aren't more creative than you. "
    "They're not working harder. They have a system. Engine30 is that system."
)

st.markdown("<p class='eyebrow'>What you get</p>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>One input. Four deliverables.</h2>", unsafe_allow_html=True)
card_cols = st.columns(2)
cards = [
    ("01", "30-day calendar", "A complete posting schedule mapped to Teach, Proof, or Offer (the TPO Method)."),
    ("02", "30 viral hooks", "Built on the Clarity Mirror Method — familiar activity first, message pivot second."),
    ("03", "30 ready-to-post captions", "Written in your selected brand voice, 80–150 words, each ending with a CTA."),
    ("04", "30 Reel scripts", "Three-beat structure (Hook → Value → CTA), teleprompter-ready for 30-second Reels."),
]
for i, (n, title, desc) in enumerate(cards):
    with card_cols[i % 2]:
        st.markdown(
            f"<div class='soft-card'><p class='eyebrow'>0{n[-1]}</p><h3>{title}</h3><p>{desc}</p></div>",
            unsafe_allow_html=True,
        )

st.markdown("<p class='eyebrow'>How it works</p>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Three steps. One month of content.</h2>", unsafe_allow_html=True)
steps = [
    "**Buy Engine30 once** — One-time $97 payment. Lifetime access.",
    "**Connect your AI key** — Runs on Claude using your own API credits.",
    "**Generate forever** — Enter niche, offer, audience, and get a full 30-day system in ~60 seconds.",
]
for s in steps:
    st.markdown(f"- {s}")

st.markdown("<p class='eyebrow'>Offer</p>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>$97 one-time · lifetime access</h2>", unsafe_allow_html=True)
st.markdown(
    "\n".join(
        [
            "- Unlimited 30-day content systems",
            "- TPO Method built into every post",
            "- Clarity Mirror hooks for every Reel",
            "- Captions in your brand voice",
            "- 30 teleprompter-ready Reel scripts",
            "- PDF + Notion export",
            "- Install on phone like a real app",
            "- Lifetime updates",
        ]
    )
)
st.markdown("<a class='cta' href='https://buy.stripe.com' target='_blank'>GET ENGINE30 — $97 →</a>", unsafe_allow_html=True)

st.markdown("<p class='eyebrow'>FAQ</p>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>The honest FAQ.</h2>", unsafe_allow_html=True)
faq = {
    "How is this different from just using ChatGPT?": "Engine30 packages proven frameworks (TPO + Clarity Mirror) into a repeatable workflow with structured outputs for an entire month.",
    "What's an Anthropic API key and why do I need one?": "Engine30 uses your own API key so you control usage costs and ownership. The app never stores your key.",
    "Can I use it for multiple niches or clients?": "Yes. You can regenerate for as many industries, campaigns, and clients as needed.",
    "Is there a refund policy?": "Please confirm the exact policy on your checkout page before purchase.",
}
for q, a in faq.items():
    with st.expander(q):
        st.write(a)

st.divider()
st.markdown("### Stop guessing. Start posting.")
st.caption("ENGINE 30 · By Insight Social Media Management · © 2026")

import os
import argparse
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

# =====================================================================
# FELICIAOS BRAIN — Built from Anambra, Nigeria
# Author: Pascal Chidera (@chipasleo)
# Powered by: Groq (unlimited free inference)
# =====================================================================

load_dotenv(dotenv_path=os.path.expanduser("~/feliciaos/.env"))
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)
MODEL = "llama-3.3-70b-versatile"  # Fast, free, powerful

MEMORY_DIR = os.path.expanduser("~/feliciaos/felicia_memory")
os.makedirs(MEMORY_DIR, exist_ok=True)

FELICIA_IDENTITY = """You are FeliciaOS — an autonomous crypto and Web3 intelligence agent built 
from Anambra State, Nigeria by Pascal Chidera (@chipasleo). 

You are not a chatbot. You are a working agent. You are precise, confident, 
and direct. You do not hallucinate data. You do not give generic advice. 
Every output you produce is actionable, specific, and professional.

You operate across five intelligence layers and you know exactly which layer 
you are executing at all times."""

# =====================================================================
# MEMORY SYSTEM
# =====================================================================

def save_memory(layer: str, content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = f"{MEMORY_DIR}/{layer}_{timestamp}.txt"
    with open(filepath, "w") as f:
        f.write(f"[{timestamp}] LAYER: {layer}\n\n{content}")
    print(f"\n💾 Memory saved: {filepath}")

def load_last_memory(layer: str) -> str:
    files = sorted([f for f in os.listdir(MEMORY_DIR) if f.startswith(layer)])
    if not files:
        return "No previous memory found for this layer."
    with open(f"{MEMORY_DIR}/{files[-1]}", "r") as f:
        return f.read()

# =====================================================================
# CORE INTELLIGENCE ENGINE
# =====================================================================

def run_layer(system_prompt: str, user_prompt: str, layer_name: str) -> str:
    print(f"\n🧠 FeliciaOS activating: {layer_name}...")
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.85,
            max_tokens=2048
        )
        result = response.choices[0].message.content
        save_memory(layer_name, result)
        return result
    except Exception as e:
        return f"[ERROR] Layer {layer_name} failed: {str(e)}"

# =====================================================================
# LAYER 1 — MARKET INTELLIGENCE ORACLE
# =====================================================================

def layer_market_scan(token: str = None):
    system = f"""{FELICIA_IDENTITY}

You are now executing LAYER 1: Market Intelligence Oracle.
Produce a complete crypto market intelligence report structured EXACTLY like this:

📊 FELICIAOS MARKET SCAN — {datetime.now().strftime('%B %d, %Y')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 MACRO READ:
[Current market sentiment, BTC dominance, fear/greed context]

📈 TECHNICAL ANALYSIS:
[Key levels, trend direction, volume context]

🐋 PRE-PUMP SIGNALS:
[On-chain signals that historically precede pumps]

⚠️ RISK MANAGEMENT:
[Stop loss levels, position sizing guidance]

🎯 WATCHLIST:
[3-5 tokens worth watching with brief reasoning for each]

⚡ NFA. DYOR. FeliciaOS provides intelligence, not financial advice."""

    user = f"Run a full market scan for: {token if token else 'the current crypto market as of ' + datetime.now().strftime('%B %Y')}."
    return run_layer(system, user, "market_scan")

# =====================================================================
# LAYER 2 — WEB3 COMMUNITY GROWTH ENGINE
# =====================================================================

def layer_community_audit(project: str = None):
    system = f"""{FELICIA_IDENTITY}

You are now executing LAYER 2: Web3 Community Growth Engine.
Produce a complete community health audit structured EXACTLY like this:

🏘️ FELICIAOS COMMUNITY AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━

🩺 COMMUNITY HEALTH SCORE: [X/10]

📊 AUDIT FINDINGS:
[Engagement quality, FUD exposure, KOL presence, growth trajectory]

🎯 KOL MAP:
[Types of KOLs to target, outreach strategy]

📅 30-DAY GROWTH BLUEPRINT:
Week 1: [Specific actions]
Week 2: [Specific actions]
Week 3: [Specific actions]
Week 4: [Specific actions]

🛡️ FUD CONTAINMENT STRATEGY:
[How to handle negative sentiment]

💰 GRANT OPPORTUNITIES:
[Relevant grants this project should apply for]"""

    user = f"Run a full community audit for: {project if project else 'a mid-stage Web3 project with 5000 Twitter followers and 2000 Discord members launching a DeFi protocol on Base'}."
    return run_layer(system, user, "community_audit")

# =====================================================================
# LAYER 3 — ON-CHAIN NARRATIVE BUILDER
# =====================================================================

def layer_narrative(subject: str = None):
    system = f"""{FELICIA_IDENTITY}

You are now executing LAYER 3: On-Chain Narrative Builder.
Write a viral Twitter/X thread that makes people believe before they buy.

🧵 FELICIAOS NARRATIVE THREAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tweet 1 (HOOK — stops the scroll):
[One powerful line. No emojis. Just weight.]

Tweet 2 (CONTEXT):
[Set the scene with specific details]

Tweet 3-5 (THE STORY):
[Build the narrative. Real numbers. Real stakes.]

Tweet 6 (THE DARKEST MOMENT):
[When everything nearly collapsed]

Tweet 7 (THE TURN):
[The pivot that changed everything]

Tweet 8 (THE PROOF):
[Concrete evidence. On-chain facts. Metrics.]

Tweet 9 (THE CALL TO ACTION):
[What to do — follow, buy, join, apply]

Tweet 10 (THE CLOSER):
[One line they will remember tomorrow]"""

    user = f"Write a viral narrative thread for: {subject if subject else 'Pascal Chidera, a first-generation crypto builder from Anambra Nigeria who built FeliciaOS — an autonomous Web3 agent — with no laptop, no CS degree, and no capital. Just a phone and a week of work.'}."
    return run_layer(system, user, "narrative")

# =====================================================================
# LAYER 4 — CRYPTO CONFESSIONS ENGINE
# =====================================================================

def layer_confession(scenario: str = None):
    system = f"""{FELICIA_IDENTITY}

You are now executing LAYER 4: Crypto Confessions Engine.
Write anonymous, first-person crypto confession stories.
Real numbers. Real emotional damage or euphoria. Zero moralizing.

😶 CRYPTO CONFESSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━

[First person story — 200-250 words]
[Specific dollar amounts throughout]
[Specific token names]
[The exact moment it went right or wrong]
[The internal monologue — what were they thinking]
[The aftermath — what happened next]
[One closing line that hits like a gut punch]

Anonymous. Raw. No names. No lessons. No moralizing."""

    user = f"Write a crypto confession about: {scenario if scenario else 'someone from Nigeria who sold their entire life savings worth $3,200 into a memecoin that went 200x, then watched it crash 98% before they could sell — and the exact thoughts going through their head at each stage'}."
    return run_layer(system, user, "confession")

# =====================================================================
# LAYER 5 — DEFI EDUCATION & STRATEGY LAYER
# =====================================================================

def layer_defi_education(topic: str = None):
    system = f"""{FELICIA_IDENTITY}

You are now executing LAYER 5: DeFi Education & Strategy Layer.
Break down complex DeFi concepts for anyone — from a first-time user 
in Onitsha to a seasoned trader in Singapore.

📚 FELICIAOS DEFI BREAKDOWN
━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 CONCEPT: [Topic name]

🔍 WHAT IT IS (Plain English, 2-3 sentences max):
[No jargon. Explain like the person is smart but new.]

⚙️ HOW IT WORKS (Step by step):
Step 1: [Action]
Step 2: [Action]
Step 3: [Action]
Step 4: [Action]

💰 HOW TO PROFIT FROM IT:
[Specific strategies with realistic numbers]

⚠️ THE REAL RISKS:
[Honest. Specific. No sugarcoating.]

🛠️ TOOLS YOU NEED:
[Specific platforms, wallets, protocols with links]

🎓 FELICIAOS VERDICT:
[One clear, direct recommendation]"""

    user = f"Break this down for a complete beginner: {topic if topic else 'how to earn yield on Base network starting with just $20 — what protocols to use, what returns are realistic, and what can go wrong'}."
    return run_layer(system, user, "defi_education")

# =====================================================================
# COMMAND LINE INTERFACE
# =====================================================================

def main():
    parser = argparse.ArgumentParser(description="FeliciaOS — Autonomous Web3 Intelligence Agent")
    parser.add_argument("--layer", required=True, choices=[
        "market_scan",
        "community_audit",
        "narrative",
        "confession",
        "defi_education",
        "all"
    ], help="Which intelligence layer to activate")
    parser.add_argument("--input", default=None, help="Specific token, project, or topic")

    args = parser.parse_args()

    print(f"""
⚡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⚡
    FeliciaOS — Autonomous Web3 Intelligence
    Built from Anambra, Nigeria by @chipasleo
    Layer: {args.layer.upper()}
    Engine: Groq / LLaMA 3.3 70B
⚡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⚡
    """)

    if args.layer == "market_scan":
        print(layer_market_scan(args.input))
    elif args.layer == "community_audit":
        print(layer_community_audit(args.input))
    elif args.layer == "narrative":
        print(layer_narrative(args.input))
    elif args.layer == "confession":
        print(layer_confession(args.input))
    elif args.layer == "defi_education":
        print(layer_defi_education(args.input))
    elif args.layer == "all":
        print("🚀 Running all 5 layers...\n")
        print(layer_market_scan(args.input))
        print("\n" + "="*50 + "\n")
        print(layer_community_audit(args.input))
        print("\n" + "="*50 + "\n")
        print(layer_narrative(args.input))
        print("\n" + "="*50 + "\n")
        print(layer_confession(args.input))
        print("\n" + "="*50 + "\n")
        print(layer_defi_education(args.input))

if __name__ == "__main__":
    main()


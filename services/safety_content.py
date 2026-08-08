from datetime import date
import random


SAFETY_TOPICS = {
    "Workplace Safety": [
        "Never operate equipment unless you have been properly trained.",
        "Wear the required PPE before entering a hazardous work area.",
        "Report unsafe conditions immediately instead of assuming someone else will.",
        "Keep walkways, emergency exits, and access routes clear.",
        "Never bypass a machine guard or safety interlock.",
    ],

    "Home Safety": [
        "Never leave cooking unattended when using an open flame.",
        "Keep medicines and household chemicals away from children.",
        "Do not overload electrical sockets.",
        "Clean water spills immediately to prevent slips and falls.",
        "Keep matches, lighters, and ignition sources away from children.",
    ],

    "Road Safety": [
        "Always wear your seatbelt before the vehicle begins moving.",
        "Never use a mobile phone while driving.",
        "Reduce speed when visibility or road conditions are poor.",
        "Check mirrors and blind spots before changing lanes.",
        "Never drive when impaired by alcohol, drugs, or extreme fatigue.",
    ],

    "Electrical Safety": [
        "Never handle electrical equipment with wet hands.",
        "Switch off and isolate electrical power before maintenance.",
        "Do not use cables with damaged insulation.",
        "Avoid connecting too many high-power appliances to one socket.",
        "Electrical repairs should be performed by qualified personnel.",
    ],

    "Fire Safety": [
        "Keep fire exits and emergency escape routes clear.",
        "Know the location of fire extinguishers in your workplace or home.",
        "Never block access to firefighting equipment.",
        "Turn off appliances that are not required.",
        "If a fire starts, raise the alarm and move to a safe location.",
    ],

    "Water Safety": [
        "Never leave children unattended near swimming pools, rivers, or open water.",
        "Do not enter floodwater when the depth or current is unknown.",
        "Avoid walking through moving floodwater whenever possible.",
        "Keep electrical equipment away from wet areas.",
        "Wear appropriate flotation equipment when required.",
    ],

    "Food Safety": [
        "Wash your hands before preparing or eating food.",
        "Keep raw and cooked foods separated.",
        "Store perishable food at safe temperatures.",
        "Do not consume food that shows signs of spoilage.",
        "Clean food preparation surfaces regularly.",
    ],

    "Health & Hygiene": [
        "Wash your hands thoroughly after using the toilet and before eating.",
        "Cover coughs and sneezes to reduce the spread of respiratory infections.",
        "Keep drinking water in clean, covered containers.",
        "Maintain clean surroundings to reduce pests and disease.",
        "Seek qualified medical advice when symptoms are serious or persistent.",
    ],

    "Cyber Safety": [
        "Never share passwords or verification codes with strangers.",
        "Be cautious of links asking for passwords or financial information.",
        "Use strong, unique passwords for important accounts.",
        "Enable multi-factor authentication whenever available.",
        "Verify unusual payment requests before sending money.",
    ],

    "Environmental Safety": [
        "Do not dump chemicals or waste into drains or waterways.",
        "Dispose of hazardous waste through appropriate channels.",
        "Avoid unnecessary burning of waste.",
        "Conserve water whenever possible.",
        "Keep public areas and drainage channels free from waste.",
    ],

    "Personal Security": [
        "Stay aware of your surroundings when walking in unfamiliar places.",
        "Avoid displaying large amounts of cash in public.",
        "Keep important documents and valuables secure.",
        "Tell someone you trust when travelling to an unfamiliar location.",
        "Trust your instincts and move away from situations that feel unsafe.",
    ],

    "Child Safety": [
        "Keep medicines and dangerous chemicals out of children's reach.",
        "Teach children never to play with electrical outlets.",
        "Never leave young children unattended near water.",
        "Teach children how to contact a trusted adult during an emergency.",
        "Keep small objects that can cause choking away from young children.",
    ],

    "Workplace Hygiene": [
        "Wash or sanitize your hands regularly.",
        "Keep shared work surfaces clean.",
        "Do not share personal protective equipment unless it is properly sanitized.",
        "Report spills and contamination immediately.",
        "Stay home and seek appropriate guidance when seriously unwell.",
    ],

    "Construction Safety": [
        "Wear the required PPE before entering a construction area.",
        "Never work beneath an unsecured suspended load.",
        "Use the correct ladder or access equipment for the task.",
        "Keep tools and materials secured to prevent falling objects.",
        "Follow site safety procedures before starting work.",
    ],

    "Agricultural Safety": [
        "Keep children away from operating farm machinery.",
        "Wear appropriate PPE when handling agricultural chemicals.",
        "Inspect machinery before operating it.",
        "Store pesticides and chemicals in properly labelled secure areas.",
        "Never operate machinery when excessively tired.",
    ],

    "Travel Safety": [
        "Keep important documents and emergency contacts accessible when travelling.",
        "Check weather and road conditions before a long journey.",
        "Tell someone you trust about your travel plans when appropriate.",
        "Keep your phone charged during long journeys.",
        "Know where emergency assistance is available when travelling.",
    ],
}


def get_daily_safety_message():
    """
    Select one safety topic and one safety tip based on today's date.
    The same message will be returned throughout the same day.
    """

    today = date.today()
    day_number = today.toordinal()

    topics = list(SAFETY_TOPICS.keys())

    topic = topics[day_number % len(topics)]

    messages = SAFETY_TOPICS[topic]

    safety_tip = messages[day_number % len(messages)]

    return format_safety_message(
        topic,
        safety_tip,
    )


def get_random_safety_message():
    """
    Select a completely random safety topic and safety tip.
    """

    topic = random.choice(
        list(SAFETY_TOPICS.keys())
    )

    safety_tip = random.choice(
        SAFETY_TOPICS[topic]
    )

    return format_safety_message(
        topic,
        safety_tip,
    )


def get_categories():
    """
    Return all available safety categories.
    """

    return list(SAFETY_TOPICS.keys())


def format_safety_message(topic, safety_tip):
    """
    Format a professional LifeGuard 365 safety message.
    """

    return (
        "🛡️ *LIFEGUARD 365*\n\n"
        "🚨 *DAILY SAFETY MESSAGE*\n\n"
        f"📌 *Category:* {topic}\n\n"
        f"⚠️ *CAUTION:*\n{safety_tip}\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "💡 *REMEMBER*\n"
        "A few seconds of caution can prevent "
        "a lifetime of regret.\n\n"
        "🛡️ Protect yourself.\n"
        "🤝 Protect others.\n"
        "❤️ Protect life.\n\n"
        "— *LifeGuard 365*"
    )
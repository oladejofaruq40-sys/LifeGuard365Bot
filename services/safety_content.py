from datetime import date
SAFETY_TOPICS = {
    "Workplace Safety": [
        "Never operate equipment unless you have 
been properly trained.",
        "Wear the required PPE before entering a 
hazardous work area.",
        "Report unsafe conditions immediately instead 
of assuming someone else will.",
        "Keep walkways, emergency exits, and access 
routes clear.",
        "Never bypass a machine guard or safety 
interlock.",
    ],
    "Home Safety": [
        "Never leave cooking unattended when using 
an open flame.",
        "Keep medicines and household chemicals 
away from children.",
        "Do not overload electrical sockets.",
        "Clean water spills immediately to prevent slips 
and falls.",
        "Keep matches, lighters, and other ignition 
sources away from children.",
    ],
    "Road Safety": [
        "Always wear your seatbelt before the vehicle 
begins moving.",
        "Never use a mobile phone while driving.",
        "Reduce speed when visibility or road 
conditions are poor.",
        "Check mirrors and blind spots before changing 
lanes.",
        "Never drive when your ability is impaired by 
alcohol, drugs, fatigue, or illness.",
    ],
    "Electrical Safety": [
        "Never handle electrical equipment with wet 
hands.",
        "Switch off and isolate electrical power before 
maintenance.",
        "Do not use cables with damaged insulation.",
        "Avoid connecting too many high-power 
appliances to one socket.",
        "Electrical repairs should be performed by 
qualified personnel.",
    ],
    "Fire Safety": [
        "Keep fire exits and emergency escape routes 
clear.",
        "Know the location of fire extinguishers in your 
workplace or home.",
        "Never block access to firefighting equipment.",
        "Turn off appliances that are not required.",
        "If a fire starts, raise the alarm and move to a 
safe location.",
    ],
    "Water Safety": [
        "Never leave children unattended near 
swimming pools, rivers, or open water.",
        "Do not enter floodwater when the depth or 
current is unknown.",
        "Avoid walking through moving floodwater 
whenever possible.",
        "Keep electrical equipment away from wet 
areas.",
        "Wear appropriate flotation equipment when 
required.",
    ],
    "Food Safety": [
        "Wash your hands before preparing or eating 
food.",
        "Keep raw and cooked foods separated.",
        "Store perishable food at safe temperatures.",
        "Do not consume food that shows signs of 
spoilage.",
        "Clean food preparation surfaces regularly.",
    ],
    "Health & Hygiene": [
        "Wash your hands thoroughly after using the 
toilet and before eating.",
        "Cover coughs and sneezes to reduce the 
spread of respiratory infections.",
        "Keep drinking water in clean, covered 
containers.",
        "Maintain clean surroundings to reduce pests 
and disease.",
        "Seek qualified medical advice when 
symptoms are serious or persistent.",
    ],
    "Cyber Safety": [
        "Never share your passwords or verification 
codes with strangers.",
        "Be cautious of links asking for passwords or 
financial information.",
        "Use strong, unique passwords for important 
accounts.",
        "Enable multi-factor authentication whenever 
available.",
        "Verify unusual payment requests before 
sending money.",
    ],
    "Environmental Safety": [
        "Do not dump chemicals or waste into drains or 
waterways.",
        "Dispose of hazardous waste through 
appropriate channels.",
        "Avoid unnecessary burning of waste.",
        "Conserve water whenever possible.",
        "Keep public areas and drainage channels free 
from waste.",
    ],
}
def get_daily_safety_message():
    """
    Selects a deterministic safety topic and message
    based on the current date.
    """
    today = date.today()
    topics = list(SAFETY_TOPICS.keys())
    topic_index = today.toordinal() % len(topics)
    topic = topics[topic_index]
    messages = SAFETY_TOPICS[topic]
    message_index = today.toordinal() % 
len(messages)
    safety_tip = messages[message_index]
    return format_safety_message(
        topic,
        safety_tip
    )
def format_safety_message(topic, safety_tip):
    return (
        " *LIFEGUARD 365*\n\n"
        " *DAILY SAFETY MESSAGE*\n\n"
        f" *Topic:* {topic}\n\n"
        f" {safety_tip}\n\n"
        "━━━━━━━━━━━━━━\n"
        "Remember:\n"
        "A few seconds of caution can prevent "
        "a lifetime of regret.\n\n"
        " Protect yourself.\n"
        " Protect others.\n"
        " Protect life.\n\n"
        "— *LifeGuard 365*"
    )
"""
This module contains static text variables and contact details
used throughout the Planet Express website.
"""

from datetime import datetime

home_page_text = """
    Welcome to Planet Express, your trusted intergalactic delivery service! 
    From tiny parcels to massive cargo, we deliver across the universe at lightning speed (well, almost).
    Whether you need a package sent to Mars, Neptune, or the far reaches of the Andromeda Galaxy, we’ve got you covered. 
    Our highly skilled crew ensures that your shipment arrives safely, (mostly) intact, and with minimal space-time anomalies. 
    Trust Planet Express—because your package deserves an adventure! 🚀
    """

about_us_text = """
    At Planet Express, we specialize in intergalactic deliveries, ensuring that packages 
    reach their destinations across the universe—safely 
    and (mostly) on time. Founded in the 31st century, 
    we’ve built a reputation for handling the jobs no one else will take, 
    whether it’s shipping fragile goods to the Outer Rim or delivering mysterious packages 
    to alien overlords. Our team, led by Captain Leela, Fry, and Bender, 
    is known for their questionable work ethic but undeniable results. 
    With cutting-edge spacecraft and a commitment to (mostly) ethical business practices,
     we make space deliveries an adventure. 🚀
    """

contact_details = {
    "company_name": "Planet Express",
    "address": "57th Street, New New York, Earth",
    "phone": "+1-800-PEXPRESS",
    "email": "info@planetexpress.com",
    "support_email": "",
    "fax": "+1-800-FAX-BOT",
    "last_updated": datetime(2025, 3, 14, 15, 30),
    "working_hours": {
        "weekdays": "09:00 - 18:00 (Earth Time)",
        "weekends": "Closed (unless there's an emergency delivery)"
    },
    "social_media": {
        "twitter": "https://twitter.com/PlanetExpress",
        "facebook": "https://facebook.com/PlanetExpress",
        "instagram": "https://instagram.com/PlanetExpress"
    },
    "emergency_contact": {
        "captain": "Turanga Leela",
        "robot_assistant": "Bender Bending Rodríguez",
        "intern": "Philip J. Fry"
    },
    "services": [
        {"name": "Intergalactic Shipping", "price": "$500"},
        {"name": "Express Lunar Delivery", "price": "$300"},
        {"name": "Zero-G Cargo Handling", "price": "$200"},
        {"name": "Hyperspace Logistics", "price": "$600"},
    ]
}

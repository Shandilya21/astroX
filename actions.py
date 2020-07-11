# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
import logging

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)

class ActionFaqAstronomy(Action):

    def name(self) -> Text:
        return "action_faq_astronomy"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_astronomy"]:
            text = """Astronomy (from Greek: ἀστρονομία) is a natural science that studies celestial objects and phenomena.
            It uses mathematics, physics, and chemistry in order to explain their origin and evolution. Objects of interest include  
            planets, moons, stars, nebulae, galaxies, and comets. Relevant phenomena include supernova explosions, gamma ray bursts, quasars, 
            blazars, pulsars, and cosmic microwave background radiation. More generally, astronomy studies everything that originates outside 
            Earth's atmosphere. Read more in the link below.."""
            message = {
                "type": "image",
                "payload": {
                    "title": "Astronomy",
                    "src": "https://starofmysore.com/wp-content/uploads/2020/04/astronomy-day-1.jpg",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []

class ActionFaqSpace(Action):

    def name(self) -> Text:
        return "action_faq_space"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_space"]:
            text = """Outer space, or simply space, is the expanse that exists beyond Earth and between celestial bodies. 
            Outer space is not completely empty—it is a hard vacuum containing a low density of particles, predominantly a plasma 
            of hydrogen and helium, as well as electromagnetic radiation, magnetic fields, neutrinos, dust, and cosmic rays. 
            The baseline temperature of outer space, as set by the background radiation from the Big Bang, is 2.7 kelvins (−270.45 °C; −454.81 °F).
            Read more below .. """
            message = {
                "type": "text",
                "payload": {
                    "title": "Space",
                    "src": "https://spaceplace.nasa.gov/story-whats-in-space/en/#",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []

class ActionFaqTelescopes(Action):

    def name(self) -> Text:
        return "action_faq_telescopes"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        intent = tracker.latest_message["intent"].get("name")
        
        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_telescopes"]:
            text = """A telescope is an optical instrument that makes distant objects appear magnified by using an arrangement of lenses or curved mirrors
            and lenses, or various devices used to observe distant objects by their emission, absorption, or reflection of electromagnetic radiation. 
            The first known practical telescopes were refracting telescopes invented in the Netherlands at the beginning of the 17th century, by using 
            glass lenses. They were used for both terrestrial applications and astronomy. Telescopes may be classified by the wavelengths of light they 
            detect: (i) X-ray telescopes, using shorter wavelengths than ultraviolet light (ii) Ultraviolet telescopes, using shorter wavelengths than 
            visible light (iii) Optical telescopes, using visible light (iii) Infrared telescopes, using longer wavelengths than visible light 
            (iv)Submillimetre telescopes, using microwave wavelengths that are longer than those of infrared light (v)Radio telescopes that use even 
            longer wavelengths. Read more below"""
            message = {
                "type": "text",
                "payload": {
                    "title": "Telescopes",
                    "src": "https://en.wikipedia.org/wiki/Telescope",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []

class ActionFaqPlanets(Action):

    def name(self) -> Text:
        return "action_faq_planets"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_planets"]:
            text = """A planet is an astronomical body orbiting a star or stellar remnant that is massive enough to be rounded by its own gravity, 
            is not massive enough to cause thermonuclear fusion, and has cleared its neighbouring region of planetesimals. As scientific knowledge 
            advanced, human perception of the planets changed, incorporating a number of disparate objects. In 2006, the International Astronomical Union 
            (IAU) officially adopted a resolution defining planets within the Solar System. This definition is controversial because it excludes many 
            objects of planetary mass based on where or what they orbit. Although eight of the planetary bodies discovered before 1950 remain "planets" 
            under the current definition, some celestial bodies, such as Ceres, Pallas, Juno and Vesta (each an object in the solar asteroid belt), 
            and Pluto (the first trans-Neptunian object discovered), that were once considered planets by the scientific community, are no longer viewed 
            as planets under the current definition of planet. Read more about Planets in details ... """
            message = {
                "type": "text",
                "payload": {
                    "title": "Telescopes",
                    "src": "https://solarsystem.nasa.gov/planets/overview/",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []

class ActionFaqMissionatISRO(Action):

    def name(self) -> Text:
        return "action_faq_mission_at_isro"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_mission_at_isro"]:
            text = """The Indian Space Research Organisation (ISRO, /ˈɪsroʊ/) (Hindi; IAST: bhārtīya antrikṣ anusandhān saṅgṭhan) is the space agency of
            the Government of India and has its headquarters in the city of Bengaluru. Its vision is to "harness space technology for national development
            while pursuing space science research & planetary exploration". The prime objective of ISRO is to use space technology and its application to 
            various national tasks. The Indian space programme was driven by the vision of Vikram Sarabhai, considered the father of the Indian space 
            programme The Indian National Committee for Space Research (INCOSPAR) was established by Jawaharlal Nehru (First Prime Minister of India) 
            under the Department of Atomic Energy (DAE) in 1962, with the urging of scientist Vikram Sarabhai recognising the need in space research.
            ISRO built India's first satellite, Aryabhata, which was launched by the Soviet Union on 19 April 1975.It was named after the mathematician 
            Aryabhata. In 1980, Rohini became the first satellite to be placed in orbit by an Indian-made launch vehicle, SLV-3. ISRO subsequently 
            developed two other rockets: the Polar Satellite Launch Vehicle (PSLV) for launching satellites into polar orbits and the Geosynchronous 
            Satellite Launch Vehicle (GSLV) for placing satellites into geostationary orbits. These rockets have launched numerous communications 
            satellites and Earth observation satellites. Satellite navigation systems like GAGAN and IRNSS have been deployed. In January 2014, 
            ISRO used an indigenous cryogenic engine CE-7.5 in a GSLV-D5 launch of the GSAT-14. 
            Read more about ISRO in details..."""
            message = {
                "type": "text",
                "payload": {
                    "title": "ISRO",
                    "src": "https://www.isro.gov.in/missions",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []

class ActionFaqMissionatatNASA(Action):

    def name(self) -> Text:
        return "action_faq_mission_at_nasa"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        intent = tracker.latest_message["intent"].get("name")
        
        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_mission_at_nasa"]:
            text = """The National Aeronautics and Space Administration (NASA; /ˈnæsə/) is an independent agency of the United States Federal Government
            responsible for the civilian space program, as well as aeronautics and space research. NASA was established in 1958, succeeding the National
            Advisory Committee for Aeronautics (NACA). The new agency was to have a distinctly civilian orientation, encouraging peaceful applications 
            in space science.Since its establishment, most US space exploration efforts have been led by NASA, including the Apollo Moon landing missions, 
            the Skylab space station, and later the Space Shuttle. NASA is supporting the International Space Station and is overseeing the development of 
            the Orion spacecraft, the Space Launch System, and Commercial Crew vehicles. The agency is also responsible for the Launch Services Program, 
            which provides oversight of launch operations and countdown management for uncrewed NASA launches. Read more about NASA in details..."""
            message = {
                "type": "text",
                "payload": {
                    "title": "Human in Space",
                    "src": "https://www.nasa.gov/topics/humans-in-space",
                },
                "type": "text",
                "payload": {
                    "title": "Mission at NASA",
                    "src": "https://www.nasa.gov/missions/",
                },
                "type": "text",
                "payload": {
                    "title": "General FAQ",
                    "src": "https://en.wikipedia.org/wiki/NASA",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []

class ActionFaqBlackHole(Action):

    def name(self) -> Text:
        return "action_faq_black_hole"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_black_hole"]:
            text = """A black hole is a region of spacetime where gravity is so strong that nothing—no particles or even electromagnetic radiation 
            such as light—can escape from it.[6] The theory of general relativity predicts that a sufficiently compact mass can deform spacetime to 
            form a black hole. The boundary of the region from which no escape is possible is called the event horizon. Although the event horizon has 
            an enormous effect on the fate and circumstances of an object crossing it, according to general relativity it has no locally detectable 
            features. In many ways, a black hole acts like an ideal black body, as it reflects no light. Moreover, quantum field theory in curved 
            spacetime predicts that event horizons emit Hawking radiation, with the same spectrum as a black body of a temperature inversely proportional 
            to its mass. This temperature is on the order of billionths of a kelvin for black holes of stellar mass, making it essentially impossible to 
            observe. Read more about Black Hole in details..."""
            message = {
                "type": "text",
                "payload": {
                    "title": "Black Hole",
                    "src": "https://www.nasa.gov/audience/forstudents/k-4/stories/nasa-knows/what-is-a-black-hole-k4.html",
                },
                "type": "text",
                "payload": {
                    "title": "General FAQ on Black Hole",
                    "src": "https://en.wikipedia.org/wiki/Black_hole",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []

class ActionFaqStarandGalaxies(Action):

    def name(self) -> Text:
        return "action_faq_star_and_galaxies"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_star_and_galaxies"]:
            text = """A star is an astronomical object consisting of a luminous spheroid of plasma held together by its own gravity. The nearest star 
            to Earth is the Sun. Many other stars are visible to the naked eye from Earth during the night, appearing as a multitude of fixed luminous 
            points in the sky due to their immense distance from Earth. Historically, the most prominent stars were grouped into constellations and 
            asterisms, the brightest of which gained proper names. Astronomers have assembled star catalogues that identify the known stars and provide 
            standardized stellar designations. The observable Universe contains an estimated 1×1024 stars, but most are invisible to the naked eye from 
            Earth, including all stars outside our galaxy, the Milky Way. A galaxy is a gravitationally bound system of stars, stellar remnants, 
            interstellar gas, dust, and dark matter. The word galaxy is derived from the Greek galaxias (γαλαξίας), literally "milky", a 
            reference to the Milky Way. Galaxies range in size from dwarfs with just a few hundred million (108) stars to giants with one hundred 
            trillion (1014) stars, each orbiting its galaxy's center of mass. Galaxies are categorized according to their visual morphology as 
            elliptical, spiral, or irregular. Many galaxies are thought to have supermassive black holes at their centers. The Milky Way's central 
            black hole, known as Sagittarius A*, has a mass four million times greater than the Sun. As of March 2016, GN-z11 is the oldest and most 
            distant observed galaxy with a comoving distance of 32 billion light-years from Earth, and observed as it existed just 400 million years 
            after the Big Bang. Read more about NASA in details..."""
            message = {
                "type": "text",
                "payload": {
                    "title": "General FAQ on Stars",
                    "src": "https://www.nationalgeographic.com/science/space/universe/stars/",
                },
                "type": "text",
                "payload": {
                    "title": "General FAQ on Galaxies",
                    "src": "https://en.wikipedia.org/wiki/Galaxy",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []
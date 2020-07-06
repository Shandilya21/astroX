## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## faq astronomy
* faq_astronomy
  - action_faq_astronomy

## faq space
* faq_space
  - action_faq_space
* greet
  - utter_greet
* deny
  - utter_goodbye

## faq telescopes
* faq_telescopes
  - action_faq_telescopes 

## faq planets
* faq_planets
  - action_faq_planets
* greet
  - utter_greet
* deny
  - utter_goodbye

## faq mission at isro
* faq_mission_at_isro
  - action_faq_mission_at_isro
* greet
  - utter_greet
* deny
  - utter_goodbye

## faq mission at nasa
* faq_mission_at_nasa
  - action_faq_mission_at_nasa
* greet
  - utter_greet
* deny
  - utter_goodbye

## faq black hole
* faq_black_hole
  - action_faq_black_hole
* greet
  - utter_greet
* deny
  - utter_goodbye

## faq star and galaxies
* faq_star_and_galaxies
  - action_faq_star_and_galaxies
* greet
  - utter_greet
* deny
  - utter_goodbye
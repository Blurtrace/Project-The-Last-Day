Implemented a structured random events system responsible for generating
unexpected situations that affect the player's resources and survival status.

The system generates events randomly and divides them into three difficulty
levels: easy, normal, and hard. Each difficulty contains a different set
of events with increasing impact on the player's resources.

Every event can affect one or more of the following elements:
- food
- water
- energy
- life
- population

Resource reductions are handled through a protected function to ensure that
values never drop below zero, improving the stability of the game system.

Some events also include a probability-based death mechanic where a member
of the group may die depending on the severity of the event.

This feature introduces unpredictability into the gameplay and forces the
player to constantly adapt their resource management strategy in order
to survive.
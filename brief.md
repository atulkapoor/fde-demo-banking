# Support intent routing for a retail bank

We run the first line of support for a digital retail bank: cards, transfers,
top-ups, exchange rates, identity checks. Every customer message arrives as
free text through the app chat and has to be routed to the right handling
queue before an agent or an automation picks it up. Today a team of triage
agents reads each message and picks one of seventy-seven queue intents by
hand; the queue definitions are stable and documented.

We have 13,000 historical messages, each with the intent the triage team
assigned, from the bank's own support logs. Around 10,000 messages a month
arrive. A wrong route costs a second hop and a slower answer; a message
routed to "unknown" is fine as long as it is rare.

The routing decision has to happen inside the bank's own cloud account; the
messages are customer data and may not leave it. The bank's platform team
will operate whatever we hand over, on their existing Linux hosts. Nobody
is waiting on the route in real time: a few seconds is fine. The system
should act only through the ticketing API to set the queue, and it must be
possible to see why any message was routed where it was.

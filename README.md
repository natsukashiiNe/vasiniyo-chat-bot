This is a branch to develop a quiz game for python telegram bot.

# Idea

The general idea is to create a system to interactively create and
distribute set of questions packed into a quiz between players. Players
can create their own quizzes or participate into **event-based** ones
(like daily ones). Rewards and penalties can be applied depending on the
results of the quizzes. This would rely on / further facilitate
**inventory** system in the chat, allowing to earn currency, status and
items.

# Quiz creation examples

## Example 1: DUEL between two players

Player 1 can *CHALLENGE* Player2 via issuing bot's command. Before the
DUEL actually starts, players can interactively bargain about the stake
of the duel and the properties of the quiz. This could include win
conditions, amount of questions, difficulty, type of questions and
themes. Quiz will then begin consisting of several questions, until
either of the players wins.

## Example 2: FREE-FOR-ALL battle

Player can create a FREE-FOR-ALL type of battle, which can be joined by
any chat participant in the allotted time. Settings of the battle can be
chosen by a creator interactively in the chat. A small fee (using
inventory system) can be used as an entrance for the battle, and global
bank can be then redistributed among top-player. Another example of
results-distribution can be choosing a penalty for the worst players.

## Example 3: "Daily" quiz

At 3:00 (or any other *reset time*) a special **EVENT** stats. Players
can register to participate in it while it is active. Then they would
allow to answer a certain sequence of questions. At the end of the day,
results would be printed. Winner or top-scorers can be rewarded with
some prizes.

# \[CORE\] Implementation tasks and notes

There are several systems to build:

## Starting a quiz

To **start a DUEL** special command can be introduced and an interactive
menu would be sent to chatter's personal conversation with the bot (to
avoid cluttering the group). In there properties like stake, question
properties (types, difficulty etc) and overall quiz's properties (time
to answer, conditions of victory etc). After setting up the quiz would
be done, whoever is being challenged would be notified in the chat with
options to "accept" or "bargain" (in which case they would be offered
the similar menu to make a counter offer). After both players agree on
the terms, quiz can be generated and started. During **FREE-FOR-ALL**
battle bargaining about the terms is not applicable, so after chatters
would setup such an event, a registry button would be simply sent in the
group. For **DAILY** activities, they would be configured by admins or
via special items in the inventory. For example, looser of the previous
daily event can be granted an item to impact the next generation of
daily quiz (like setting a topic for questions). To take part in the
daily event issuing *entry-permits* to all group members (inventory
system) every reset can be done.

## Answering questions

Questions should be issued and answered in a personal conversation with
a bot to avoid unnecessary spam in the group or leaking other
participant's answers. Live board of the ongoing quiz in the group and
in all participant's chat can be generated to show current scores of the
players.

## Types of questions

There are several open-source and freely available questions sources.
Adapter can be used to access any of those and extract common properties
like difficulty, theme etc. With range-based questions "winner" of a
round can be decided ranging player's answers (whoever got closer wins).

## Items distributions

After a quiz ends, we can distribute items. Those could be good ones for
winning or bad ones for losing. For example we can have a function that
transfer some items from a loser to a winner in a *duel*. Or rewarding
first 3 places in daily quiz. Something like that.

# \[ADDITIONAL\] Functionality to extend the module

## Privacy settings

Players can be allowed to deny other players to challenge them by
tweaking their privacy settings for the chat.

## Dependant modules:

This module can be used to extend already existing system of the group,
**inventory** specifically. Chatters would be allowed to make use of
theirs items.

# Planned progress

- \[x\] Make outline with basic data structures and "shallow" modules to
  be filled later
- [ ] Provide simple terminal based simulation of telegram group to act
  as testing ground:
- [ ] Implement fetching questions functionality
- [ ] Implement telegram events, handlers and menus.

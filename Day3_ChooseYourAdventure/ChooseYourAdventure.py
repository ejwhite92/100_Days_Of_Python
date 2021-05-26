print('''
 __________________________________________________________________________

                         nnnnnnHHHHHHHHHHHHHnnnnnn
                   nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
                nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
             nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
           nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
          HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
        nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn
       HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
      HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
     HHHHHHHHHHHHHHHHHHHHHHH^^~"    ~H~    ~~^^HHHHHHHHHHHHHHHHHHHHHHH
    HHHHHHHHHHHHHHHHHHHHHH:^                    ^HHHHHHHHHHHHHHHHHHHHHH
   nHHHHHHHHHHHHHHHHHHHHH:                       ^HHHHHHHHHHHHHHHHHHHHHn
   HHHHHHHHHHHHHHHHHHHHH::                        ^HHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHH:                   .      HHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHH|:                          |HHHHHHHHHHHHHHHHHHHHH
 HHHHHHHHHHHHHH%%%%:::H|: ~~~~----- -      ------  |:::%%%%HHHHHHHHHHHHHHH
 HH~              ~HHHH|:   ~~  -----    - ---     |HHHH~              ~HH
                   HHHH|:\\\.                 ./// |HHHH
     ____________   HHH|: \\\\\\\\. / \ .////////  |HHH
    /____________\   HH|:=-- ----  \.  : (_@_> .   |HH
   /%%%%%%%%%%%  %\   H|:   ~-- ~~:|.  :   ~ -'   :|H
  |%%%%%%%%%%%%%  %|  ||:        .:|.  :         :'||   "Stop running. I only
  /:   _)%%%%%'.--.    |:.      :(.     .)\      : |       want to talk..."
 ( _-=%%%%%%'.%(  )    |:|     /::::._.-~  \       |
  (    :    )%~/~~|    ::|    / /.____    . \    : :
  :--------~|     :    `:::  (  \%========/\       '
  (__:_) |% |(   /    /%%::\     ~~~~----'  \     '=\
   (  : )|% |   /    /H%%%::\                    '==%\
    `---'|% | -~ ---(%%H%%%:::.\           /   .===%==)---
    |  _.%%.%.|      \%%H%%%%n:::._______.::.-===:%==/
    |  ~~~~~~~|       \%%DrS%%%%~---------~=====%%==/
  __________________________________________________________________________
''')
print("Welcome to the Lost City.")
print("You seem to have attracted a follower...")
first = input('A strange machine follows you through the dissheveled city square. Now it\'s quickened its pace. You turn a corner into an alley way. To your left is a door. Go LEFT through the corridor or keep STRAIGHT down the alley? L or S ')
if first == 'S':
    print('You pass the doorway. The thing is so close you can hear a dull hum whiring from beneath its mangeled exterior. You break into a sprint. You turn the corner. Dead end. You touch your hands to the brick as the being\'s arms wrap around your neck.\n END')
else:
    print('You run through the doorway into what appears to be an old warehouse. Scattered glass crunches under feet as you sprint to the otherside of the chasm. As you approach the far wall you see two doors. Will you go RIGHT or LEFT?')
    choice = input('R or L ')
    if choice == 'L':
        print('Ripping open the door you barrell down the dark corridor, down a tile hallway, and out the far door into a crumbling courtyard. Youdouble over to catch your breathe as you hear His mechanical grind. You turn to face the sound only to see the machine\'s cold gaze as he tackles you to the ground.\n END.')
    else:
        print('Tearing open the door you run down the hallway to what appears to be a break area. The machine\'s pursuit rings a metallic clatter throughout the building. You now notice the door in the corner spilling light into the room. Panicked, you grab the handle and run out the door. You\'re now behind the building. Your car is parked several meters away and the machine is calling for you from the building. Can you beat him to your car? RUN to the car or STAY and fight?')
        decision = input('R or S ')
        if decision == 'S':
            print('You\'ve arrived at your last stand. The machine sprints accross the divide and you\'re in its arms. What were you thinking fighting an android? Do you know what kind of decision you just made? The car was right there.\n END.')
        else:
            print('You turn and sprint to the car. It\'s faster than you - you hear the machine\'s footfalls closing in. You reach the car before it does and slam your keys into the ignition. Accelerating you pull away just as he grabs for the car. Sparks explode from the pavement as his steel body drags across the road, refusing to release your door handle. What does he actually want? Where did he come from, and why is he here still? You\'ll never know, for you\'ve escaped.')
            print('Well done. Be careful out there.')

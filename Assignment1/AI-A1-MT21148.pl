/*
just compile the file and write 

lets_begin .

*/

lets_begin :-
  how_to_use,
  make_answers,
  give_suitable_masters(Field).


how_to_use:-
  write('Confuse which carrer to opt, which courses will be the best for you?'), nl,
  write('Do not worry we have made a perfect advisory system to resolve all your queries'), nl,
  write('NOTE:-Write the number of the option you are interested in, as shown in the options, followed by a dot "." to answer any question'), nl, nl.


give_suitable_masters(Field) :-
  masters(Field), !.


:- dynamic(information_collected/2).



make_answers :-
  retract(information_collected(_, _)),
  fail.
make_answers.






characterstics(ml,UK):-
loves_algo(yes),
solving_problems(solving_problems),
likes_thinking_logically,
loves_info_security(no),
likes_probability(yes),
free_time(no),
likes_computers_or_circuits(computers),
loves_number_system(yes),
like_maths(yes),
likes_discrete_maths(no),
UK='You have the logical ability and can solve problems.
For Higher Studies, you can opt the field of "Data Engineering", as You have a profound interest in the algo, mathematics, 
probabilities, and number system.'.


characterstics(ai,UK):-
loves_algo(yes),
likes_probability(yes),
loves_number_system(no),
solving_problems(solving_problems),
likes_discrete_maths(yes),
likes_computers_or_circuits(computers),
loves_info_security(no),
like_maths(no),
likes_thinking_logically,
free_time(no),

UK='You have the logical ability and can solve problems.
For Higher Studies, you can opt the field of "ARTIFICIAL INTELLIGENCE", as You have a profound interest in the algo, discrete mathematics, 
probabilities.'.


characterstics(appdevelopment,UK):-
likes_android(yes),
loves_algo(no),
likes_computers_or_circuits(computers),
loves_info_security(no),
solving_problems(solving_problems),
free_time(no),
likes_thinking_logically,

UK='You have the logical ability and are also interested in solving problems but do not like algo.
For Higher Studies, you can opt for "APP DEVELOPMENT", as You have a profound interest in  Android and logical thinking.'.


characterstics(vlsidesign,UK):-
vlsi_design(yes),
likes_circuits_design,
likes_computers_or_circuits(circuits),
likes_thinking_logically,
solving_problems(solving_problems),
UK='You have the logical ability and can solve problems.
For Higher Studies, you can opt the field of "VLSI DESIGN ENGINEER," as You have a profound interest in Circuit Design, Vlsi Design, and Circuits.'.


characterstics(computer_security,UK):-
loves_info_security(yes),
loves_algo(no),
likes_probability(yes),
likes_android(no),
likes_computers_or_circuits(computers),
solving_problems(solving_problems),
loves_number_system(yes),
likes_thinking_logically,
free_time(no),
like_maths(yes),

UK='You have the logical ability and can solve problems.
For Higher Studies, you can opt the field of "INFORMATION SECURITY," as You have a profound interest in Information security, Probabilities, and Number systems.'.


characterstics(cb,UK):-
biology(yes),
likes_imaginary_thinking,
like_maths(no),
loves_number_system(yes),
likes_computers_or_circuits(computers),
solving_problems(solving_problems),

UK='You have Imaginary Thinking and like to solve problems.
For Higher Studies, you can opt the field of "COMPUTATIONAL BIOLOGY," as You have a profound interest in Biology, Number systems, and solving real-world problems.'.

characterstics(csp,UK):-
communication_system(yes),
likes_circuits_design,
likes_computers_or_circuits(circuits),
solving_problems(solving_problems),
vlsi_design(no),

UK='You can solve problems.
For Higher Studies, you can opt the field of "ELECTRONICS AND COMMUNICATION ENGINEER," as You have a profound interest in Circuit Design, Communication systems, and Circuits.'.

characterstics(gap,UK):-
UK='No database found for the options you have choosen.',nl.

 

likes_circuits_design:-circuits(yes).
likes_thinking_logically:-likes_logic_nonlogic(logic).
likes_imaginary_thinking:-likes_logic_nonlogic(imaginary).

masters(computer_science):-
characterstics(ai,UK),
write('As you are an M.tech Student,  Recommended branch: Computer Science '),nl,
write('It seems you have experience with computers and you know how to operate the software with ease.'),nl,
write(UK),nl,
write('We are suggesting some career options with highest priority as 1, as per your skillset, I want the best thing to happen for you, Have a bright future :'),nl,
write('#1.) AI ENGINEER'),nl,
write('#2.) DATA ENGINEER'),nl,
write('#3.) DATA ANALYST'),nl,
write('#4.) NLP ENGINEER'),nl,
write('#5.) DATA RESEARCHER'),nl,
write('#6.) SOFTWARE ENGINEER'),nl.
 



masters(computational_bio):-
characterstics(cb,UK),
write('As you are an M.tech Student, Recommended Branch: Computational Biology'),nl,
write('It seems you have experience with Computers and also you shows a great interest in Biology.'),nl,
write(UK),nl,
write('We are suggesting some career options with highest priority as "1", as per your skillset, I want the best thing to happen for you, Have a bright future :'),nl,
write('#1.) COMPUTATIONAL ENGINEER'),nl,
write('#2.) SOFTWARE ENGINEER'),nl,
write('#3.) SYSTEM ENGINEER'),nl.


masters(computer_science):-
characterstics(appdevelopment,UK),
write('As you are an M.tech Student,  Recommended branch: Computer Science '),nl,
write('It seems you have experience with computers and you know how to operate the software with ease.'),nl,
write(UK),nl,
write('We are suggesting some career options with highest priority as "1", as per your skillset, I want the best thing to happen for you, Have a bright future :'),nl,
write('#1.) GAME DEVELOPER'),nl,
write('#2.) MOBILE APP DEVELOPER'),nl,
write('#3.) SYSTEM ENGINEER'),nl,
write('#4.) SOFTWARE ENGINEER'),nl.


masters(computer_science):-
characterstics(ml,UK),
write('As you are an M.tech Student,  Recommended branch: Computer Science '),nl,
write('It seems you have experience with computers and you know how to operate the software with ease.'),nl,
write(UK),nl,
write('We are suggesting some career options with highest priority as "1", as per your skillset, I want the best thing to happen for you, Have a bright future :'),nl,
write('#1.) DATA SCIENTIST'),nl,
write('#2.)  DATA RESEARCHER '),nl,
write('#3.) NLP ENGINEER'),nl,
write('#4.) SOFTWARE ENGINEER'),nl.


masters(electronics):-
characterstics(vlsidesign,UK),
vlsi_design(yes),
write('As you are an M.tech Student, Recommended Branch: Electronics and Communication'),nl,
write('It seems you have experience with Circuits and Hardware componenets.'),nl,
write(UK),nl,
write('We are suggesting some career options with highest priority as "1", as per your skillset, I want the best thing to happen for you, Have a bright future :'),nl,
write('#1.) VLSI DESIGN ENGINEER '),nl,
write('#2.) EMBEDDING ENGINEER'),nl,
write('#3.) VLSI FLOW ENGINEER'),nl,
write('#4.) SYSTEM ENGINEER'),nl.




masters(electronics):-
characterstics(csp,UK),
write('As you are an M.tech Student, Recommended Branch: Electronics and Communication'),nl,
write('It seems you have experience with Circuits and Hardware componenets.'),nl,
write(UK),nl,
write('We are suggesting some career options with highest priority as "1", as per your skillset, I want the best thing to happen for you, Have a bright future :'),nl,
write('#1.)COMMUNICATION ENGINEER '),nl,
write('#2.)EMBEDDING ENGINEER '),nl,
write('#3.)  GDS ENGINEER'),nl,
write('#4.)RTL DESIGNER'),nl,
write('#5.) SYSTEM ENGINEER'),nl.


masters(computer_science):-
characterstics(computer_security,UK),
write('As you are an M.tech Student,  Recommended branch: Computer Science '),nl,
write('It seems you have experience with computers and you know how to operate the software with ease.'),nl,
write(UK),nl,
write('We are suggesting some career options with highest priority as "1", as per your skillset, I want the best thing to happen for you, Have a bright future :'),nl,
write('#1.) COMPUTER SECURITY ENGINEER'),nl,
write('#2.)INFORMATION SECURITY ENGINEER'),nl,
write('#3.)  DATA SECURITY ENGINEER'),nl,
write('#4.)  CLOUD SUPPORT ENGINEER '),nl,
write('#5.)   SYSTEM ENGINEER '),nl.



masters(gap_year):-
characterstics(gap,UK),
write('As you are an M.tech Student,Recommendation: Develop some skills in a particular field take some time to figure out what you like '),nl,
write(UK),nl,
write('In the current situation, We are unable to predict a particular branch for you. You have many skill sets, and some skills match a specific branch, and some do not. We will recommend taking a gap year and making skillset in a particular direction easier to assign a particular Branch to you.'),nl.


user_ans(yes) :-
  write('Yes Absolutely').

user_ans(imaginary):-
	write('No, I like to think more in an imaginary way.').
  
user_ans(logic):-
write('I Like to think logically more.').

user_ans(no_solving_problems) :-
  write('No, I am not good at solving puzzles and problems.').

user_ans(circuits):-
write('I am more interested in ciruits not computers.').

user_ans(computers):-
write('I am more interested in computer rather than circuits.').

user_ans(no) :-
  write('No').


user_ans(solving_problems) :-
  write('Yaa, I am good at solving puzzles and problems.').


curious(loves_info_security):-
write('Are you found the branch of information security, cryptography, Interesting?'),nl.

curious(circuits):-
write('Do you know about the circuits, and does their system make you curious to learn them more?'),nl.

curious(solving_problems):-
write('Are you good at solving puzzles and problems?'),nl.

curious(likes_computers_or_circuits):-
write('Which one do you like the most, circuits or computers?'),nl.

curious(like_maths):-
write('Do you admire mathematics? '),nl.

curious(free_time):-
write('Do you anyhow get the free time to manage things?'),nl.


curious(likes_discrete_maths):-
write('Does Discrete Mathematics attract you? '),nl.

curious(likes_probability):-
write('are you interested in statics and likes probability?'),nl.

curious(vlsi_design):-
write('Are you passionate about circuits and VLSI design?'),nl.

curious(loves_number_system):-
write('Do you have an interest in the number system?'),nl.

curious(likes_android):-
write('Are you passionate about learning android systems?'),nl.

curious(communication_system):-
write('Do you have an interest in the communication system?'),nl.

curious(likes_logic_nonlogic):-
write('Do you like to think logically or in an imaginary way?'),nl.

curious(biology):-
write('Do you like the field of biology also?'),nl.

curious(loves_algo):-
write('Are you anyhow interested in Algos and Data structures?'),nl.





likes_android(Reply) :-
  information_collected(likes_android, Reply).
likes_android(Reply) :-
  \+ information_collected(likes_android, _),
  question(likes_android, Reply, [yes, no]).




free_time(Reply) :-
  information_collected(free_time, Reply).
free_time(Reply) :-
  \+ information_collected(free_time, _),
  question(free_time, Reply, [yes, no]).

circuits(Reply) :-
  information_collected(circuits, Reply).
circuits(Reply) :-
  \+ information_collected(circuits, _),
  question(circuits, Reply, [yes, no]).

likes_discrete_maths(Reply) :-
  information_collected(likes_discrete_maths, Reply).
likes_discrete_maths(Reply) :-
  \+ information_collected(likes_discrete_maths, _),
  question(likes_discrete_maths, Reply, [yes, no]).

  solving_problems(Reply) :-
  information_collected(solving_problems, Reply).
solving_problems(Reply) :-
  \+ information_collected(solving_problems, _),
  question(solving_problems, Reply, [solving_problems, no_solving_problems]).


likes_logic_nonlogic(Reply) :-
  information_collected(likes_logic_nonlogic, Reply).
likes_logic_nonlogic(Reply) :-
  \+ information_collected(likes_logic_nonlogic, _),
  question(likes_logic_nonlogic, Reply, [logic,imaginary]).

like_maths(Reply) :-
  information_collected(like_maths, Reply).
like_maths(Reply) :-
  \+ information_collected(like_maths, _),
  question(like_maths, Reply, [yes, no]).


likes_computers_or_circuits(Reply) :-
  information_collected(likes_computers_or_circuits, Reply).
likes_computers_or_circuits(Reply) :-
  \+ information_collected(likes_computers_or_circuits, _),
  question(likes_computers_or_circuits, Reply, [computers, circuits]).




loves_number_system(Reply) :-
  information_collected(loves_number_system, Reply).
loves_number_system(Reply) :-
  \+ information_collected(loves_number_system, _),
  question(loves_number_system, Reply, [yes, no]).


likes_probability(Reply) :-
  information_collected(likes_probability, Reply).
likes_probability(Reply) :-
  \+ information_collected(likes_probability, _),
  question(likes_probability, Reply, [yes, no]).

loves_info_security(Reply) :-
  information_collected(loves_info_security, Reply).
loves_info_security(Reply) :-
  \+ information_collected(loves_info_security, _),
  question(loves_info_security, Reply, [yes, no]).

vlsi_design(Reply) :-
  information_collected(vlsi_design, Reply).
vlsi_design(Reply) :-
  \+ information_collected(vlsi_design, _),
  question(vlsi_design, Reply, [yes, no]).

loves_algo(Reply) :-
  information_collected(loves_algo, Reply).
loves_algo(Reply) :-
  \+ information_collected(loves_algo, _),
  question(loves_algo, Reply, [yes, no]).

communication_system(Reply) :-
  information_collected(communication_system, Reply).
communication_system(Reply) :-
  \+ information_collected(communication_system, _),
  question(communication_system, Reply, [yes, no]).

biology(Reply) :-
  information_collected(biology, Reply).
biology(Reply) :-
  \+ information_collected(biology, _),
  question(biology, Reply, [yes, no]).




possible_answers([], _).
possible_answers([Head|Tail], Index) :-
  write(Index), write(' '), user_ans(Head), nl,
  NewIndex is Index + 1,
  possible_answers(Tail, NewIndex).


back(0, [Head|_], Head).
back(Index, [Head|Tail], Response) :-
  Index > 0,
  NewIndex is Index - 1,
  back(NewIndex, Tail, Response).



question(Question, Answer, Choices) :-
  curious(Question),
  possible_answers(Choices, 0),
  read(Index),
  back(Index, Choices, Response),
  asserta(information_collected(Question, Response)),
  Response = Answer.









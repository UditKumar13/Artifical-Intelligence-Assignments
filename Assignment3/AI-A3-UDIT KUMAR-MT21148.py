# forward chaining rule engine
# trying out durable rules engine
#

#pip install durable_rules

from durable.lang import *

with ruleset('M.tech'):
    # will be triggered by 'grades' and 'selected field' facts

    #biology  and music 
    @when_all((m.grades >=80) & (m.interested_field == 'Biology') & (m.passion == 'music') )
    def bio(c):
        c.assert_fact('extra',{'data' :'music'})
        c.assert_fact({ 'course_1': 'Introduction to Quantative biology', 'course_2': 'Algo in Computation biology' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'Biology') & (m.passion =='music'))
    def bio(c):
        c.assert_fact('extra',{'data' :'music'})
        c.assert_fact({ 'course_1': 'Network Biology', 'course_2': 'Data Structures for Genomics' })

    
     #biology  and sports 
    @when_all((m.grades >=80) & (m.interested_field == 'Biology') & (m.passion == 'sports'))
    def bio(c):
        c.assert_fact('extra',{'data' :'sports'})
        c.assert_fact({ 'course_1': 'Introduction to Quantative biology', 'course_2': 'Algo in Computation biology' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'Biology') & (m.passion =='sports'))
    def bio(c):
        c.assert_fact('extra',{'data' :'sports'})
        c.assert_fact({ 'course_1': 'Network Biology', 'course_2': 'Data Structures for Genomics' })

     #biology  and sports 
    @when_all((m.grades >=80) & (m.interested_field == 'Biology') & (m.passion == 'body-building'))
    def bio(c):
        c.assert_fact('extra',{'data' :'body-building'})
        c.assert_fact({ 'course_1': 'Introduction to Quantative biology', 'course_2': 'Algo in Computation biology' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'Biology') & (m.passion =='body-building'))
    def bio(c):
        c.assert_fact('extra',{'data' :'body-building'})
        c.assert_fact({ 'course_1': 'Network Biology', 'course_2': 'Data Structures for Genomics' })


    @when_all((m.grades >=80) & (m.interested_field == 'Biology') & (m.passion =='public-speaking'))
    def bio(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Introduction to Quantative biology', 'course_2': 'Algo in Computation biology' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'Biology') & (m.passion =='public-speaking'))
    def bio(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Network Biology', 'course_2': 'Data Structures for Genomics' })
    
    #Ai 
    @when_all((m.grades >=80) & (m.interested_field == 'Artificial_Intelligence') & (m.passion =='music'))
    def ai(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Game thoery', 'course_2': 'Robotics' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'Artificial_Intelligence') & (m.passion =='music'))
    def ai(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Computer Vision ', 'course_2': 'Natural language processing' })

    #ai - sports 
    @when_all((m.grades >=80) & (m.interested_field == 'Artificial_Intelligence') & (m.passion =='sports'))
    def ai(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Game thoery', 'course_2': 'Robotics' })
      
    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'Artificial_Intelligence') & (m.passion =='sports'))
    def ai(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Computer Vision ', 'course_2': 'Natural language processing' })

    #ai- body-building
   

    @when_all((m.grades >=80) & (m.interested_field == 'Artificial_Intelligence') & (m.passion =='body-building'))
    def ai(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Game thoery', 'course_2': 'Robotics' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'Artificial_Intelligence') & (m.passion =='body-building'))
    def ai(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Computer Vision ', 'course_2': 'Natural language processing' })


    @when_all((m.grades >=80) & (m.interested_field == 'Artificial_Intelligence') & (m.passion =='public-speaking'))
    def ai(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Game thoery', 'course_2': 'Robotics' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'Artificial_Intelligence') & (m.passion =='public-speaking'))
    def ai(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Computer Vision ', 'course_2': 'Natural language processing' })


    #circuits and Electronics 

      

    @when_all((m.grades >=80) & (m.interested_field == 'circuits_electronics') & (m.passion =='music'))
    def cir(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Advanced Embedded logic design', 'course_2': 'Digital VLSI Design' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'circuits_electronics') & (m.passion =='music'))
    def cir(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Quantum material and devices ', 'course_2': 'Circuit theory and devices' })

    #cir - sports 
    @when_all((m.grades >=80) & (m.interested_field == 'circuits_electronics') & (m.passion =='sports'))
    def cir(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Advanced Embedded logic design', 'course_2': 'Digital VLSI Design' })
      
    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'circuits_electronics') & (m.passion =='sports'))
    def cir(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Quantum material and devices ', 'course_2': 'Circuit theory and devices' })

    #cir- body-building
   

    @when_all((m.grades >=80) & (m.interested_field == 'circuits_electronics') & (m.passion =='body-building'))
    def cir(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Advanced Embedded logic design', 'course_2': 'Digital VLSI Design' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'circuits_electronics') & (m.passion =='body-building'))
    def cir(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Quantum material and devices ', 'course_2': 'Circuit theory and devices' })

    @when_all((m.grades >=80) & (m.interested_field == 'circuits_electronics') & (m.passion =='public-speaking'))
    def cir(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Advanced Embedded logic design', 'course_2': 'Digital VLSI Design' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'circuits_electronics') & (m.passion =='public-speaking'))
    def cir(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Quantum material and devices ', 'course_2': 'Circuit theory and devices' })

    


    #Design and Animation  

      

    @when_all((m.grades >=80) & (m.interested_field == 'design_animation') & (m.passion =='music'))
    def ani(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Introduction to 3D animation', 'course_2': 'Game Design and Development' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'design_animation') & (m.passion =='music'))
    def ani(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Design of Interactive System', 'course_2': 'Visual Design and Communication' })

    #ani - sports 
    @when_all((m.grades >=80) & (m.interested_field == 'design_animation') & (m.passion =='sports'))
    def ani(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Introduction to 3D animation', 'course_2': 'Game Design and Development' })
      
    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'design_animation') & (m.passion =='sports'))
    def ani(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Design of Interactive System', 'course_2': 'Visual Design and Communication' })

    #ani- body-building
   

    @when_all((m.grades >=80) & (m.interested_field == 'design_animation') & (m.passion =='body-building'))
    def ani(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Introduction to 3D animation', 'course_2': 'Game Design and Development' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'design_animation') & (m.passion =='body-building'))
    def ani(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Design of Interactive System', 'course_2': 'Visual Design and Communication' })


    @when_all((m.grades >=80) & (m.interested_field == 'design_animation') & (m.passion =='public-speaking'))
    def ani(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Introduction to 3D animation', 'course_2': 'Game Design and Development' })
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'design_animation') & (m.passion =='public-speaking'))
    def ani(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Design of Interactive System', 'course_2': 'Visual Design and Communication' })

    #SDE
  

    @when_all((m.grades >=80) & (m.interested_field == 'algorithm') & (m.passion =='music'))
    def sde(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Advanced Algorithms', 'course_2': 'Advanced Programming'})
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'algorithm') & (m.passion =='music'))
    def sde(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Mordern algorithms', 'course_2': 'Algorithm Design and Analysis'})

    #sde - sports 
    @when_all((m.grades >=80) & (m.interested_field == 'algorithm') & (m.passion =='sports'))
    def sde(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Advanced Algorithms', 'course_2': 'Advanced Programming'})
      
    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'algorithm') & (m.passion =='sports'))
    def sde(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Mordern algorithms', 'course_2': 'Algorithm Design and Analysis'})

    #sde- body-building
   

    @when_all((m.grades >=80) & (m.interested_field == 'algorithm') & (m.passion =='body-building'))
    def sde(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Advanced Algorithms', 'course_2': 'Advanced Programming'})
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'algorithm') & (m.passion =='body-building'))
    def sde(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Mordern algorithms', 'course_2': 'Algorithm Design and Analysis'})


    @when_all((m.grades >=80) & (m.interested_field == 'algorithm') & (m.passion =='public-speaking'))
    def sde(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Advanced Algorithms', 'course_2': 'Advanced Programming'})
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'algorithm') & (m.passion =='public-speaking'))
    def sde(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Mordern algorithms', 'course_2': 'Algorithm Design and Analysis'})

    #Network and system

    @when_all((m.grades >=80) & (m.interested_field == 'network_system') & (m.passion =='music'))
    def net(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Computer Network', 'course_2': 'Compiler'})
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'network_system') & (m.passion =='music'))
    def net(a):
        a.assert_fact('extra',{'data' :'music'})
        a.assert_fact({ 'course_1': 'Mobile Computing', 'course_2': 'Operating System'})

    #net - sports 
    @when_all((m.grades >=80) & (m.interested_field == 'network_system') & (m.passion =='sports'))
    def net(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Computer Network', 'course_2': 'Compiler'})
      
    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'network_system') & (m.passion =='sports'))
    def net(a):
        a.assert_fact('extra',{'data' :'sports'})
        a.assert_fact({ 'course_1': 'Mobile Computing', 'course_2': 'Operating System'})

    #net- body-building
   

    @when_all((m.grades >=80) & (m.interested_field == 'network_system') & (m.passion =='body-building'))
    def net(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Computer Network', 'course_2': 'Compiler'})
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'network_system') & (m.passion =='body-building'))
    def net(a):
        a.assert_fact('extra',{'data' :'body-building'})
        a.assert_fact({ 'course_1': 'Mobile Computing', 'course_2': 'Operating System'})

#net- body-building
   

    @when_all((m.grades >=80) & (m.interested_field == 'network_system') & (m.passion =='public-speaking'))
    def net(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Computer Network', 'course_2': 'Compiler'})
      

    @when_all((m.grades >=60) & (m.grades <80) & (m.interested_field == 'network_system') & (m.passion =='public-speaking'))
    def net(a):
        a.assert_fact('extra',{'data' :'public-speaking'})
        a.assert_fact({ 'course_1': 'Mobile Computing', 'course_2': 'Operating System'})

    @when_all(+m.course_1)
    def output(uk):
        print('Suggested Course 1  for you is : {0} and Suggested Course 2 for you is : {1}'.format(uk.m.course_1,uk.m.course_2))

# for extra curricular activities : 
with ruleset('extra'):
    
    @when_all((m.data == 'music'))
    def music(d):
        d.assert_fact({'advice' : '2.If you are a bad singer, try to learn an instrument like: piano, guitar'})
        d.assert_fact({'advice' : '1.If you are a good singer, join the singing club, and do the practice and grow with IIITD'})

    @when_all((m.data == 'sports'))
    def sports(d):
        d.assert_fact({'advice' : '2.If you like indoor sports, you can play chess, tabel tennis in IIITD'})
        d.assert_fact({'advice' : '1.If you like outdoor sports, you can play football, cricket even do the swimming in IIITD'})

    @when_all((m.data == 'body-building'))
    def body(d):
        d.assert_fact({'advice' : '3.Join the GYM'})
        d.assert_fact({'advice' : '2.Do 100 pushups everyday'})
        d.assert_fact({'advice' : '1.Do 100 crunches'})

    @when_all((m.data == 'public-speaking'))
    def speak(d):
        d.assert_fact({'advice' : '3.Join the TEDX-IIITD'})
        d.assert_fact({'advice' : '2.Take part into various public debates and interactive seesions'})
        d.assert_fact({'advice' : '1.Do improve skill of speaking with others, even can start teaching other students.'})


    @when_all(+m.advice)
    def output(uk):
        print('Extra curricular activity for you: {0}'.format(uk.m.advice))






assert_fact('M.tech', { 'grades': 66, 'interested_field': 'Biology' , 'passion':'sports'})

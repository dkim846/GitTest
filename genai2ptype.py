
####final




import random
resplist = ("cooling servers consumes massive water supplies."),
(" Training big models adds greenhouse gasses"),
("Microsoft’s water use rose 34% in a year from AI.")
fax = ["Using renewable energy in AI data centers can cut emissions by over 70%",
            "Generative AI can also help design energy-efficient materials and cut waste in industries",
            "Cooling AI servers with recycled water helps protect freshwater supplies."]

print("Hello, this is EcoJohn!")


yn=input("Are you aware of the effects of GenAI?==>(yes/no)")


if yn == "yes":
      
      print("Perfect!")
      

      cur=input("Are you curious about energy,water or carbon")

      if cur == "energy":
           print("Generative AI models consume massive amounts of electricity driving up overall energy demand")
           c1=input("Now would you like some fun facts?")
           if c1 == "yes":
              
              for doo in fax:
                   print(doo)
           print("Sorry my friend, i ran out of facts. Goodbye my friend")
    
      elif cur== "water":
           print("Generative AI data centers use huge volumes of water for cooling, sometimes millions of liters a day")
           c2=input("Now would you like some fun facts?")
           
           if c2=="yes":
                  
                 for doo in fax:
                   print(doo)
           print("Sorry friend, Im all out of facts.Goodbye friend.")

              
          
      if cur =="carbon":
          print("Training large AI models can release as much carbon as running five cars for their entire lifetimes")
          c3=input("Now would you like some fun facts?")
          if c3=="yes":    

                for doo in fax:
                 print(doo)
      print("Sorry my friend, I cant think of anymore facts.Goodbye my friend!")
              
          
        
       
else:
      
     print("Thats why I exist! throughout your experience using GenAi,")

     inq=input ("Would you like some fun facts to get started?==>")

     if inq == "yes":

        fact=random.choice(resplist)
        if inq == "yes":
         print(fact)
         for doo in fax:

            pow=input("Would you like another fun fact?")
            if pow == "yes":
               
               print("Amazing!",doo)
        else:
           print("All good! I am always here if needed")
           

        print("Those are all the fun facts i've got! Sorry my friend.Goodbye")
            
           

    

               
            
        
        
             






                  

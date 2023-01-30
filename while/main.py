from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
#if __name__ == "__main__":
#    print(random_koala_fact())





def unique_koala_facts(n):
    unique_koala_facts = []
    if n > 1000:
        n = 1000
    for i in range(n):
        fact = random_koala_fact()
        if fact not in unique_koala_facts:
            unique_koala_facts.append(fact)
    unique_koala_facts = list(set(unique_koala_facts))
 
    unique_koala_facts = (unique_koala_facts)
    return (unique_koala_facts)


data = ["Koalas are found in the eucalyptus forests of eastern Australia. They have grey fur with a cream-coloured chest, and strong, clawed feet, perfect for living in the branches of trees!", "The koala's nickname is a Native Bear.", "They live and sleep in the eucalyptus trees. It's hot, light and dry here.", "The koala breaths oxygen from air.", "Koalas live for 20 or more years.", "Cuddly critters, koalas measure about 60cm to 85cm long, and weigh about 14kg.", "The koalas have white on the underside and gray on the rest of its body.", "After 1 month the cub is 1 cm. long.", "Eucalyptus leaves are super tough and poisonous! Luckily for koalas, they have a long digestive organ called a cecum which allows them to break down the leaves unharmed.", "A joey grows and develops in the pouch for about six months. Once strong enough, the youngster rides around on its mother\u2019s back for a further six months, only using the pouch to feed.", "The koala cub stays in the mother's pouch for 5 months.", "Koala\u2019s grow up to become big eaters, shifting up to one kilogram of eucalyptus leaves in a day! They are fussy, too, and will select the most nutritious and tastiest leaves from the trees where they live.", "The koala might look cuddly but the koala has very sharp teeth and very sharp claws.", "One cub is born at a time.", "The koala weighs 15 to 30 pounds.", "Koalas are nocturnal marsupials famous for spending most of their lives asleep in trees. During the day they doze, tucked into forks or nooks in the trees, sleeping for up to 18 hours. This sedentary lifestyle can be attributed to the fact they have unusually small brains and survive on a diet of nutrient-poor leaves. Koalas tend to smell strongly of eucalyptus and musk. This is thought to discourage fleas and other animals from living in its fur", "Although you may have heard people call them koala \"bears\", these awesome animals aren't bears at all \u2013 they are in fact marsupials. A group of mammals, most marsupials have pouches where their newborns develop.", "The koala cub is blind when it's born.", "The mother has a pouch.", "The koala is a marsupial mammal.", "The koala's young is called a cub.", "Koalas sleep for up to 19 hours.", "The koala has big ears and a big nose.", "The koala has very thick fur.", "Koalas don\u2019t have much energy and, when not feasting on leaves, they spend their time dozing in the branches. Believe it or not, they can sleep for up to 18 hours a day!", "When an infant koala \u2013 called a joey \u2013 is born, it immediately climbs up to its mother\u2019s pouch. Blind and earless, a joey uses its strong sense of touch and smell, as well as natural instinct, to find its way.", "The koala's young are born alive.", "They are warm-blooded.", "These magnificent mammals get their name form an Aboriginal term meaning, \"no drink\". It\u2019s believed this is because koalas get almost all their moisture from the leaves they eat, and rarely drink water."]
#state the lenght of the list
print(len(data))

# print(unique_koala_facts(2000))
print(len(unique_koala_facts(2000000)))







def num_joey_facts():
    my_list = {}
    m = []
    unique_joey_fact_list = []
    for i in range(1000):
        #get a cool random koala fact
        fact = random_koala_fact()

        #if the string "joey" is in my_list, add the fact to the list
        if "joey" in fact:
            unique_joey_fact_list.append(fact)
        
        # add the fact to my_list, and set 1 to the value of the key. If the key exists, add 1 to the value
        my_list[fact] = my_list.get(fact, 0) + 1

    # create a set, remove the duplicates
    m = set(unique_joey_fact_list)
    # print(unique_joey_fact_list)
    return len(m)

# print(num_joey_facts())

# my_list = {}
# m = []
# unique_joey_fact_list = []
# counter = 0
# for i in range(1000):
#     #get a cool random koala fact
#     fact = random_koala_fact()

#     #if the string "joey" is in my_list, add the fact to the list
#     if "joey" in fact:
#         unique_joey_fact_list.append(fact)
    
#     # add the fact to my_list, and set 1 to the value of the key. If the key exists, add 1 to the value
#     my_list[fact] = my_list.get(fact, 0) + 1
#     counter += 1

#     # once one of the values reaches 10, stop the loop
#     if counter == 10:
#         break

# # create a set, remove duplicates
# m = set(unique_joey_fact_list)
# # print(unique_joey_fact_list)
# print(counter)

        
         

   

#         # create a set, remove duplicates
#         m = set(unique_joey_fact_list)
#         counter = unique_joey_fact_list.count(fact)
#         # print(unique_joey_fact_list)
#     return counter

# print(num_joey_facts())




#give the weight of the koala in KG from the random koala fact list
def koala_weight():
    for i in range(int(1000)):
        fact = random_koala_fact()
        if "weight" and "kg" in fact:
            print (fact)
            #filter and select 2 numbers from fact before string 'kg'
            weight_KG = fact.split("kg")[0][-2:]
            
            
            return int(weight_KG)


#print(koala_weight())



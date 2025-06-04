# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)

# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)

# all_animals_3 = farm_animals | wild_animals
# print(all_animals_3)

from prescription_data import adverse_interactions

meds_to_watch = set()

for interaction in adverse_interactions:
    #meds_to_watch = meds_to_watch.union(interaction)
    #meds_to_watch = meds_to_watch | interaction
    #meds_to_watch.update(interaction)
    meds_to_watch |= interaction
    
print(sorted(meds_to_watch))
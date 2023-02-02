import random

def split_prize_pool(prize_pool, people):
  # Calculate the total number of shares
  shares = len(people)

  # Initialize a list to store the prize amounts for each person
  prize_amounts = [0] * shares

  # Loop through the people and assign a random prize amount to each person
  for i in range(shares):
    # Calculate the remaining prize pool and the number of remaining people
    remaining_prize_pool = prize_pool - sum(prize_amounts)
    remaining_people = shares - i

    # Calculate the maximum prize amount that can be assigned to the current person
    max_prize_amount = remaining_prize_pool // remaining_people

    # Assign a random prize amount to the current person, ensuring that it is positive and does not exceed the maximum prize amount
    prize_amounts[i] = random.randint(1, max_prize_amount)

  # Distribute the remaining prize amount evenly among the people, if necessary
  remaining_prize_pool = prize_pool - sum(prize_amounts)
  if remaining_prize_pool > 0:
    for i in range(shares):
      prize_amounts[i] += remaining_prize_pool // shares

  # Create a dictionary to store the final prize amounts for each person
  final_prize_amounts = {}
  for i, person in enumerate(people):
    final_prize_amounts[person] = prize_amounts[i]

  # Sort the dictionary of final prize amounts in ascending order
  sorted_prize_amounts = sorted(final_prize_amounts.items(), key=lambda x: x[1], reverse=True)

  # Create a list of strings in the desired format
  result = ""
  for i, (person, prize_amount) in enumerate(sorted_prize_amounts):
    result += (f'{i+1}. {person}: {prize_amount} R$\n')

  # Return the list of strings
  return result
#This function uses a a modified version of the "knapsack" algorithm, which is a well-known algorithm for solving the problem of selecting a set of items with the highest total value, subject to the constraint that the total weight of the items does not exceed a given capacity.

def dictize(string):
    data_dict = {}
    for line in string.strip().split("\n"):
        parts = line.split(":")
        person = parts[0].split("@")[1].split(">")[0].strip()
        prize_amount = parts[1].split(" R$")[0].strip()
        data_dict[person] = prize_amount
    return data_dict


